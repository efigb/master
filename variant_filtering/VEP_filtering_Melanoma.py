#! usr/bin/python3 

import click
import pandas as pd
from tqdm import tqdm
tqdm.pandas()

# List of consequences from Ensembl VEP ordered from worse to less worse

CONSEQUENCES_LIST = [
    'transcript_ablation',
    'splice_acceptor_variant',
    'splice_donor_variant',
    'stop_gained',
    'frameshift_variant',
    'stop_lost',
    'start_lost',
    'transcript_amplification',
    'inframe_insertion',
    'inframe_deletion',
    'missense_variant',
    'protein_altering_variant',
    'splice_region_variant',
    'splice_donor_5th_base_variant',
    'splice_donor_region_variant',
    'splice_polypyrimidine_tract_variant',
    'incomplete_terminal_codon_variant',
    'start_retained_variant',
    'stop_retained_variant',
    'synonymous_variant',
    'coding_sequence_variant',
    'mature_miRNA_variant',
    '5_prime_UTR_variant',
    '3_prime_UTR_variant',
    'non_coding_transcript_exon_variant',
    'intron_variant',
    'NMD_transcript_variant',
    'non_coding_transcript_variant',
    'upstream_gene_variant',
    'downstream_gene_variant',
    'TFBS_ablation',
    'TFBS_amplification',
    'TF_binding_site_variant',
    'regulatory_region_ablation',
    'regulatory_region_amplification',
    'feature_elongation',
    'regulatory_region_variant',
    'feature_truncation',
    'intergenic_variant'
]
  
# 1/ Function to filter by MANE transcript

def transcript_filter(groups_list, vep_out_df):
    final_df = pd.DataFrame()
    for g in tqdm(groups_list):
        mut = g[0] # first element of list
        gene = g[1] # second element of list
        transcripts_df = vep_out_df[(vep_out_df['Uploaded_variation'] == mut) & (vep_out_df['Gene'] == gene)] # for each variant in dataframe that is equal to the variant in the list (unique value)
        if len(transcripts_df) > 1: # this selects those variants that have more than 1 transcript
            mane_transcripts_df = transcripts_df[transcripts_df['MANE_SELECT'] != '-']
            if len(mane_transcripts_df) == 1:
                df2 = mane_transcripts_df # select mane trancript
            elif len(mane_transcripts_df) == 0:
                can_df = transcripts_df[transcripts_df['CANONICAL'] == 'YES']
                if len(can_df) == 1:
                    df2 = can_df # select canonical transcript
                elif len(can_df) == 0:
                    df2 = transcripts_df # take all trancripts when no information of MANE or CANONICAL
                elif len(can_df) >1:
                    df2 = transcripts_df[0]
                    print('Transcript filter Warning: more than 1 canonical transcript.')
                    print(can_df)
                else:
                    print('Transcript filter Warning: transcript filtering skipped: No MANE, No CANONICAL, No multiple transcripts') # show this message and display it to show that something is missing in the code
                    print(can_df)
            elif len(mane_transcripts_df) > 1:
                df2 =  transcripts_df[0] # filter first transcript for those with the same uploaded variation and gene
                print('Transcript filter Warning: selected only the first transcripts when more han one allele possible per variant and gene')
                print(transcripts_df)
            else:
                print('Transcript filter Warning: transcript filtering skipped: different than 0, 1 or more than 1 transcripts possible') # show this message and display it to show that something is missing in the code
                print(transcripts_df)
        elif len(transcripts_df) == 1: # this means there is only 1 transcript for this variant so no need to filter
            df2 = transcripts_df 
        else:
            print('Transcript filter Warning: No transcript for this variant?')

        final_df = pd.concat([final_df, df2], ignore_index=True)

    return final_df


# 2/ Function to select a unique consequence per selected transcript

def consequence_worse(row,CONSEQUENCES_LIST):
    # This is the consequences list with VEP/Gnomad older versions ordered by worse to less worse effect
    conseq = row['Consequence'].split(',')  # split comma separated values of Consequence column
    num_elements = len(conseq)
    if num_elements == 1: # when there is only one Consequence for the variant
        return conseq[0] # return first value (unique one in this case) to avoid returning a list
    elif num_elements > 1: # when there is more than one Consequence for the variant
        for element in CONSEQUENCES_LIST: # for each element of the ordered list of consequences
            for cons in conseq: # for each element of the column Consequences
                if cons == element: # if the consequence is equal to the element
                    return element
                    break
                #else:
                    print('Consequence type Warning: This consequence type:', cons,', does not match the element in consequence list:', element)
    else:
        print('Consequence type Warning: No number of consequence type (or different than 1 or more): ', num_elements)
    return

# 3/ Filter multiple transcripts per WORSE_conseq

def worse_conseq_filter (df):
    # Filter duplicated rows based on columns Uploaded variation and Gene based on order in consequence list of column WORSE_conseq
    annot_df = df.sort_values(by='WORSE_conseq', key=lambda x: x.map(lambda y: CONSEQUENCES_LIST.index(y))).drop_duplicates(subset=['Uploaded_variation', 'Gene'])
    return annot_df

# 4/ Transform mutations dataframe (VEP input) to VEP format prior to merge

def change_format (row2):

    ref = row2['REF']
    alt = row2['ALT']
    pos = row2['POS']
    mut_type = row2['mut_type']
    position = row2['POS']

    if mut_type == 'INDEL':

        if len(ref) == 1: # this is an insertion
            ref = '-' # change for "-"
            alt = alt[1:] #change for same without first character
            pos = pos + 1 # add 1 to position
        else: # this is a deletion
            ref = ref[1:] # change for same without first character
            alt = '-' # change for "-"
            pos = pos + 1 # add 1 to position
        row2['REF'] = ref
        row2['ALT'] = alt
        row2['POS'] = pos
    return row2


# 5/ Merge transformed annotated variants with the mutations dataframe (VEP input)

def merge_mutations(annot_df, mut_format_df):
    
    # Check data type of POS column that is in different format in the two dataframes: 
    print(mut_format_df)
    annot_df['POS'] = annot_df['POS'].astype(int) #change data type so it is the same as data type in both dataframes 
    print(annot_df)

    merged_df = annot_df.merge(mut_format_df, on=['#CHROM','POS','REF','ALT'], how = 'left') # this retains all rows from the left DataFrame while matching rows from the right DataFrame
    return merged_df


# Click options to set in the command before running the script
@click.command()

@click.option('--input_annot', # this is the output of VEP
              '-i',
              required = True,
              help="path to vep output chromosome files")

@click.option('--input_mut', # this is the input of VEP or mutations table
              '-i2',
              required = True,
              help="path to vep input chromosome files")

@click.option('--output_file',
              '-o',
              required = True,
              help="path to output folder")

def main(input_annot, output_file, input_mut):

    # 1/ Read mutaion files (1 per chromosome) and return a dataframe
    columns = ['Uploaded_variation', 'Location', 'Allele', 'Gene',	'Feature', 'Feature_type', 'Consequence', 'cDNA_position', 'CDS_position', 'Protein_position', 'Amino_acids','Codons','Existing_variation','IMPACT','DISTANCE','STRAND','FLAGS','SYMBOL','SYMBOL_SOURCE','HGNC_ID','CANONICAL','MANE_SELECT','MANE_PLUS_CLINICAL','ENSP',	'SOURCE', 'AF',	'AFR_AF', 'AMR_AF','EAS_AF', 'EUR_AF','SAS_AF','CLIN_SIG','SOMATIC','PHENO','gnomADg', 'gnomADg_AF', 'gnomADg_NFE']
    vep_out_df = pd.read_csv(input_annot, sep="\t", names= columns, comment='#', header=None)
    print(vep_out_df)

    # Reformat Uploaded variation column so all separators are "_" to split this table to CHROM POS REF ALT
    print(vep_out_df['Uploaded_variation'][0:5])
    vep_out_df['Uploaded_variation'] = vep_out_df['Uploaded_variation'].str.replace('/','_')
    vep_out_df = pd.concat([vep_out_df, vep_out_df['Uploaded_variation'].str.split('_', expand=True)], axis=1)
    vep_out_df = vep_out_df.rename(columns={0:'#CHROM', 1: 'POS', 2:'REF', 3: 'ALT', 4: "other allele"})

    # 2/ Read mutation files (1 per chromosome) and return a dataframe
   
    mut_df = pd.read_csv(input_mut, sep="\t", header=0)
    print(mut_df)
  
    # Check in a new dataframe the number of transcripts per position and sort it by its location in genome
    grp_df = vep_out_df.groupby(['Uploaded_variation','Gene'], as_index=False).count().sort_values('Location',ascending=False)
    # Make a list from these two columns that results in unique values
    groups_list = grp_df[['Uploaded_variation','Gene']].values.tolist()

    
    # 3/ Apply the functions defined (not main)

    final_df = transcript_filter(groups_list, vep_out_df) # Apply first function to filter transcripts by MANE
    final_df['WORSE_conseq'] = final_df.progress_apply(lambda row: consequence_worse(row,CONSEQUENCES_LIST), axis=1) # Apply second function to add worse consequence
    annot_df = worse_conseq_filter(final_df) # Apply third function to filter transcripts by worse consequence
    mut_format_df = mut_df.progress_apply(lambda row2: change_format (row2), axis=1) # Apply fourth function to transform mutation table to VEP format
    merged_df = merge_mutations(annot_df, mut_format_df) # Apply last function to filter 
    merged_df.to_csv(output_file,sep='\t',compression='gzip',index=None)


if __name__ == "__main__":
    main()

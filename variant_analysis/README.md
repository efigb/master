# Analysis of Variants

This folder contains the code related to the post-processing of the somatic (`somatic`) and germline (`germline`) variant files obtained with nf-core Sarek and nf-core OncoAnalyzer for normal versus tumor samples of the patient. These directories include the following files:

- `somatic`: This folder includes the code to perform the post-processing of the somatic variants.
  
  - `sarek_variants`: Reading and filtering variant data from original VCF files obtained with nf-core Sarek from Mutect2 and Strelka callers. Classify variant types (SNV and MNV and INDELs) and calculation of variant allele frequencies (VAF).
    
    > SAREK_processing_melanoma.ipynb <br>
    > SAREK_processing_sarc_pri.ipynb <br>
    > SAREK_processing_sarc_met.ipynb <br>
    
  - `oncoanalyzer_variants`: Reading and filtering variant data from original VCF files obtained with nf-core OncoAnalyzer from SAGE caller. Classify variant types (SNV and MNV and INDELs) and calculation of variant allele frequencies (VAF).

    > ONCOANALYSER_SAGE_processing_melanoma.ipynb <br>
    > ONCOANALYSER_SAGE_processing_sarc_pri.ipynb <br>
    > ONCOANALYSER_SAGE_processing_sarc_met.ipynb <br>
    
  - `consensus_mut`: Includes analysis of mutations passing quality filters from exported tables in `sarek_variants` and `oncoanalyser_variants` to obtain the final list of mutations that were identified in a minimum of 2 of the 3 callers (Mutect2, Strelka and SAGE) named consensus mutations and the calculation of VAF from this subset. Additionally it includes a mutation caller comparison based on the number of mutations identified in each sample as well as a comparison on the mutation type (from SNV and MNV to INDELs) identified in the consensus mutation set. A bash script is also provided that calculates percent reduction of the mutations upon quality filtering.
 
    > Caller_and_mutations_Comparison.ipynb <br>
    > Consensus_Mutations_melanoma.ipynb <br>
    > Consensus_Mutations_sarc_pri.ipynb <br>
    > Consensus_Mutations_sarc_met.ipynb <br>
    > Reduction.sh <br>
    
  - `clonality`: Includes analysis of consensus mutations (obtained in `consensus_mut`) to calculate the Cancer Cell Fraction (CCF) value. For CCF, Purity and Copy Number values were obtained from allele-specific copy number analysis software ASCAT (from Sarek pipeline) and Purple (from Oncoanalyser pipeline). Classification into clonal and subclonal mutations was performed based on CCF Purple files.
 
    > CCF_ASCAT_melanoma.ipynb <br>
    > CCF_ASCAT_sarc_pri.ipynb <br>
    > CCF_ASCAT_sarc_met.ipynb <br>
    > CCF_Purple_clonals_melanoma.ipynb <br>
    > CCF_Purple_clonals_sarc_pri.ipynb <br>
    > CCF_Purple_clonals_sarc_met.ipynb <br>
    
  - `phylogeny`: Compares the number of clonal mutations from `clonality` in each sample and computes a phylogenetic tree based on the similarities/disparities within. Also analyses the percent of mutations that are clonal.

- `germline`: This folder includes the code to perform the post-processing of the germline variants obtained with GATK Haplotypecaller tool from nf-core Sarek pipeline. Post-processing of the variants includes the quality filtering of the variants, the calculation of VAF and the addition of the mutation type (SNP, MNV and INDELs) considering biallelic sites. Additionally a comparison of the number of quality filtered germline samples from 4 pediatric patients is also provided.

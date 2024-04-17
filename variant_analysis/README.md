# Analysis of Variants

This folder contains the code related to the post-processing of the somatic (`somatic`) and germline (`germline`) variant files obtained with nf-core Sarek and nf-core OncoAnalyzer for normal versus tumor samples of the patient. These directories include the following files:

- `somatic`: This folder includes the code in Jupyter notebooks to perform the post-processing of the somatic variants.
  - `sarek_variants`: Reading and filtering variant data from original VCF files obtained with nf-core Sarek from Mutect2 and Strelka callers. Classify variant types (SNV and MNV and INDELs) and calculation of variant allele frequencies (VAF).
  - `oncoanalyzer_variants`: Reading and filtering variant data from original VCF files obtained with nf-core OncoAnalyzer from SAGE caller. Classify variant types (SNV and MNV and INDELs) and calculation of variant allele frequencies (VAF).
  - `consensus_mut`: Includes analysis of mutations passing filters from exported tables in `sarek_variants` and `oncoanalyser_variants` to obtain the final list of mutations that were identified in a minimum of 2 of the 3 callers (Mutect2, Strelka and SAGE) named consensus mutations and the calculation of VAF from this subset. Additionally it includes a mutation caller comparison based on the number of mutations identified in each sample as well a comparison on the mutation type (from SNV and MNV to INDELs) identified in the consensus mutation set.
  - `clonality`: Includes analysis of consensus mutations (obtained in `consensus_mut`) to calculate the Cancer Cell Fraction (CCF) value. For CCF, Purity and Copy Number values were obtained from allele-specific copy number analysis software ASCAT (from Sarek pipeline) and Purple (from Oncoanalyser pipeline). The analysis of clonal and subclonal mutations was performed from CCF Purple files. 
  - `phylogeny`:


   Also includes the `mutation_rate.ipynb` that was used to calculate the 

- `germline`: This folder includes the code in Jupyter notebooks to perform the post-processing of the germline variants obtained with GATK Haplotypecaller tool from nf-core Sarek pipeline.



        > fdsafjal.ipynb <br>
        > fjajlfsf.ipynb <br>
      
    fasdfasfadd from [fafassd](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.26/). This Refsafjkaklja

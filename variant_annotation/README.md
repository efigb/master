# Variant annotation

This folder contains the code related to the annotation of germline and somatic variant tables with VEP, including the code to create input files to run VEP (`vep_input`) and filtering of annotated variants (`variant_processing`). These directories include the following files:

- `vep_input`: This folder includes the code in Jupyter notebooks to create input files from germline variants and somatic variants in tumors.

  To run VEP variant data is required to be splitted into chromosomes. The following notebooks perform this conversion in each sample and store data in a VEP input directory:
  
   > VEP_input_chr_melanoma.ipynb <br>
   > VEP_input_chr_sarcoma.ipynb <br>
   > VEP_input_chr_lung.ipynb <br>
   > VEP_input_chr_germline.ipynb <br>
  
  The `qmap_files` folder includes the code to obtain a map jobs file to run VEP with [QMap](https://github.com/bbglab/qmap) in the cluster for specific samples. 

- `variant_processing`: This folder includes the code to perform the post-processing of the germline variants obtained with GATK Haplotypecaller tool from nf-core Sarek pipeline. Post-processing of the variants includes the quality filtering of the variants, the calculation of VAF and the addition of the mutation type (SNP, MNV and INDELs) considering biallelic sites.

  - `fasfa`: Reading fsaas
  - `fsaaf`: Reading afasaf 
   

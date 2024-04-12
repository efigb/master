# Whole Genome Sequencing (WGS) Analysis

This folder contains the code related to pre-processing of sequencing data, including `reads_mapping` and `variant_calling` using the conda environment `nf_nextflow.yml`. 

- `reads_mapping` includes the following:
  
    - `input_files`, cotaining jupyter notebook files to generate the input files in csv format to run nf-core sarek pipeline based on sequencing data table information.

        > SAREK_input_1.ipynb <br>
        > SAREK_input_2.ipynb <br>
      
      Each notebook generates one input file: the first one to run samples from blood and tumor 1 and tumor 2 (input_1) and the last to include tumor3 (input_2). The               resulting csv input files to run the pipeline are also included:

        > input.csv <br>
        > input_lung.csv <br>
        
    - `commands.txt`, containing the commands used to run sarek to map reads.

Reference Genome files to run sarek can be downloaded from [NCBI](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.26/). This Reference Genome is without ALT contigs.

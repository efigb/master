# Sequencing reads mapping: nf-core Sarek pipeline
This folder contains notebook files to generate the input csv files to run Sarek pipeline based on table with sequencing data information.
 > SAREK_input_1.ipynb<br>
 > SAREK_input_2.ipynb<br>

Notebook files to generate an input csv file to run Sarek pipeline based on table with sequencing data information. Each notebook generates one input file: the first one to run samples from blood and tumor 1 and tumor 2 (input_1) and the last  to include tumor3 together with blood sample (input_2).<br>
- Run Sarek:

    > run_Sarek.sh<br>

Bash script to run Sarek in terminal from input samples.<br>


To run sarek, first install and activate the conda environment mutcall.yml.

Reference Genome files to run sarek can be downloaded from here.

Notice that the Reference Genome used is without ALT contigs (this is the one used in hmf pipeline, platinum in gcloud). Explanation here.

commands.txt: The commands used to run sarek with mutect, strelka and ascat.
Input_for_sarek_normal_tissues_case3.ipynb: Notebook that explains how to prepare the input files.

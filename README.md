# FINAL MASTER PROJECT
#### Master in Bioinformatics, International University of Valencia (VIU) <br>Barcelona Biomedical Genomics Lab (BBGLab) https://bbglab.irbbarcelona.org/ <br>Institut de Recerca Biomèdica de Barcelona (IRB Barcelona)

This repository contains the code to reproduce the data from the final master project entitled *"Estudio de la evolución tumoral en un paciente pediátrico".* <br> **Student:**     Elisabet Figuerola Bou <br>**Supervisor:**     Mònica Sánchez Guixé <br>**Academic tutor:** Ángela Riffo<br>**Course:**     2023-2024


The following figure indicates the workflow used to reproduce all the results. 
A blood sample and three tumor samples of a pediatric patient were sequenced by Whole Genome Sequencing at depth of 30X and 120X, respectively, and obtained FASTQ files. This data was pre-processed with the nf-core sarek pipeline (https://github.com/nf-core/sarek) using GATK practices to obtain BAM files. Somatic mutations were called using the matched normal sample with the DNA analysis workflow from Hartwig Medical Foundation implemented in nf-core (nf-core oncoanalyser) (https://github.com/nf-core/oncoanalyser) in addition to the sarek pipeline, to obtain the VCF files. Germline variants were obtained with the sarek pipeline tool GATK haplotypecaller. Annotation of the variants was analysed with Variant Effect Predictor (VEP) tool from Ensembl (https://github.com/Ensembl/ensembl-vep). Creating all input files, reading and processing intermediate tables and compute graphical figures was performed with Jupyter notebooks and each process is shown in orange (further details in the following lines). <br>
<br>
![IMAGE](https://github.com/efigb/master/blob/main/Workflow.png?raw=true) <br>
Created with Biorender.com
<br>
<br>
**1.SAREK files:**<br>
- Input files:

    > SAREK_input_1.ipynb<br>
    > SAREK_input_2.ipynb<br>

Notebook files to generate an input csv file to run Sarek pipeline based on table with sequencing data information. Each notebook generates one input file: the first one to run samples from blood and tumor 1 and tumor 2 (input_1) and the last  to include tumor3 together with blood sample (input_2).<br>
- Run Sarek:

    > run_Sarek.sh<br>

Bash script to run Sarek in terminal from input samples.<br>

**2.Oncoanalyser files:**<br>

> nameofthefile.ipynb<br>

description

**3.VCF files analysis:**<br>
- SAREK caller analysis<br>

> nameofthefile.ipynb<br>

description

- Oncoanalyser caller analysis<br>

> nameofthefile.ipynb<br>

description

- Caller comparison<br>

> nameofthefile.ipynb<br>

description

- Common mutations<br>

> nameofthefile.ipynb<br>

description

- Phylogenetic analysis<br>

> nameofthefile.ipynb<br>

description

- Mutation rate<br>

> nameofthefile.ipynb<br>

description

**4.Variant annotation:**
- VEP input files

> nameofthefile.ipynb<br>

description

- Consequence types<br>

> nameofthefile.ipynb<br>

description

- Variant selection<br>

> nameofthefile.ipynb<br>

description

**5.Mutational signatures:**<br>

> nameofthefile.ipynb<br>

description
    

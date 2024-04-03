# FINAL MASTER PROJECT
#### Master in Bioinformatics, International University of Valencia (VIU)
#### Barcelona Biomedical Genomics Lab (BBGLab) https://bbglab.irbbarcelona.org/
#### Institut de Recerca Biomèdica de Barcelona (IRB Barcelona)

This repository contains the code to reproduce the data from the final master project entitled "Estudio de la evolución tumoral en un paciente pediátrico". 

Student:      Elisabet Figuerola Bou

Supervisor:     Mònica Sánchez Guixé

Academic tutor: Ángela Riffo

Course:         2023-2024


The following figure indicates the workflow used to reproduce all the results. 
A blood sample and two tumor samples of a pediatric patient were sequenced by Whole Genome Sequencing at depth of 30X and 120X, respectively, and obtained FASTQ files. This data was pre-processed with the nf-core sarek pipeline (https://github.com/nf-core/sarek) using GATK practices to obtain BAM files. The DNA analysis workflow from Hartwig Medical Foundation implemented in nf-core (nf-core oncoanalyser) was used in addition to the sarek pipeline for the variant calling (https://github.com/nf-core/oncoanalyser) to obtain the VCF files. All input files, reading files, processing intermediate tables and compute graphical figures were computed with Jupyter notebook and each process is shown in orange. 

![IMAGE](https://github.com/efigb/master/blob/main/Workflow.png?raw=true)


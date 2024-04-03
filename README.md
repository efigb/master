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
Sequencing data was pre-processed with the nf-core sarek pipeline (https://github.com/nf-core/sarek) using GATK practices to obtain BAM files. In addition to sarek pipeline, the DNA analysis workflow from Hartwig Medical Foundation implemented in nf-core (nf-core oncoanalyser) was used for the variant calling (https://github.com/nf-core/oncoanalyser). All input files, reading and processing intermediate tables and compute graphical figures were processed with Jupyter notebook and is shown in orange. 

![IMAGE](https://github.com/efigb/master/blob/Workflow.png?raw=true)

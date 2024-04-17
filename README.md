# FINAL MASTER PROJECT
#### Master in Bioinformatics, International University of Valencia (VIU) <br>Barcelona Biomedical Genomics Lab (BBGLab) https://bbglab.irbbarcelona.org/ <br>Institut de Recerca Biomèdica de Barcelona (IRB Barcelona)

This repository contains the code to reproduce the data from the final master project entitled *"Estudio de la evolución tumoral en un paciente pediátrico".* <br> **Student:**     Elisabet Figuerola Bou <br>**Supervisor:**     Mònica Sánchez Guixé <br>**Academic tutor:** Ángela Riffo<br>**Course:**     2023-2024


The following figure indicates the workflow used to reproduce all the results. 
A blood sample and three tumor samples of a pediatric patient were sequenced by Whole Genome Sequencing at depth of 30X and 120X, respectively, and obtained FASTQ files. This data was pre-processed with the [nf-core sarek pipeline](https://github.com/nf-core/sarek) using GATK practices to obtain BAM files. Somatic mutations were called using the matched normal sample with the DNA analysis workflow from Hartwig Medical Foundation implemented in nf-core ([nf-core oncoanalyser](https://github.com/nf-core/oncoanalyser)) in addition to the sarek pipeline, to obtain the VCF files. Germline variants were called with the sarek pipeline tool GATK haplotypecaller. Annotation of the variants was analysed with [Variant Effect Predictor (VEP)](https://github.com/Ensembl/ensembl-vep) tool from Ensembl. Creating all input files, reading and processing intermediate tables and compute graphical figures was performed with Jupyter notebooks, which are grouped in three main processes represented as a file icon (further details in the following lines). <br>
<br>
![IMAGE](https://github.com/efigb/master/blob/main/Github_Bioinfo_Workflow.png?raw=true) <br>
Created with Biorender.com
<br>
<br>

***
## Organization of the repository:

**1. Whole Genome Sequencing (WGS) Analysis** `wgs_analysis`

- **Mapping of Sequencing Reads** `reads_mapping`, contains data to run the Sarek pipeline and obtain the mapped reads in BAM file format.

- **Variant Calling** `variant_calling`, contains data to run nf-sarek `sarek` and nf-oncoanalyser `oncoanalyser` pipelines and obtain the corresponding variant files in VCF format.

**2. Variant Analysis** `variant_analysis`

 This section contains data related to the analysis of variants including filtering of variants, clonality and phylogenetic analyses and mutation rate. 
 
**3. Variant Annotation** `variant_vep`

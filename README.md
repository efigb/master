# FINAL MASTER PROJECT
#### Master in Bioinformatics, International University of Valencia (VIU) <br>Barcelona Biomedical Genomics Lab (BBGLab) https://bbglab.irbbarcelona.org/ <br>Institut de Recerca Biomèdica de Barcelona (IRB Barcelona)

This repository contains the code to reproduce the data from the final master project entitled *"Estudio de la evolución tumoral en un paciente pediátrico".* <br> **Student:**     Elisabet Figuerola Bou <br>**Supervisor:**     Mònica Sánchez Guixé <br>**Academic tutor:** Ángela Riffo<br>**Course:**     2023-2024


The following figure indicates the workflow used to reproduce all the results. 
A `blood` sample and three tumor samples (`tumor1 or melanoma`; `tumor2 or sarcoma-primary`; `tumor3 or sarcoma-metastasis`) of a pediatric patient were sequenced by Whole Genome Sequencing at depth of 30X and 120X, respectively, and obtained FASTQ files. This data was pre-processed with the [nf-core sarek pipeline](https://github.com/nf-core/sarek) using GATK practices to obtain BAM files. Somatic mutations were called using the matched normal sample with the DNA analysis workflow from Hartwig Medical Foundation implemented in nf-core ([nf-core oncoanalyser](https://github.com/nf-core/oncoanalyser)) in addition to the sarek pipeline, to obtain the VCF files. Germline variants were called with the sarek pipeline tool GATK haplotypecaller. Annotation of the variants was analysed with [Variant Effect Predictor (VEP)](https://github.com/Ensembl/ensembl-vep) tool from Ensembl. Creating all input files, reading and processing intermediate tables and compute graphical figures was performed with Jupyter notebooks, which are grouped in three main processes represented as a file icon (further details in the following lines). <br>
<br>
![IMAGE](https://github.com/efigb/master/blob/main/Github_Bioinfo_Workflow.png?raw=true) <br>
Created with Biorender.com
<br>
<br>

***
## Organization of the repository and location of Figures:

**1. Whole Genome Sequencing (WGS) Analysis** `wgs_analysis`

- **Mapping of Sequencing Reads** `reads_mapping`, contains data to run the Sarek pipeline and obtain the mapped reads in BAM file format.

- **Variant Calling** `variant_calling`, contains data to run nf-sarek `sarek` and nf-oncoanalyser `oncoanalyser` pipelines and obtain the corresponding variant files in VCF format.

**2. Variant Analysis** `variant_analysis`

 This section contains data related to the analysis of somatic and germline variants including filtering of variants, clonality and phylogenetic analyses. 

 2.1 Germline variants `germline`:<br>
 
  **Figure 9B**<br>
  **Figure 9C**<br>
   
 2.2 Somatic variants `somatic`:<br>
 - `consensus_mut`: <br>
  **Figure 10** <br>
  **Figure 11** <br>
  **Figure 12A** <br>
  **Figure 13**<br>
 - `clonality`:<br>
  **Figure 14** <br>
  **Figure 15** <br>
 - `phylogeny`:<br>
  **Figure 16** <br>
 
**3. Variant Annotation** `variant_annotation`

 This section contains the code to run VEP: split the variant tables into chromosome files, the code to writte a [QMap](https://github.com/bbglab/qmap) jobs file to parallelize jobs and the final QMap files.

## Conda environment:
 `tfm_environment.yml`: This is the main conda environment used in this project in all jupiter notebooks as kernel.
 Some analysis include other conda environments which can be found in the according directory.
 
**4. Variant Filtering** `variant_filtering`

 This section contains filtering of annotated variants in previous section and selection of variants that are protein damaging and cancer drivers from [intOGen](https://www.intogen.org/about). <br>
  **Figure 17**

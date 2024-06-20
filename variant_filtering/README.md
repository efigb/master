# Variant filtering

This folder contains the code related to the filtering of somatic variant tables and the selection of damaging variants.

  To filter variants based on [MANE Select and MANE Plus Clinical](https://www.ensembl.org/info/genome/genebuild/mane.html) and Ensembl predicted consequences [Ensembl-Predicted Variant Consequences](https://www.ensembl.org/info/genome/variation/prediction/predicted_data.html). The following notebooks and script perform this filtering in samples:
  
   > VEP_filtering_Sarcoma-pri.ipynb <br>
   > VEP_filtering_Sarcoma-met.ipynb <br>
   > VEP_filtering_Melanoma.py <br>
  
  The `QMAP_file_filter_Melanoma.ipynb` file includes the code to obtain a map jobs file (`Melanoma_filter.qmap`)to run the script with [QMap](https://github.com/bbglab/qmap) in the cluster for melanoma sample.

 Finally filtered by its effect at the protein level and its prediction as cancer drivers based on [intOGen](https://www.intogen.org/search) data is included in `Damaging_variants_selection.ipynb`.

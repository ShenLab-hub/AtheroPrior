# AtheroPrior
Code and datasets for mechanism-guided prioritization of environmental chemicals with atherogenic potential.

Data integration

This script illustrates the data integration procedure used in this study.

The master dataset (logP_BCF_CompTox.csv) was sequentially merged with individual assay datasets using the unique chemical identifier DTXSID.

For each integration step, only the input filename (input_file_2) and the corresponding columns (new_columns) need to be updated according to the dataset being merged.

The same procedure was applied to integrate the following datasets:

processed ATG_DR4_LXR_CIS;
processed TOX21_FXR_BLA_Antagonist_ch1;
processed TOX21_PPARg_BLA_Antagonist_ch1;
processed TOX21_PXR_agonist;
Predicted_concentration_in_human_blood.

Ultimately, all datasets were integrated into a single file, integrated_dataset.csv, which served as the input for ToxPi analysis.

This repository provides the script using the TOX21_PPARg_BLA_Antagonist_ch1 dataset as an example. The identical workflow was repeated for the remaining datasets.

## Data sources

The file "Predicted_concentration_in_human_blood.csv" is not distributed in this repository.
It can be downloaded from the supplementary materials of:

HExpPredict: in vivo exposure prediction of human blood exposome using a random forest model and its application in chemical risk prioritization.
Environmental Health Perspectives. 2023;131(3):37009.
https://doi.org/10.1289/EHP11305

# FastQC and MultiQC Analysis Repository

## Overview
This repository contains results from FastQC and MultiQC analyses used for assessing the quality of raw sequence data from high throughput sequencing pipelines.

## Repository Contents
- `SRR12816729_fastqc.html`: FastQC report for sample SRR12816729.
- `SRR12951228_fastqc.html`: FastQC report for sample SRR12951228.
- `multiqc_report.html`: Comprehensive report generated by MultiQC that summarizes the FastQC results.

## FastQC Analysis
FastQC provides several key plots to assess data quality:
- **Per Base Sequence Quality**: Shows the quality scores across all bases at each position in the reads.
- **Sequence Duplication Levels**: Displays the level of duplication for each sequence, highlighting potential contamination.
- and much more

## MultiQC Report
MultiQC compiles data from multiple FastQC reports to create an overview of the dataset:
- **Aggregate Quality Scores Plot**: This plot combines the quality scores from all samples, giving a snapshot of the overall sequencing quality.
- **Duplication Levels Overview**: Summarizes the duplication statistics across all samples, which can indicate the efficiency of the sequencing process.
- Etc...

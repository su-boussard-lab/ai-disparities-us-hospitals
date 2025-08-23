# 1. Title  
**AI Implementation in U.S. Hospitals: Regional Disparities and System-Level Implications**

# 2. Abstract  
AI has the potential to improve healthcare delivery, but uneven geographic adoption and implementation can reinforce existing care gaps and inefficiencies. We analyzed data from 3560 U.S. hospitals using the 2023 American Hospital Association (AHA) Annual Survey, 2023-2024 AHA IT Supplement,  community-level socioeconomic indicators, and 2023-2025 Center for Medicare & Medicaid Services (CMS) hospital quality metrics to assess: where AI is implemented, what factors are associated with implementation, and patterns of early AI adoption across geographic regions. We found that hospital AI implementation is significantly clustered, with geographic hotspots and coldspots of adoption. Regions with higher healthcare access need indicators were less likely to have hospitals with AI-based predictive models. Geographically weighted regression reveals that factors associated with AI implementation vary by region, suggesting that adoption patterns reflect diverse local contexts and institutional characteristics. These findings provide a baseline understanding of early AI deployment patterns in U.S. hospitals. Future efforts should develop standardized, detailed, and model-specific AI implementation metrics and consider local context rather than pursuing uniform deployment strategies.


# 3. File Organization  

## General Notes  
- **Notebook Purpose**: These notebooks are organized for transparency and easier interpretation.  
- **Future Code Release**: A more modular and reproducible version of the codebase (in `.py` scripts) will be shared after the peer review process is complete.  
- **Cell Outputs**: All notebook outputs have been cleared.  
- **Data Notice**: This project uses a mix of proprietary and publicly available datasets.  
  - AHA data requires a subscription and cannot be shared.  
  - Public datasets are cited in the manuscript, linked in the corresponding notebooks, and in Section 4 (Datasets).  
- **Code Availability**: This repository includes the core analysis code used in the study. Some portions have been simplified for clarity and readability (e.g., repeated applications of similar functions or complex troubleshooting steps).  
  If the user has access to all necessary data (including proprietary datasets) and needs the full executable code for replication, please contact the corresponding author (ymh@stanford.edu).  
- **Notebook Documentation**: Each notebook includes a description of its purpose and workflow.  
- **Folder Structure**: Files are organized alphabetically to reflect the analysis workflow.


## Notebooks  

### A. Data Preprocessing  
- `A0_data_collection`: Describes data collection process and source. 
- `A1_preprocessing_hospital`: Processes AHA Annual Survey and IT Supplement data.  
- `A2_preprocessing_geodata`: Processes community-level geographic variables.  
- `A3_preprocessing_healthoutcome`: Processes CMS hospital quality metric data.

### B. Descriptive Statistics  
- `B1_table_one`: Generates descriptive statistics.  
- `B2_concordance_analysis`: Assesses alignment between healthcare need and AI implementation.

### C. Spatial Analysis  
- `C1_visualization_distribution`: Visualizes the geographic distribution of hospital AI implementation.  
- `C2_cluster_analysis`: Measures spatial autocorrelation and characterizes clusters.  
- `C3_hotspot_national_analysis`: Identifies hotspots and coldspots of AI adoption nationwide.  
- `C4_hotspot_regional_analysis`: Identifies hotspots and coldspots at the state and census division level.  
- `C5_GWR`: Runs geographically weighted regression of hospital/community factors on AI implementation.

### D. Longitudinal Analysis  
- `D1_feature_importance`: Uses random forest to identify key features predicting AI/ML implementation.  
- `D2_longitudinal_analysis`: Assesses whether AI implementation level is associated with changes in hospital care quality over time.


# 4. Datasets
#### Hospital Data  
- 2023 and 2024 AHA Data (https://www.ahadata.com/) - proprietary data. requires subscription for access
#### Community Data 
- Zipcode & Hospital Service Area Crosswalk Data (https://data.dartmouthatlas.org/supplemental/#crosswalks)
- 2023 Area Deprivation Index (https://www.neighborhoodatlas.medicine.wisc.edu/)
- 2022 Social Vulnerability Index (https://www.atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html)
- Hospital Professional Shortage Area & Medically Underserved Area (https://data.hrsa.gov/data/download?data=SHORT#SHORT)
- Census API (https://www.census.gov/data/developers/data-sets.html)
#### Hospital Care Quality Data 
- CMS Hospital Care Quality (https://data.cms.gov/provider-data/archived-data/hospitals)


# 5. Environment

Use `environment.yml` to recreate the environment.


# 6. Preprint

This study is currently under review.  
Preprint available at: https://www.medrxiv.org/content/10.1101/2025.06.27.25330441v1


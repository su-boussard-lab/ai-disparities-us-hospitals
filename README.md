# 1. Title  
**AI Implementation in U.S. Hospitals: Regional Disparities and System-Level Implications**

# 2. Abstract  
AI has the potential to improve healthcare delivery, but uneven geographic adoption and implementation can reinforce existing care gaps and inefficiencies. We analyzed data from 3092 U.S. hospitals using the 2023 American Hospital Association (AHA) Data, community-level socioeconomic indicators, and 2023-2025 CMS hospital quality metrics to assess: where AI is implemented, what factors drive implementation, and how AI is associated with hospital quality. We found that hospital AI implementation is significantly clustered. Over 67% of deployments were misaligned with potential healthcare needs. Clustering and hotspot analysis identified regions with high and low AI adoption to guide targeted deployment interventions. Geographically weighted regression reveals that factors driving AI implementation vary by region, suggesting universal strategies may be ineffective. These findings underscore the urgent need for region-specific strategies to ensure AI implementation aligns with healthcare delivery needs and improves outcomes across all geographic regions.


# 3. File Organization  

## General Notes  
- **Cell Outputs**: All notebook outputs have been cleared.  
- **Data Notice**: This project uses a mix of proprietary and publicly available datasets.  
  - AHA data requires a subscription and cannot be shared.  
  - Public datasets are cited in the manuscript and linked in the notebooks.  
- **Code Availability**: This repository includes the core analysis code used in the study. Some portions have been simplified for clarity and readability (e.g., repeated applications of similar functions, or complex troubleshooting steps).  
  If the user has access to all necessary data (including proprietary datasets) and needs the full, executable code for replication, please contact the corresponding author (ymh@stanford.edu).  
- **Notebook Documentation**: Each notebook includes a description of its purpose and workflow.  
- **Folder Structure**: Files are organized alphabetically to reflect the analysis workflow.

## Notebooks  

### A. Data Preprocessing  
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


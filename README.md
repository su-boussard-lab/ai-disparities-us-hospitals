## 1. Title
### AI Implementation in U.S. Hospitals: Regional Disparities and System-Level Implications 

## 2. Abstract
AI has the potential to improve healthcare delivery, but uneven geographic adoption and implementation can reinforce existing care gaps and inefficiencies. We analyzed data from 3092 U.S. hospitals using the 2023 American Hospital Association (AHA) Data, community-level socioeconomic indicators, and 2023-2025 CMS hospital quality metrics to assess: where AI is implemented, what factors drive implementation, and how AI is associated with hospital quality. We found that hospital AI implementation is significantly clustered. Over 67% of deployments were misaligned with potential healthcare needs Clustering and hotspot analysis identify regions with high and low AI adoption to guide targeted deployment interventions. Geographically weighted regression reveals that factors driving AI implementation vary by region, suggesting universal strategies may be ineffective. AI holds transformative potential for healthcare, yet adoption is geographically clustered and often misaligned with areas of greatest need. These findings underscore the urgent need for region-specific strategies to ensure AI implementation aligns with healthcare delivery needs and improves outcomes across all geographic regions.

##  2. File Organization

- **Cell Outputs**: All outputs have been cleared.  
- **Data Notice**: This project uses a mix of proprietary and publicly available datasets. Proprietary AHA data requires a subscription. Public datasets are cited in the manuscript and linked in the notebooks.  
- **File Structure**: Folders and files are organized alphabetically to reflect the analysis workflow.  
- **Notebook Documentation**: Each notebook includes a brief description of its purpose and workflow.  
- **Code Annotations**: Portions of the code were cleaned and annotated using ChatGPT-4o for readability.


#### **A_preprocessing_data**: Code for Data Preprocessing

- **A1_preprocessing_hospital**: Processes AHA annual survey and IT supplement 
- **A2_preprocessing_geodata**: Process geographical community variables  
- **A3_preprocessing_healthoutcome**: Process CMS quality metric data 
  
#### **B_descriptive_stat**: Code for Descriptive Statistics 

- **B1_table_one**: Generate descriptive statistics 
- **B2_concordance_analysis**: Assess alignment between healthcare need and AI implementation levels


#### **C_spatial_analysis**: Code for Spatial Analysis

- **C1_visualization_distribution**: Visualize the geographic distribution of hospitals in the U.S. based on their level of AI implementation
- **C2_cluster_analysis**: Characterize spatial autocorrelation and identify statistically significant clusters, 
- **C3_hotspot_national_analysis** : Identify statistically significant hotspots and coldspots of hospital AI adoption across the United States
- **C4_hotspot_regional_analysis** : Identify statistically significant hotspots and coldspots of hospital AI adoption across the United States in census division and state level 
- **C5_GWR** : Run geographically weighted regression between hosptial/community characteristics and AI implementation level


#### **D_longitudinal_analysis**: Code for Longitudinal Analysis

- **D1_feature_importance**: Conduct machine learning (random forest) to identify the most important feature predicting the AI/ML implementation level
- **D2_longitudinal_analysis**: Assess whether AI implementation level affects the change in hospital care quality overtime

# 1. Title
**The Landscape of AI Implementation in U.S. Hospitals**

# 2. Abstract
AI has the potential to improve healthcare delivery, but uneven adoption and implementation can reinforce existing care gaps and inefficiencies. We analyzed data from 3,560 U.S. hospitals using the 2023 American Hospital Association (AHA) Annual Survey, 2023–2024 AHA IT Supplement, community-level socioeconomic indicators, and 2023–2025 Center for Medicare & Medicaid Services (CMS) hospital quality metrics to examine: where AI is implemented, what factors are associated with implementation, and patterns of early AI adoption across geographic regions. We found that hospital AI implementation is significantly clustered, with hotspots and coldspots of adoption. Regions with higher healthcare access needs were less likely to have hospitals with AI-based predictive models. Geographically weighted regression showed that factors associated with predictive AI implementation vary by region, suggesting that adoption patterns reflect diverse local contexts and institutional characteristics. These findings provide a baseline snapshot of early AI deployment patterns in U.S. hospitals in 2023 and 2024, highlighting the uneven and context-dependent nature of implementation. Future efforts should develop standardized, detailed, model-specific AI implementation metrics and account for local context rather than pursuing uniform deployment strategies.

# 3. File Organization

## General Notes
- **Notebook purpose:** Organized for transparency and ease of interpretation.  
- **Cell outputs:** All notebook outputs have been cleared.  
- **Data notice:** This project uses a mix of proprietary and publicly available datasets. AHA data require a subscription and cannot be shared. Public datasets are cited in the manuscript, linked in the corresponding notebooks, and listed in Section 4 (*Datasets*).  
- **Code availability:** Researchers with access to the necessary datasets may contact the corresponding author (ymh@stanford.edu) for executable support or additional details.  
- **Notebook documentation:** Each notebook includes a description of its purpose and workflow.  
- **Folder structure:** Files are organized alphabetically to reflect the analysis workflow.

## Notebooks
### A. Data Preprocessing
- `A0_data_collection`: Describes data collection process and sources.  
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

### D. Feature Importance
- `D1_feature_importance`: Uses random forest to identify key features predicting AI/ML implementation.  

### E. Exploratory Analysis
- `E1_longitudinal_analysis`: Assesses whether AI implementation level is associated with changes in hospital care quality over time.

# 4. Datasets

### Hospital Data
- **2023–2024 AHA Annual Survey and IT Supplement** — proprietary data; subscription required for access ([AHA Data Portal](https://www.ahadata.com/))

### Community Data
- Zip Code & Hospital Service Area Crosswalk Data — [Dartmouth Atlas](https://data.dartmouthatlas.org/supplemental/#crosswalks)  
- 2023 Area Deprivation Index — [University of Wisconsin Neighborhood Atlas](https://www.neighborhoodatlas.medicine.wisc.edu/)  
- 2022 Social Vulnerability Index — [CDC/ATSDR](https://www.atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html)  
- Hospital Professional Shortage Area & Medically Underserved Area — [HRSA Data Portal](https://data.hrsa.gov/data/download?data=SHORT#SHORT)  
- Census API — [U.S. Census Bureau](https://www.census.gov/data/developers/data-sets.html)

### Hospital Care Quality Data
- **CMS Hospital Care Quality** — [Centers for Medicare & Medicaid Services](https://data.cms.gov/provider-data/archived-data/hospitals)

# 5. System Requirements and Installation Guide

### 5.1 System Requirements
- Operating System: macOS 15.6.1  
- Python Version: 3.11.11  
- Hardware: No special hardware requirements  
- Dependencies: All required packages are listed in `environment.yml`

### 5.2 Installation Guide
Estimated install time: 2–5 minutes on a standard laptop.

1. **Install Conda**  

We recommend using [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).

2. **Clone the repository**
```
git clone https://github.com/su-boussard-lab/ai-disparities-us-hospitals.git
```
3. **Go to project folder**
```
cd ai-disparities-us-hospitals
```
4. **Create conda environment** 
```
conda env create -f environment.yml
```
# 6. Expected Output and Run Time 

### 6.1 Expected Output 
The Jupyter Notebook walks through the full data engineering and analysis pipeline using placeholder structures. While no output is generated without the proprietary dataset, each code cell will display:
- Print statements confirming processing steps
- Comments describing expected results (e.g., summary tables, visualizations)

### 6.2 Expected Run Time 
Each notebook cell executes in approximately **3 to 60 seconds** on a standard laptop (tested on macOS 15.6.1 with Apple M1, 16 GB RAM).  
Total runtime for the full notebook is approximately **10–15 minutes**, depending on the system and any skipped cells.

# 6. Preprint

This study is currently under review.  
Preprint available at: https://www.medrxiv.org/content/10.1101/2025.06.27.25330441v1


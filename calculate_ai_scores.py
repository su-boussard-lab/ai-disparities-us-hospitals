# load necessary functions 
import pandas as pd

def create_union_aipred_row(row):
    """
    Create unified aipred value for a single row.
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        int: Unified aipred value
    """
    # Check if 2024 format questions are available and not null
    if pd.notna(row['predml_it']) or pd.notna(row['predoth_it']):
        # 2024 format - hierarchical approach
        if row['predml_it'] == 1:
            return 1
        elif row['predoth_it'] == 1:
            return 2
        else:
            return 3
    else:
        # 2023 format - return existing column
        return row['aipred_it']


def calculate_base_ai_implementation_row(row):
    """
    Calculate base AI implementation score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: Base AI implementation score
    """
    # Base AI implementation score (continuous)
    # Return None if the input value is null
    
    if pd.isna(row['aipred_it_union']):
        return None
    elif row['aipred_it_union'] == 1:  # Machine Learning
        return 2
    elif row['aipred_it_union'] == 2:  # Other Non-Machine Learning Predictive Models
        return 1
    else:  # Neither (3) or Do not know (4)
        return 0

def calculate_base_ai_implementation_row_imputed(row):
    """
    Calculate base AI implementation score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: Base AI implementation score
    """
    # Base AI implementation score (continuous)
    # Return None if the input value is null
    
    if pd.isna(row['aipred_it_union']):
        return 0
    elif row['aipred_it_union'] == 1:  # Machine Learning
        return 2
    elif row['aipred_it_union'] == 2:  # Other Non-Machine Learning Predictive Models
        return 1
    else:  # Neither (3) or Do not know (4)
        return 0

def calculate_ai_implementation_breadth_row(row):
    """
    Calculate AI implementation breadth score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: AI implementation breadth score
    """
    # Start with base score
    base_score = calculate_base_ai_implementation_row(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0
    else:
        breadth_score = base_score
        # Implementation Breadth Score - count use cases
        use_case_cols = ['aitraj_it', 'airfol_it', 'aimhea_it', 'airect_it', 
                     'aibill_it', 'aische_it', 'aipoth_it', 'aicloth_it']
        for col in use_case_cols:
            if row[col] is None:
                breadth_score += 0
            else:
                breadth_score += row[col] * 0.25  # 0.25 points per use case
        return breadth_score

def calculate_ai_implementation_breadth_row_imputed(row):
    """
    Calculate AI implementation breadth score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: AI implementation breadth score
    """
    # Start with base score
    base_score = calculate_base_ai_implementation_row_imputed(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0
    else:
        breadth_score = base_score
        # Implementation Breadth Score - count use cases
        use_case_cols = ['aitraj_it', 'airfol_it', 'aimhea_it', 'airect_it', 
                     'aibill_it', 'aische_it', 'aipoth_it', 'aicloth_it']
        for col in use_case_cols:
            if row[col] is None:
                breadth_score += 0
            else:
                breadth_score += row[col] * 0.25  # 0.25 points per use case
        return breadth_score

def calculate_ai_development_row(row):
    """
    Calculate AI development score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: AI development score
    """
    # Start with base score
    base_score = calculate_base_ai_implementation_row(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0 
    else:
        dev_score = base_score
        if 'mlsed_it' in row and pd.notna(row['mlsed_it']):
            dev_score += row['mlsed_it'] * 2  # Self-developed
        if 'mldev_it' in row and pd.notna(row['mldev_it']):
            dev_score += row['mldev_it']  # EHR developer
        if 'mlthd_it' in row and pd.notna(row['mlthd_it']):
            dev_score += row['mlthd_it']  # Third-party
        if 'mlpubd_it' in row and pd.notna(row['mlpubd_it']):
            dev_score += row['mlpubd_it'] * 0.5  # Public domain
        return dev_score
    
def calculate_ai_development_row_imputed(row):
    """
    Calculate AI development score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: AI development score
    """
    # Start with base score
    base_score = calculate_base_ai_implementation_row_imputed(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0 
    else:
        dev_score = base_score
        if 'mlsed_it' in row and pd.notna(row['mlsed_it']):
            dev_score += row['mlsed_it'] * 2  # Self-developed
        if 'mldev_it' in row and pd.notna(row['mldev_it']):
            dev_score += row['mldev_it']  # EHR developer
        if 'mlthd_it' in row and pd.notna(row['mlthd_it']):
            dev_score += row['mlthd_it']  # Third-party
        if 'mlpubd_it' in row and pd.notna(row['mlpubd_it']):
            dev_score += row['mlpubd_it'] * 0.5  # Public domain
        return dev_score

def calculate_ai_evaluation_row2023(row):
    """
    Calculate AI evaluation score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: AI evaluation score
    """
    # Start with base score
    base_score = calculate_base_ai_implementation_row(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0
    else:
        eval_score = base_score
        # For model accuracy (MLACCU)
        if row['mlaccu_it'] is None:
            eval_score += 0
        elif row['mlaccu_it'] == 1:  # All models
            eval_score += 1
        elif row['mlaccu_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mlaccu_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mlaccu_it'] == 4:  # Few models
            eval_score += 0.25
        # For None (5) or Do not know (6), no points added
    
    # For model bias (MLBIAS)
        if row['mlbias_it'] is None:
            eval_score += 0
        elif row['mlbias_it'] == 1:  # All models
            eval_score += 1
        elif row['mlbias_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mlbias_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mlbias_it'] == 4:  # Few models
            eval_score += 0.25
        # For None (5) or Do not know (6), no points added
    
        return eval_score
    

def calculate_ai_evaluation_row2023_imputed(row):
    """
    Calculate AI evaluation score for a single row (hospital).
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        float: AI evaluation score
    """
    # Start with base score
    base_score = calculate_base_ai_implementation_row_imputed(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0
    else:
        eval_score = base_score
        # For model accuracy (MLACCU)
        if row['mlaccu_it'] is None:
            eval_score += 0
        elif row['mlaccu_it'] == 1:  # All models
            eval_score += 1
        elif row['mlaccu_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mlaccu_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mlaccu_it'] == 4:  # Few models
            eval_score += 0.25
        # For None (5) or Do not know (6), no points added
    
    # For model bias (MLBIAS)
        if row['mlbias_it'] is None:
            eval_score += 0
        elif row['mlbias_it'] == 1:  # All models
            eval_score += 1
        elif row['mlbias_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mlbias_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mlbias_it'] == 4:  # Few models
            eval_score += 0.25
        # For None (5) or Do not know (6), no points added
    
        return eval_score
    
def calculate_ai_evaluation_row2024(row):
    """Calculate AI evaluation score for 2024 survey data."""
    if (row['data_source_year_it'] == 2023):
        return None
    base_score = calculate_base_ai_implementation_row(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0
    else:
        eval_score = base_score
        
        # Model Accuracy (MLACCU)
        if row['mlaccu_it'] == 1:  # All models
            eval_score += 1.0
        elif row['mlaccu_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mlaccu_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mlaccu_it'] == 4:  # Few models
            eval_score += 0.25
        
        # Model Bias (MLBIAS)
        if row['mlbias_it'] == 1:  # All models
            eval_score += 1.0
        elif row['mlbias_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mlbias_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mlbias_it'] == 4:  # Few models
            eval_score += 0.25
        
        # Post-implementation Evaluation (MLEVAL)
        if row['mleval_it'] == 1:  # All models
            eval_score += 1.0
        elif row['mleval_it'] == 2:  # Most models
            eval_score += 0.75
        elif row['mleval_it'] == 3:  # Some models
            eval_score += 0.5
        elif row['mleval_it'] == 4:  # Few models
            eval_score += 0.25
        
        # Governance accountability count
        governance_count = sum([
            row['aemdse_it'] == 1,   # Senior Executive
            row['aemsctf_it'] == 1,  # ML Committee
            row['aemdsc_it'] == 1,   # Clinical Committee
            row['aemdepl_it'] == 1,  # Dept Leaders
            row['aemits_it'] == 1    # IT Staff
        ])
        
        # Add governance points (simple additive)
        eval_score += governance_count * 0.25  # 0.25 per governance mechanism
        
        return eval_score
    

def calculate_ai_evaluation_row2024_imputed(row):
    """Calculate AI evaluation score for 2024 survey data."""
    if (row['data_source_year_it'] == 2023):
        return None
    base_score = calculate_base_ai_implementation_row_imputed(row)
    if base_score is None:
        return None
    elif base_score == 0:
        return 0
    else:
        eval_score = base_score
        
        # Model Accuracy (MLACCU)
        if row.get('mlaccu_it') == 1:  # All models
            eval_score += 1.0
        elif row.get('mlaccu_it') == 2:  # Most models
            eval_score += 0.75
        elif row.get('mlaccu_it') == 3:  # Some models
            eval_score += 0.5
        elif row.get('mlaccu_it') == 4:  # Few models
            eval_score += 0.25
        
        # Model Bias (MLBIAS)
        if row.get('mlbias_it') == 1:  # All models
            eval_score += 1.0
        elif row.get('mlbias_it') == 2:  # Most models
            eval_score += 0.75
        elif row.get('mlbias_it') == 3:  # Some models
            eval_score += 0.5
        elif row.get('mlbias_it') == 4:  # Few models
            eval_score += 0.25
        
        # Post-implementation Evaluation (MLEVAL)
        if row.get('mleval_it') == 1:  # All models
            eval_score += 1.0
        elif row.get('mleval_it') == 2:  # Most models
            eval_score += 0.75
        elif row.get('mleval_it') == 3:  # Some models
            eval_score += 0.5
        elif row.get('mleval_it') == 4:  # Few models
            eval_score += 0.25
        
        # Governance accountability count
        governance_count = sum([
            row.get('aemdse_it') == 1,   # Senior Executive
            row.get('aemsctf_it') == 1,  # ML Committee
            row.get('aemdsc_it') == 1,   # Clinical Committee
            row.get('aemdepl_it') == 1,  # Dept Leaders
            row.get('aemits_it') == 1    # IT Staff
        ])
        
        # Add governance points (simple additive)
        eval_score += governance_count * 0.25  # 0.25 per governance mechanism
        
        return eval_score

def calculate_llm_readiness_score(row):
    if row.get('llmhos_it') == 1:  # No
        return 0
    elif row.get('llmhos_it') == 2 :  # Currently using
        return 3
    elif row.get('llmhos_it') == 3 :  # Plan next year
        return 2
    elif row.get('llmhos_it') == 4 :  # Plan next 5 years
        return 1
    else:  # Don't know
        return None
    
def calculate_all_ai_scores_row(row):
    """
    Calculate all AI/ML implementation scores as continuous measures for a single row.
    
    Args:
        row: A pandas Series representing a single hospital row
        
    Returns:
        dict: Dictionary with all calculated scores
    """
    # Calculate all scores
    base_score = calculate_base_ai_implementation_row(row)
    breadth_score = calculate_ai_implementation_breadth_row(row)
    dev_score = calculate_ai_development_row(row)
    eval2023_score = calculate_ai_evaluation_row2023(row)
    eval2024_score = calculate_ai_evaluation_row2024(row)
    llm_readiness_score = calculate_llm_readiness_score(row)
    base_score_imputed = calculate_base_ai_implementation_row_imputed(row)
    breadth_score_imputed = calculate_ai_implementation_breadth_row_imputed(row)
    dev_score_imputed = calculate_ai_development_row_imputed(row)
    eval2023_score_imputed = calculate_ai_evaluation_row2023_imputed(row)
    eval2024_score_imputed = calculate_ai_evaluation_row2024_imputed(row)
    
    return {
        'ai_base_score': base_score,
        'ai_base_breadth_score': breadth_score,
        'ai_base_dev_score': dev_score,
        'ai_base_eval_score_2023': eval2023_score, 
        'ai_base_eval_score_2024': eval2024_score, 
        'llm_readiness_score': llm_readiness_score,
        'ai_base_score_imputed': base_score_imputed,
        'ai_base_breadth_score_imputed': breadth_score_imputed,
        'ai_base_dev_score_imputed': dev_score_imputed,
        'ai_base_eval_score_2023_imputed': eval2023_score_imputed, 
        'ai_base_eval_score_2024_imputed': eval2024_score_imputed, 
    }



def apply_ai_scores_to_dataframe(df):
    """
    Apply all AI score calculations row by row to a dataframe.
    
    Args:
        df: A pandas DataFrame with hospital data
        
    Returns:
        pandas.DataFrame: DataFrame with added AI score columns
    """
    # Initialize empty columns for scores
    df['ai_base_score'] = float('nan')
    df['ai_base_breadth_score'] = float('nan')
    df['ai_base_dev_score'] = float('nan')
    df['ai_base_eval_score_2023'] = float('nan')
    df['ai_base_eval_score_2024'] = float('nan')
    df['llm_readiness_score'] = float('nan')
    df['ai_base_score_imputed'] = float('nan')
    df['ai_base_breadth_score_imputed'] = float('nan')
    df['ai_base_dev_score_imputed'] = float('nan')
    df['ai_base_eval_score_2023_imputed'] = float('nan')
    df['ai_base_eval_score_2024_imputed'] = float('nan')
    
    # Apply row by row calculations
    for index, row in df.iterrows():
        scores = calculate_all_ai_scores_row(row)
        for score_name, score_value in scores.items():
            df.at[index, score_name] = score_value
    
    return df

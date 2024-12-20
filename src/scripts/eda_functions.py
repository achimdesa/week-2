import numpy as np

def basic_metrics(df):
    return df.describe()

def compute_dispersion(df, columns):
    dispersions = {}
    for col in columns:
        dispersions[col] = {'variance': np.var(df[col]), 'std_dev': np.std(df[col])}
    return dispersions

def bivariate_analysis(df, target_col, features):
    correlations = {}
    for feature in features:
        if feature in df.columns:
            correlations[feature] = df[[feature, target_col]].corr().iloc[0, 1]
        else:
            print(f"Feature '{feature}' not found in the DataFrame columns")
    return correlations

def compute_correlation_matrix(df, columns):
    return df[columns].corr()

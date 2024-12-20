# import pandas as pd

# def load_data(filepath):
#     """Load the CSV file into a Pandas DataFrame."""
#     return pd.read_csv(filepath)

# def clean_data(df):
#     """Clean the data by filling missing values for numeric columns with the column mean."""
#     numeric_cols = df.select_dtypes(include=["number"]).columns
#     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#     return df

# def segment_users(df, duration_col):
#     """Segment users into decile classes based on session duration and compute total data."""
#     df['decile_class'] = pd.qcut(df[duration_col], 5, labels=False) + 1
#     df['total_data'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
#     return df

# def aggregate_experience_metrics(df):
#     """Aggregate experience metrics per customer."""
#     return df.groupby('MSISDN/Number').agg({
#         'TCP DL Retrans. Vol (Bytes)': 'mean',
#         'Avg RTT DL (ms)': 'mean',
#         'Avg Bearer TP DL (kbps)': 'mean',
#         'Handset Type': 'first'
#     }).reset_index()

# def get_top_handsets(df, top_n=10):
#     """Get the top 10 handsets used by the customers."""
#     return df['Handset Type'].value_counts().head(top_n)

# def get_top_manufacturers(df, top_n=3):
#     """Get the top 3 handset manufacturers."""
#     return df['Handset Manufacturer'].value_counts().head(top_n)

# def get_top_handsets_per_manufacturer(df, manufacturers):
#     """Get the top handsets for each of the top 3 manufacturers."""
#     result = {}
#     for manufacturer in manufacturers:
#         result[manufacturer] = df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
#     return result

import pandas as pd

def load_data(filepath):
    """Load the CSV file into a Pandas DataFrame."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Clean the data by filling missing values for numeric columns with the column mean."""
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    return df

def segment_users(df, duration_col):
    """Segment users into decile classes based on session duration and compute total data."""
    df['decile_class'] = pd.qcut(df[duration_col], 5, labels=False) + 1
    df['total_data'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    return df

def aggregate_experience_metrics(df):
    """Aggregate experience metrics per customer."""
    return df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Handset Type': 'first'
    }).reset_index()

def get_top_handsets(df, top_n=10):
    """Get the top 10 handsets used by the customers."""
    return df['Handset Type'].value_counts().head(top_n)

def get_top_manufacturers(df, top_n=3):
    """Get the top 3 handset manufacturers."""
    return df['Handset Manufacturer'].value_counts().head(top_n)

def get_top_handsets_per_manufacturer(df, manufacturers):
    """Get the top handsets for each of the top 3 manufacturers."""
    result = {}
    for manufacturer in manufacturers:
        result[manufacturer] = df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
    return result

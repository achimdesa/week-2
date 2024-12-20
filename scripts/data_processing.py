import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    # Select only numeric columns for filling missing values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    return df


def segment_users(df, duration_col):
    df['decile_class'] = pd.qcut(df[duration_col], 5, labels=False) + 1
    df['total_data'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    return df

def get_top_handsets(df, top_n=10):
    # Adjust 'Handset Type' if it matches your actual column name
    return df['Handset Type'].value_counts().head(top_n)


def get_top_manufacturers(df, top_n=3):
    return df['Handset Manufacturer'].value_counts().head(top_n)

def get_top_handsets_per_manufacturer(df, manufacturers):
    result = {}
    for manufacturer in manufacturers:
        result[manufacturer] = df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
    return result


def aggregate_experience_metrics(df):
    # Aggregate experience metrics per customer
    return df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Handset Type': 'first'
    })

def get_top_bottom_frequent(df, column, top_n=10):
    """
    Get the top, bottom, and most frequent values for a specified column.

    Parameters:
    - df (pd.DataFrame): Data frame containing the data.
    - column (str): The column for which top, bottom, and frequent values are computed.
    - top_n (int): The number of top and bottom values to return.

    Returns:
    - dict: A dictionary containing 'top', 'bottom', and 'frequent' values.
    """
    top_values = df[column].nlargest(top_n)
    bottom_values = df[column].nsmallest(top_n)
    most_frequent = df[column].value_counts().head(top_n)

    return {
        'top': top_values,
        'bottom': bottom_values,
        'frequent': most_frequent
    }

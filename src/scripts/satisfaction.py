import numpy as np
from sklearn.linear_model import LinearRegression

def calculate_engagement_scores(df):
    """
    Calculate the engagement score for each user based on session frequency,
    duration, and total data (DL + UL).
    """
    df['Total Traffic (Bytes)'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    engagement_score = df[['Dur. (ms)', 'Total Traffic (Bytes)']].sum(axis=1)
    return engagement_score

def calculate_experience_scores(df):
    """
    Calculate the experience score for each user based on RTT, TCP retransmission,
    and throughput.
    """
    # Calculate throughput (Download + Upload) / Duration
    df['Throughput'] = (df['Total DL (Bytes)'] + df['Total UL (Bytes)']) / df['Dur. (ms)']
    # Calculate experience score as a combination of network parameters
    experience_score = df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'TCP DL Retrans. Vol (Bytes)', 'Throughput']].sum(axis=1)
    return experience_score

def build_regression_model(df, target='satisfaction_score'):
    """
    Build a regression model to predict satisfaction scores.
    """
    X = df[['engagement_score', 'experience_score']]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model

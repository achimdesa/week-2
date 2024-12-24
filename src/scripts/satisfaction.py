from sklearn.linear_model import LinearRegression

def calculate_experience_scores(df):
    """Calculate the experience score for each user based on RTT, TCP retransmission, and throughput."""
    df['Throughput'] = (df['Total DL (Bytes)'] + df['Total UL (Bytes)']) / df['Dur. (ms)']
    experience_score = df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'TCP DL Retrans. Vol (Bytes)', 'Throughput']].sum(axis=1)
    return experience_score

def build_regression_model(df, target='satisfaction_score'):
    """Build a linear regression model to predict satisfaction scores."""
    X = df[['engagement_score', 'experience_score']]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model

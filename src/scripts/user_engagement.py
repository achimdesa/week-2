# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

# def aggregate_metrics(df):
#     # Aggregate sessions frequency, duration, and total traffic (download + upload)
#     agg_df = df.groupby('MSISDN/Number').agg({
#         'Dur. (ms)': 'sum',  # Total session duration
#         'Bearer Id': 'count',  # Session frequency (count of sessions)
#         'Total DL (Bytes)': 'sum',  # Total download traffic
#         'Total UL (Bytes)': 'sum'   # Total upload traffic
#     }).reset_index()
    
#     agg_df['Total Traffic (Bytes)'] = agg_df['Total DL (Bytes)'] + agg_df['Total UL (Bytes)']
#     return agg_df

# def normalize_metrics(agg_df):
#     # Normalize the engagement metrics using MinMaxScaler
#     scaler = MinMaxScaler()
#     agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']] = scaler.fit_transform(agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']])
#     return agg_df

# # Apply K-Means Clustering
# def kmeans_clustering(agg_df, k=3):
#     # Perform k-means clustering
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     agg_df['Engagement Cluster'] = kmeans.fit_predict(agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']])
#     return agg_df, kmeans
# def kmeans_clustering2(agg_df, k=3):
#     """
#     Perform k-means clustering on the engagement and experience scores.
#     """
#     # Use 'engagement_score' and 'experience_score' instead of Dur. (ms) and Bearer Id
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     agg_df['Cluster'] = kmeans.fit_predict(agg_df[['engagement_score', 'experience_score']])
#     return agg_df['Cluster'], kmeans
# def elbow_method(agg_df):
#     # Plot the elbow method to determine the optimal number of clusters
#     distortions = []
#     for k in range(1, 10):
#         kmeans = KMeans(n_clusters=k, random_state=42)
#         kmeans.fit(agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']])
#         distortions.append(kmeans.inertia_)
    
#     plt.figure(figsize=(8, 6))
#     plt.plot(range(1, 10), distortions, marker='o')
#     plt.title('Elbow Method')
#     plt.xlabel('Number of clusters')
#     plt.ylabel('Distortion')
#     plt.show()

# def top_customers(agg_df, metric, top_n=10):
#     # Return the top N customers based on the provided metric
#     return agg_df.nlargest(top_n, metric)

# def top_applications(df, top_n=10):
#     # Aggregate user total traffic per application and get the top N most engaged users per application
#     app_agg_df = df.groupby('Handset Type').agg({
#         'Total DL (Bytes)': 'sum',
#         'Total UL (Bytes)': 'sum'
#     }).reset_index()
    
#     app_agg_df['Total Traffic (Bytes)'] = app_agg_df['Total DL (Bytes)'] + app_agg_df['Total UL (Bytes)']
#     return app_agg_df.nlargest(top_n, 'Total Traffic (Bytes)')



import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
def calculate_engagement_scores(df):
    """Calculate the engagement score based on session duration and total data."""
    # Compute total data traffic
    df['Total Traffic (Bytes)'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    
    # Engagement score is the sum of session duration and total data traffic
    engagement_score = df[['Dur. (ms)', 'Total Traffic (Bytes)']].sum(axis=1)
    return engagement_score

def normalize_metrics(agg_df):
    """Normalize the engagement metrics using MinMaxScaler."""
    scaler = MinMaxScaler()
    agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']] = scaler.fit_transform(agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']])
    return agg_df

def kmeans_clustering2(agg_df, k=3):
    """Perform K-Means clustering on engagement and experience scores."""
    kmeans = KMeans(n_clusters=k, random_state=42)
    agg_df['Cluster'] = kmeans.fit_predict(agg_df[['engagement_score', 'experience_score']])
    return agg_df['Cluster'], kmeans

def elbow_method(agg_df):
    """Use the Elbow method to determine the optimal number of clusters."""
    distortions = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(agg_df[['Dur. (ms)', 'Bearer Id', 'Total Traffic (Bytes)']])
        distortions.append(kmeans.inertia_)
    
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 10), distortions, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.show()

def top_customers(agg_df, metric, top_n=10):
    """Return the top N customers based on the provided metric."""
    return agg_df.nlargest(top_n, metric)

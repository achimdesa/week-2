# import matplotlib.pyplot as plt
# import seaborn as sns

# def plot_user_overview(df):
#     """Plot the distribution of handsets used by customers."""
#     plt.figure(figsize=(10, 6))
#     sns.countplot(x="Handset Type", data=df, order=df['Handset Type'].value_counts().index)
#     plt.title("Distribution of Handsets")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

# def plot_user_engagement(df):
#     """Plot user engagement with session duration and data traffic."""
#     plt.figure(figsize=(10, 6))
#     sns.scatterplot(x="engagement_score", y="Total Traffic (Bytes)", hue="Handset Type", data=df)
#     plt.title("User Engagement Analysis")
#     plt.xlabel("Engagement Score")
#     plt.ylabel("Total Traffic (Bytes)")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()

# def plot_experience(df):
#     """Plot experience metrics based on network parameters."""
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x="Handset Type", y="Avg RTT DL (ms)", data=df)
#     plt.title("Experience Metrics by Handset Type")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

# def plot_satisfaction(df):
#     """Plot satisfaction clusters based on engagement and experience scores."""
#     plt.figure(figsize=(10, 6))
#     sns.scatterplot(x="engagement_score", y="experience_score", hue="Cluster", data=df, palette="Set1", s=100)
#     plt.title("Satisfaction Clusters")
#     plt.xlabel("Engagement Score")
#     plt.ylabel("Experience Score")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()



import matplotlib.pyplot as plt
import seaborn as sns

def plot_user_overview(df):
    """Plot the distribution of handsets used by customers."""
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Handset Type", data=df, order=df['Handset Type'].value_counts().index)
    plt.title("Distribution of Handsets")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_user_engagement(df):
    """Plot user engagement with session duration and data traffic."""
    # Ensure that Total Traffic (Bytes) is calculated
    df['Total Traffic (Bytes)'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="engagement_score", y="Total Traffic (Bytes)", hue="Handset Type", data=df)
    plt.title("User Engagement Analysis")
    plt.xlabel("Engagement Score")
    plt.ylabel("Total Traffic (Bytes)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_experience(df):
    """Plot experience metrics based on network parameters."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Handset Type", y="Avg RTT DL (ms)", data=df)
    plt.title("Experience Metrics by Handset Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_satisfaction(df):
    """Plot satisfaction clusters based on engagement and experience scores."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="engagement_score", y="experience_score", hue="Cluster", data=df, palette="Set1", s=100)
    plt.title("Satisfaction Clusters")
    plt.xlabel("Engagement Score")
    plt.ylabel("Experience Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

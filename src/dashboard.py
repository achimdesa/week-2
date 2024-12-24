import streamlit as st
import pandas as pd
from scripts.visualizations import plot_user_overview, plot_user_engagement, plot_experience, plot_satisfaction
from scripts.data_processing import clean_data, segment_users, aggregate_experience_metrics, get_top_handsets, get_top_manufacturers
from scripts.satisfaction import build_regression_model, calculate_experience_scores
from scripts.user_engagement import kmeans_clustering2

# Streamlit App
st.title("TellCo User Engagement & Satisfaction Dashboard")

# Step 1: Upload the CSV file
uploaded_file = st.file_uploader("Upload your telecom dataset (CSV file)", type=["csv"])

if uploaded_file is not None:
    # Step 2: Load the CSV into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Display the first few rows of the data for reference
    st.write("Here's a preview of your data:")
    st.dataframe(df.head())

    # Step 3: Clean the data (fill missing values)
    df_cleaned = clean_data(df)

    # Step 4: Navigation Menu for Tasks (User Overview, Engagement, Experience, Satisfaction)
    task = st.sidebar.selectbox("Choose an analysis task", 
                                ["User Overview", "User Engagement", "Experience Analytics", "Satisfaction Analysis"])

    # Task 1: User Overview Analysis
    if task == "User Overview":
        st.subheader("User Overview Analysis")

        # Top 10 Handsets
        top_handsets = get_top_handsets(df_cleaned)
        st.write("Top 10 Handsets:")
        st.dataframe(top_handsets)

        # Top 3 Manufacturers
        top_manufacturers = get_top_manufacturers(df_cleaned)
        st.write("Top 3 Manufacturers:")
        st.dataframe(top_manufacturers)

        # Segmentation of users based on duration and data usage
        df_segmented = segment_users(df_cleaned, duration_col="Dur. (ms)")
        st.write("Segmented Users based on Session Duration:")
        st.dataframe(df_segmented[['MSISDN/Number', 'decile_class', 'total_data']].head())

        # Visualization for user overview (Plotting Handsets distribution)
        st.subheader("Handset Distribution")
        plot_user_overview(df_cleaned)

    # Task 2: User Engagement Analysis
    elif task == "User Engagement":
        st.subheader("User Engagement Analysis")

        # Calculate engagement scores
        df_cleaned['engagement_score'] = calculate_experience_scores(df_cleaned)
        st.write("Engagement Scores:")
        st.dataframe(df_cleaned[['MSISDN/Number', 'engagement_score']].head())

        # Visualize user engagement
        plot_user_engagement(df_cleaned)

    # Task 3: Experience Analytics
    elif task == "Experience Analytics":
        st.subheader("Experience Analytics")

        # Aggregate experience metrics
        experience_metrics = aggregate_experience_metrics(df_cleaned)
        st.write("Aggregated Experience Metrics:")
        st.dataframe(experience_metrics.head())

        # Visualize experience analytics
        plot_experience(df_cleaned)

    # Task 4: Satisfaction Analysis
    elif task == "Satisfaction Analysis":
        st.subheader("Satisfaction Analysis")

        # Calculate engagement and experience scores
        df_cleaned['experience_score'] = calculate_experience_scores(df_cleaned)
        df_cleaned['satisfaction_score'] = (df_cleaned['engagement_score'] + df_cleaned['experience_score']) / 2
        st.write("Satisfaction Scores:")
        st.dataframe(df_cleaned[['MSISDN/Number', 'satisfaction_score']].head())

        # Build regression model to predict satisfaction
        model = build_regression_model(df_cleaned, target='satisfaction_score')
        st.write("Regression model built to predict satisfaction scores.")

        # Perform K-Means Clustering (K=2) on engagement and experience scores
        clusters, kmeans_model = kmeans_clustering2(df_cleaned[['engagement_score', 'experience_score']], k=2)
        df_cleaned['cluster'] = clusters
        st.write("User Clusters based on Satisfaction:")
        st.dataframe(df_cleaned[['MSISDN/Number', 'cluster']].head())

        # Visualize satisfaction analysis
        plot_satisfaction(df_cleaned)


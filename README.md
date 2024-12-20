# TellCo User Engagement, Experience & Satisfaction Analysis
### Week 2 Challenge - 10 Academy AI Mastery Program

## Table of Contents
1. Project Overview
2. Data Description
3. Project Structure
4. Tasks Breakdown
   - Task 1: User Overview Analysis
   - Task 2: User Engagement Analysis
   - Task 3: Experience Analytics
   - Task 4: Satisfaction Analysis
5. Setup and Installation
6. How to Run the Project
7. Results and Insights
8. Next Steps
9. Conclusion & Recommendation

---

## Project Overview

TellCo, a mobile service provider in the Republic of Pefkakia, has shared its xDR (data session detail) records for an in-depth analysis. The goal is to analyze user behavior, engagement, experience, and satisfaction to identify growth opportunities and make a recommendation to the investor on whether TellCo is worth acquiring. This analysis is broken down into four key tasks:

- **Task 1: User Overview Analysis**
- **Task 2: User Engagement Analysis**
- **Task 3: Experience Analytics**
- **Task 4: Satisfaction Analysis**

This project aims to deliver insights on customer behavior using SQL, Python, machine learning, and visualization techniques, which can help the investor make an informed decision.

---

## Data Description

The dataset is sourced from TellCo’s xDR (data session detail) records, which contain information on user activity, data consumption, network parameters, and device characteristics. Key columns in the dataset include:

- **Bearer Id, IMSI, MSISDN/Number, IMEI**: User/device identifiers.
- **Start/End time, Duration (ms)**: Session time details.
- **Download (DL) & Upload (UL) data (Bytes)**: Traffic volume.
- **RTT, TCP Retransmission**: Network performance metrics.
- **Handset Type & Manufacturer**: Device characteristics.
- **Application Data**: Social Media, Google, YouTube, Netflix, Gaming, and more.

---

## Project Structure

```plaintext
├── .vscode/              # VSCode-specific settings
├── data/                 # Data source files
│   ├── schema.sql        # SQL schema for xDR data
│   ├── week-2-data.csv   # Dataset used for analysis
├── notebooks/            # Jupyter notebooks for analysis tasks
│   ├── eda_task_1.ipynb  # Task 1: User Overview Analysis
│   ├── eda_task_2.ipynb  # Task 2: User Engagement Analysis
│   ├── eda_task_3.ipynb  # Task 3: Experience Analytics
│   ├── eda_task_4.ipynb  # Task 4: Satisfaction Analysis
│   └── scripts/          # Python scripts for reusable code
│       ├── db_connection.py  # Database connection functions
│       ├── data_processing.py  # Data cleaning/processing functions
│       ├── clustering.py   # Clustering logic (K-means, Elbow method)
│       ├── satisfaction.py  # Engagement, experience, and satisfaction score calculations
│       ├── visualizations.py  # Plotting and visualizations
├── README.md             # Project documentation (this file)
├── requirements.txt      # Required Python libraries


Tasks Breakdown
Tasks Breakdown
Task 1: User Overview Analysis
Objective: Explore customer behavior based on device and application usage.
Key Metrics:
Top 10 handsets used by customers.
Top 3 handset manufacturers.
Total download and upload data per application.
Analysis:
Univariate, bivariate, and correlation analysis to understand device popularity and application usage.
Segmentation of users into deciles based on session duration and data volume.
Task 2: User Engagement Analysis
Objective: Measure user engagement through session frequency, session duration, and data traffic.
Key Metrics:
Top 10 customers based on engagement metrics.
Normalization of engagement metrics.
Clustering of users using K-Means to group customers into high, medium, and low engagement.
Elbow method to determine optimal clusters.
Task 3: Experience Analytics
Objective: Evaluate user experience through network parameters and device characteristics.
Key Metrics:
TCP retransmission, Round Trip Time (RTT), Throughput.
Distribution of throughput and TCP values across different handsets.
K-Means clustering of users based on network performance metrics.
Task 4: Satisfaction Analysis
Objective: Analyze customer satisfaction by combining engagement and experience scores.
Key Metrics:
Engagement and experience scores calculated using Euclidean distance.
Satisfaction score as the average of engagement and experience scores.
K-Means clustering to group users based on satisfaction.

Setup and Installation
1. Clone the Repository

git clone git@github.com:SolomonZinabu/week-2.git
cd week-2


Install the necessary Python libraries:

pip install -r requirements.txt

3. Set Up PostgreSQL Database
Install PostgreSQL on your machine.
Create a database and load the schema:

CREATE DATABASE telecom_data;
psql -U postgres -d telecom_data -f data/schema.sql
Load the dataset:

COPY xdr_data FROM 'C:/path_to_file/week-2-data.csv' DELIMITER ',' CSV HEADER;
How to Run the Project
Launch Jupyter Notebooks:

jupyter notebook
Open the notebooks for each task:
eda_task_1.ipynb - User Overview Analysis
eda_task_2.ipynb - User Engagement Analysis
eda_task_3.ipynb - Experience Analytics
eda_task_4.ipynb - Satisfaction Analysis
Database Connection: Make sure the db_connection.py script has your PostgreSQL credentials.

db_config = {
    'host': 'localhost',
    'database': 'telecom_data',
    'user': 'postgres',
    'password': 'password'
}
Run the Analysis: Execute each notebook to perform the analysis, generate insights, and visualize data.

Results and Insights
Task 1: User Overview

Top Handsets: Huawei and Apple dominate the market.
Top Applications: Gaming, YouTube, and Social Media drive the most data usage.

Task 2: User Engagement

Engagement Clusters: 3 clusters were identified:
High Engagement: Users with frequent, long sessions and high data usage.
Medium Engagement: Moderate sessions and data consumption.
Low Engagement: Minimal sessions and data traffic.

Task 3: Experience Analysis

Network Parameters:
Devices like iPhones generally have higher throughput, while certain Android devices experience more TCP retransmission issues.

Task 4: Satisfaction Analysis

Satisfaction Scores: Derived from engagement and experience scores. High satisfaction users tend to have low network issues and high engagement.
Recommendation: Based on the analysis, TellCo should focus on improving network quality for low-satisfaction clusters to reduce churn.

Next Steps

Further analysis on retention strategies for low-engagement users.
Develop a Streamlit dashboard for real-time tracking of customer insights.
Implement marketing strategies targeting high-engagement, satisfied users for premium services.

Conclusion & Recommendation

Based on the user engagement, experience, and satisfaction analysis, TellCo has a solid user base with significant growth potential. However, the company needs to focus on improving network quality and service reliability to retain customers in low-satisfaction clusters. The recommendation to the investor is to proceed with the acquisition as there are clear opportunities for growth by enhancing customer experience and expanding premium offerings.

References
10 Academy: Week 2 Challenge Documentation
Pandas Documentation
Scikit-learn Documentation
PostgreSQL Documentation
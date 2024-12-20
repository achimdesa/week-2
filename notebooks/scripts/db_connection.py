import psycopg2
import pandas as pd

def get_data_from_postgres(query, db_config):
    """
    Connect to PostgreSQL database and execute the provided query.

    Parameters:
    - query (str): SQL query to execute.
    - db_config (dict): Database configuration dictionary containing:
        - 'host': Database host
        - 'database': Database name
        - 'user': Database user
        - 'password': Database password

    Returns:
    - pd.DataFrame: DataFrame containing the query results.
    """
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_config['host'],
            database=db_config['database'],
            user=db_config['user'],
            password=db_config['password']
        )
        # Execute the query and load the data into a DataFrame
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

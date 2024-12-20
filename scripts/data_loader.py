import pandas as pd

def load_data(file_path):
    """
    Load the CSV file into a pandas DataFrame.
    
    :param file_path: Path to the CSV file
    :return: DataFrame
    """
    return pd.read_csv(file_path)

# Example usage
if __name__ == "__main__":
    data = load_data('../data/Week2_challange_data_source(CSV).csv')
    print(data.head())

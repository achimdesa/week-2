import pandas as pd

def load_data(file_path):
    
    #Load the CSV file into a pandas DataFrame.
    
    #:param file_path: Path to the CSV file
    #:return: DataFrame
   
    return pd.read_csv(file_path)

# Example usage
if __name__ == "__main__":
    data = load_data(r'E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W2Data\\Week2_challenge_data_source.csv')
    print(data.head())


# df = pd.read_csv('Week2_challenge_data_source.csv')
# print(df.head())
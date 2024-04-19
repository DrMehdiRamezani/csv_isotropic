import pandas as pd
import os
import glob

directory_path = r"C:\Users\mer\Documents\dev\VSCode_test\XML_2_CSV\csv_isotropic\asset"


# Function to read the CSV file and fix the number of columns
def fix_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, header=None)

    # Find the maximum number of columns in the DataFrame
    max_cols = df.apply(lambda row: row.count(), axis=1).max()
 
    # Iterate over each row and add commas to match the maximum number of columns
    for index, row in df.iterrows():
        if row.count() < max_cols:
            row[row.last_valid_index() + 1] = None

    # Save the DataFrame to a new CSV file
    new_file_path = file_path.split('.')[0] + '_isotropic.csv'
    df.to_csv(new_file_path, index=False, header=False)
    
    print("Fixed CSV file saved as:", new_file_path)

# Check if the directory exists
if os.path.exists(directory_path):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Filter out files with ".csv" extension 
    csv_files = [file for file in files if file.endswith(".csv")]
    print(csv_files)
    # Process each XML file
    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        print(file_path)

        # Call the function to fix the CSV file
        fix_csv(file_path)
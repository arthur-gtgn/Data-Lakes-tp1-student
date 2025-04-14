import os
import pandas as pd

def unpack_data(input_dir: str, output_file: str) -> None:
    """
    Unpacks and combines multiple CSV files from a directory into a single CSV file.

    Parameters:
    input_dir (str): Path to the directory containing the CSV files.
    output_file (str): Path to the output combined CSV file.
    """

    # Step 1: Initialize an empty list to store DataFrames
    data = []

    # Step 2: Loop over files in the input directory
    for filename in os.listdir(input_dir):
        
        print(f"🔨 Processing file {filename}")
        
        # Step 3: Check if the file is a CSV or matches a naming pattern
        if "data-" in filename:

            # Step 4: Read the CSV file using pandas
            df = pd.read_csv(f'{input_dir}/{filename}')

            # Step 5: Append the DataFrame to the list
            data.append(df)
            
            print("🎉 File read successfull!")

    # Step 6: Concatenate all DataFrames
    result = pd.concat(data)
    
    # Step 7: Save the combined DataFrame to output_file
    result.to_csv(output_file)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Unpack and combine protein data")
    parser.add_argument("--input_dir", type=str, required=True, help="Path to input directory")
    parser.add_argument("--output_file", type=str, required=True, help="Path to output combined CSV file")
    args = parser.parse_args()

    unpack_data(args.input_dir, args.output_file)

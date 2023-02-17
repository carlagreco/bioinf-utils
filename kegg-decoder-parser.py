#!/usr/bin/env python

"""
This script creates an file to use for KEGGdecoder from the kofamscan oneline output
"""

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="This script creates an file to use for keggdecoder from the kofam oneline output")

required = parser.add_argument_group('required arguments')

required.add_argument("-i", "--input-file", help="Input kofam one-line file(s)", action="store", dest="input_file", required=True, nargs="*")
parser.add_argument("-o", "--output-table", help='Output table name (default: "output.tsv")', action="store", dest="output_file", default="output.tsv")

# Create a list of all .txt files in the current directory
args = parser.parse_args()

files = args.input_file

# Create an empty list to store the processed dataframes
dfs = []

# Loop through the files and process each one
for file in files:
    # Read the file into a Pandas dataframe
    df = pd.read_table(file, header=None, usecols = [0,1], names=['locus_tag', 'Kofam'], index_col=None)

    #get samplename column
    df['sample'] =  file.split('_')[0]
    
    # Add an underscore and the count to each repeated 'sample' value
    df['sample'] = df['sample'].str.cat(df.groupby('sample').cumcount().astype(str), sep='_')

    # Drop the 'locus_tag' column
    df = df.drop(columns=['locus_tag'])

    # Rearrange colums 
    df = df[['sample','Kofam']]

    # Add the processed dataframe to the list
    dfs.append(df)

# Concatenate the processed dataframes into a single dataframe
result = pd.concat(dfs)

result.dropna(axis=0,
    how='any',
    inplace=True
)

# Save the resulting dataframe to an output file
result.to_csv(args.output_file, sep = "\t", index=False, header=False)
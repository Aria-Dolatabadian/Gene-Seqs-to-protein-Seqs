#reads CSV file containing a column with DNA sequences and adds protein sequences to the CSV file

import pandas as pd
from Bio.Seq import Seq

# Define a function to translate DNA sequences to protein sequences
def translate_sequence(dna_sequence):
    seq = Seq(dna_sequence)
    return str(seq.translate())

# Replace 'your_input.csv' with your CSV file containing the gene sequences
input_file = 'All chromosomes.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Assuming the gene sequences are in a column named 'gene_sequence'
# You can change the column name to match your CSV file
df['protein_sequence'] = df['Sequence'].apply(translate_sequence)

# Replace 'your_output.csv' with the desired output CSV file name
output_file = 'my_output.csv'

# Save the DataFrame with the added protein sequences as a new CSV file
df.to_csv(output_file, index=False)

print("CSV file with protein sequences saved to:", output_file)

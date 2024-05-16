import os
import csv

# Directory containing the .glb files
input_directory = '/home/aalab/Desktop/tripoFT/tensors'

# Directory where the metadata.csv file will be saved
output_directory = '/home/aalab/Desktop/tripoFT'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List to hold metadata
metadata = []

# Gather information about each .glb file
for filename in os.listdir(input_directory):
    if filename.endswith('.glb'):
        file_path = os.path.join(input_directory, filename)
        file_info = os.stat(file_path)
        metadata.append({
            'filename': filename,
            'size': file_info.st_size,  # Size in bytes
            'object_path': file_path  # Full path to the .glb file
        })

# Write metadata to a CSV file in the output directory
output_file_path = os.path.join(output_directory, 'metadata.csv')
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['filename', 'size', 'object_path'])
    writer.writeheader()
    for data in metadata:
        writer.writerow(data)

print(f'Metadata file saved at: {output_file_path}')

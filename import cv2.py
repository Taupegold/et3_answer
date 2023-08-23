import os
import csv
import shutil
import time


# Source directory containing the image dataset
source_directory = "C:/Users/Lenovo/Desktop/dairies"

# Destination directory where all images will be copied
destination_directory = "C:/Users/Lenovo/Desktop/dest"

# CSV file path to save the image information
csv_file_path = "C:/Users/Lenovo/Desktop/csvfile/csvname"

# Function to recursively traverse the directory tree, copy images, and extract information
def copy_images_and_extract_info(source, destination, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image Name', 'Size (bytes)', 'Last Modified'])
        
        for root, _, files in os.walk(source):
            for file in files:
                if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                    source_file = os.path.join(root, file)
                    destination_file = os.path.join(destination, file)
                    
                    # Copy the image to the destination directory
                    shutil.copy2(source_file, destination_file)
                    
                    # Extract information about the image
                    image_size = os.path.getsize(destination_file)
                    last_modified = os.path.getmtime(destination_file)
                    local_time = time.ctime(last_modified)
                    
                    # Write the image information to the CSV file
                    writer.writerow([file, image_size, local_time])

# Copy images from source directory to destination directory, extract information, and save to CSV
copy_images_and_extract_info(source_directory, destination_directory, csv_file_path)








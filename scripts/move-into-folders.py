import os
import shutil
import datetime

# Set the source directory
source_dir = 'C:/Users/chris/Pictures/Python-test'

# Set the destination directory
dest_dir = 'C:/Users/chris/Pictures/Python-test'

# Get the list of files in the source directory
files = os.listdir(source_dir)

# Loop through the files
for file in files:
    # Get the creation time of the file
    creation_time = os.path.getmtime(os.path.join(source_dir, file))
    # Convert the creation time to a datetime object
    creation_date = datetime.datetime.fromtimestamp(creation_time)
    # Create a new directory based on the year and month of the creation date
    new_dir = os.path.join(dest_dir, f'{creation_date.year}' + '-' + f'{creation_date.month:02d}' + '-' + f'{creation_date.day:02d}')
    # Create the new directory if it doesn't exist
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    # Move the file to the new directory
    shutil.move(os.path.join(source_dir, file), os.path.join(new_dir, file))

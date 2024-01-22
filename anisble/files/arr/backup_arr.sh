#!/bin/bash

# Set the source and destination paths
source_path=/home/ccalifice/
backup_path=/mnt/server_backup/
timestamp=$(date "+%Y%m%d_%H%M%S")
log_path=/scripts/
# Stop containers
docker stop $(docker ps -q)

# Create a tar archive excluding cache and hidden files
file_name="${timestamp}_arr_backup.tar.gz"
tar -czf $source_path$file_name --exclude=*/cache --exclude=*/blobs --exclude=*/generated --exclude=*/MediaCover --exclude=*/logs --exclude=*/Cache --exclude=*/Logs --exclude=*/Metadata --exclude=*/Crash\ Reports --exclude=*/Media --exclude=~/.* $source_path


# Use rsync to copy the created archive to the destination
rsync -av --progress "${source_path}${file_name}" "$backup_path"

# Optionally, remove the local backup file after copying
rm $source_path$file_name

# Restart containers
docker start $(docker ps -a -q)

echo "${file_name} -  backup complete" >> ${source_path}${log_path}backup.log
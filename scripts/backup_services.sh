#!/bin/bash

# Set the source and destination paths
source_path=/home/ccalifice/
backup_path=/mnt/server_backup/services/
timestamp=$(date "+%Y%m%d_%H%M%S")

# Stop containers
echo "stopping containers" >> ${source_path}backup.log
docker stop $(docker ps -q)

# Create a tar archive excluding cache and hidden files
file_name="${timestamp}_services_backup.tar.gz"

echo "Creating archive $source_path$file_name" >> ${source_path}backup.log


tar -czf $source_path$file_name --exclude=*/cache --exclude=*/logs --exclude=*/Cache --exclude=*/Logs --exclude=*/photoprism/storage --exclude=*/model-cache --exclude=*/immich-app/library $source_path


# Use rsync to copy the created archive to the destination
rsync -av --progress "${source_path}${file_name}" "$backup_path"

# Optionally, remove the local backup file after copying
rm $source_path$file_name

# Restart containers
echo "starting containers" >> ${source_path}backup.log
docker start $(docker ps -a -q)

echo "${file_name} -  backup complete" >> ${source_path}backup.log
import subprocess
import datetime

def create_tar_with_ignores(source_dir, output_tar):
    # Convert ignore_folders to a set for faster membership checks    

    # Create a list of files and folders to include in the tar command
    exclude_set = {        
        "'./stash/generated/*'",        
        "'./streaming/config/navidrome/data/cache/*'",
    }

    exclude_string = ' '.join([f'--exclude={item}' for item in exclude_set])

    # Build the tar command
    tar_command = [
        'tar',
        '-czvf',
        output_tar,
        '-C',
        source_dir,
        '.',
        exclude_string
    ]

    print(' '.join(tar_command))

    # Execute the tar command
    subprocess.run(tar_command)

if __name__ == "__main__":

    date = datetime.datetime.now()

    # Example usage
    source_directory = '/home/ccalifice/'
    output_tarfile = f"./{date}.tar.gz".replace(" ", "_").replace(":", "-")

    create_tar_with_ignores(source_directory, output_tarfile)

    print(f'Tar file "{output_tarfile}" created successfully.')
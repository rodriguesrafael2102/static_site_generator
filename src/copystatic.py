import os
import shutil

destination_directory = "/home/faelrodrigues21/public/public"
source_directory = "/home/faelrodrigues21/public/static"

def contains_directory(file_path):
    if not os.path.isdir(file_path):
        return False

    for file_name in os.listdir(file_path):
        file_path_inside = os.path.join(file_path,file_name)

        if os.path.isdir(file_path_inside):
            return True
    return False

def delete_file_destination(destination_directory, original_dest_direct = None):
    if original_dest_direct is None:
        original_dest_direct = destination_directory

    for filename in os.listdir(destination_directory):
        file_path = os.path.join(destination_directory, filename)

        if os.path.isdir(file_path):
            delete_file_destination(file_path, original_dest_direct) # recursion
            continue

        elif os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file in Destination folder: {file_path}")

    list_files = os.listdir(destination_directory)

    if len(list_files) == 0:
        if destination_directory != original_dest_direct:
            shutil.rmtree(destination_directory)
            print(f"Deleted directory: {destination_directory}")
            return

def copy_files_from_source(destination_directory, source_directory, original_sourc_direct = None):
    directory_created= False
    source_directory_base = os.path.basename(source_directory)
    if original_sourc_direct is None:
        original_sourc_direct = source_directory

    list_of_files = os.listdir(source_directory)
    
    for file_name in list_of_files:
        file_path = os.path.join(source_directory, file_name)
        source_base_name = os.path.basename(file_path)
        
        if os.path.isdir(file_path):
            copy_files_from_source(destination_directory, file_path, original_sourc_direct)
            continue

        if not os.path.isdir(f"{destination_directory}/{source_directory_base}") and source_directory != original_sourc_direct: 
            os.mkdir(f"{destination_directory}/{source_directory_base}")
            print(f"Created directory: {destination_directory}/{source_directory_base}")
            new_destination_directory = f"{destination_directory}/{source_directory_base}"
            directory_created = True
        
        if directory_created:
            shutil.copy(file_path, f"{new_destination_directory}/{source_base_name}")
            print(f"Copied file: {file_path}  -- Copied to: {new_destination_directory}/{source_base_name}")
        else:
            shutil.copy(file_path, f"{destination_directory}/{source_base_name}")
            print(f"Copied file: {file_path}  -- Copied to: {destination_directory}/{source_base_name}")




def move_files(destination_directory, source_directory):
    delete_file_destination(destination_directory)
    copy_files_from_source(destination_directory, source_directory)























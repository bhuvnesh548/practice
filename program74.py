import os


def rename_files_sequentially(folder_path, base_name="program"):
    # Check if the provided path exists and is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: The path '{folder_path}' is not a valid directory.")
        return

    # List all items in the directory
    all_items = os.listdir(folder_path)

    # Filter out directories, keeping only files
    files = [
        f for f in all_items if os.path.isfile(os.path.join(folder_path, f))
    ]

    # Sort files alphabetically to ensure consistent ordering
    files.sort()

    # Counter for sequential naming
    count = 1

    for filename in files:
        # Get the full current path of the file
        old_file_path = os.path.join(folder_path, filename)

        # Extract the file extension (e.g., '.txt', '.py')
        file_extension = os.path.splitext(filename)[1]

        # Create the new filename with the sequence number and original extension
        new_filename = f"{base_name}{count}{file_extension}"
        new_file_path = os.path.join(folder_path, new_filename)

        try:
            # Rename the file on the disk
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{filename}' -> '{new_filename}'")
            count += 1
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

    print(f"\nSuccessfully renamed {count - 1} files.")


# --- HOW TO RUN THIS ---
# Replace 'YOUR_FOLDER_PATH_HERE' with your actual folder path.
# Use 'r' before the string to handle Windows backslashes correctly.
target_folder = r"C:\Users\bhuvnesh\Desktop\practice"

rename_files_sequentially(target_folder)

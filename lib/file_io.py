def write_file(file_name, file_content):
    # Add .txt extension to the file name
    full_file_name = f"{file_name}.txt"
    
    # Open the file in write mode
    with open(full_file_name, 'w', encoding='utf-8') as file:
        # Write the content to the file
        file.write(file_content)

def append_file(file_name, append_content):
    # Add .txt extension to the file name
    full_file_name = f"{file_name}.txt"
    
    # Open the file in append mode
    with open(full_file_name, 'a', encoding='utf-8') as file:
        # Append the content to the file
        file.write(append_content)

def read_file(file_name):
    # Add .txt extension to the file name
    full_file_name = f"{file_name}.txt"
    
    # Open the file in read mode
    with open(full_file_name, 'r', encoding='utf-8') as file:
        # Read the content of the file
        return file.read()

def file_processor():
    """Read a file, modify its content, and write to a new file with error handling."""
    
    # Get input filename from user with error handling
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            with open(input_filename, 'r') as infile:
                content = infile.read()
            break  # Exit loop if file read successfully
        except FileNotFoundError:
            print(f"Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied when accessing '{input_filename}'. Please try another file.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode file '{input_filename}'. It may be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Please try again.")

    # Process the content (example modification: convert to uppercase)
    modified_content = content.upper()  # You can replace this with your own modification logic

    # Get output filename from user
    while True:
        output_filename = input("Enter the name of the output file: ")
        if output_filename.strip() == "":
            print("Output filename cannot be empty. Please try again.")
            continue
        
        try:
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
            print(f"Successfully wrote modified content to '{output_filename}'")
            break
        except PermissionError:
            print(f"Error: Permission denied when writing to '{output_filename}'. Please try another filename.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Please try again.")

if __name__ == "__main__":
    file_processor()
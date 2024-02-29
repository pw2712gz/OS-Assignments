# Ayub Yusuf
# Assignment #4
# This program calculates the page number and offset for a given 32-bit virtual address.
# It outputs the results for three test addresses into the file output.txt.

def calculate_page_number_and_offset(address):
    page_size = 4096  # Define the page size as 4 KB
    page_number = address // page_size  # Calculate the page number
    offset = address % page_size  # Calculate the offset within the page
    return page_number, offset

# List of virtual addresses to process
addresses = [19986, 347892, 5978]

output_filename = "output.txt"

with open(output_filename, "w") as file:
    # Writing header information to the file
    file.write("Ayub Yusuf\n")
    file.write("Assignment #4\n")
    file.write("Febuary 21, 2024\n")
    
    # Process each address and write the results to the file
    for address in addresses:
        page_number, offset = calculate_page_number_and_offset(address)
        file.write(f"The address {address} is in:\n")
        file.write(f"Page number = {page_number}\n")
        file.write(f"Offset = {offset}\n\n")

# Confirmation message 
print(f"Output written to {output_filename}.")

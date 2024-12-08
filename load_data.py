import os
import numpy as np

def load_data(subdirectory, xyz_filename, prop_filename, save_filename):
    """
    Load data from the specified subdirectory and filenames.

    Args:
    - subdirectory (str): The subdirectory where the files are located.
    - xyz_filename (str): The name of the .xyz file.
    - prop_filename (str): The name of the .prop file.
    - save_filename (str): The name of the file to save the parsed data.
    """
    cur_path = os.getcwd()
    file_path = os.path.join(cur_path, subdirectory)
    xyz_file = os.path.join(file_path, xyz_filename)
    prop_file = os.path.join(file_path, prop_filename)

    lattice_vec = []
    # Filter and read only lines that start with "Lattice"
    with open(xyz_file, 'r') as file:
        
        lattice_lines = [line.strip() for line in file if line.startswith("Lattice")]
        
        for lattice_line in lattice_lines:
            # Step 1: Extract the part after "Lattice="
            lattice_values = lattice_line.split('=')[1]
            # Step 2: Find the first and last occurrence of the quotation mark
            start_quote_index = lattice_line.find('"')  # Find the first quote
            end_quote_index = lattice_line.rfind('"')    # Find the last quote
            # Step 3: Slice the string to get only the numbers inside the quotes
            # Since we want the part before the last quote, we use start_quote_index + 1
            cleaned_numbers = lattice_line[start_quote_index + 1:end_quote_index]

            # Step 2: Split the string into individual number strings and convert to floats
            lattice_numbers = [float(value) for value in cleaned_numbers.split()]
            lattice_vec.append(np.array(lattice_numbers))
    lattice_vec = np.array(lattice_vec)

    lattice_eng = []
    with open(prop_file, 'r') as file:
        # Load the data
        # Note: usecols specifies the columns to load
        parsed_data = np.loadtxt(file, dtype={
        'names': ('Energy', 'Classification', 'Cutoff_3A', 'Cutoff_5A'),
        'formats': ('f8', 'U10', 'i4', 'i4')
        })
        for (eng, _, _, _) in parsed_data:
            lattice_eng.append(float(eng))
            
    lattice_eng = np.array(lattice_eng)
    # print(lattice_eng)
    # Combine the vectors and energy into a single 2D array
    data_to_save = np.column_stack((lattice_eng, lattice_vec))  # This creates a (594, 5) array

    # Save to a text file
    np.savetxt(save_filename, data_to_save, header="Energy V1 V2 V3 V4 V5 V6 V7 V8 V9", fmt='%.6e')
    


# Extract 5A data set
if __name__ == "__main__":
    subdirectory = "raw_data/5A/"
    xyz_filename = "traj-5A.xyz"
    prop_filename = "traj-5A.prop"
    save_filename = "crystal_parsed_data/5A_parsed_file.txt"

    load_data(subdirectory, xyz_filename, prop_filename, save_filename)
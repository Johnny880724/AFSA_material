import numpy as np
import os
class CrystalData:
    """A class for handling crystal data and computing smoothed kernel potentials."""

    def __init__(self,filename):
        """Initialize with crystal data.
        
        Args:
            data (np.ndarray): A numpy array representing crystal data points.
        """
        self.read_data(filename)

    @staticmethod
    def normalize(arr):
        """Normalize an array to the range [0, 1].

        Args:
            arr (np.ndarray): Array to normalize.

        Returns:
            np.ndarray: Normalized array with values between 0 and 1.
            tuple: A tuple containing the original minimum and maximum values of the array.
        """
        arr_min, arr_max = np.min(arr), np.max(arr)
        arr_norm = (arr - arr_min) / (arr_max - arr_min)
        return arr_norm, (arr_min, arr_max)

    def read_data(self, filename="5A_parsed_file.txt"):
        """Read data from a specified file in the crystal_parsed_data directory.

        Args:
            filename (str): Name of the file to read data from. Defaults to '5A_parsed_file.txt'.

        Returns:
            np.ndarray: Loaded data as a NumPy array.
        """
        # Get the current directory and build the full file path
        cur_path = os.getcwd()
        file_path = os.path.join(cur_path, "crystal_parsed_data", filename)
        print(f"Reading data from: {file_path}")
        
        # Load the data from the file
        try:
            self.data = np.loadtxt(file_path)
            self.data_E, (self.E_min, self.E_max) = self.normalize(self.data[:,0])
            columns = [1, 2, 3, 5, 6, 9]
            self.data_pos, (self.pos_min, self.pos_max) = self.normalize(self.data[:,columns])
        except IOError:
            print(f"Error: File {file_path} not found or could not be read.")
            self.data = None
            return None

    
    @staticmethod
    def kernel_func(r, h):
        """Compute a Gaussian kernel function.

        Args:
            r (float or np.ndarray): Distance or array of distances.
            h (float): Smoothing length parameter that scales the kernel.

        Returns:
            float or np.ndarray: Computed kernel values based on distance.
        """
        # Calculate the kernel value with Gaussian form
        return np.exp(-0.5 * (r / h) ** 2)

    def smoothed_kernel_potential(self, pos, h):
        """Calculate the smoothed kernel potential based on distance and smoothing length.
        
        Args:
            pos (1D np.array): The position of the reference point.
            h   (float): The smoothing length, controlling the spread of the kernel.
        
        Returns:
            float: The smoothed kernel potential value.
        """
        r = np.linalg.norm(pos[np.newaxis,:] - self.data_pos[:,:],axis=-1)
        # print(kernel_func(r,h))
        rho = np.sum(self.kernel_func(r,h))
        Erho = np.sum(self.kernel_func(r,h) * self.data_E)
        E = Erho / rho

        return E


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # Code inside this block will only run when this file is executed directly
    print("Running as a standalone script!")

    # Example usage:
    crystal = CrystalData('5A_parsed_file.txt')

    # Normalize some random data for testing
    N_grid = 100
    grid_axis = np.linspace(0,1,N_grid)
    x,y = np.copy(grid_axis),np.copy(grid_axis)
    xmesh, ymesh = np.meshgrid(x,y)
    Emesh = np.zeros_like(xmesh)
    for i in range(N_grid):
        for j in range(N_grid):
            Emesh[i,j] = crystal.smoothed_kernel_potential(np.array([xmesh[i,j],ymesh[i,j],0.4,0.5,0.5,0.5]),0.05)
    # Create a pcolormesh plot
    plt.figure(figsize=(8, 6))
    plt.pcolormesh(xmesh, ymesh, Emesh, shading='auto', cmap='viridis')
    plt.colorbar(label='E Field')  # Label for color bar
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('2D Color Mesh Plot of E Field')
    plt.show()
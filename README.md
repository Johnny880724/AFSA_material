# AFSA_material

This project is aimed at applying Artificial Fish-Swarm Algorithm (AFSA) on finding the minimums in the phase space of materials. 

The minimums (including global minimums) represent the possibility of the stable/metastable states. Due to the traditional methods( i.e. gradient decent) has its own limit, the more methods can be explored make the approach more efficient.

In this project, we have shown at the following figures, because of the good randomness, the early steps with less points, ASFA can reach much better performance. The details of each note are described at the following sub terms.

## Fishs_on_materials.ipynb
The gradient descent and AFSA are used to find the global and local minima of a two-dimensional random Gaussian potential.
Here are the parameters of gradient descent:
```python
num_initial_points = 1000 # The number of initial points
initial_points = np.random.uniform(-10, 10, (num_initial_points, 2))
learning_rate = 0.1
max_iterations = 500 
tolerance = 1e-5
```

## load_data.py
The `load_data.py` script is used to load and process data from specified subdirectories and filenames. It includes functions to extract lattice vectors from `.xyz` files and lattice energies from `.prop` files.

### Example Usage
From Ref.[2], material energy raw data can be downloaded, which contains the position data `traj-5A.xyz` and the energy data `traj-5A.prop`. Extract and store the vectors and energy data with the following code:
```python
from load_data import load_data
subdirectory = "raw_data/5A/"
xyz_filename = "traj-5A.xyz"
prop_filename = "traj-5A.prop"
save_filename = "crystal_parsed_data/5A_parsed_file.txt"

load_data(subdirectory, xyz_filename, prop_filename, save_filename)
```

![contour_plot](https://github.com/Johnny880724/AFSA_material/blob/main/images/Contour_Plot.png)


## Reference
[1] Artificial Fish Swarming Algorithm: https://arxiv.org/abs/2011.05700 <br />
[2] ML on crystal: https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc04665k <br />
[3] Fish sworm csdn: https://blog.csdn.net/hba646333407/article/details/103082418 <br />
[4] Smoothed particle hydrodyanmics: https://ui.adsabs.harvard.edu/abs/1992ARA%26A..30..543M/abstract

# AFSA_material

This project is aimed at applying the Artificial Fish-Swarm Algorithm (AFSA) to find the minima in the configuration space of materials. 

The minimums (including global minimums) represent the possibility of the stable/metastable states. Due to the traditional methods( i.e. gradient decent) has its own limit, the more methods can be explored make the approach more efficient.

To discover more of technologically relevant, experimentally synthesizable, sufficiently long-lived novel materials, computational exploration of the materials configuration space is beneficial. In the configuration space of a given material, the global and local minima represent the possible ground state and metastable states of matter, respectively. The synthesizability of polymorphs can be assessed by the size of attraction basins. The lifetime of a candidate metastable structure is determined by the energy barrier around the basin. In this project, we focus on identifying candidate polymorphs. The traditional method( i.e. gradient descent approach) consists of random structure sampling and computationally demanding atomic relaxation calculations. For a more efficient methodology, we implemented the ASFA algorithm and its variant and performed a comparative study with the conventional approach. 

![comparison](https://raw.githubusercontent.com/Johnny880724/AFSA_material/refs/heads/main/images/global%20energy%20minimums%20serach%20competition%20between%20GD%20and%20AFSA.png)

The x-axis represent the times of each algorithim ask to calculate energy and the y represent the lowest minimums they found.

In this project, we have shown at the above figure, because of the good randomness, the early steps with less points, ASFA can reach much better performance. The details of each note are described at the following sub terms.

## Fishs_on_materials.ipynb
In this note we generate a toy model of well in a 2D space to observe the different behaviour of two algotrithim. The following picture is the example of the 2D gaussian wells in a space.

![contour_plot](https://github.com/Johnny880724/AFSA_material/blob/main/images/Contour_Plot.png)

The gradient descent and AFSA are used to find the global and local minima of a two-dimensional random Gaussian potential.The evolution of AFSA animation is collectred in the folder called animation.

Here are the parameters of gradient descent:
```python
num_initial_points = 1000 # The number of initial points
initial_points = np.random.uniform(-10, 10, (num_initial_points, 2))
learning_rate = 0.1
max_iterations = 500 
tolerance = 1e-5
```
Here are the parameters of AFSA:
```python
num_particles = 30  # Number of particles
max_iterations = 30  # Maximum number of iterations
w = 0.5  # Inertia weight
c1 = 1.5  # Self-attraction coefficient
c2 = 1.5  # Group-attraction coefficient
boundary_min = -10  # Minimum boundary value
boundary_max = 10   # Maximum boundary value
max_velocity = 1.0  # Maximum velocity
penalty_factor = 100  # Penalty factor for particles out of bounds
```
one extra parameter is used to repulse the fishes AFSA from global minimums and find local minimums:
```python
repulsion = 5  # Repulsion of found minimums 
```

We can get the global and local minima by GD as shown below:
![GD](https://github.com/Johnny880724/AFSA_material/blob/main/images/Gradient%20Descent.png)

And we can get the evolution of AFSA on 2D well with much smaller amount of iteration shown below:
![AFSA_GB](https://github.com/Johnny880724/AFSA_material/blob/main/animations/pso_animation_convert.gif)

By observing the repusion, you will find out a possibility of points evolved out to find other local minimums:
![AFSA_LB](https://github.com/Johnny880724/AFSA_material/blob/main/images/PSO_Local_Minima.png)

## load_data.py
The `load_data.py` script is used to load and process data from Ref.[2] specified subdirectories and filenames. It includes functions to extract lattice vectors from `.xyz` files and lattice energies from `.prop` files.

### Example Usage
From Ref.[2], material energy raw data can be downloaded, which contains the position data `traj-5A.xyz` and the energy data `traj-5A.prop`. Extract and store the lattice vectors and energy data with the following code:
```python
from load_data import load_data
subdirectory = "raw_data/5A/"
xyz_filename = "traj-5A.xyz"
prop_filename = "traj-5A.prop"
save_filename = "crystal_parsed_data/5A_parsed_file.txt"

load_data(subdirectory, xyz_filename, prop_filename, save_filename)
```



## Fishs_on_real_crystal.ipynb
In this note, by applying the GD and non-modified AFSA, we use the crystal data from Ref.[2] to do the search. We applied the gaussian kernel fitting to smooth and interpolate the 9D phase space. And we tuned the parameter at finsh_on material note to compete the efficiency between each algorithm.

## Reference
[1] Artificial Fish Swarming Algorithm: https://arxiv.org/abs/2011.05700 <br />
[2] ML on molecular crystal: https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc04665k <br />
[3] Fish swarm csdn: https://blog.csdn.net/hba646333407/article/details/103082418 <br />
[4] Smoothed particle hydrodynamics: https://ui.adsabs.harvard.edu/abs/1992ARA%26A..30..543M/abstract <br />
[5] random structure sampling and gradient descent approach: https://ui.adsabs.harvard.edu/abs/1992ARA%26A..30..543M/abstract <br />
https://pubs.aip.org/aip/apr/article/8/3/031310/124790/Metastable-materials-discovery-in-the-age-of-large

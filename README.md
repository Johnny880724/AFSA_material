# AFSA_material
An application of the Artificial Fish-Swarm Algorithm (AFSA) to the optimization of material potential energy.

## load_data.py
The `load_data.py` script is used to load and process data from specified subdirectories and filenames. It includes functions to extract lattice vectors from `.xyz` files and lattice energies from `.prop` files.

### Example Usage
From Ref.[2], material energy raw data can be downloaded, which contains the position data `traj-5A.xyz` and the energy data `traj-5A.prop`. Use the following script
```python
subdirectory = "raw_data/5A/"
xyz_filename = "traj-5A.xyz"
prop_filename = "traj-5A.prop"
save_filename = "crystal_parsed_data/5A_parsed_file.txt"

load_data(subdirectory, xyz_filename, prop_filename, save_filename)
```



## Reference
[1] Artificial Fish Swarming Algorithm: https://arxiv.org/abs/2011.05700 <br />
[2] ML on crystal: https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc04665k <br />
[3] Fish sworm csdn: https://blog.csdn.net/hba646333407/article/details/103082418 <br />
[4] Smoothed particle hydrodyanmics: https://ui.adsabs.harvard.edu/abs/1992ARA%26A..30..543M/abstract

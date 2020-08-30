# password-manager
Password manager to store encrypted passwords.

### Installation
The repository is supposed to run using the conda environment provided in "environment.yml". Having conda command (from Anaconda or Miniconda) you can install it moving to this folder and typing the following command in shell:

`conda env create environment.yml`

In case of further commits requiring different packages, you can update the environment by typing:

`conda env update environment.yml`

Finally, this repository can be installed as a (editable) package (named _PasswordManager_) using setuptools:

`python setup.py develop`

### Notes

Please, change "configuration.yml" path key to match the desired output folder. For example:

`path : C:\Users\"username"\Documents\folder`

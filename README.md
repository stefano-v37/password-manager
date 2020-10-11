# password-manager
Password manager to store encrypted passwords.

### Installation
The repository is supposed to run using the conda environment provided in "environment.yml". Having conda command (from Anaconda or Miniconda) you can install it moving to this folder and typing the following command in shell:

`conda env create environment.yml`

In case of further commits requiring different packages, you can update the environment by typing:

`conda env update environment.yml`

Finally, this repository can be installed as a (editable) package (named _PasswordManager_) using setuptools:

`python setup.py develop`

### How-to

Please, modify "configuration.yml" to add the desired users and a related key.
This key is supposed to match a system environment variable containing the desired folder
For example:

`path : `
`   default : pswdb`
`   user1 : env1`
`   user2 : env2`

Where ` echo %pswdb%` (Windows cmd) is:

`C:\Users\"username"\Documents\folder`

At the moment a default key is needed for the functionalities of the app.
# password-manager
Password manager to store encrypted passwords.

### Installation
The repository is supposed to run with packages listed in ".\environment.yml". I suggest using conda commands (from Anaconda or Miniconda) in shell:

```
conda env create path-to-package\environment.yml`
```

In case of further commits requiring different packages (not expected), you can update the environment by executing:

```
conda activate password-manager
conda env update path-to-package\environment.yml
```

Finally, this repository can be installed as a (editable) package (named _PasswordManager_) using setuptools:

```
python setup.py develop
```

### How-to

Please, modify "configuration.yml" to add the desired users and related keys.
Thos keys are supposed to match system environment variables linking to the desired folder.

For example:

```
path : 
   default : pswdb
   user1 : env1
   user2 : env2
```

Where ` echo %pswdb%` (Windows cmd) is:

```
C:\Users\"username"\Documents\folder
```

At the moment a default key is needed for the functionalities of the app.
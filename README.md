# password-manager
Password manager to store encrypted passwords.

### 1. Installation
The repository has been developed with packages listed in ".\environment.yml". These assure the stability of the module and I suggest using conda commands (from Anaconda or Miniconda) in shell:

```
conda env create path-to-package\environment.yml`
```

In case of further commits requiring different packages (not expected), you can update the environment by executing:

```
conda activate password-manager
conda env update path-to-package\environment.yml
```
(Probably, the module could still be working even with different version of the packages)

Finally, this repository can be installed as a package (named _PasswordManager_) using setuptools:

```
python path-to-package/setup.py
```

Eventually, as an editable package:

```
python path-to-package/setup.py develop
```

### 2. Configuration

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

### 3. Execution

To run the module you can import the package and use its methods but I suggest using the gui by executing the `__main__.py` file:

```
python -m PasswordManager
```
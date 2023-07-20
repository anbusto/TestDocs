# anbusto.github.io


## Requirements
You will need to install the following:

sphinx
sphinx_bootstrap_theme

```
pip install -U sphinx
pip install sphinx_bootstrap_theme      

```

We will also need to set up the Github account to use the Github Pages for the PyRIID repo.
I currnetly do not have permission to do this.

We also need to add the following folders to the PyRIID project

docs/

source/

To generate new files for updates in riid we must first redo the rst files with the following command
in the main PyRIID folder:

```
sphinx-apidoc -o source .\riid\ 
```

Then we need to rebuild the html files with the following command:

```
sphinx-build -b html source docs
```

You can see the changes locally in your file explorer. Once you approve, once you push these files to PyRIID then you will automatically trigger the workflow that is set up eariler in Github. If that workflow succeeds then your html files will be published to the specified website.

Or we just use the custom workflow that I made that generates the html pages and deploys them on any push. 



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

We also need to add the following folder to the PyRIID project

docs/
    /_sources
    /_static
    /.doctrees
    /build_files
    /source


I have made a workflow that creates the html files from a branch push, however it probably needs to push those updated files to the branch it is working on possibly or we do no workflow and we just have documentation for someone to run when we need the documentation updated.


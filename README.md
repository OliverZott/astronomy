# Astronomy Repository

Various examples and astronomy related training projects.

## Prerequisites

### pip

```bash
# Create/activate/deactivate venv
python -m venv venv
.\venv\Scripts\activate
source venv/bin/activate
.\venv\Scripts\deactivate

# Install packages with activated env and check
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list

# Freeze and Upgrade current packages  
pip freeze > pip_list.txt   
pip install --upgrade --force-reinstall -r requirements.txt
```

### conda

- `conda env create -f environment.yml`
- `conda env list`
- `conda activate astro_env` to activate env (also has to be done in VS Code!)
  - Check if Editor/Ide/Jupyter uses correct env and python-interpreter
  - `conda list` to check packages
- Maybe need to integrate conda-env into jupyter notebook/lab
  - <https://stackoverflow.com/questions/40694528/how-to-know-which-python-is-running-in-jupyter-notebook>
  - <https://stackoverflow.com/questions/53004311/how-to-add-conda-environment-to-jupyter-lab>

### Jupyter

- <https://towardsdatascience.com/how-to-set-up-anaconda-and-jupyter-notebook-the-right-way-de3b7623ea4a>
- <https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084>
- <https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874>

- extensions
  - `conda install -c conda-forge jupyter_contrib_nbextensions`  ... globally install jupyter extensions
  - <https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231>
  - <https://github.com/ipython-contrib/jupyter_contrib_nbextensions>

### Usefull tools (VS Code)

Settings:

- create settings file
- `format on save enable`
- `format notebook enable`

Tools

- install Autopep8 extension
- **markdownlint** by  David Anson

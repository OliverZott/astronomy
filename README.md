# Astronomy Repository

Various examples and astronomy related training projects.

## Prerequisites

### pip

create/activate/deactivate venv

```bash
python -m venv venv
.\venv\Scripts\activate
. venv/bin/activate
.\venv\Scripts\deactivate
```

install packages with activated env and check

````bash
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list
````

Freeze current packages  
`pip freeze > pip_list.txt   (to freeze current state)`

upgrade requirements-file  
`pip install --upgrade --force-reinstall -r requirements.txt`

### conda

- `conda env create -f environment.yml`
- `conda activate astro_env` to activate env (also has to be done in VS Code!)
  - Check if Editor/Ide/Jupyter uses correct env and python-interpreter
  - `conda list` to check packages
- Maybe need to integrate conda-env into jupyter notebook/lab
  - <https://stackoverflow.com/questions/40694528/how-to-know-which-python-is-running-in-jupyter-notebook>
  - <https://stackoverflow.com/questions/53004311/how-to-add-conda-environment-to-jupyter-lab>

### Usefull tools (VS Code)

- **markdownlint** by  David Anson

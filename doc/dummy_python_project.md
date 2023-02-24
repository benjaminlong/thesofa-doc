# Dummy Python Project

Starting a simple python project with a virtual env, **pip** (package installer for Python), **pytest** (unit-tests) and **git** (versioning tool).

```
project_dir/
  - doc/ # <-- Project's documentation
  - src/ # <-- Project's source code
    - tests/
      - test_template.py
    template.py
  - ./venv/ # <-- Project's virutalenv
  - requirement.txt # <-- Project's deps
  - README.md
```

### I. Virtual env

```python
path/to/project/dir$ python3 -m venv ./venv
path/to/project/dir$ python3 -m venv path/to/your/venv
```

##### Active
```python
path/to/project/dir$ source venv/bin/activage
```
##### Deactivate
```python
path/to/project/dir$ deactivate
```


### II. Dependencies
> Make sure your virtualenv is activated

##### Init project dependencies

```python
(venv) path/to/project/dir$ pip install -r requirements.txt
```

##### Add dependency 

Adding [pytest](https://docs.pytest.org/en/7.2.x/) python package: 

```python
# CLI exemple to install pytest dependency
(venv) path/to/project/dir$ pip install pytest
Collecting pytest
  Downloading pytest-7.2.1-py3-none-any.whl (317 kB)
[...]
Successfully installed [...] pytest-7.2.1 [...]
```

> Python dependencies should be managed inside a requirements.txt file or inside setup.py|setup.cfg

##### Remove dependency

```python
(venv) path/to/project/dir$ pip uninstall pytest
```

### III. UnitTest

To run pytest:
```python
(venv) path/to/project/dir$ pytest
(venv) path/to/project/dir$ pytest path/to/your/test_dummy.py
```

### IV. Git

```

```

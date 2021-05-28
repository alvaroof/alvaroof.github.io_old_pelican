# Repository for alvaroof.github.io personal website. 

Description to be added.

---
## Pelican installation

### Create repository
create repository with name username.github.io
cd ~ $ git clone https://github.com/tu_username/tu_username.github.io.git
cd tu_username.github.io

### create new branch source, in which all the files will go
git checkout -b source

### create requirements.txt
pelican==4.6.0
pelican-jupyter==0.10.0
markdown
ghp-import
notebook==5.6.0
nbconvert==5.6.0
python-gettext==4.0.0

### create virtualenv pelican_env using python 3.7
pip install virtualenv
viritualenv pelican_env
pelican_env/scripts/activate
pip install -r requirements.txt

### create starting template for pelican
pelican-quickstart

### commit everything into source. first create gitignore containing .vscode, pelican_env
git add -A
git commit -m "First commit"

### place some content in content/
pelican content -o output -s pelicanconf.py
pelican content -o output -s publishconf.py
ghp-import output -b gh-pages
git push git@github.com:alvaroof/alvaroof.github.io.git gh-pages:master

## DONE.
---
## Add plugins

### First download plugins from github by cloning repository in a different folder
git clone --recursive https://github.com/getpelican/pelican-plugins pelican-plugins

---

## Customize Theme

### First download Pelican themes from github by cloning repository in a different folder
git clone --recursive https://github.com/getpelican/pelican-themes pelican-themes


---

## Process jupyter notebooks

### Add the following to pelicanconf.py
```python
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
```




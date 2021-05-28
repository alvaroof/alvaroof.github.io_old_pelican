pelican content -o output -s pelicanconf.py
pelican content -o output -s publishconf.py
ghp-import output -b gh-pages
git push git@github.com:alvaroof/alvaroof.github.io.git gh-pages:master
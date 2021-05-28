pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push git@github.com:alvaroof/alvaroof.github.io.git gh-pages:master
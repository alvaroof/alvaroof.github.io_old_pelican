Title: Code Test
Date: 2021-05-18 10:30
Modified: 2021-05-18 10:30
Category: Tutorial
Slug: code-test
Authors: Alvaro Ortiz
Summary: Mi primer post usando Pelican y GitHub Pages

# This is just the Title inside the Markdown

```python
################################################################################
# OS FUNCTIONALITIES
# PROXY PROBLEMS, SSL PROBLEMS, AND OTHER CALAMITIES
# CONVERT jupyter notebooks to other formats
# MAGIC FUNCTIONS
# PROBLEMS LOADING CUSTOM MODULES
# USE CUSTOM PARAMETERS IN PYTHON SCRIPTS
# PICKLE
# PROGRESS BAR
# ZIPS
# CODE CHECKS
# add value to variable, such as path
# GIT CALAMITIES
# Read data from github repo using requests
################################################################################

################################################################################
# OS FUNCTIONALITIES
################################################################################

##Display environmental variables
import os
%env

## Check if file or dir exists
import os
os.path.isfile('./final_data_folder')
os.path.isdir(directory)
os.path.exists('./final_data_2020.csv')

## Remove file or dir
import os
os.remove("ChangedFile.csv")
print("File Removed!")

## only if dir is empty
os.rmdir()

################################################################################
# PROXY PROBLEMS AND OTHER CALAMITIES
################################################################################

# BUT WHAT HAPPENS WHEN YOUR USER AND PASSWORD HAVE SPECIAL CHARCTERS?
# YOU NEED TO ENCODE THEM!
from urllib.parse import quote

username = quote('type your user')
password = quote('type your password')
proxy = 'proxy address or IP'
proxy_port = 'port'

proxy_http = 'http://' + username + ':' + password + '@' + proxy + ':' + proxy_port
proxy_https = 'https://' + username + ':' + password + '@' + proxy + ':' + proxy_port

# THEN WE HAVE TWO OPTIONS

# 1. the first solution is more specific, just modify proxy for one specific request
proxies = {'http' : proxy_http, 'https': proxy_https}
url = 'https://google.com'
r = requests.get(url, proxies=proxies)

# 2. this is an all-purpose every-request solution
os.environ['http_proxy'] = proxy_http
os.environ['https_proxy'] = proxy_https
url = 'https://google.com'
r = requests.get(url)

print(r.status_code)
print(r.text)


#calling pip behind proxy
pip install --proxy http://user:password@10.185.190.100:8080 torch

# IF in pycharm there is a problem with the SSL certificate when downloading packages
# add the following to %APPDATA%/pip/pip.ini

[global]
trusted-host = pypi.python.org
               pypi.org
               files.pythonhosted.org

#################################################################################
# CONVERT jupyter notebooks to other formats
################################################################################

#convert notebook to other formats
jupyter nbconvert --to html my_notebook.ipynb
jupyter nbconvert --to script .\tpa_analytics_nlp_analysis_v2.ipynb

#################################
# MAGIC FUNCTIONS
#################################

#tracks how long this takes to run
%time #only this line
%%time #all the code in the cell

####################################
# PROBLEMS LOADING CUSTOM MODULES
####################################

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

# After this just do the following

from project1.module1 import whatever_module

########################################################
# USE CUSTOM PARAMETERS IN PYTHON SCRIPTS
###########################################################

import sys
import argparse

if __name__ == '__main__':

    # Initiate the parser
    parser = argparse.ArgumentParser()

    # Add long and short argument
    parser.add_argument("--width", "-w", help="set output width")

    # Read arguments from the command line
    args = parser.parse_args()
    print('Parameters...\n')
    print(args.width)
    
# This allows to define width when running from shell --> python main.py --width 3

########################################################
# USE PYTHON VARS AS BASH PARAMETERS INSIDE NOTEBOOK
###########################################################

%%bash -s "$output_filename" "$shiny_destination"

echo "Copying $1 into $2"
cp $1 $2

#####################################
# PICKLE
#####################################

import pickle 
python_object = object() 
file_object = open('filename_pi.obj', 'wb') 
pickle.dump(python_object, file_object)

file_object = open('filename_pi.obj', 'rb') 
python_object = pickle.load(file_object)

# or using PANDAS
original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
pd.to_pickle(original_df, "./dummy.pkl")
unpickled_df = pd.read_pickle("./dummy.pkl")

#####################################
# PROGRESSBAR
#####################################
#How to create PROGRESSBAR beyond tqdm()
import progressbar

# How many users for progress bar
n_users = len(users)
cnter = 0
bar = progressbar.ProgressBar(maxval=n_users+1, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

# For each user
for user in users:
    # Update the progress bar
    cnter+=1 
    #DO SOMETHING
    bar.update(cnter)

bar.finish()

#####################################
# ZIPS
#####################################
import os
import zipfile

local_zip = '/tmp/horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp/horse-or-human')
zip_ref.close()

#######################################################################
# CODE CHECKS
#######################################################################

#USE PYLINT!
https://docs.pylint.org/en/1.6.0/tutorial.html


###############################################################
# add value to variable, such as path
###############################################################

PATH=~/opt/bin:$PATH.

###############################################################
# GIT CALAMITIES
################################################################################

git config --global --unset-all http.proxy
git config --global --add http.proxy http://USER:PASSWORD@10.185.190.100:8080
git config --global --unset-all https.proxy
git config --global --add https.proxy https://USER:PASSWORD@10.185.190.100:8080

# Issue authenticating to 2FA in gitlab. Need to deactivate SSL check, and if you fail to enter
# the personal access token at the beginning, then probably you will need to also unset the cresential.helper and retry

git config --global http.sslVerify false
git config --system --unset credential.helper


#######################################################################
# READ FROM WEB
#######################################################################

# load global data but US
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

#######################################################################
# READ DATA FROM GDRIVE
#######################################################################

# Run this cell to connect to your Drive folder
from google.colab import drive
drive.mount('/content/gdrive')

df = pd.read_csv('/content/gdrive/My Drive/colab/processed_SERVICE.CLIENTS.PHARMACIE@BAYER.COM_extract_2021-03-02.csv')
df['target'] = df['target'].astype('category')




```


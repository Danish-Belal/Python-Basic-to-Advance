

import flask
import  pandas as pd

# To Create a vistual enviroument first we need to install (virtaulenv)
# write in your powershell (pip install virtualenv)

# We create a new virtual envirounment  using (virtualenv Myproject) --> this will create a new virtual envirounment

# then we activate our new vitrual envirounment .
# for window --> (.\Myprojectven\Scripts\activate.ps1)  -->  sometime it throw script running error because ms policy.
# for resolving this problem --> (Set-ExecutionPolicy Unrestricted -Scope Process) on your powershell then press y for yes
# Then activate it again.

# for Linux/MacOS -->  source Myproject/bin/activate


# pip freeze commands.

# pip freeze --> will give you all install module along with version .
# pip freeze > requirment.txt  --> will create a txt file and print all module with their version in txt file
# you can share this file to use same environment.

# if you want to create same environment on other virtual environment use pip install requirment.txt 
# this will install all module along with their version which present in requirment.txt



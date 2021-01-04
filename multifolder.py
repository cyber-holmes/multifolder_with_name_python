## import modules
import os
import getpass 
## importing of modules done
## create path
a="c:\\Users\\"
b= getpass.getuser()
c="\\Desktop"
d=a+b+c
os.chdir(d)
##path is created
##create a folders and make loop out of it
files=["haha","haha2","haha3","haha4"]
for file in files:
 os.mkdir(file)


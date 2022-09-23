import os
import git

# Create directory that contains the image labelling python script
LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

# Clones labelimg repo is the labeling directory does not exist
# ****** RUN ONCE *******
if not os.path.exists(LABELIMG_PATH):
    os.makedirs(LABELIMG_PATH)
    git.Repo.clone_from('https://github.com/heartexlabs/labelImg.git', LABELIMG_PATH)

# Check if Mac or Windows, then install labelimg program
# ****** RUN ONCE *******
if os.name == 'posix':
    pass
elif os.name =='nt':
    os.system(f'cmd /c "cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc"')
else:
    print("No Operating System?")

# RUn the labelimg program
if os.name == 'posix':
    pass
elif os.name =='nt':
    os.system(f'python .\{LABELIMG_PATH}\labelImg.py')
else:
    print("No Operating System?")

# SHORTCUT "W" KEY TO WRAP AROUND DESIRED IMAGE CONTENT
# BE VERY CAREFUL WHAT YOU NAME THE CONTENT
# SAVE THE CONTENT CAPTURED!
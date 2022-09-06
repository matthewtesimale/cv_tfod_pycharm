# Computer Vision - Tensorflow Object Detection - PyCharm
A repository with the tools necessary for executing the Nicholas Renotte tensorflow tutorial within PyCharm instead of Jupyter Notebooks.

Utilize the scripts within this repo and follow the instructions below:

Clone repo
create virtual environment & python interpreter
	Settings
	Project: {name}
	Gear button & ADD
		Virtual Environment
		Location: inside project directory
		Base Interpreter: path to python 3.10 executable
.\{venv}\Scripts\activate
(ensure you are in the virtual environment)
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

run capture_images.py
run label_images.py

save 80% of images and annotations in ~\Tensorflow\workspace\images\train
save 20% of images and annotations in ~\Tensorflow\workspace\images\test



# Computer Vision - Tensorflow Object Detection - PyCharm
A repository with the tools necessary for executing the Nicholas Renotte tensorflow tutorial within PyCharm instead of Jupyter Notebooks.

Utilize the scripts within this repo and follow the instructions below:

<ol>
<li>Clone repo</li>
<li>create virtual environment & python interpreter</li>
<li>Settings</li>
<li>Project: {name}</li>
<li>Gear button & ADD</li>
<li>Virtual Environment</li>
<li>Location: inside project directory</li>
<li>Base Interpreter: path to python 3.10 executable</li>
<li>.\{venv}\Scripts\activate</li>
<li>(ensure you are in the virtual environment)</li>
<li>python -m pip install --upgrade pip</li>
<li>python -m pip install -r requirements.txt</li>
<li>run capture_images.py</li>
<li>run label_images.py</li>
<li>save 80% of images and annotations in ~\Tensorflow\workspace\images\train</li>
<li>save 20% of images and annotations in ~\Tensorflow\workspace\images\test</li>
<li>run paths.py</li>
<li>change the name of CUSTOM_MODEL_NAME to something that is not in ~\Tensorflow\workspace\models</li>
<li>(OPTIONAL - ENABLE CUDA AND CNN DRIVERS)</li>
<li>run training.py</li>
<li>Ensure that labels in image annotations match what the LABEL_MAP has.</li>
<li>Check what is the highest checkpoint value in ~\Tensorflow\workspace\models\{name of model}</li>
<li>change the 'ckpt-#' to whatever the highest checkpoint is in the folder above</li>
<li>run video_processing.py</li>
</ol>

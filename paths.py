import os
import git

# ------------------------------- SETUP PATHS -------------------------------
# Name of model - Should change if wanting to version a model
CUSTOM_MODEL_NAME = 'my_ssd_mobnet_guns'
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
JSON_TO_XML_NAME = 'labelme2voc.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow', 'scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow', 'models'),
    'JSON_TO_XML_PATH': os.path.join('Tensorflow', 'json_xml', 'examples', 'bbox_detection'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace', 'annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace', 'images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace', 'models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace', 'pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME),
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'export'),
    'TFJS_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'tfjsexport'),
    'TFLITE_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'tfliteexport'),
    'PROTOC_PATH': os.path.join('Tensorflow', 'protoc')
 }

files = {
    'PIPELINE_CONFIG': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME),
    'JSON_TO_XML_SCRIPT': os.path.join(paths['JSON_TO_XML_PATH'], JSON_TO_XML_NAME)
}

for path in paths.values():
    if not os.path.exists(path):
        if os.name == 'posix':
            pass
        if os.name == 'nt':
            os.makedirs(path)

# ------------ Download TF Models Pretrained Models from Tensorflow Model Zoo and Install TFOD ------------
if os.name=='nt':
    os.system(f'cmd /c "pip install wget"')
    import wget

if not os.path.exists(os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection')):
    git.Repo.clone_from('https://github.com/tensorflow/models', paths['APIMODEL_PATH'])

if not os.path.exists(files['JSON_TO_XML_SCRIPT']):
    git.Repo.clone_from('https://github.com/wkentaro/labelme.git', paths['JSON_TO_XML_PATH'])

# Install Tensorflow Object Detection
if os.name == 'posix':
    # !apt -get install protobuf -compiler
    # !cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out =. && cp object_detection/packages/tf2/setup.py . && python -m pip install .
    pass

if os.name == 'nt' and not os.path.exists(os.path.join(paths["PROTOC_PATH"], 'protoc-3.15.6-win64.zip')):
    url = "https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protoc-3.15.6-win64.zip"
    wget.download(url)
    os.system(f'move protoc-3.15.6-win64.zip {paths["PROTOC_PATH"]}')
    os.system(f'cd {paths["PROTOC_PATH"]} && tar -xf protoc-3.15.6-win64.zip')
    os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join(paths['PROTOC_PATH'], 'bin'))
    os.system(f'cmd /c "cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && copy object_detection\\packages\\tf2\\setup.py setup.py && python setup.py build && python setup.py install"')
    os.system(f'cmd /c "cd Tensorflow/models/research/slim && pip install -e ."')

if os.name =='posix':
    # !wget {PRETRAINED_MODEL_URL}
    # !mv {PRETRAINED_MODEL_NAME+'.tar.gz'} {paths['PRETRAINED_MODEL_PATH']}
    # !cd {paths['PRETRAINED_MODEL_PATH']} && tar -zxvf {PRETRAINED_MODEL_NAME+'.tar.gz'}
    pass
if os.name == 'nt' and not os.path.exists(os.path.join(paths["PRETRAINED_MODEL_PATH"], PRETRAINED_MODEL_NAME+".tar.gz")):
    wget.download(PRETRAINED_MODEL_URL)
    os.system(f'move {PRETRAINED_MODEL_NAME+".tar.gz"} {paths["PRETRAINED_MODEL_PATH"]}')
    os.system(f'cd {paths["PRETRAINED_MODEL_PATH"]} && tar -zxvf {PRETRAINED_MODEL_NAME+".tar.gz"}')

import os
import training as sp

VERIFICATION_SCRIPT = os.path.join(sp.paths['APIMODEL_PATH'], 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')
# Verify Installation
os.system(f'python {VERIFICATION_SCRIPT}')

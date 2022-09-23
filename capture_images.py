import cv2
import uuid
import os
import time

# DEFINE IMAGE CATEGORIES TO COLLECT INTO #
labels = ['handgun', 'shotgun']
number_imgs = 10

# SETUP FOLDERS ON OS #
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

if not os.path.exists(IMAGES_PATH):
    # Check if os system is Mac
    if os.name == 'posix':
        pass
    # Check if os system is Windows
    if os.name == 'nt':
         os.makedirs(IMAGES_PATH)
# Create each directory representing the image categories as defined above
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)

# CAPTURE IMAGES USING OPENCV #
for label in labels:
    # Connect to video source (0 = webcam)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(3)
    # Begin loop to capture {number_imgs} pictures for each category
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        # Create path for image as well as image name
        # (path_to_collected_images + image_category_directory + image_name)
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        # cv2.imwrite(filename, image)
        # filename: A string representing the file name. The filename must include image format like .jpg, .png, etc.
        # image: It is the image that is to be saved.
        # Return Value: It returns true if image is saved successfully.
        cv2.imwrite(imgname, frame)
        # Show the image that was taken
        cv2.imshow('frame', frame)
        time.sleep(3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

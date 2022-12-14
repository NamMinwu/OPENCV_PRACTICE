import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
people = ['Ben Afflek', 'Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR = r'C:\Users\남민우\opencv_python\Faces\train'


features = []
labels = []

def test_train():
    for person in people:
        label = people.index(person)
        i = 1
        while True:
            file_path = f"./Faces/train/{person}/{i}.jpg"
            try:
                file = open(file_path)
                file.close()
                img_array = cv.imread(file_path)
                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
                for (x,y,w,h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    features.append(faces_roi)
                    labels.append(label)
                
                i += 1

            except FileNotFoundError:
                break


# def create_train():
#     for person in people:
#         path= os.path.join(DIR, person)
#         label = people.index(person)

#         for img in os.listdir(path):
#             img_path = os.path.join(path, img)
            
#             img_array = cv.imread(img_path)
#             gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
#             faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
#             for (x,y,w,h) in faces_rect:
#                 faces_roi = gray[y:y+h, x:x+w]
#                 features.append(faces_roi)
#                 labels.append(label)

test_train()


print('Training done ----------')


features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features list and ther labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

cv.waitKey(0)
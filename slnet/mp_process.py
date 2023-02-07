import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
cnt = 0

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def draw_styled_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             )
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             )
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             ) 

def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, lh, rh])


def plt_imshow(title='image', img=None, figsize=(8 ,5), file_name='img'):
    global cnt
    plt.figure(figsize=figsize)
 
    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []
 
            for i in range(len(img)):
                titles.append(title)
 
        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
 
            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
            save_name = str(cnt)+'.png'
            plt.savefig(save_name)

    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.savefig('')
    
    plt.show()

DATA_PATH = os.path.join('MP_Data') 
actions = np.array(['']) # sign language name
no_sequences = 100
sequence_length = 30

for action in actions:
    try: 
        os.makedirs(os.path.join(DATA_PATH, str(action)))
    except:
        pass

for action in actions: 
    dirmax = 1
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(dirmax+sequence)))
        except:
            pass

def file_naming(x):
    namestr = "000"+str(x)
    while len(namestr)>3: namestr = namestr[1:]
    return namestr

image_path = os.path.join('data_image')
save_Path = os.path.join('MP_Data')

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    image_list = os.listdir(image_path)
    
    for sl_name in os.listdir(image_path):
        cnt = 1
        sl_video_path = os.path.join(image_path + "/" + sl_name)
        
        for num_video in os.listdir(sl_video_path):
            num_sl_image_path = os.path.join(sl_video_path+"/"+num_video)
            print(num_sl_image_path)
            image_cnt = 1
            for num_image in os.listdir(num_sl_image_path):
                num_image_path = os.path.join(num_sl_image_path + "/" + num_image)
                frame = cv2.imread(num_image_path)
                print(frame)

                img_original = frame

                img, res = mediapipe_detection(frame, holistic)

                draw_styled_landmarks(img, res)

                keypoints = extract_keypoints(res)
                npy_path = os.path.join(save_Path, str(cnt), file_naming(image_cnt))
                np.save(npy_path, keypoints)
                print(npy_path)
                image_cnt+=1
            cnt+=1

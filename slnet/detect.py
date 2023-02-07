import numpy as np
import tensorflow as tf
import cv2
import os
from matplotlib import pyplot as plt
import time 
import mediapipe as mp
from tensorflow.keras.preprocessing.sequence import pad_sequences

def detecting():
    mp_holistic = mp.solutions.holistic
    mp_drawing = mp.solutions.drawing_utils

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

    model = tf.keras.models.load_model('model_files/sl.h5') # Input trained h5 file
    actions = np.array([]) # Input sign language name


    sequence = []
    result = []
    rr = []

    valid_path = os.path.join('valid')
    valid_list = os.listdir(valid_path)
    total_size = len(valid_list)
    
    with mp_holistic.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.5) as holistic:
        for image_path in os.listdir(valid_path):
            num_image = os.path.join(valid_path + "/" + image_path)

            frame = cv2.imread(num_image)
            img_original = frame

            image, res = mediapipe_detection(frame, holistic)

            draw_styled_landmarks(image, res)

            keypoints = extract_keypoints(res)
            sequence.append(keypoints)
            sequence = sequence[-1*total_size:]

        cur = sequence[0:30]
        ret = model.predict(np.expand_dims(cur, axis=0))[0]   

        for i in range(30, total_size, 1):
            cur = cur[1:]
            cur.append(sequence[i])
            ret = model.predict(np.expand_dims(cur, axis=0))[0]
            result.append(actions[np.argmax(ret)])

    sz = len(result)
    cnt = 1
    for j in range(0, sz):
        if j == sz - 1: 
            tmp = []
            tmp.append(result[j])
            tmp.append(cnt)
            rr.append(tmp)
            break

        if result[j]==result[j+1]: cnt+=1

        else:
            tmp = []
            tmp.append(result[j])
            tmp.append(cnt)
            rr.append(tmp)
            cnt = 1

    res_sentence = []    
    sz_rr = len(rr)                  
    f_flag = False

    for j in range(0, sz_rr):
        idx_str = rr[j][0]
        idx_num = rr[j][1]

        for k in res_sentence:
            if idx_str == k:
                f_flag = True
                break

        if f_flag:
            f_flag = False
            continue
        
        for k in range(j, sz_rr):
            if idx_str==rr[k][0] and idx_num<rr[k][1]: break
            
            if k==sz_rr-1:
                res_sentence.append(idx_str)
    
    print(res_sentence)
import cv2
import mediapipe as mp
import os
import time
import math
import HandTrackingModule as htm
import FaceMeshModule as fmm
wCam=1280
hCam=720
cap = cv2.VideoCapture(2)
cap.set(3,wCam)
cap.set(4, hCam)
if not cap.isOpened():
    print("ERROR: Cannot open camera")
    exit()

folderPath=os.path.join(os.path.dirname(__file__), "Monkey Images")
myList=os.listdir(folderPath)
print(myList)
overlayList=[]

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    image = cv2.resize(image, (300, 200))  # Resize to 200x300
    overlayList.append(image)

print(len(overlayList))
mesh=fmm.FaceMeshDetector(maxFaces=1)
detector=htm.handDetector(maxHands=2, detectionCon=0.5)
while True:
    success, img=cap.read()
    if not success:
        print("ERROR: Failed to read frame from camera")
        break

    img=detector.findHands(img)
    lmlist=detector.findPosition(img, draw=False)
    faces=mesh.findFaceMesh(img)
    face_detected = len(faces) > 0
    tipids=[4,8,12,16,20]
    faceids=[61, 291, 4, 152, 14]
    
    def distance(a, b):
          return math.hypot(a[0]-b[0], a[1]-b[1])
    if(len(lmlist)!=0):
        fingers=[]
        #thumb
        if len(detector.results.multi_hand_landmarks) >= 2:
                lmlist_hand1=detector.findPosition(img, handNo=0, draw=False)
                lmlist_hand2=detector.findPosition(img, handNo=1, draw=False)
                if len(lmlist_hand1) != 0 and len(lmlist_hand2) != 0:
                        fingers_hand1 = [1 if lmlist_hand1[i][2] < lmlist_hand1[i-1][2] else 0 for i in tipids]
                        fingers_hand2 = [1 if lmlist_hand2[i][2] < lmlist_hand2[i-1][2] else 0 for i in tipids]
        
                        if sum(fingers_hand1) == 5 and sum(fingers_hand2) == 5:
                                img[0:200, 0:300]=overlayList[0]

        
        
                
        else:
            h,w,c=img.shape
            left_cheek = (int(faces[0][234][0]), int(faces[0][234][1]))
            right_cheek = (int(faces[0][454][0]), int(faces[0][454][1]))
            face_width = distance(left_cheek, right_cheek)

            # 3. Calculate Mouth Corners in Pixels
            left_mouth = (int(faces[0][61][0]), int(faces[0][61][1]))
            right_mouth = (int(faces[0][291][0]), int(faces[0][291][1]))
            
            chin_x=int(faces[0][14][0])
            chin_y=int(faces[0][14][1])
            chin=(chin_x, chin_y)
            index_finger_x=lmlist[8][1]
            index_finger_y=lmlist[8][2]
            index_finger=(index_finger_x, index_finger_y)
                    
           
            THINKING_FINGER_DIST=150
            SMILE_THRESHOLD=40
            IDEA_FINGER_HEIGHT=chin_y
            smile=(distance(left_mouth, right_mouth))
            
            if index_finger_y< lmlist[7][2] and smile>SMILE_THRESHOLD and distance(index_finger, chin)>THINKING_FINGER_DIST:
                    img[0:200, 0:300]=overlayList[2]
            elif index_finger_y< lmlist[7][2] and distance(index_finger, chin)<THINKING_FINGER_DIST:
                    img[0:200, 0:300]=overlayList[1]
    else:
        if len(overlayList) > 3:
                img[0:200, 0:300]=overlayList[3]

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
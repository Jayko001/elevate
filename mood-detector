import cv2 
import time
from deepface import DeepFace

t = 15 #setting the time after which the photo will automatically be captured
timeout = time.time() + t 

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0) #using the webcam
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        
        if key == ord('s') or time.time() > timeout:  #executed if if 's' is pressed or time t has passed
            cv2.destroyAllWindows() #clearing all the data
            face_analysis = DeepFace.analyze(frame,actions=['emotion']) #analyzing the emotions of saved image - 
            print(face_analysis)
            print(face_analysis['dominant_emotion']) #printing the dominant emotion in the image
            break
            
        elif key == ord('q'): #stopping the program if 'q' is pressed
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

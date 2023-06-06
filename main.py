import cv2
import face_recognition
import spotify_usage as spot
import time



# keep track of state diagram
# 0 = music not playing
# 1 = music playing
state = 0

vid = cv2.VideoCapture(0)
# Lower res to improve performance
vid.set(3,160)
# Keeps track of face coordinates
face_locations = []

while True:
    ret, frame = vid.read()
    #convert to HSV colorspace
    img = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(img)

    if face_locations:
        if state == 0:
            spot.start_playback()
            state == 1
    else:
        time.sleep(2) # 2 second grace period

        # Check for faces after grace period
        ret, frame = vid.read()
        img = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(img)
        if not face_locations:
            spot.pause_playback()
            state = 0

    # Show video frame
    cv2.imshow('frame', frame)
    
    #press q to stop running
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()




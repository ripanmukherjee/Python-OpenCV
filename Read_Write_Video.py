#Show video from webcam
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() #here ret will check True or False and frame will capture the video

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Show video from webcam as gray scale
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() #here ret will check True or False and frame will capture the video

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # if you want to display as gray 
    cv2.imshow('Frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Writing the video from webcam to a directory
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))
while(True):
    ret, frame = cap.read() #here ret will check True or False and frame will capture the video
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # by set method you can also set the frame of the video. Max height and width is 1280 and 720
        cap.set(3, 700)
        cap.set(4, 700)

        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # if you want to display as gray
        cv2.imshow('Frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


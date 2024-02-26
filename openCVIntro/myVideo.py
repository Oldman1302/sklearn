import cv2

# Call access to camera, 0: main camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    # ret - shows success capture operation
    # frame - captured frame
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # Конец, клавиша q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# make resources free are linked with VideoCapture object
cap.release()
cv2.destroyAllWindows()

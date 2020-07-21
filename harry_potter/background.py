import cv2
#Data from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    if ret:
        #back is what camera is reading
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord('q'):
            # Q is pressed so save the image
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()






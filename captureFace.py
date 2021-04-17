import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

name = "Ishwar"

def enableCamera():
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "{}.png".format(name)
            cv2.imwrite("./known_faces/"+img_name, frame)
            print("{} written!".format(img_name))

    cam.release()

    cv2.destroyAllWindows()


enableCamera()
import cv2

def take_snapshot():
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite()method is used to save an image to any storage divice
        cv2.imwrite("newPicture1.jpg",frame)
        result=False

    #releases the camera
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()
import numpy as np
import pyautogui as pag
import cv2
import time

global frame

def print_pos(event,x,y,flags,param):
    cv2.putText(frame,"("+str(x)+","+str(y)+")",(100,100),font,1,(255,255,255),2)

    cv2.imshow("Name",frame)

def  open_cv():
        
    cap = cv2.VideoCapture(0)
    scrn_x,scrn_y = pag.size()
    ocr_ok = 0;

    ##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200);
    ##cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600);

    cv2.namedWindow("Name",cv2.WND_PROP_FULLSCREEN);
    cv2.setWindowProperty("Name", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN);
    ##cv2.setMouseCallback("Name",print_pos);

    print("width : " + str(scrn_x) + "\nheight : " + str(scrn_y))
    print(int(scrn_x/2-100))
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    while(True):
    

    # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.resize(frame,(scrn_x,scrn_y),interpolation = cv2.INTER_CUBIC)

    # Our operations on the frame come here
        xp,yp = pag.position()
        cv2.putText(frame,"("+str(xp)+","+str(yp)+")",(xp,yp),font,1,(255,255,255),2)

        cv2.putText(frame,str(time.ctime()[11:19]),(int(.75*scrn_x),int(.1*scrn_y)),font,2,(255,255,255),2)

        #cv2.rectangle(frame,(xp,yp),(xp+300,yp+300),(0,255,0),12)
        cv2.rectangle(frame,(int(scrn_x/2-400),int(scrn_y/2-200)),(int(scrn_x/2+400),int(scrn_y/2+200)),(0,255,0),10)
        cv2.rectangle(frame,(int(scrn_x-300),int(scrn_y-100)),(int(scrn_x-5),int(scrn_y-5)),(0,0,255),5)
        cv2.putText(frame,"OK",(int(scrn_x-200),int(scrn_y-25)),font,2,(0,0,255),2)

    # Display the resulting frame
        #cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN)
        if xp >= scrn_x-300 and yp >= scrn_y-100 and xp <= scrn_x - 5 and yp <= scrn_y - 5 :
            cv2.putText(frame,str(int(ocr_ok/20)),(100,100),font,1,(255,255,255),2)

            ocr_ok += 1
            if ocr_ok == 100:
                break;
        else:
            cv2.putText(frame,str(ocr_ok),(100,100),font,1,(255,255,255),2)
            ocr_ok = 0
            

        cv2.imshow("Name",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    print("OK");
    return ocr_ok,frame[(int(scrn_y/2-200)):int(scrn_y/2+200),(int(scrn_x/2-400)):int(scrn_x/2+400),:]
##    return 1

if __name__ == "__main__":
    ok,ocr = open_cv()
    if ok != 0:
        cv2.namedWindow("Test");
        cv2.imshow("Test",ocr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


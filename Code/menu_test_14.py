import numpy as np
import pyautogui as pag
import cv2
import time

global strig 
strig = ""

def clikz(event,x,y,flags,param):
    global strig
    if event == cv2.EVENT_LBUTTONDOWN:
    ##      if( x > 0 and x < 230 ):
    ##          print("podaaaa!!!!")
            if ( x > 0*int(scrn_x/4) and x < 1*int(scrn_x/4) and  y > 1*int(scrn_y/4) and y < 2*int(scrn_y/4)) :
                strig += "1";
            elif ( x > 1*int(scrn_x/4) and x < 2*int(scrn_x/4) and  y > 1*int(scrn_y/4) and y < 2*int(scrn_y/4)) :
                strig += "2";
            elif ( x > 2*int(scrn_x/4) and x < 3*int(scrn_x/4) and  y > 1*int(scrn_y/4) and y < 2*int(scrn_y/4)) :
                strig += "3";
            elif ( x > 3*int(scrn_x/4) and x < 4*int(scrn_x/4) and  y > 1*int(scrn_y/4) and y < 2*int(scrn_y/4)) :
                strig += "4";
            elif ( x > 0*int(scrn_x/4) and x < 1*int(scrn_x/4) and  y > 2*int(scrn_y/4) and y < 3*int(scrn_y/4)) :
                strig += "5";
            elif ( x > 1*int(scrn_x/4) and x < 2*int(scrn_x/4) and  y > 2*int(scrn_y/4) and y < 3*int(scrn_y/4)) :
                strig += "6";
            elif ( x > 2*int(scrn_x/4) and x < 3*int(scrn_x/4) and  y > 2*int(scrn_y/4) and y < 3*int(scrn_y/4)) :
                strig += "7";
            elif ( x > 3*int(scrn_x/4) and x < 4*int(scrn_x/4) and  y > 2*int(scrn_y/4) and y < 3*int(scrn_y/4)) :
                strig += "8";
            elif ( x > 0*int(scrn_x/4) and x < 1*int(scrn_x/4) and  y > 3*int(scrn_y/4) and y < 4*int(scrn_y/4)) :
                strig += "Calling";
            elif ( x > 1*int(scrn_x/4) and x < 2*int(scrn_x/4) and  y > 3*int(scrn_y/4) and y < 4*int(scrn_y/4)) :
                strig += "9";
            elif ( x > 2*int(scrn_x/4) and x < 3*int(scrn_x/4) and  y > 3*int(scrn_y/4) and y < 4*int(scrn_y/4)) :
                strig += "0";
            elif ( x > 3*int(scrn_x/4) and x < 4*int(scrn_x/4) and  y > 3*int(scrn_y/4) and y < 4*int(scrn_y/4)) :
                strig = strig[:-1];
            else:
                pass
            print(strig)
            print("("+str(x)+","+str(y)+")")
           
                             
img=cv2.imread("white.png")

cv2.namedWindow("pic",cv2.WND_PROP_FULLSCREEN);
cv2.setWindowProperty("pic", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN);    

font = cv2.FONT_HERSHEY_SIMPLEX
scrn_x,scrn_y = pag.size()
print(scrn_x,scrn_y)

while(True):
    img = cv2.imread("white.png")
    xp,yp = pag.position() #This takes the mouse pointer location in the screen

    img = cv2.resize(img,(scrn_x,scrn_y),interpolation = cv2.INTER_CUBIC) # this is used to resize the imcoming feed to fit the screen size

    cv2.putText(img,"("+str(xp)+","+str(yp)+")",(xp,yp),font,1,(0,0,0),2) #this prints the location of the pointer on screen as a tupple

    #horizontal
    '''cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-1075)),(int(scrn_x-5),int(scrn_y-810)),(0,0,255),2) #rect 1
    cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-805)),(int(scrn_x-5),int(scrn_y-542)),(0,0,255),2) #rect 2
    cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-535)),(int(scrn_x-5),int(scrn_y-272)),(0,0,255),2) #rect 3
    cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-265)),(int(scrn_x-5),int(scrn_y-5)),(0,0,255),2) #rect 4

    #vertical 
    cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-1075)),(int(scrn_x-1435),int(scrn_y-5)),(0,0,255),2) #rect 1
    cv2.rectangle(img,(int(scrn_x-1430),int(scrn_y-1075)),(int(scrn_x-950),int(scrn_y-5)),(0,0,255),2) #rect 2
    cv2.rectangle(img,(int(scrn_x-945),int(scrn_y-1075)),(int(scrn_x-465),int(scrn_y-5)),(0,0,255),2) #rect 3
    cv2.rectangle(img,(int(scrn_x-460),int(scrn_y-1075)),(int(scrn_x-5),int(scrn_y-5)),(0,0,255),2) #rect 4'''


    cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-1075)),(int(scrn_x-1430),int(scrn_y-805)),(0,0,255),2)

    cv2.putText(img,"1",(int(scrn_x/8),int(3*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"2",(int(3*scrn_x/8),int(3*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"3",(int(5*scrn_x/8),int(3*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"4",(int(7*scrn_x/8),int(3*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"5",(int(scrn_x/8),int(5*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"6",(int(3*scrn_x/8),int(5*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"7",(int(5*scrn_x/8),int(5*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"8",(int(7*scrn_x/8),int(5*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"9",(int(3*scrn_x/8),int(7*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"0",(int(5*scrn_x/8),int(7*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"Call",(int(scrn_x/8),int(7*scrn_y/8)),font,1,(2,2,2),2)
    cv2.putText(img,"Backspace",(int(7*scrn_x/8),int(7*scrn_y/8)),font,1,(2,2,2),2)

    cv2.putText(img,strig,(int(scrn_x/8),int(scrn_y/8)),font,1,(2,2,2),2)

    cv2.setMouseCallback('pic',clikz)

    cv2.imshow("pic",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # When everything done, release the capture
cv2.destroyAllWindows()

##cv2.waitKey(0)
##cv2.namedWindow("pic");


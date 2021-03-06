import numpy as np
import pyautogui as pag
import cv2
import time


def gal():

	def clikz(event,x,y,flags,param):
	    
	    if event == cv2.EVENT_LBUTTONDOWN:
	   
		    if ( x > 0*int(scrn_x/4) and x < 1*int(scrn_x/4) and  y > 2*int(scrn_y/4) and y < 3*int(scrn_y/4)) :
		        print("Before");
		    elif ( x > 3*int(scrn_x/4) and x < 4*int(scrn_x/4) and  y > 2*int(scrn_y/4) and y < 3*int(scrn_y/4)) :
		        print("After");
		    else:
		        pass
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
	    cv2.rectangle(img,(int(scrn_x-1915),int(scrn_y-265)),(int(scrn_x-5),int(scrn_y-5)),(0,0,255),2) #rect 4'''

	    #vertical 
	    
	    cv2.rectangle(img,(int(scrn_x-1430),int(scrn_y-1075)),(int(scrn_x-465),int(scrn_y-5)),(0,0,255),2) #rect 2
	    
	    img1=cv2.imread("death-note-l.jpg")
	    img1_temp = cv2.resize(img1,(int(scrn_x-465),int(scrn_y-5)),interpolation = cv2.INTER_CUBIC)
	   


	    

	    
	    cv2.putText(img,"<",(int(scrn_x/16),int(7*scrn_y/16)),font,1,(2,2,2),2)
	    
	    cv2.putText(img,">",(int(9*scrn_x/16),int(7*scrn_y/16)),font,1,(2,2,2),2)
	   
	    
	    cv2.setMouseCallback('pic',clikz)

	    cv2.imshow("pic",img)
	    cv2.imshow('pic',img1_temp)

	    if cv2.waitKey(1) & 0xFF == ord('q'):
	    	break
	    # When everything done, release the capture
	cv2.destroyAllWindows()

	

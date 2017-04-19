from test_3 import open_cv
import cv2

a,x = open_cv()
cv2.namedWindow("test");
cv2.imshow("test",x);
cv2.waitKey(0)
cv2.destroyAllWindows()

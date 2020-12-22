import cv2
import numpy as np
v=[34,172,56,172,255,255]
mypoint=[] #cw,y

c=cv2.VideoCapture(0)
def findcolor(img):
  imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  newPoints=[]
  lower_v = np.array([v[0:3]])
  upper_v = np.array([v[3:6]])
  # create mask image by values
  mask = cv2.inRange(imghsv, lower_v, upper_v)
  cw,y=getContour(mask)
  if cw != 0 and y != 0:
    newPoints.append([cw, y])
  #make circle on dected image, if image is not dected ,there nothing have circle
  cv2.circle(imgContours, (cw, y), 15, (0,255,0), cv2.FILLED)
  return newPoints
def getContour(edge):
  contours, hierachy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  x,y,h,w=0,0,0,0
  for cnt in contours:
    # Draw all contours
    # -1 signifies drawing all contours
    cv2.drawContours(imgContours, cnt, -1, (0, 255, 0), 3)
    peri = cv2.arcLength(cnt, True)


    # it give approx points in particular shapes
    # 0.02*peri= (peri/100)*2
    approx_points = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    x, y, h, w = cv2.boundingRect(approx_points)
  return x+w//2,y
def drawpoint(myp):
  for p in myp:
    cv2.circle(imgContours,(p[0],p[1]),10,(0,255,0),cv2.FILLED)

while True:
  s, im = c.read()
  imgContours=im.copy()
  new=findcolor(im)
  if len(new) != 0:
    for newP in new:
      mypoint.append(newP)
  drawpoint(mypoint)
  cv2.imshow("video",imgContours)
  cv2.waitKey(1)
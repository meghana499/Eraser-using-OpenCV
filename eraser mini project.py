import cv2

drawing = False 
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)          

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False     

img=cv2.imread("book.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

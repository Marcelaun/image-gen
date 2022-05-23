import cv2

img = cv2.imread("assets/madara.jpg"); # import image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert image to gray color
img_invert = cv2.bitwise_not(img_gray) #gray scale to inversion of the image
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0) #smooting the inverted image


def dodgev2(x, y):
    return cv2.divide(x, 255-y, scale=256)

final_img = dodgev2(img_gray,img_smoothing)



cv2.imshow('img',img) # displaying the original image
cv2.imshow("Gray Image",img_gray)
cv2.imshow("Inverted Image",img_invert)
cv2.imshow("Smooth Image",img_smoothing)
cv2.imshow("Final Photo",final_img)

cv2.imwrite("madara.jpg",final_img)

cv2.waitKey(0) #waits until the pressing any key.
cv2.destroyAllWindows() # this function destroy all windows of images after clicking any button.
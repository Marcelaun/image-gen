import cv2

img = cv2.imread("assets/chapeu-branco.jpg"); # import image

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_img = cv2.bitwise_not(grey_img)
#invert_img=255-grey_img
blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
invblur_img = cv2.bitwise_not(blur_img)
#invblur_img=255-blur_img
sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)
cv2.imwrite('sketch.png', sketch_img)

cv2.imshow('sketch image', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
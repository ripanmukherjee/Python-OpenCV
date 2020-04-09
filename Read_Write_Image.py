#Reading the Image
import cv2

img_gray = cv2.imread('lena.jpg', 0)
img_color = cv2.imread('lena.jpg', 1)
img_unchange = cv2.imread('lena.jpg', -1)
print(img_gray)
print(img_color)
print(img_unchange)

cv2.imshow('Image', img_gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()

cv2.imshow('Image', img_color)
cv2.waitKey(1000)
cv2.destroyAllWindows()

cv2.imshow('Image', img_unchange)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#Write the image in directory
import cv2

img_gray = cv2.imread('lena.jpg', 0)

cv2.imshow('Image', img_gray)
#cv2.waitKey(0) or cv2.waitKey(1000) 0 or any number you can give, any other number signifies the milisecond,
# but 0 signifies that pic will wait for user to press the button
cv2.waitKey(1000)
cv2.destroyAllWindows()

cv2.imwrite('lena_copy.png', img_gray)


#Write the image in directory when user press keyboard
import cv2

img_gray = cv2.imread('lena.jpg', 0)

cv2.imshow('Image', img_gray)
#cv2.waitKey(0) or cv2.waitKey(1000) 0 or any number you can give, any other number signifies the milisecond,
# but 0 signifies that pic will wait for user to press the button
k = cv2.waitKey(0)
if k == 27: #27 is defined method why user press esc key in the key board
    cv2.destroyAllWindows()
elif k == ord('s'): #when the user press s button in keyboard
    cv2.imwrite('lena_copy.png', img_gray)
    cv2.destroyAllWindows()
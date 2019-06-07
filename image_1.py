import cv2
#here '1' is used to indicate that the image is colored, '0' indicates that the image is black and white
img=cv2.imread(r"C:\Users\wabale\PycharmProjects\untitled3\temp.jpg",1)
#a colored will have 3 channels n 1 channel for a black n white image
#to print dimensions
print(img)
#to print the pixels
print(img.shape)
#to return the type
print(type(img))
#to display the image
cv2.imshow("temp",img)
#so that the image is displayed till the time user does not click a key
cv2.waitKey()

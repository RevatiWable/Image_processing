import cv2
img=cv2.imread(r"C:\Users\wabale\PycharmProjects\untitled3\temp.jpg",1)
#to resize the image
#resized_image=cv2.resize(img,(200,200))
#to resize the image by half
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("temp",resized_image)
cv2.waitKey()
import cv2

image = cv2.imread("pic.jpg",cv2.IMREAD_UNCHANGED)
#cv2.imshow("TITLE", image)
scale_percent = 50
new_width = int(image.shape[1] * scale_percent/100)
new_height = int(image.shape[0] * scale_percent/100)

output = cv2.resize(image, (new_width,new_height))
cv2.imwrite("NewImage.png", output)
cv2.imshow("TITLE", output)

cv2.waitKey(0)
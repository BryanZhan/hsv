import cv2

img = cv2.imread("mp2a.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_h = img_hsv[:, :, 0]
img_s = img_hsv[:, :, 1]
img_v = img_hsv[:, :, 2]

equal_img_v = cv2.equalizeHist(img_v)
img_hsv[:, :, 2] = equal_img_v
img1 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("opencv", img1)
cv2.waitKey(0)
import os
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) #Chỉnh để chọn nguồn video, ví dụ: 0 cho camera

#thu thập data khuôn mặt của từng ng
face_id = input ("Nhập tên =>>")
age = input("Nhap tuoi ++>")
#level = input("Nhập cấp ")
print ("Đang khởi chạy camera, xin vui lòng đợi")

count =0 #chụp ảnh sau này còn lấy
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
# Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#hàm detectmulti
    faces = face_cascade.detectMultiScale(gray)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count +=1
#Ghi tạo file của khác hàng và chuyển màu xám
        cv2.imwrite(f"dataset/User."+str(face_id)+"."+str(count)+".jpg", gray[y:y + h, x:x + w])
        cv2.imshow("Khuôn mặt", frame)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
    if count >= 5:
        break
print("exit")
cap.release()
cv2.destroyAllWindows()




import os
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) #Chỉnh để chọn nguồn video, ví dụ: 0 cho camera

# Định dạng tên biến + mở file ghi tên ng dùng
face_count =0
if face_count == 0:
    if os.path.exists("List.py"):
        with open("List.py", "r") as file:
            for line in file:
                if line.startswith("name_"):
                    face_count += 1
print(face_count)
face_id = input("Nhập tên =>>")
print("Đang khởi chạy camera, xin vui lòng đợi")

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
        cv2.imwrite(f"dataset/User." + str(face_count)+"."+ str(face_id) + "." + str(count)+".jpg", gray[y:y + h, x:x + w])
        cv2.imshow("Khuôn mặt", frame)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
    if count >= 2:
        break

# gán biến tí lấy
variable_name = f"name_{face_count}"
with open("List.py","a") as file:
    file.write(f"{variable_name} = '{face_id}'\n")

print("exit")
cap.release()
cv2.destroyAllWindows()




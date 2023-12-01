import cv2
import numpy as np
from PIL import Image
import os

# Khai báo thư mục dataset

path = "dataset"

# Khởi tạo mô hình nhận diện khuôn mặt

recognizer = cv2.face.LBPHFaceRecognizer.create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Tạo hàm lấy ảnh và nhãn

def getImagesAndLabels(path):
    # nên tạo 1 folder
#    folder_name = name
#    subfolder_path = create_subfolder(parent_folder, folder_name)
    # Quet folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []

    # Check if there are any files in the directory
    if not imagePaths:
        print("[WARNING] No files found in dataset")
        return faces, ids

    # Lặp qua từng tệp ảnh trong dataset
    for imagePath in imagePaths:
        # Tách tên tệp và phần mở rộng
        filename, extension = os.path.splitext(os.path.basename(imagePath))

        # Lấy nhãn của khuôn mặt
        id = int(filename.split(".")[-1])

        # Chuyển đổi ảnh sang dạng grayscale và uint8
        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, "uint8")

        faces.append(img_numpy)
        ids.append(id)
    return faces, ids

# Huấn luyện mô hình
faces, ids = getImagesAndLabels(path)

recognizer.train(faces,np.array(ids))

recognizer.write("Trainer/Trainer.yml")
print("[INFO] Khuon mat duoc train: {}".format(len(np.unique(ids))))

cv2.destroyAllWindows()



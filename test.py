import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import Label, Button, Canvas
from PIL import Image, ImageTk
import threading
import List

window = tk.Tk()
window.title("Ứng dụng Nhận diện khuôn mặt")
window.geometry("800x600+200+100")  # width x height + right + down
window.attributes('-topmost', True)

cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer.create()
recognizer.read("Trainer/Trainer.yml")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
names = [getattr(List, attr) for attr in dir(List) if attr.startswith("name_")]

name_label = Label(window, text="Tên: ", bg="yellow")
name_label.pack()
confidence_label = Label(window, text="Độ chính xác: ")
confidence_label.pack()

canvas = Canvas(window, width=640, height=480)
canvas.pack()

def detect_face():
    def video_processing():
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                if confidence < 150:
                    name = names[id]
                    confidence = "        {0}%".format(round(confidence))
                else:
                    name = "Unknow"
                    confidence = "         0%"
                name_label.config(text="Tên: " + name)
                confidence_label.config(text="Độ chính xác: " + str(confidence) + "%")

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(image=img)
            canvas.create_image(0, 0, image=img, anchor=tk.NW)
            canvas.image = img
    video_thread = threading.Thread(target=video_processing)
    video_thread.daemon = True
    video_thread.start()

def stop_and_save():
    cap.release()
    cv2.destroyAllWindows()
    window.destroy()

start_button = Button(window, text="Nhận diện", command=detect_face)
start_button.pack()

end_button = Button(window, text="Kết thúc", command=stop_and_save)
end_button.pack()

window.mainloop()

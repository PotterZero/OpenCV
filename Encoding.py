import serial
import time
import os

# Thay đổi đường dẫn tới file hex của bạn
arduino_code_path = "C:\\Users\\Admin\\Documents\\Arduino\\Servo_simple\\Servo_simple.ino.arduino_avr.uno.hex"

# Kết nối với Arduino thông qua cổng COM, hãy thay đổi cổng COM tương ứng của bạn
ser = serial.Serial('COM3', 9600, timeout=1)

# Chờ Arduino khởi động
time.sleep(2)

# Kiểm tra xem file hex có tồn tại không
if os.path.exists(arduino_code_path):
    # Mở file hex và gửi dữ liệu xuống Arduino
    with open(arduino_code_path, 'rb') as f:
        hex_data = f.read()
        ser.write(hex_data)
    print("Open and success action !")
else:
    print(f"File not found: {arduino_code_path}")

# Đóng kết nối
ser.close()

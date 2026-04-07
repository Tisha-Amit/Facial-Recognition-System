import serial
import time
import cv2
import numpy as np

ser = serial.Serial('COM3', 115200, timeout=10)  # Update 'COM3' to your port (e.g., COM4)
while True:
    if ser.read() == b'\xff':  # Start marker
        size_data = ser.read(4)
        size = int.from_bytes(size_data, byteorder='little')
        frame_data = ser.read(size)
        if ser.read() == b'\xfe':  # End marker
            frame = np.frombuffer(frame_data, dtype=np.uint8)
            frame = frame.reshape((176, 240, 2))  # RGB565 is 2 bytes per pixel
            # Convert RGB565 to RGB888
            r = (frame[:, :, 0] & 0xF8) | (frame[:, :, 1] >> 5)
            g = ((frame[:, :, 1] & 0x1C) << 3) | ((frame[:, :, 0] & 0x07) << 5)
            b = frame[:, :, 1] & 0xF8
            rgb_frame = np.dstack((r, g, b)).astype(np.uint8)
            cv2.imshow('Frame', rgb_frame)
            cv2.waitKey(1)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            cv2.imwrite(f'raw_frame_{timestamp}.jpg', rgb_frame)
            print(f"Frame saved as raw_frame_{timestamp}.jpg")

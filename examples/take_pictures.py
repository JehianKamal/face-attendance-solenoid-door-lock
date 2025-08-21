import cv2
import os

# Folder untuk menyimpan foto wajah
folder_name = 'faces_data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

faceCascade = cv2.CascadeClassifier("../src/haarcascade_frontalface_default.xml")
total_images = 5
counter = 1
ids = 1  # ganti id jika lebih dari satu orang

# Gunakan webcam default
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Gagal mengambil gambar dari kamera")
        break

    frame_copy = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 3)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Tekan 'c' untuk capture foto
        if cv2.waitKey(1) & 0xff == ord('c'):
            roi_face = frame_copy[y:y+h, x:x+w]
            cv2.imwrite(f'{folder_name}/people.{ids}.{counter}.jpg', roi_face)

            counter += 1
            if counter > total_images:
                print(f'[INFO] {total_images} IMAGE CAPTURE SUCCESSFULL!!')

    cv2.imshow('Capture Image', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

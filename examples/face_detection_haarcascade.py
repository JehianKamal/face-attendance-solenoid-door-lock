# Copyright 2025 ariefsetyonugroho
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import numpy as np


def findFace(img):
    faceCascade = cv2.CascadeClassifier("../src/haarcascade_frontalface_default.xml")

    if img is None:
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 8)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak bisa dibuka")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("Gagal membaca frame dari kamera")
        break

    findFace(img)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


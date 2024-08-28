import base64
import numpy as np
import requests
import cv2 as cv

url = "http://127.0.0.1:5000/img"

response = requests.get(url)
corpo = response.json()
status = response.status_code
buffer = base64.b64decode(string64)
buffer = base64.b64decode(string64.replace("data:image/png;base64,", ""))
imgArray = np.frombuffer(buffer, np.int8)
img = cv.imdecode(imgArray, cv.IMREAD_UNCHANGED)

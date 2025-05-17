import cv2

def process_frame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect vehicles (simplified)
    cars = cv2.CascadeClassifier('cars.xml')
    detected = cars.detectMultiScale(gray, 1.1, 1)
    return detected

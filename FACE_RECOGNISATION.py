import cv2

# Load the pre-fed image for recognition
pre_fed_image_path = 'c:/Users/ANKIT KUMAR/OneDrive/Documents/TYAGI.jpg'
pre_fed_image = cv2.imread(pre_fed_image_path)
pre_fed_image_gray = cv2.cvtColor(pre_fed_image, cv2.COLOR_BGR2GRAY)

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the video stream
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        
        # Perform face recognition by comparing with the new pre-fed image
        # Implement your recognition logic here using techniques like feature matching or deep learning models
        
        # Display a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

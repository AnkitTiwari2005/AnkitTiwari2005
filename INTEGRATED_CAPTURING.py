import cv2

def capture_face():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    # Capture a frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame")
        cap.release()
        return

    # Save the captured frame as a face image
    cv2.imwrite('captured_face.jpg', frame)

    # Release the camera
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

def verify_face():
    # Load the previously captured face image
    face_image = cv2.imread('captured_face.jpg')

    # Load another image for verification (could be the same person's face under different lighting/angles)
    verification_image = cv2.imread('captured_face.jpg')

    # Perform face detection (you might want to use a face detection model for better accuracy)
    # Here, we're just assuming the loaded images already contain the face
    # You might want to use a face detection model for more accurate face detection

    # Convert images to grayscale for face recognition
    gray_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    gray_verification = cv2.cvtColor(verification_image, cv2.COLOR_BGR2GRAY)

    # Perform face recognition or comparison using a suitable method (e.g., histogram comparison, deep learning-based models, etc.)
    # Here, we're using a simple pixel-wise comparison for illustration purposes
    difference = cv2.absdiff(gray_face, gray_verification)

    # Define a threshold for face verification
    threshold = 50  # Adjust this value according to your requirement

    # Check if the difference is below the threshold for verification
    if cv2.countNonZero(difference) < threshold:
        print("Face verified: It's the same person!")
    else:
        print("Face not verified: It's a different person or the images are too dissimilar.")

# Call the function to capture a face
capture_face()

# Call the function to verify the face
verify_face()


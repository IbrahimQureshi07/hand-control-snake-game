import cv2

# Try to open the camera (0 is usually the default camera)
# If you have multiple cameras, try 1, 2, etc.
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("ERROR: Could not open camera!")
    print("\nTroubleshooting tips:")
    print("1. Make sure your camera is not being used by another program")
    print("2. Try changing 0 to 1 or 2 in VideoCapture(0)")
    print("3. Check if your camera drivers are installed")
    print("4. On Windows, check Privacy settings: Settings > Privacy > Camera")
    exit()

print("Camera opened successfully!")
print("Press 'q' to quit")

# Main loop to capture and display video
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Check if frame was read successfully
    if not ret:
        print("ERROR: Could not read frame from camera")
        break
    
    # Display the frame in a window
    cv2.imshow('Camera Test', frame)
    
    # Wait for 'q' key to quit (wait 1 millisecond)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

print("Camera test finished!")





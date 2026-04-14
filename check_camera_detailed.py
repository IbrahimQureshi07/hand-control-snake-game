import cv2
import sys

print("=" * 50)
print("Camera Diagnostic Tool")
print("=" * 50)
print()

# Check if OpenCV is installed
try:
    print(f"✓ OpenCV version: {cv2.VideoCapture.__module__}")
    print(f"✓ OpenCV installed successfully")
except Exception as e:
    print(f"✗ OpenCV not installed properly: {e}")
    sys.exit(1)

print()
print("Checking available cameras...")
print("-" * 50)

# Try to find which camera index works
working_camera = None
for i in range(5):  # Check cameras 0-4
    print(f"Trying camera index {i}...", end=" ")
    cap = cv2.VideoCapture(i)
    
    if cap.isOpened():
        # Try to read a frame to confirm it's working
        ret, frame = cap.read()
        if ret and frame is not None:
            print(f"✓ WORKING! Camera {i} is available")
            if working_camera is None:
                working_camera = i
            cap.release()
        else:
            print(f"✗ Opens but can't read frames")
            cap.release()
    else:
        print(f"✗ Not available")
    cap.release()

print()
print("=" * 50)

if working_camera is not None:
    print(f"SUCCESS! Found working camera at index {working_camera}")
    print()
    print("Opening camera window...")
    print("Press 'q' to quit")
    print()
    
    # Open the working camera
    cap = cv2.VideoCapture(working_camera)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('Camera Test - Press Q to Quit', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed successfully!")
else:
    print("ERROR: No working camera found!")
    print()
    print("Troubleshooting Steps:")
    print("1. Check Windows Privacy Settings:")
    print("   - Press Win + I (Settings)")
    print("   - Go to Privacy & Security > Camera")
    print("   - Turn ON 'Camera access'")
    print("   - Turn ON 'Let desktop apps access your camera' (IMPORTANT!)")
    print()
    print("2. Check Device Manager:")
    print("   - Press Win + X")
    print("   - Select 'Device Manager'")
    print("   - Look under 'Cameras' or 'Imaging devices'")
    print("   - If you see yellow warning, right-click > Update driver")
    print()
    print("3. Restart your computer")
    print()
    print("4. Check if camera works in Windows Camera app:")
    print("   - Press Win key, type 'Camera', open it")
    print("   - If it doesn't work there, it's a driver/hardware issue")





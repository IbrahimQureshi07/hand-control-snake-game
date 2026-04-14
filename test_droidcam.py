"""
Quick test script to verify DroidCam is working
Run this before running the main game
"""

import cv2

print("=" * 50)
print("Testing DroidCam Connection...")
print("=" * 50)
print()

# Try to open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ ERROR: Could not open camera!")
    print()
    print("Troubleshooting:")
    print("1. Make sure DroidCam is running on your phone")
    print("2. Make sure DroidCam client is connected on laptop")
    print("3. Try closing other apps that might be using camera")
    print("4. Check if camera index is correct (try 1 or 2 instead of 0)")
    exit()

print("✅ Camera opened successfully!")
print()

# Try to read a frame
ret, frame = cap.read()

if not ret:
    print("❌ ERROR: Could not read frame from camera!")
    cap.release()
    exit()

print("✅ Frame captured successfully!")
print(f"   Frame size: {frame.shape[1]}x{frame.shape[0]}")
print()
print("✅ DroidCam is working perfectly!")
print()
print("You can now run: python snake_game_tkinter.py")
print("=" * 50)

# Show camera feed for 3 seconds
print("Showing camera feed for 3 seconds...")
print("Press any key to close")

import time
start_time = time.time()
while time.time() - start_time < 3:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('DroidCam Test - Press any key to close', frame)
        if cv2.waitKey(1) & 0xFF != 255:  # Any key pressed
            break

cap.release()
cv2.destroyAllWindows()

print("Test complete!")





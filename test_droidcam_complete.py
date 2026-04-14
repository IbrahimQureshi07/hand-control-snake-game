"""Complete DroidCam connection test"""
import cv2
import sys

print("=" * 60)
print("DroidCam Complete Connection Test")
print("=" * 60)

# Test 1: Check if any camera is available
print("\n[TEST 1] Checking available cameras...")
cameras_found = []
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret and frame is not None:
            print(f"  Camera {i}: WORKING (Size: {frame.shape})")
            cameras_found.append(i)
        cap.release()
    else:
        cap.release()

if cameras_found:
    print(f"\n[RESULT] Found {len(cameras_found)} working camera(s) at index: {cameras_found}")
    print("  If DroidCam Virtual Camera is enabled, it should be in this list!")
else:
    print("\n[RESULT] NO CAMERAS FOUND!")
    print("  This means:")
    print("  1. DroidCam Virtual Camera is NOT enabled")
    print("  2. OR DroidCam client is NOT connected")
    print("  3. OR No camera is available on this system")

# Test 2: Check DroidCam HTTP (if available)
print("\n[TEST 2] Checking DroidCam HTTP streaming...")
try:
    import urllib.request
    DROIDCAM_IP = "192.168.0.106"
    DROIDCAM_PORT = "4747"
    url = f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/video"
    
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    with urllib.request.urlopen(req, timeout=2) as response:
        data = response.read(1000)
        if b'<html' in data.lower() or b'<!doctype' in data.lower():
            print(f"  HTTP Status: {response.getcode()}")
            print("  [RESULT] HTTP returns HTML page (not video stream)")
            print("  This means DroidCam free version doesn't support HTTP streaming")
        elif b'\xff\xd8\xff' in data:
            print("  [RESULT] HTTP returns video stream!")
        else:
            print(f"  [RESULT] Unknown format: {data[:50]}")
except Exception as e:
    print(f"  [RESULT] HTTP connection failed: {e}")

# Final recommendations
print("\n" + "=" * 60)
print("RECOMMENDATIONS:")
print("=" * 60)

if cameras_found:
    print("\n[GOOD NEWS] Camera(s) found!")
    print(f"  Use camera index {cameras_found[0]} in the game")
    print("  The game should automatically detect it.")
else:
    print("\n[ACTION REQUIRED] Enable DroidCam Virtual Camera:")
    print("  1. Open DroidCam client on laptop")
    print("  2. Make sure phone is connected (WiFi or USB)")
    print("  3. Click 'Start' in DroidCam client")
    print("  4. Go to Settings > Virtual Camera > Enable")
    print("  5. Restart DroidCam client")
    print("  6. Run this test again to verify")

print("\n" + "=" * 60)





"""Quick test script to check DroidCam connection"""
import cv2
import time

DROIDCAM_IP = "192.168.0.106"
DROIDCAM_PORT = "4747"

# Try different URL formats
urls = [
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/video",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/mjpegfeed?640x480",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/videofeed",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/",
]

print("Testing DroidCam connection...")
print(f"IP: {DROIDCAM_IP}:{DROIDCAM_PORT}")
print("=" * 50)

for url in urls:
    print(f"\nTrying: {url}")
    cap = cv2.VideoCapture(url)
    
    if cap.isOpened():
        print("✅ Opened! Reading frame...")
        start = time.time()
        ret, frame = cap.read()
        
        if ret and frame is not None:
            print(f"✅ SUCCESS! Frame received: {frame.shape}")
            print(f"✅ Working URL: {url}")
            print("\nShowing frame for 3 seconds...")
            
            for i in range(30):  # 3 seconds at 10fps
                ret, frame = cap.read()
                if ret:
                    cv2.imshow('DroidCam Test', frame)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
            
            cap.release()
            cv2.destroyAllWindows()
            print("\n✅ DroidCam is working! Use this URL in game code.")
            exit(0)
        else:
            print("⚠️ Opened but no frame")
            cap.release()
    else:
        print("❌ Could not open")

print("\n❌ None of the URLs worked!")
print("\nCheck:")
print("1. DroidCam app running on phone?")
print("2. DroidCam client connected on laptop?")
print("3. Both on same WiFi?")
print("4. IP address correct?")





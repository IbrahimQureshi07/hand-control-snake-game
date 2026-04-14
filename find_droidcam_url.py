"""Find the correct DroidCam video URL"""
import urllib.request
import socket

DROIDCAM_IP = "192.168.0.106"
DROIDCAM_PORT = "4747"

# Common DroidCam URLs
urls = [
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/video",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/mjpegfeed",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/mjpegfeed?640x480",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/videofeed",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/cam_1.mjpg",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/cam_1.mjpeg",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/stream",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/",
]

print("=" * 60)
print("Finding Correct DroidCam Video URL")
print("=" * 60)

for url in urls:
    print(f"\nTesting: {url}")
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=3) as response:
            status = response.getcode()
            content_type = response.headers.get('Content-Type', 'Unknown')
            data = response.read(1000)  # Read first 1000 bytes
            
            print(f"  Status: {status}")
            print(f"  Content-Type: {content_type}")
            print(f"  Data length: {len(data)} bytes")
            
            # Check if it's video stream
            if b'\xff\xd8\xff' in data:  # JPEG start
                print(f"  [SUCCESS] Contains JPEG data! This is likely the video stream!")
                print(f"  Use this URL: {url}")
                break
            elif b'<html' in data.lower() or b'<!doctype' in data.lower():
                print(f"  [HTML] This is an HTML page, not video stream")
            elif 'mjpeg' in content_type.lower() or 'video' in content_type.lower():
                print(f"  [POSSIBLE] Content-Type suggests video: {content_type}")
            else:
                print(f"  [UNKNOWN] First 50 bytes: {repr(data[:50])}")
                
    except Exception as e:
        print(f"  [ERROR] {e}")

print("\n" + "=" * 60)
print("If no URL found, check DroidCam app settings")
print("=" * 60)





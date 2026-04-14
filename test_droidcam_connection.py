"""Quick test to check if DroidCam server is running"""
import urllib.request
import urllib.error
import socket

DROIDCAM_IP = "192.168.0.106"
DROIDCAM_PORT = "4747"

urls = [
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/video",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/mjpegfeed?640x480",
    f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/",
]

print("=" * 50)
print("Testing DroidCam Server Connection...")
print(f"IP: {DROIDCAM_IP}:{DROIDCAM_PORT}")
print("=" * 50)
print()

# First test if port is open
print("Step 1: Testing if port is open...")
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((DROIDCAM_IP, int(DROIDCAM_PORT)))
    sock.close()
    if result == 0:
        print(f"  ✅ Port {DROIDCAM_PORT} is OPEN")
    else:
        print(f"  ❌ Port {DROIDCAM_PORT} is CLOSED")
        print("  → DroidCam server not running or not reachable")
except Exception as e:
    print(f"  ❌ Error: {e}")
print()

# Test URLs
print("Step 2: Testing URLs...")
for url in urls:
    print(f"Testing: {url}")
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=3) as response:
            status = response.getcode()
            print(f"  Status Code: {status}")
            if status == 200:
                print(f"  ✅ SUCCESS! Server is responding!")
                print(f"  ✅ Use this URL in game: {url}")
                break
    except urllib.error.URLError as e:
        print(f"  ❌ Connection Error: {e}")
    except socket.timeout:
        print(f"  ❌ Timeout - Server not responding")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    print()

print("=" * 50)
print("If all failed:")
print("1. Check DroidCam app is running on phone")
print("2. Check DroidCam client is connected on laptop")
print("3. Check both devices on same WiFi")
print("4. Try browser: http://192.168.0.106:4747/video")
print("=" * 50)


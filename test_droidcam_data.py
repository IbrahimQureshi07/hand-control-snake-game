"""Test what DroidCam actually returns"""
import urllib.request
import numpy as np
import cv2

DROIDCAM_IP = "192.168.0.106"
DROIDCAM_PORT = "4747"
url = f"http://{DROIDCAM_IP}:{DROIDCAM_PORT}/video"

print("=" * 60)
print("Testing DroidCam Data Format")
print("=" * 60)

try:
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    with urllib.request.urlopen(req, timeout=5) as response:
        print(f"Status: {response.getcode()}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
        print()
        
        # Read first chunk
        data = response.read(100000)
        print(f"Data length: {len(data)} bytes")
        print(f"First 100 bytes (hex): {data[:100].hex()}")
        print(f"First 100 bytes (repr): {repr(data[:100])}")
        print()
        
        # Check for JPEG markers
        jpeg_start = data.find(b'\xff\xd8\xff')
        print(f"JPEG start marker (FF D8 FF) at: {jpeg_start}")
        
        if jpeg_start != -1:
            jpeg_end = data.find(b'\xff\xd9', jpeg_start)
            print(f"JPEG end marker (FF D9) at: {jpeg_end}")
            
            if jpeg_end != -1:
                jpeg_data = data[jpeg_start:jpeg_end + 2]
                print(f"JPEG data size: {len(jpeg_data)} bytes")
                
                # Try to decode
                nparr = np.frombuffer(jpeg_data, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                if frame is not None:
                    print(f"SUCCESS! Frame decoded: {frame.shape}")
                else:
                    print("FAILED: Could not decode JPEG")
                    # Save raw data for inspection
                    with open('droidcam_raw.jpg', 'wb') as f:
                        f.write(jpeg_data)
                    print("Saved raw JPEG data to 'droidcam_raw.jpg'")
            else:
                print("ERROR: JPEG end marker not found")
        else:
            print("ERROR: JPEG start marker not found")
            print("This might be HTML or other format")
            
            # Check if it's HTML
            if data.startswith(b'<'):
                print("Data appears to be HTML")
                print(f"First 500 chars: {data[:500].decode('utf-8', errors='ignore')}")
            
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

print("=" * 60)





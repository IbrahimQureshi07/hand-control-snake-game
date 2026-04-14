# 📱 DroidCam IP Setup Guide

## Problem:
OpenCV camera indices se DroidCam detect nahi ho raha.

## Solution: DroidCam IP Address Use Karo

### Step 1: DroidCam IP Address Find Karo

1. **DroidCam Client** kholo
2. **IP Address** note karo (usually top par dikhta hai)
   - Example: `192.168.1.100`
   - Ya `192.168.0.105`

### Step 2: Code Mein IP Set Karo

`snake_game_tkinter.py` file kholo aur **Line ~160** par jao:

**Find this code:**
```python
# First, try DroidCam IP if available
# Uncomment and set your DroidCam IP address if using WiFi:
# DROIDCAM_IP = "192.168.1.XXX"  # Replace with your DroidCam IP
```

**Change to:**
```python
# First, try DroidCam IP if available
DROIDCAM_IP = "192.168.1.100"  # ← Yahan apna IP dalo (DroidCam client se)
droidcam_url = f"http://{DROIDCAM_IP}:4747/video"
print(f"Trying DroidCam IP: {droidcam_url}")
test_cap = cv2.VideoCapture(droidcam_url)
if test_cap.isOpened():
    ret, frame = test_cap.read()
    if ret and frame is not None:
        print(f"✅ DroidCam found via IP!")
        self.cap = test_cap
        # Continue to MediaPipe initialization below
```

**Aur neeche wale lines uncomment karo:**
```python
# Uncomment these lines (remove #):
        if test_cap.isOpened():
            ret, frame = test_cap.read()
            if ret and frame is not None:
                print(f"✅ DroidCam found via IP!")
                self.cap = test_cap
                # Skip to MediaPipe initialization
```

---

## Quick Fix:

1. DroidCam client se IP address note karo
2. `snake_game_tkinter.py` mein line ~160 par IP set karo
3. Uncomment the DroidCam IP code section
4. Game run karo

---

## Example:

**DroidCam Client Shows:** `192.168.1.100`

**Code Mein:**
```python
DROIDCAM_IP = "192.168.1.100"  # Your IP
droidcam_url = f"http://{DROIDCAM_IP}:4747/video"
```

---

## Alternative: Virtual Camera Enable Karo

Agar IP method kaam nahi kare:

1. DroidCam client kholo
2. Settings > Virtual Camera > **Enable**
3. Restart DroidCam client
4. Game run karo

---

**IP address mil gaya? Code update kar doon?**





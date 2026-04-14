# Camera Test Script

A simple Python script to test if your laptop camera is working using OpenCV.

## How to Use

1. **Install OpenCV** (if you haven't already):
   ```
   pip install opencv-python
   ```

2. **Run the script**:
   ```
   python test_camera.py
   ```

3. **Press 'q' to quit** the camera window

## What the Script Does

- Opens your default camera (usually camera 0)
- Shows a live video feed in a window
- Allows you to quit by pressing 'q'

## Troubleshooting: Camera Won't Open

### Problem 1: "Could not open camera" error

**Solution 1: Check if camera is being used**
- Close other programs that might be using the camera (Zoom, Teams, Skype, etc.)
- Close any browser tabs that might be accessing the camera

**Solution 2: Try a different camera index**
- If you have multiple cameras, edit the script and change `VideoCapture(0)` to `VideoCapture(1)` or `VideoCapture(2)`

**Solution 3: Windows Privacy Settings**
- Go to: Settings > Privacy > Camera
- Make sure "Allow apps to access your camera" is ON
- Make sure "Allow desktop apps to access your camera" is ON (important!)

**Solution 4: Check camera drivers**
- Open Device Manager (search in Start menu)
- Look under "Cameras" or "Imaging devices"
- If you see a yellow warning icon, update the drivers

**Solution 5: Restart your computer**
- Sometimes a simple restart fixes camera issues

### Problem 2: Black screen or no video

**Solution:**
- Make sure nothing is covering your camera lens
- Check if the camera LED light is on (if your laptop has one)
- Try the script again after closing other programs

### Problem 3: "ModuleNotFoundError: No module named 'cv2'"

**Solution:**
- Install OpenCV: `pip install opencv-python`
- If that doesn't work, try: `pip3 install opencv-python`

## Understanding the Code (For Beginners)

- `cv2.VideoCapture(0)` - Opens camera number 0 (your default camera)
- `cap.read()` - Takes a photo (frame) from the camera
- `cv2.imshow()` - Shows the photo in a window
- `cv2.waitKey(1)` - Waits for keyboard input (checks if 'q' was pressed)
- `cap.release()` - Closes the camera so other programs can use it





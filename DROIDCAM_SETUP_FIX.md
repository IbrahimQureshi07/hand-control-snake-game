# DroidCam Setup Fix

## Problem
DroidCam `/video` endpoint HTML return kar raha hai, video stream nahi. Yeh isliye kyunki DroidCam free version HTTP streaming support nahi karta.

## Solution: Use DroidCam Virtual Camera

### Step 1: Enable Virtual Camera in DroidCam Client
1. DroidCam client open karo (laptop pe)
2. Settings > Virtual Camera > Enable
3. Ya Settings > Advanced > Virtual Camera > Enable
4. DroidCam client ko restart karo

### Step 2: Check Virtual Camera
1. Windows Camera app open karo
2. Camera list mein "DroidCam" ya "DroidCam Source" dikhna chahiye
3. Agar dikhe to Virtual Camera enable hai

### Step 3: Run Game
```bash
python snake_game_tkinter.py
```

Game automatically Virtual Camera ko detect kar lega (camera index 0, 1, 2, etc.)

## Alternative: Use DroidCam Pro
DroidCam Pro version HTTP streaming support karta hai, lekin free version mein Virtual Camera hi best option hai.

## Troubleshooting
- Agar Virtual Camera enable nahi ho raha: DroidCam client update karo
- Agar camera detect nahi ho raha: DroidCam client restart karo
- Agar still nahi chal raha: DroidCam client > Settings > Reset





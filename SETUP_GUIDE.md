# 🚀 Setup Guide - Friend Ke Laptop Par Install Karne Ke Liye

## ✅ Good News!
**Sab kuch ready hai!** Bas yeh steps follow karo:

---

## 📦 Step 1: Libraries Install Karo

### Option A: Ek Command Se Sab Install (Recommended)
```bash
pip install -r requirements.txt
```

Yeh command automatically install kar dega:
- `opencv-python` (camera access ke liye)
- `mediapipe` (hand detection ke liye)

### Option B: Alag Alag Install Karo
```bash
pip install opencv-python
pip install mediapipe
```

---

## 🎮 Step 2: Game Run Karo

### Keyboard Mode (Testing Ke Liye):
```bash
python snake_game_tkinter.py
```

### Hand Control Mode:
1. `snake_game_tkinter.py` file kholo
2. Line 11 par jao
3. Change karo:
   ```python
   CONTROL_MODE = 'hand'  # 'keyboard' se 'hand' kar do
   ```
4. Save karo
5. Run karo:
   ```bash
   python snake_game_tkinter.py
   ```

---

## 🎯 Hand Control Gestures

Game start hone ke baad:
- **Hand up karo** = Snake UP jayega
- **Hand down karo** = Snake DOWN jayega
- **Hand left karo** = Snake LEFT jayega
- **Hand right karo** = Snake RIGHT jayega

**Tip:** Index finger ko wrist se alag direction mein move karo.

---

## ❓ Troubleshooting

### Problem 1: "OpenCV or MediaPipe not installed"
**Solution:**
```bash
pip install opencv-python mediapipe
```

### Problem 2: "Could not open camera"
**Solution:**
- Check karo camera kisi aur app mein use to nahi ho raha
- Windows Settings > Privacy > Camera > "Allow desktop apps" ON karo
- Camera driver check karo

### Problem 3: Hand detection kaam nahi kar raha
**Solution:**
- Camera ke saamne khade ho jao
- Hand clearly dikhni chahiye
- Lighting achhi honi chahiye
- Index finger ko clearly move karo

---

## 📋 Quick Checklist

- [ ] `pip install -r requirements.txt` run kiya
- [ ] Camera working hai (test kiya)
- [ ] `CONTROL_MODE = 'hand'` kar diya
- [ ] Game run kiya
- [ ] Hand gestures test kiye

---

## 🎉 Done!

Agar sab kuch install ho gaya aur game run ho raha hai, to hand control kaam karega!

**Koi problem? Batao!**





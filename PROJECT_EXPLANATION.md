# Snake Game Project - Complete Explanation

## 🎮 Game Features (Yeh Sab Hai!)

✅ **Snake Movement**: Arrow keys se snake move hota hai  
✅ **Food (Red Balls)**: Random jagah par red food appear hota hai  
✅ **Eating**: Snake food ko khaata hai  
✅ **Growth**: Food khane ke baad snake lamba hota hai  
✅ **New Food**: Har baar food khaane ke baad naya food alag jagah par aata hai  
✅ **Score**: Har food par 10 points milte hain  
✅ **Game Over**: Snake apne aap se takraaye to game over  
✅ **Restart**: 'R' key press karke restart kar sakte ho  

---

## 📦 Installation - Kya Install Karna Hai Aur Kyun?

### Package 1: pygame
**Command:**
```bash
pip install pygame
```

**Kyun chahiye?**
- pygame ek Python library hai jo games banane ke liye use hoti hai
- Isse hum window bana sakte hain, graphics draw kar sakte hain
- Keyboard input handle kar sakte hain
- Game loop (update, render) manage kar sakte hain

**Kya karta hai?**
- Game window banata hai
- Snake aur food ko screen par dikhata hai
- Arrow keys ko detect karta hai
- Game ko smooth chalata hai

---

## 🎯 Control Mode Kaise Change Karein?

### Location: `snake_game.py` file mein

**Line 8 par jao:**
```python
CONTROL_MODE = 'keyboard'  # YAHAN CHANGE KARO
```

### Options:

1. **Arrow Keys ke liye:**
   ```python
   CONTROL_MODE = 'keyboard'
   ```

2. **Hand Control ke liye (baad mein):**
   ```python
   CONTROL_MODE = 'hand'
   ```

**Exact Steps:**
1. `snake_game.py` file kholo
2. Line 8 par jao
3. `'keyboard'` ko `'hand'` kar do (ya vice versa)
4. File save karo

---

## 🚀 Kaise Run Karein?

### Step 1: Terminal/Command Prompt Kholo
- `Win + R` press karo
- `cmd` type karo, Enter

### Step 2: Project Folder Mein Jao
```bash
cd "C:\Users\User\Desktop\hand snake game task"
```

### Step 3: pygame Install Karo (Pehli Baar)
```bash
pip install pygame
```

### Step 4: Game Run Karo
```bash
python snake_game.py
```

---

## 🎮 Game Controls

- **↑ (Up Arrow)**: Snake up jayega
- **↓ (Down Arrow)**: Snake down jayega
- **← (Left Arrow)**: Snake left jayega
- **→ (Right Arrow)**: Snake right jayega
- **R Key**: Game over ke baad restart karne ke liye
- **Close Window**: Game band karne ke liye

---

## 📁 Files Ka Structure

```
hand snake game task/
├── snake_game.py          ← Main game file (YAHAN SE RUN KARO)
├── test_camera.py         ← Camera test ke liye (abhi use nahi)
├── check_camera_detailed.py ← Camera diagnostic (abhi use nahi)
├── PROJECT_EXPLANATION.md ← Yeh file (explanation)
└── README.md              ← Camera troubleshooting
```

---

## 🔧 Agar Installation Mein Problem Aaye

### Problem: `pip` command nahi chalta
**Solution:**
```bash
python -m pip install pygame
```

### Problem: Permission error
**Solution:**
```bash
pip install --user pygame
```

### Problem: Python nahi mil raha
**Solution:**
- Python install karo: https://www.python.org/downloads/
- Installation ke time "Add Python to PATH" check karo

---

## 🎯 Baad Mein Hand Control Add Karne Ke Liye

Jab aapke dost ke laptop par camera kaam karega:

1. `snake_game.py` mein `CONTROL_MODE = 'hand'` kar do
2. MediaPipe install karo: `pip install mediapipe`
3. Hand detection code add karo (main baad mein bata dunga)

---

## ✅ Summary - Aaj Ke Liye

1. ✅ Game ready hai - arrow keys se khel sakte ho
2. ✅ Food (red balls) random jagah par aata hai
3. ✅ Snake food ko khaata hai aur lamba hota hai
4. ✅ Score system hai
5. ✅ Game over aur restart feature hai

**Abhi ke liye:**
- `pip install pygame` run karo
- `python snake_game.py` run karo
- Arrow keys se khelo!

**Baad mein:**
- Camera fix hone par hand control add kar denge

---

## ❓ Questions?

Agar koi problem aaye to batao!





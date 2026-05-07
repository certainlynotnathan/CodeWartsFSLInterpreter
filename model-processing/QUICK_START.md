# 🚀 Quick Start - Test Your Model

## Ready to test? Follow these 3 steps:

### 1️⃣ Install Dependencies (if needed)
```bash
pip install mediapipe==0.9.1.0 opencv-python tensorflow scikit-learn numpy matplotlib
```

### 2️⃣ Navigate to model-processing folder
```bash
cd model-processing
```

### 3️⃣ Run the webcam test
```bash
python test_live.py
```

**Press Q to quit**

---

## 🎥 What to Expect

- Your webcam will open
- MediaPipe will draw landmarks on your hands and body
- Top 5 predictions will show on the left with confidence scores
- Detected signs will appear at the top as a sentence

---

## ⚡ Your Model Info

- **Model**: fsl_105_model.h5
- **Actions**: 105 Filipino Sign Language gestures
- **Input**: 30 frames of MediaPipe landmarks (258 values per frame)
- **Output**: Predicted sign with confidence score

---

## 💡 Tips for Best Results

1. **Good lighting** - Make sure your face and hands are well-lit
2. **Clear background** - Helps MediaPipe detect landmarks better
3. **Full visibility** - Keep hands in frame
4. **Normal speed** - Perform signs at natural speed
5. **Wait for detection** - Model predicts every 30 frames (~1 second)

---

## 🐛 Quick Troubleshooting

**Webcam won't open?**
- Close other apps using the camera
- Try changing camera index in test_live.py line 108: `cap = cv2.VideoCapture(1)`

**Module not found?**
- Run: `pip install -r ../requirements.txt`

**Low accuracy?**
- Ensure you're performing signs from your training set
- Check lighting and hand visibility

---

**Ready? Run `python test_live.py` now! 🎉**

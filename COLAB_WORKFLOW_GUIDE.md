# 🎯 COMPLETE COLAB WORKFLOW GUIDE

## 📁 DIRECTORY STRUCTURE

This guide shows you exactly where to put your data and what each notebook produces.

---

## 🗂️ FOLDER STRUCTURE OVERVIEW

```
/content/  (Your Colab workspace root)
│
├── 📂 videos/                          ← YOU CREATE THIS - Upload your raw videos here
│   ├── 📂 hello/
│   │   ├── 0.mp4
│   │   ├── 1.mp4
│   │   ├── 2.mp4
│   │   └── ... (20-30 videos recommended)
│   │
│   ├── 📂 thank_you/
│   │   ├── 0.mp4
│   │   ├── 1.mp4
│   │   └── ...
│   │
│   ├── 📂 please/
│   │   └── ...
│   │
│   └── 📂 [your_other_signs]/
│       └── ...
│
├── 📂 videos_30frames/                 ← CREATED BY video_preprocess.ipynb
│   ├── 📂 hello/
│   │   ├── 0.mp4  (exactly 30 frames)
│   │   ├── 1.mp4  (exactly 30 frames)
│   │   └── ...
│   │
│   ├── 📂 thank_you/
│   │   └── ...
│   │
│   └── 📂 [your_other_signs]/
│       └── ...
│
├── 📂 MP_Data/                         ← CREATED BY video_landmark_extraction.ipynb
│   ├── 📂 hello/
│   │   ├── 📂 0/                       (video 0)
│   │   │   ├── 0.npy                   (frame 0 landmarks - 258 values)
│   │   │   ├── 1.npy                   (frame 1 landmarks)
│   │   │   ├── 2.npy
│   │   │   └── ... (30 .npy files total)
│   │   │
│   │   ├── 📂 1/                       (video 1)
│   │   │   ├── 0.npy
│   │   │   └── ... (30 .npy files)
│   │   │
│   │   └── 📂 [0 to N]/                (N = number of videos)
│   │
│   ├── 📂 thank_you/
│   │   ├── 📂 0/
│   │   └── ...
│   │
│   └── 📂 [your_other_signs]/
│       └── ...
│
└── 📄 my_fsl_model.h5                  ← CREATED BY train_model.py (your trained model!)

```

---

## 🔄 DATA FLOW BETWEEN NOTEBOOKS

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: YOU UPLOAD YOUR VIDEOS                                 │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  📂 videos/                                                      │
│     ├── hello/ (20 videos)                                       │
│     ├── thank_you/ (20 videos)                                   │
│     └── please/ (20 videos)                                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: RUN video_preprocess.ipynb                             │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  INPUT:  videos/                                                 │
│  OUTPUT: videos_30frames/                                        │
│  ACTION: Normalizes all videos to exactly 30 frames             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: RUN video_landmark_extraction.ipynb                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  INPUT:  videos_30frames/                                        │
│  OUTPUT: MP_Data/                                                │
│  ACTION: Extracts MediaPipe landmarks (258 values per frame)    │
│          Saves as .npy files                                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 4: RUN train_model.py                                     │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  INPUT:  MP_Data/                                                │
│  OUTPUT: my_fsl_model.h5                                         │
│  ACTION: Trains LSTM model on landmarks                         │
│          Saves trained model                                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 5: DOWNLOAD YOUR MODEL                                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  files.download('my_fsl_model.h5')                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 EXAMPLE: 3 Signs with 20 Videos Each

### Initial Setup (What YOU create):

```
videos/
├── hello/
│   ├── 0.mp4, 1.mp4, 2.mp4, ..., 19.mp4  (20 videos)
├── thank_you/
│   ├── 0.mp4, 1.mp4, 2.mp4, ..., 19.mp4  (20 videos)
└── please/
    ├── 0.mp4, 1.mp4, 2.mp4, ..., 19.mp4  (20 videos)

Total: 60 videos
```

### After video_preprocess.ipynb:

```
videos_30frames/
├── hello/
│   ├── 0.mp4, 1.mp4, ..., 19.mp4  (each exactly 30 frames)
├── thank_you/
│   ├── 0.mp4, 1.mp4, ..., 19.mp4  (each exactly 30 frames)
└── please/
    ├── 0.mp4, 1.mp4, ..., 19.mp4  (each exactly 30 frames)

Total: 60 videos (normalized)
```

### After video_landmark_extraction.ipynb:

```
MP_Data/
├── hello/
│   ├── 0/  (0.npy, 1.npy, ..., 29.npy)  ← 30 landmark files
│   ├── 1/  (0.npy, 1.npy, ..., 29.npy)
│   ├── ...
│   └── 19/ (0.npy, 1.npy, ..., 29.npy)
│
├── thank_you/
│   ├── 0/ to 19/  (each with 30 .npy files)
│
└── please/
    ├── 0/ to 19/  (each with 30 .npy files)

Total: 60 folders × 30 files = 1,800 .npy files
Each .npy file contains 258 landmark values
```

### After train_model.py:

```
my_fsl_model.h5  ← Your trained model (ready to use!)
```

---

## 🎬 STEP-BY-STEP COLAB SETUP

### Cell 1: Install Dependencies
```python
!pip install mediapipe==0.9.1.0 opencv-python tensorflow scikit-learn matplotlib
```

### Cell 2: Mount Google Drive (Optional but Recommended)
```python
from google.colab import drive
drive.mount('/content/drive')
```

### Cell 3: Create Initial Directory and Upload Videos
```python
import os

# Create videos directory
os.makedirs('videos', exist_ok=True)

# Option A: Upload from local computer
from google.colab import files
uploaded = files.upload()

# Option B: Copy from Google Drive
# !cp -r /content/drive/MyDrive/my_sign_videos/* /content/videos/

# Verify structure
!ls -R videos/
```

### Cell 4: Configure Your Dataset
```python
# Define your signs
actions = ['hello', 'thank_you', 'please']  # ← CHANGE THIS

# Number of videos per sign
no_sequences = 20  # ← CHANGE THIS to match your videos

# Frames per video (always 30)
sequence_length = 30
```

### Cell 5: Run video_preprocess.ipynb
```python
# Paste the preprocessing code here
# It will read from 'videos/' and create 'videos_30frames/'
```

### Cell 6: Run video_landmark_extraction.ipynb
```python
# Paste the landmark extraction code here
# It will read from 'videos_30frames/' and create 'MP_Data/'
```

### Cell 7: Run train_model.py
```python
# Paste the training code here
# It will read from 'MP_Data/' and create 'my_fsl_model.h5'
```

### Cell 8: Download Your Model
```python
from google.colab import files
files.download('my_fsl_model.h5')
```

---

## 🔑 KEY VARIABLES TO CHANGE

In **ALL notebooks**, make sure these match:

```python
# Your sign language gestures
actions = np.array(['hello', 'thank_you', 'please', 'sorry', 'help'])

# Number of videos you have per sign
no_sequences = 20  # If you have 20 videos per sign

# Always 30 frames
sequence_length = 30
```

---

## ✅ CHECKLIST

- [ ] **Step 1**: Create `videos/` folder with subfolders for each sign
- [ ] **Step 2**: Upload 15-30 videos per sign (named 0.mp4, 1.mp4, etc.)
- [ ] **Step 3**: Update `actions` array with your sign names
- [ ] **Step 4**: Update `no_sequences` to match your video count
- [ ] **Step 5**: Run `video_preprocess.ipynb` → creates `videos_30frames/`
- [ ] **Step 6**: Run `video_landmark_extraction.ipynb` → creates `MP_Data/`
- [ ] **Step 7**: Run `train_model.py` → creates `my_fsl_model.h5`
- [ ] **Step 8**: Download your trained model!

---

## 🚨 COMMON MISTAKES TO AVOID

1. **Mismatched folder names**: Make sure folder names match your `actions` array exactly
2. **Wrong video numbering**: Videos should be named 0.mp4, 1.mp4, 2.mp4, etc.
3. **Inconsistent video counts**: All signs should have the same number of videos
4. **Forgetting to update variables**: Change `actions` and `no_sequences` in ALL notebooks

---

## 💡 PRO TIPS

1. **Start small**: Test with 2-3 signs and 10 videos each first
2. **Use Google Drive**: Mount Drive to avoid re-uploading if session disconnects
3. **Save checkpoints**: After each step, the folders persist in Colab
4. **Check outputs**: Use `!ls -R MP_Data/` to verify structure after each step

---

## 📊 FILE SIZE ESTIMATES

- Raw video (30 sec): ~5-10 MB each
- 30-frame video: ~1-2 MB each
- Landmark .npy file: ~2 KB each
- Trained model: ~5-20 MB

**Example for 5 signs × 20 videos:**
- Raw videos: ~1 GB
- MP_Data: ~6 MB (3,000 .npy files)
- Model: ~10 MB

---

## 🆘 TROUBLESHOOTING

**Q: "No such file or directory: MP_Data/hello/0"**
- A: Run `video_landmark_extraction.ipynb` first to create MP_Data/

**Q: "Shape mismatch during training"**
- A: Make sure all videos have exactly 30 frames and 258 landmarks

**Q: "Session disconnected, lost my data"**
- A: Use Google Drive to save your folders, or download MP_Data/ as backup

---

## 🎉 SUCCESS!

Once you have `my_fsl_model.h5`, you can:
1. Replace the existing model in the webapp
2. Test with `test_live.py` or `test_video.py`
3. Deploy your custom sign language translator!

---

**Need help?** Check that your folder structure matches the examples above!

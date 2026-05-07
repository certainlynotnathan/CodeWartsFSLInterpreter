"""
Quick verification script to check if your model is compatible
"""
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from keras.layers import Conv1D

print("=" * 60)
print("MODEL COMPATIBILITY CHECK")
print("=" * 60)

# Load actions
try:
    actions = np.load('../models/action_labels.npy', allow_pickle=True)
    print(f"✓ Actions loaded: {len(actions)} actions")
    print(f"  Sample actions: {actions[:5]}")
except Exception as e:
    print(f"✗ Error loading actions: {e}")
    exit(1)

# Build model architecture
try:
    from tensorflow.keras.layers import Dropout
    from tensorflow.keras.regularizers import l2
    
    model = Sequential()
    # 1. Feature Extraction with early dropout
    model.add(Conv1D(64, kernel_size=3, activation='relu', input_shape=(30, 258)))
    model.add(Dropout(0.3))
    # 2. Smaller LSTMs with Heavy L2 Regularization
    model.add(LSTM(64, return_sequences=True, kernel_regularizer=l2(0.001)))
    model.add(Dropout(0.5))
    model.add(LSTM(128, return_sequences=False, kernel_regularizer=l2(0.001)))
    model.add(Dropout(0.5))
    # 3. Dense Classification Head
    model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))
    model.add(Dropout(0.3))
    model.add(Dense(actions.shape[0], activation='softmax'))
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    print(f"✓ Model architecture built successfully")
except Exception as e:
    print(f"✗ Error building model: {e}")
    exit(1)

# Load weights
try:
    model.load_weights('../models/fsl_105_model.h5')
    print(f"✓ Model weights loaded from fsl_105_model.h5")
except Exception as e:
    print(f"✗ Error loading model weights: {e}")
    exit(1)

# Test prediction with dummy data
try:
    dummy_sequence = np.random.rand(1, 30, 258)
    prediction = model.predict(dummy_sequence, verbose=0)
    predicted_action = actions[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    print(f"✓ Test prediction successful")
    print(f"  Predicted action: {predicted_action}")
    print(f"  Confidence: {confidence:.2%}")
except Exception as e:
    print(f"✗ Error during prediction: {e}")
    exit(1)

print("=" * 60)
print("✓ ALL CHECKS PASSED - Model is ready to use!")
print("=" * 60)
print("\nYou can now run:")
print("  python test_live.py   - for webcam testing")
print("  python test_video.py  - for video file testing")

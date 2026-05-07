# FSL Translator - Model Comparison Guide

## Available Apps

You now have **two versions** of the FSL Translator app, each using a different model:

### Version 1 (Original)
- **File**: `fsl_translator_app.py`
- **Model**: `models/fsl_105_model.h5`
- **Run**: Double-click `run_app.bat` or run `python fsl_translator_app.py`
- **UI Color**: Green theme
- **Title**: "Filipino Sign Language Translator"

### Version 2 (New)
- **File**: `fsl_translator_app_v2.py`
- **Model**: `models/fsl_105_model_2.h5`
- **Run**: Double-click `run_app_v2.bat` or run `python fsl_translator_app_v2.py`
- **UI Color**: Cyan/Teal theme
- **Title**: "Filipino Sign Language Translator V2"

## Key Differences

### Visual Differences
| Feature | Version 1 | Version 2 |
|---------|-----------|-----------|
| Title Color | White | Cyan |
| Translation Text Color | Green | Cyan |
| Start Button Color | Green | Teal |
| Model Info Display | No | Yes (shows model filename) |

### Technical Differences
- **Model File**: Different trained models
- **Predictions**: May vary based on training differences
- **Accuracy**: Compare both to see which performs better for your use case

## How to Compare Models

1. **Run both apps side by side** (not simultaneously - camera conflict)
2. **Test the same signs** with each version
3. **Compare results**:
   - Which detects signs faster?
   - Which has better accuracy?
   - Which handles transitions better?

## Testing Workflow

```bash
# Test Version 1
python fsl_translator_app.py
# Perform signs, note results
# Close app

# Test Version 2
python fsl_translator_app_v2.py
# Perform same signs, compare results
# Close app
```

## Both Apps Share

- ✅ Same UI layout
- ✅ Same sign stabilization logic
- ✅ Same sentence builder
- ✅ Same TTS functionality
- ✅ Same camera settings
- ✅ Same action labels (105 signs)

## Which One to Use?

- **Use V1** if it performs better in your tests
- **Use V2** if the new model is more accurate
- **Keep both** to compare and choose based on situation

## Notes

- Both apps use the same `action_labels.npy` file
- Both apps cannot run simultaneously (camera conflict)
- Both apps have identical features, only the model differs
- The model with better training should give better results

## Quick Launch

### Windows:
- **V1**: Double-click `run_app.bat`
- **V2**: Double-click `run_app_v2.bat`

### Command Line:
```bash
# Version 1
python fsl_translator_app.py

# Version 2
python fsl_translator_app_v2.py
```

## Troubleshooting

If V2 doesn't work:
1. Check that `models/fsl_105_model_2.h5` exists
2. Verify it has the same architecture as V1
3. Check that it was trained with the same 105 actions
4. Ensure the file isn't corrupted

Both apps will show clear error messages if the model fails to load.

# Project Setup Guide - Isolated Python Environment

## Overview
This project uses an isolated Python virtual environment (`venv`) to keep dependencies separate from your system Python. This prevents version conflicts and makes the project reproducible.

## Quick Start

### 1. Activate Virtual Environment

**Windows (PowerShell or Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell - if you get an execution policy error):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies
After activation, install all required packages:
```bash
pip install -r requirements.txt
```

### 3. Deactivate Virtual Environment
When done working, deactivate the environment:
```bash
deactivate
```

---

## Project Dependencies

The `requirements.txt` file includes:
- **tensorflow** (2.13.0): Deep learning and neural network training
- **flask** (2.3.3): Web framework for the app
- **numpy** (1.24.3): Numerical computing
- **pillow** (10.0.0): Image processing
- **matplotlib** (3.7.2): Data visualization
- **jupyter** (1.0.0): Interactive notebooks
- **scikit-learn** (1.3.0): Machine learning utilities
- **scipy** (1.11.2): Scientific computing

---

## Using with VS Code

### Select Correct Python Interpreter
1. Open Command Palette: `Ctrl + Shift + P`
2. Search for "Python: Select Interpreter"
3. Choose the interpreter from `./venv/bin/python` (or `./venv/Scripts/python` on Windows)

### Run Flask App
Make sure the venv is activated, then:
```bash
python app.py
```

### Use Jupyter Notebooks
1. Activate the venv
2. Run: `jupyter notebook`
3. Open either notebook in the browser
4. When prompted to select a kernel, choose the one from your venv

---

## Verifying Installation

To confirm everything is installed correctly, run:
```bash
python -c "import tensorflow, flask, numpy; print('✓ All core packages available')"
```

Or test with the app:
```bash
python app.py
```

---

## Troubleshooting

**"venv\Scripts\activate is not recognized":**
- Ensure you're in the project directory: `cd "d:\projects\ML projects\plant disease final"`
- Try using the full path: `.\venv\Scripts\activate`

**"ModuleNotFoundError: No module named...":**
- Make sure the venv is activated (you should see `(venv)` in your terminal prompt)
- Run `pip install -r requirements.txt` again

**"pip is not found":**
- The venv might not be properly activated
- Try: `python -m pip install -r requirements.txt`

---

## Project Structure in Venv

```
project/
├── venv/                           # Isolated Python environment (do not commit to git)
│   ├── Scripts/                    # Executable files (activate, pip, python, etc.)
│   ├── Lib/                        # Installed packages
│   └── pyvenv.cfg                  # Environment configuration
├── requirements.txt                # List of all dependencies
├── app.py                          # Flask application
├── model_vgg16.h5                  # Trained model
├── resnetplant.h5                  # Trained model
├── Transfer Learning Resnet 50.ipynb
├── Transfer Learning vgg16.ipynb
├── dataset/                        # Training/test data
└── templates/                      # HTML templates
```

---

## Next Steps

1. ✅ Virtual environment created (`venv/` folder)
2. ✅ Dependencies listed in `requirements.txt`
3. ⏭️ **Now**: Activate venv and install dependencies:
   ```bash
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. ⏭️ **Then**: Select the venv interpreter in VS Code
5. ⏭️ **Finally**: Run notebooks or app within the isolated environment


# MemeDetector

Experience a real time Meme-Machine! This project employs AI-Powered technologies to detect hand gestures and face expressions to trigger and display context-aware meme images!



## ✨Features

•🎥 Real-time webcam processing

•✋ Hand gesture detection using MediaPipe Hands

•😀 Facial landmark detection using MediaPipe Face Mesh

•🖼️ Automatic meme display based on detected gestures and facial expressions

•⚡ Fast and lightweight with OpenCV

•📷 Live webcam overlay system


## 🛠️Tech Stack

• Python

• OpenCV

• MediaPipe

• NumPy
## 📂Project Structure

AI-Meme-Detector/

 │── Monkey Images/                     # Folder containing meme images

  │── HandTrackingModule.py      # MediaPipe hand tracking module

  │── FaceMeshModule.py          # MediaPipe face mesh module

  │── memeRecognizer.py          # Main application 

  │── requirements.txt 

  │── demo.mp4

  └── README.md
## 🧑‍💻Installation

1. Install Python

Download the latest version of Python from:

https://www.python.org/downloads/

During installation:

✅ Check "Add Python to PATH"
Click Install Now

Verify the installation:
```bash
python --version
```
or
```bash
py --version
```
2. Install Visual Studio Code

Download Visual Studio Code from:

https://code.visualstudio.com/

After installation:

•Open VS Code.

•Go to the Extensions tab (Ctrl + Shift + X).

•Install the following extensions:

•Python (Microsoft) – Python language support, debugging, and IntelliSense.

•Pylance – Fast type checking and intelligent code completion.

•Code Runner – Quickly run Python files directly from VS Code.

•Jupyter (Optional but Recommended) – For working with Jupyter notebooks.

•Restart VS Code if prompted.


## 🚀Run Locally

1. Clone the project
```bash
  git clone https://github.com/your-username/Meme-Detector.git

  
```
Replace your-username with your GitHub username.

2. Go to the project directory

```bash
  cd Meme-Detector
```

3. Create a Virtual Environment
•Windows
```bash
python -m venv venv
```

If the above command doesn't work:

```bash
py -m venv venv
```

•macOS / Linux
```bash
python3 -m venv venv
```
3. Activate the Virtual Environment

Windows (Command Prompt)
```bash
venv\Scripts\activate
```

Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```
macOS / Linux
```bash
source venv/bin/activate
```

If successful, your terminal will show something similar to:
```bash
(venv) C:\Users\YourName\Meme-Detector>
```
4. Install Dependencies


Install all required packages using:

```bash
pip install -r requirements.txt
```

If you don't have a requirements.txt file yet, install the packages manually or the command doesn't work:

```bash
pip install opencv-python mediapipe numpy
```
5. Verify Installation



Check that the packages were installed correctly:

```bash
pip list
```
You should see packages including:
```bash
mediapipe

numpy

opencv-python    
```
## 📸How it works 

1. Captures live video from your webcam.
2. Detects hands using handDetectionModule.
3. Detects facial landmarks using faceMeshModule.
4. Recognizes predefined gestures and expressions.
5. Displays corresponding memes on the live camera feed in real time.


## 🖼️Demo

Enter the following command or open demo.mp4 from project file
```bash
start demo.mp4
```
## 📌 Future Improvements 

•🎯 More hand gestures

•😂 Larger meme library

•🎞️ GIF support

•🔊 Sound effects

•🎮 Gesture-controlled menu

•📁 Custom meme packs

•🧠 Smarter expression recognition

•✨ Improved animations and UI
## Contributing

Contributions are always welcome!

1. Fork this repository.

2. Create a new feature branch.

3. Commit your changes.

4. Push your branch.

5. Open a Pull Request.

Please adhere to this project's `code of conduct`.


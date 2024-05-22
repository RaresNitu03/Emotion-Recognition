# Emotion Recognition Application Guide

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
    - [Python Installation](#python-installation)
    - [PyCharm IDE Installation](#pycharm-ide-installation)
3. [Running the Application](#running-the-application)
    - [Webcam Emotion Recognition](#webcam-emotion-recognition)
    - [Photo Emotion Recognition](#photo-emotion-recognition)
4. [Function Explication](#function-explication)
    - [Webcam Emotion Recognition Function](#webcam-emotion-recognition-function)
    - [Photo Emotion Recognition Function](#photo-emotion-recognition-function)
5. [References](#references)

## Overview
The Emotion Recognition Application is designed to detect emotions either from live webcam feed or from a photo. It utilizes OpenCV and DeepFace libraries for face detection and emotion recognition.

## Installation
### Python Installation
Before running the application, ensure that Python is installed on your machine. Follow the steps below:
1. **Check Python Version:** Open your terminal/command prompt and type:

        python --version

    If Python is not installed, you will need to install it.
2. **Install Python:**
- For beginners: Install Python from the Microsoft Store.
- For advanced users: Download Python from the Python.org website.

### PyCharm IDE Installation
PyCharm is the recommended Integrated Development Environment (IDE) for this project. Follow these steps to install PyCharm:
1. **Download PyCharm:** Go to the JetBrains website and download PyCharm Community Edition.
2. **Install PyCharm:** Run the downloaded .exe file and follow the installation instructions.

## Running the Application
To start the application, follow these steps:
1. Add folder in your workspace.
2. Install the required packages (OpenCV and DeepFace) using the Python packages tab.
   - **Attention:** For the correct running of the application, the following versions must be installed (OpenCV - 4.5.5.62, DeepFace – 0.0.73 and in case of error, the tensorflow version should be adapted to 2.14.0).
3. Run the `main.py` Python file.
4. A window will open showing the main menu.

    To detect emotions from live webcam feed, follow these steps:
5. From the main menu press the Webcam Emotion Recognition button.
6. A new window will open accessing the device's webcam that will display the detected emotion.
7. Close the window by pressing any key when you are ready, you will be redirected back to the menu.

    To detect emotions from a photo, follow these steps:
8. Back in the main menu, you can press the Photo Emotion Recognition button.
9. A new window will open. By pressing the select photo button, you will be redirected to a window to choose any photo from your computer.
10. The selected photo will be displayed with detected faces and annotated emotions.
11. To close, press any key, and you will be redirected back to the main menu.

    To close the application
12. You can press the close button or close the window.


## Function Explication
### Webcam Emotion Recognition Function
The `webcam_emotion_recognition()` function establishes a graphical interface for real-time emotion analysis from a webcam stream. This functionality relies on OpenCV for video processing and face detection, and DeepFace for emotion recognition on identified faces. Upon invocation, the function initializes a dedicated window for webcam usage, continuously captures video frames, identifies faces within each frame, and then overlays emotion predictions onto the detected faces. This annotated video feed is displayed within the window. The function also monitors user input to facilitate the closing of the webcam window and termination of the application. Overall, it offers a streamlined approach for integrating real-time emotion analysis capabilities into applications utilizing webcam input.

### Photo Emotion Recognition Function
The `photo_emotion_recognition()` function integrates tkinter, OpenCV, and DeepFace libraries to facilitate a user-friendly graphical interface for analyzing emotions within selected photographs. Upon invocation, it presents a visually engaging window allowing users to explore emotional nuances captured in images. Leveraging OpenCV's image processing capabilities, it detects facial features within the selected photograph, subsequently employing DeepFace's algorithms to analyze emotional expressions. The annotated photo, enriched with predicted emotions, provides users with valuable insights into the depicted individuals' emotional states. Intuitive controls, including a "Select Photo" button for input and a "Close" button for conclusion, ensure seamless user interaction. With robust error handling mechanisms in place, the function prioritizes a smooth user experience, fostering an environment conducive to insightful exploration of emotional content encapsulated within photographs.

## References
- [GeeksForGeeks](https://www.geeksforgeeks.org/)
- [GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- [OpenCV Documentation](https://docs.opencv.org/)
- [DeepFace Documentation](https://deepface.readthedocs.io/en/latest/index.html)

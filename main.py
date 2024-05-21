import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from deepface import DeepFace

# Function for webcam emotion recognition
def webcam_emotion_recognition():
    # Create a new window for webcam emotion recognition
    webcam_window = tk.Toplevel()
    webcam_window.title("Webcam Emotion Recognition")

    # Load the face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Open the webcam
    video = cv2.VideoCapture(0, cv2.CAP_ANY)

    if not video.isOpened():
        raise IOError("Cannot open webcam")

    # Function to close the webcam window
    def close_webcam():
        video.release()
        cv2.destroyAllWindows()
        webcam_window.destroy()

    window_width, window_height = 400, 200
    screen_width = webcam_window.winfo_screenwidth()
    screen_height = webcam_window.winfo_screenheight()

    # Loop to capture frames from the webcam
    while video.isOpened():
        _, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('video')
        cv2.moveWindow('video', (screen_width - window_width) // 2 - 50, (screen_height - window_height) // 2 - 125)
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around detected faces and annotate with emotions
        for x, y, w, h in face:
            image = cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)
            try:
                analyze = DeepFace.analyze(frame, actions=['emotion'])
                cv2.putText(image, f"Emotion: {analyze['dominant_emotion']}", (x - 50, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), thickness=2)
                print(analyze['dominant_emotion'])
            except:
                print('no face')

        # Display the frame in the window
        cv2.imshow('video', frame)
        key = cv2.waitKey(1) & 0xFF
        if key != 255:
            close_webcam()
            break

# Function for photo emotion recognition
def photo_emotion_recognition():
    # Create a new window for photo emotion recognition
    photo_window = tk.Toplevel()
    photo_window.title("Photo Emotion Recognition")

    # Set background image
    background_image_path = "./Photos_Bk/Image.jpeg"  # Provide the path to your background image
    background_image = Image.open(background_image_path)
    window_width, window_height = background_image.size

    # Calculate the position to place the window in the middle of the screen
    screen_width = photo_window.winfo_screenwidth()
    screen_height = photo_window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    photo_window.geometry(f"{window_width}x{window_height}+{x+70}+{y}")

    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(photo_window, image=background_photo)
    background_label.image = background_photo
    background_label.pack(fill="both", expand=True)

    # Function to open file dialog and analyze photo
    def open_file_dialog():
        filename = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if filename:
            analyze_photo_emotion(filename, photo_window)

    # Function to analyze emotion in the selected photo
    def analyze_photo_emotion(filename, parent_window):
        try:
            image = cv2.imread(filename)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.namedWindow('Emotion Recognition')
            cv2.moveWindow('Emotion Recognition', (screen_width - window_width) // 2 + 20, (screen_height - window_height) // 2)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                face_roi = image[y:y+h, x:x+w]
                analyze = DeepFace.analyze(face_roi, actions=['emotion'])
                emotion = analyze['dominant_emotion']
                cv2.putText(image, f"Emotion: {emotion}", (x - 50, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

            cv2.imshow('Emotion Recognition', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print(emotion)
            parent_window.destroy()
        except Exception as e:
            print('Error analyzing emotions:', e)

    # Function to close the photo window
    def close_photo_window():
        photo_window.destroy()

    photo_window.protocol("WM_DELETE_WINDOW", close_photo_window)

    button_x = window_width // 2
    button_y = window_height // 2

    # Create a button to select a photo
    button = tk.Button(photo_window, text="Select Photo", command=open_file_dialog, bg="blue", fg="white", font=("Helvetica", 12, "bold"))
    button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    # Create a close button for the photo window
    close_button = tk.Button(photo_window, text="Close", command=close_photo_window, bg="blue", fg="white", font=("Helvetica", 12, "bold"))
    close_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    photo_window.mainloop()

# Function to close the main window
def close_main_window(root):
    root.destroy()

# Function to create the main menu
def main_menu():
    root = tk.Tk()
    root.title("Emotion Recognition APP")

    # Load main background image
    background_image_path = "./Photos_Bk/main.png"
    background_image = Image.open(background_image_path)
    photo = ImageTk.PhotoImage(background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.pack()

    # Create title text
    canvas.create_text(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2 - 100, text="Emotion Recognition APP", font=("Helvetica", 36, "bold"), fill="blue")

    button_x = root.winfo_screenwidth() // 2
    button_y = root.winfo_screenheight() // 2 + 50
    button_padx = 10

    # Create buttons for webcam and photo emotion recognition
    webcam_button = tk.Button(canvas, text="Webcam Emotion Recognition", command=webcam_emotion_recognition, bg="blue", fg="white", font=("Helvetica", 14, "bold"))
    webcam_button_window = canvas.create_window(button_x - button_padx - webcam_button.winfo_reqwidth() // 2, button_y - 70, window=webcam_button)

    photo_button = tk.Button(canvas, text="Photo Emotion Recognition", command=photo_emotion_recognition, bg="blue", fg="white", font=("Helvetica", 14, "bold"))
    photo_button_window = canvas.create_window(button_x + button_padx + photo_button.winfo_reqwidth() // 2, button_y - 70, window=photo_button)

    # Create a close button for the main window
    close_button = tk.Button(canvas, text="Close", command=lambda: close_main_window(root), bg="blue", fg="white", font=("Helvetica", 14, "bold"))
    close_button_window = canvas.create_window(root.winfo_screenwidth() // 2, button_y - 15, window=close_button)

    root.mainloop()

# Run the main menu
if __name__ == "__main__":
    main_menu()

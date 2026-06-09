"""
Aura Reflect – AI-Based Mood Detection System
Developed by: Priya Dharshini V
Description: Detects facial emotions via webcam or image upload and displays
             mood-based motivational quotes using DeepFace + OpenCV + Tkinter.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont
import cv2
from deepface import DeepFace
from PIL import Image, ImageTk
import threading
import random
import os

# ── Mood-based quotes ──────────────────────────────────────────────────────────
MOOD_QUOTES = {
    "happy": [
        "Your smile is your superpower. Keep shining! 🌟",
        "Happiness looks gorgeous on you! Keep going! 😊",
        "You radiate joy — the world is better with your energy! ✨",
    ],
    "sad": [
        "It's okay to not be okay. Better days are coming. 🌈",
        "Every storm runs out of rain. You are stronger than you think. 💙",
        "Tears water the seeds of your future strength. 🌱",
    ],
    "angry": [
        "Take a deep breath. You are in control. 🧘",
        "Channel that fire into fuel — you have the power to change things. 🔥",
        "Pause. Breathe. Your calmness is your strength. 💪",
    ],
    "surprise": [
        "Life is full of wonderful surprises — embrace them! 🎉",
        "Stay curious, stay amazed. The world has so much to offer! 🌍",
        "Wow moments are the best moments. Enjoy this one! 🤩",
    ],
    "fear": [
        "Courage is not the absence of fear — it's moving forward despite it. 🦁",
        "You have survived every difficult moment so far. This too shall pass. 🌟",
        "Fear is just excitement without breath. Breathe, and go for it! 💫",
    ],
    "disgust": [
        "Trust your instincts — they're protecting you. 🛡️",
        "It's okay to walk away from things that don't align with your values. 🌿",
        "Boundaries are beautiful. Honour your feelings. 💜",
    ],
    "neutral": [
        "A calm mind is a powerful mind. You're doing great. 🧠",
        "Steady and focused — you're exactly where you need to be. 🎯",
        "Peace is productive. Keep that energy! ☁️",
    ],
}

MOOD_COLORS = {
    "happy":    "#FFD700",
    "sad":      "#6495ED",
    "angry":    "#FF6347",
    "surprise": "#FF69B4",
    "fear":     "#9370DB",
    "disgust":  "#3CB371",
    "neutral":  "#87CEEB",
}

MOOD_EMOJI = {
    "happy": "😊", "sad": "😢", "angry": "😠",
    "surprise": "😲", "fear": "😨", "disgust": "🤢", "neutral": "😐",
}


class AuraReflect:
    def __init__(self, root):
        self.root = root
        self.root.title("Aura Reflect – AI Mood Detection")
        self.root.geometry("780x620")
        self.root.configure(bg="#1C1C2E")
        self.root.resizable(False, False)

        self.cap = None
        self.webcam_running = False
        self.current_frame = None

        self._build_ui()

    # ── UI ─────────────────────────────────────────────────────────────────────
    def _build_ui(self):
        # Title
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        tk.Label(self.root, text="✨ Aura Reflect", font=title_font,
                 bg="#1C1C2E", fg="#A78BFA").pack(pady=(18, 2))
        tk.Label(self.root, text="AI-Powered Mood Detection System",
                 font=("Helvetica", 11), bg="#1C1C2E", fg="#888888").pack()

        # Video / image display frame
        self.display_label = tk.Label(self.root, bg="#2D2D44",
                                      width=480, height=320,
                                      text="📷  Webcam feed or uploaded image appears here",
                                      font=("Helvetica", 10), fg="#666680",
                                      relief="flat")
        self.display_label.pack(pady=12)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#1C1C2E")
        btn_frame.pack()

        self._btn(btn_frame, "📷  Start Webcam",  "#7C3AED", self.start_webcam).grid(row=0, column=0, padx=8)
        self._btn(btn_frame, "⏹  Stop Webcam",   "#4B5563", self.stop_webcam).grid(row=0, column=1, padx=8)
        self._btn(btn_frame, "🖼  Upload Image",  "#0EA5E9", self.upload_image).grid(row=0, column=2, padx=8)
        self._btn(btn_frame, "🔍  Detect Mood",   "#059669", self.detect_mood).grid(row=0, column=3, padx=8)

        # Result panel
        result_frame = tk.Frame(self.root, bg="#2D2D44", bd=0)
        result_frame.pack(fill="x", padx=30, pady=14)

        self.mood_label = tk.Label(result_frame, text="Mood: —",
                                   font=("Helvetica", 14, "bold"),
                                   bg="#2D2D44", fg="#FFFFFF")
        self.mood_label.pack(pady=(10, 2))

        self.quote_label = tk.Label(result_frame, text="Detect a mood to see your personalised quote ✨",
                                    font=("Helvetica", 11), bg="#2D2D44", fg="#AAAACC",
                                    wraplength=680, justify="center")
        self.quote_label.pack(pady=(2, 12))

    def _btn(self, parent, text, color, cmd):
        return tk.Button(parent, text=text, command=cmd,
                         bg=color, fg="white", font=("Helvetica", 10, "bold"),
                         relief="flat", padx=12, pady=8, cursor="hand2",
                         activebackground=color, activeforeground="white")

    # ── Webcam ─────────────────────────────────────────────────────────────────
    def start_webcam(self):
        if self.webcam_running:
            return
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not access webcam. Please check your camera.")
            return
        self.webcam_running = True
        threading.Thread(target=self._webcam_loop, daemon=True).start()

    def _webcam_loop(self):
        while self.webcam_running:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.current_frame = frame.copy()
            self._show_frame(frame)
        if self.cap:
            self.cap.release()

    def stop_webcam(self):
        self.webcam_running = False

    # ── Image upload ───────────────────────────────────────────────────────────
    def upload_image(self):
        self.stop_webcam()
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")])
        if not path:
            return
        frame = cv2.imread(path)
        if frame is None:
            messagebox.showerror("Error", "Could not read image file.")
            return
        self.current_frame = frame
        self._show_frame(frame)

    # ── Display helper ─────────────────────────────────────────────────────────
    def _show_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        img.thumbnail((480, 320))
        imgtk = ImageTk.PhotoImage(img)
        self.display_label.configure(image=imgtk, text="")
        self.display_label.image = imgtk

    # ── Mood detection ─────────────────────────────────────────────────────────
    def detect_mood(self):
        if self.current_frame is None:
            messagebox.showwarning("No Input", "Please start the webcam or upload an image first.")
            return
        self.mood_label.config(text="Analysing... 🔍", fg="#FACC15")
        self.quote_label.config(text="")
        self.root.update()
        threading.Thread(target=self._run_detection, daemon=True).start()

    def _run_detection(self):
        try:
            result = DeepFace.analyze(self.current_frame,
                                      actions=["emotion"],
                                      enforce_detection=False)
            emotion = result[0]["dominant_emotion"].lower()
            self._display_result(emotion)
        except Exception as e:
            self.root.after(0, lambda: self.mood_label.config(
                text="Could not detect a face. Try again. 😕", fg="#FF6B6B"))

    def _display_result(self, emotion):
        quote  = random.choice(MOOD_QUOTES.get(emotion, MOOD_QUOTES["neutral"]))
        color  = MOOD_COLORS.get(emotion, "#AAAACC")
        emoji  = MOOD_EMOJI.get(emotion, "🙂")
        label  = f"{emoji}  Mood Detected: {emotion.capitalize()}"

        self.root.after(0, lambda: self.mood_label.config(text=label, fg=color))
        self.root.after(0, lambda: self.quote_label.config(text=quote, fg="#E2E8F0"))

    # ── Cleanup ────────────────────────────────────────────────────────────────
    def on_close(self):
        self.stop_webcam()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AuraReflect(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()

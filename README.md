# ✨ Aura Reflect — AI-Based Mood Detection System

> *"Your emotions are valid. Let AI reflect them back to you."*

Aura Reflect is a real-time facial emotion detection application built with Python. It uses **DeepFace** and **OpenCV** to identify a user's emotion from a live webcam feed or an uploaded image, then responds with a personalised, mood-based motivational quote — all within a clean **Tkinter GUI**.

Developed as part of a **Women's Hackathon 2025** project by **Priya Dharshini V**, B.Tech IT, Panimalar Engineering College.

---

## 🎯 Features

- 📷 **Live Webcam Detection** — real-time emotion recognition from your camera
- 🖼️ **Image Upload** — detect mood from any photo
- 🧠 **7 Emotion Classes** — Happy, Sad, Angry, Surprise, Fear, Disgust, Neutral
- 💬 **Personalised Quotes** — mood-matched motivational messages displayed instantly
- 🎨 **Clean GUI** — dark-themed Tkinter interface with colour-coded results
- ⚡ **Threaded processing** — non-blocking UI during analysis

---

## 🖥️ Demo

```
[Start Webcam] → Face detected → Mood: Happy 😊
→ "Your smile is your superpower. Keep shining! 🌟"
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| DeepFace | Facial emotion recognition (CNN-based) |
| OpenCV | Webcam capture & image processing |
| Tkinter | GUI framework |
| Pillow (PIL) | Image display in Tkinter |

---

## 📁 Project Structure

```
aura_reflect/
│
├── aura_reflect.py      # Main application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/aura-reflect.git
cd aura-reflect
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python aura_reflect.py
```

> **Note:** On first run, DeepFace will automatically download the required model weights (~100MB). Ensure you have an internet connection.

---

## 📸 How to Use

1. Launch the app — a dark-themed GUI window opens
2. Click **📷 Start Webcam** to begin live detection, OR
3. Click **🖼 Upload Image** to load a photo from your device
4. Click **🔍 Detect Mood** to analyse the face
5. Your detected emotion and a personalised quote appear instantly!

---

## 🧪 Emotions Detected

| Emotion | Quote Example |
|---|---|
| 😊 Happy | "Your smile is your superpower. Keep shining!" |
| 😢 Sad | "Every storm runs out of rain. You are stronger than you think." |
| 😠 Angry | "Take a deep breath. You are in control." |
| 😲 Surprise | "Life is full of wonderful surprises — embrace them!" |
| 😨 Fear | "Courage is not the absence of fear — it's moving forward despite it." |
| 🤢 Disgust | "Trust your instincts — they're protecting you." |
| 😐 Neutral | "A calm mind is a powerful mind. You're doing great." |

---

## 💡 How It Works

```
Camera / Image Input
        ↓
OpenCV — frame capture & preprocessing
        ↓
DeepFace.analyze() — CNN-based emotion classification
        ↓
Dominant emotion extracted
        ↓
Mood-matched quote randomly selected
        ↓
Tkinter GUI — result displayed with colour coding
```

DeepFace internally uses a pre-trained deep neural network (based on FER-2013 dataset) to classify facial expressions into 7 emotion categories.

---

## 🏆 Project Context

This project was built and presented at a **Women's Hackathon (2025)**, focusing on:
- Mental wellness and emotional awareness through AI
- Accessible, user-friendly design
- Practical application of Machine Learning in everyday life

---

## 👩‍💻 Author

**Priya Dharshini V**
B.Tech Information Technology | Panimalar Engineering College (Anna University)
📧 priyadharshini241it@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/priya-dharshini-v-6b0401387)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Made with 💜 and Python*

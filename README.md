# 🎵 Epic Magic Rap Video (PRO)

## 📹 Video Status

⚠️ **Das Musik-Video ist noch NICHT fertig!** / **The music video is NOT finished yet!**

Um das Video zu erstellen, folge den Schritten unten. / To create the video, follow the steps below.

### Was wird benötigt / What is needed:
- ✅ Video-Datei (`input/video.mp4`) 
- ✅ Audio-Datei (`input/audio.mp3` oder [(Ooh-ooh).mp3](https://github.com/user-attachments/files/24377147/Ooh-ooh.mp3))
- ⏳ Pipeline ausführen / Run the pipeline
- ⏳ Final video erstellen / Create final video

---

## 🎯 Projekt-Übersicht / Project Overview

Dieses Projekt erstellt ein professionelles Rap-Video mit:
- **Lip-Sync** (Wav2Lip GAN)
- **Audio-Analyse** (Librosa)
- **Magic FX** (FFmpeg Filter)
- **3:05 Minuten Dauer** (185 Sekunden)

This project creates a professional rap video with:
- **Lip-Sync** using Wav2Lip GAN
- **Audio Analysis** with Librosa
- **Magic FX** using FFmpeg filters
- **3:05 minutes duration** (185 seconds)

---

## 📁 Projekt-Struktur / Project Structure

```
epic-rap-magic-video/
├── input/
│   ├── video.mp4
│   └── audio.mp3
├── pipeline.py
├── requirements.txt
└── README.md
```

---

## 🔧 Requirements

- Python 3.9+
- ffmpeg
- NVIDIA GPU empfohlen / recommended
- gdown (für Wav2Lip Model / for Wav2Lip model)

---

## 🚀 Installation & Setup

### 1️⃣ Abhängigkeiten installieren / Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Input-Dateien vorbereiten / Prepare input files
```bash
mkdir -p input
# Kopiere video.mp4 und audio.mp3 in den input/ Ordner
# Copy video.mp4 and audio.mp3 to the input/ folder
```

### 3️⃣ Pipeline starten / Start pipeline
```bash
python pipeline.py
```

---

## 🎬 Pipeline-Schritte / Pipeline Steps

Das Script führt automatisch folgende Schritte aus:

1. **STEP 1: Lip-Sync** - Wav2Lip GAN für realistische Lippenbewegungen
2. **STEP 2: Trim** - Video auf 3:05 Minuten schneiden
3. **STEP 3: Audio Analysis** - RMS Energy-Analyse für Effekte
4. **STEP 4: Magic FX** - Visuelle Effekte (Kontrast, Blur, Color Overlay)
5. **STEP 5: Final** - Zusammenführung von Video und Audio

**Output:** `final_epic_video.mp4`

---

## 📚 Zusätzliche Ressourcen / Additional Resources

- Video Preview: https://github.com/user-attachments/assets/5cd7e68a-9cf6-4b97-a84e-b3c6eb375089
- Audio Sample: [(Ooh-ooh).mp3](https://github.com/user-attachments/files/24377147/Ooh-ooh.mp3)

---

## ✅ Fertigstellung / Completion

Nach erfolgreichem Durchlauf der Pipeline ist das Video fertig:
- ✅ `final_epic_video.mp4` wurde erstellt
- ✅ Alle Effekte wurden angewendet
- ✅ Video ist bereit zur Veröffentlichung

After successful pipeline execution, the video is ready:
- ✅ `final_epic_video.mp4` has been created
- ✅ All effects have been applied
- ✅ Video is ready for publication


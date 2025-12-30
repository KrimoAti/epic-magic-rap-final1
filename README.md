# epic-magic-rap-final1
epic-rap-magic-video/ ├── input/ epic-rap-magic-video/
├── input/
│   ├── video.mp4import os
import librosa
import numpy as np

# ========= CONFIG =========
VIDEO = "input/video.mp4"
AUDIO = "input/audio.mp3"
DURATION = 185  # 3:05 Minuten
OUT = "final_epic_video.mp4"

# ========= STEP 1: LIPSYNC (Wav2Lip GAN) =========
os.system("""
git clone https://github.com/Rudrabha/Wav2Lip
cd Wav2Lip && pip install -r requirements.txt
gdown https://drive.google.com/uc?id=1rwQx0isG8yR9U-2z3Zq6F6pX6KJ1QJ5c -O wav2lip_gan.pth
python inference.py --checkpoint_path wav2lip_gan.pth --face ../input/video.mp4 --audio ../input/audio.mp3 --outfile ../lipsync.mp4
""")

# ========= STEP 2: TRIM =========
os.system(f"""
ffmpeg -y -i lipsync.mp4 -t {DURATION} trimmed.mp4
""")

# ========= STEP 3: AUDIO ANALYSIS =========
y, sr = librosa.load(AUDIO)
energy = librosa.feature.rms(y=y)[0]
np.save("energy.npy", energy)

# ========= STEP 4: MAGIC FX OVERLAY =========
os.system("""
ffmpeg -y -i trimmed.mp4 -filter_complex "
eq=contrast=1.2:brightness=0.05,
boxblur=2:1,
drawbox=x=0:y=0:w=iw:h=ih:color=red@0.05:t=fill
" magic.mp4
""")

# ========= STEP 5: FINAL =========
os.system(f"""
ffmpeg -y -i magic.mp4 -i {AUDIO} -c:v libx264 -pix_fmt yuv420p -shortest {OUT}
""")

print("DONE → final_epic_video.mp4")

│   └── audio.mp3# Epic Magic Rap Video (PRO)

## Requirements
- Python 3.9+
- ffmpeg
- NVIDIA GPU empfohlen

## Run
```bash
pip install -r requirements.txt
python pipeline.py

├── pipeline.py
├── requirements.txttorch
torchaudio
numpy
librosa
opencv-python
ffmpeg-python
openai-whisper

└── README.md# Epic Magic Rap Video (PRO)

## Requirements
- Python 3.9+
- ffmpeg
- NVIDIA GPU empfohlen

## Run
```bash
pip install -r requirements.txt
python pipeline.py

│   ├── video.mp4 │ 
---

## 6️⃣ Start (nur das)
```bash
pip install -r requirements.txt
python pipeline.py
  └── audio.mp3 ├── pipeline.py ├── requirements.txt └── README.md


https://github.com/user-attachments/assets/eb051514-cbc

https://github.com/user-attachments/assets/5cd7e68a-9cf6-4b97-a84e-b3c6eb375089

[(Ooh-ooh).mp3](https://github.com/user-attachments/files/24377147/Ooh-ooh.mp3)
b-4aea-96ae-3560692d5e41


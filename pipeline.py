import os
import librosa
import numpy as np

# ========= CONFIG =========
VIDEO = "input/video.mp4"
AUDIO = "input/audio.mp3"
DURATION = 185  # 3:05 Minuten
OUT = "final_epic_video.mp4"

# ========= STEP 1: LIPSYNC (Wav2Lip GAN) =========
print("🎬 STEP 1: Lip-Sync mit Wav2Lip GAN...")
os.system("""
git clone https://github.com/Rudrabha/Wav2Lip
cd Wav2Lip && pip install -r requirements.txt
gdown https://drive.google.com/uc?id=1rwQx0isG8yR9U-2z3Zq6F6pX6KJ1QJ5c -O wav2lip_gan.pth
python inference.py --checkpoint_path wav2lip_gan.pth --face ../input/video.mp4 --audio ../input/audio.mp3 --outfile ../lipsync.mp4
""")

# ========= STEP 2: TRIM =========
print("✂️ STEP 2: Video trimmen...")
os.system(f"""
ffmpeg -y -i lipsync.mp4 -t {DURATION} trimmed.mp4
""")

# ========= STEP 3: AUDIO ANALYSIS =========
print("🎵 STEP 3: Audio-Analyse...")
y, sr = librosa.load(AUDIO)
energy = librosa.feature.rms(y=y)[0]
np.save("energy.npy", energy)

# ========= STEP 4: MAGIC FX OVERLAY =========
print("✨ STEP 4: Magic FX hinzufügen...")
os.system("""
ffmpeg -y -i trimmed.mp4 -filter_complex "
eq=contrast=1.2:brightness=0.05,
boxblur=2:1,
drawbox=x=0:y=0:w=iw:h=ih:color=red@0.05:t=fill
" magic.mp4
""")

# ========= STEP 5: FINAL =========
print("🎉 STEP 5: Finales Video erstellen...")
os.system(f"""
ffmpeg -y -i magic.mp4 -i {AUDIO} -c:v libx264 -pix_fmt yuv420p -shortest {OUT}
""")

print("✅ FERTIG → final_epic_video.mp4")
print("🎬 Das Musik-Video ist jetzt FERTIG!")

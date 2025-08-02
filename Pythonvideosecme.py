import time
import webbrowser
import random

print("📽️ Video Seçme Programı")
isim = input("Merhaba, isminiz nedir? ")
print(f"Merhaba {isim}, senin için rastgele bir video seçiliyor...")
time.sleep(2)

# 10 farklı video linki
videolar = [
    "https://www.youtube.com/watch?v=1KXLEzneHTY",
    "https://www.youtube.com/watch?v=Gio7gXUN61k",
    "https://www.youtube.com/watch?v=oody5g-VVmA",
    "https://www.youtube.com/shorts/VVIlYsoa6xs",
    "https://www.youtube.com/watch?v=CIEEYIn3xgE&list=RDCIEEYIn3xgE&start_radio=1",
    "https://www.youtube.com/shorts/LTW58jrIZ3Q",
    "https://www.youtube.com/watch?v=nqa9cL-1K4s",
    "https://www.youtube.com/watch?v=tdd8n64BjIM",
    "https://www.youtube.com/shorts/vww7an5i0TQ",
    "https://www.youtube.com/shorts/x4hfgE8JeiE"
]

# Rastgele bir video seç
secilen_video = random.choice(videolar)

print("Video hazır! Açılıyor...")
time.sleep(2)

# Seçilen videoyu aç
webbrowser.open(secilen_video)

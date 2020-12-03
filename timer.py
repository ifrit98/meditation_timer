import time
import random
from sys import argv
from playsound import playsound

if len(argv) < 5:
    lo = 180  # min 3 min
    hi = 1200 # max 20 min
    sigma = 300 # variance sec ~ 5 min
    mu = abs(hi - lo) / 2  # sec
else:
    lo = int(argv[1])
    hi = int(argv[2])
    mu = int(argv[3])
    sigma = int(argv[4])

print("Params:", {'lo': lo, 'hi': hi, 'mu': mu, 'sigma': sigma})
print("Countdown to practice...")
for i in reversed(range(10)):
    print(i)
    time.sleep(1)


clamp = lambda val, minv, maxv: max(min(val, maxv), minv)
sample = lambda mu, sigma: int(clamp(abs(random.gauss(mu, sigma)), lo, hi))

sound_path = 'gong.mp3'

# Start practice
print("Begin practice!")
playsound(sound_path)

meditation_time = sample(mu, sigma)
time.sleep(meditation_time)

# End practice - 2x for effect
print("End practice!")
playsound(sound_path)
playsound(sound_path)

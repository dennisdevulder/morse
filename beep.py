import sounddevice as sd
import numpy as np
import time, pygame
from subprocess import call

pygame.init()

noise = np.random.uniform(-1, 1, 44100*60)

def setvolume(vol):
  call(["amixer", "cset", "numid=1", vol])

def stream():
  sd.play(noise, 44100)

playing = False
iteration = 1
byt = 0x7D
mouse_down = False
send = True 
setvolume("off")

while True:
  if not playing:
    stream()
    is_playing = True

  if(iteration > 128):
    iteration = 1
    send = False

  setvolume("off")
  time.sleep(0.010)
  
  if(send):
    bytc = byt & iteration
    setvolume("400")

    if(bytc == 0):
      time.sleep(0.030)
    else:
      time.sleep(0.130)

    iteration <<= 1

  setvolume("off")
  time.sleep(0.010)

sd.wait()
setvolume("400")
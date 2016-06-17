import sounddevice as sd
import numpy as np
import time, pygame
from subprocess import call

pygame.init()

noise = np.random.uniform(-1, 1, 44100*10)

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
payload = []

while True:
  if not playing:
    stream()
    playing = True

  if(iteration > 128):
    iteration = 1
    send = False

  setvolume("off")
  time.sleep(0.010)
  
  if(send):
    bytc = byt & iteration
    setvolume("400")

    if(bytc == 0):
      payload += [0]
      time.sleep(0.030)
    else:
      payload += [1]
      time.sleep(0.130)

    iteration <<= 1

  setvolume("off")
  time.sleep(0.010)
  print(payload)

sd.wait()
setvolume("400")

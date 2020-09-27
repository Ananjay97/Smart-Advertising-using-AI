import subprocess
import time
while True:
  print("Launching process..")
  p = subprocess.Popen("main.py", shell=True) # Place your 'main.py' location here
  p.wait()
  print("Restarting in 2 seconds..")
  time.sleep(2)

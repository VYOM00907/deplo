import subprocess
from multiprocessing import Process
import threading
import time
from sys import exit


def lonc():
    subprocess.run(["bash","-c","nohup python3 testowa/tester.py "])


    
t1 = Process(target=lonc, args=())
t1.start()
    
    

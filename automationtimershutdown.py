import time
import subprocess
from selenium import webdriver
while True:
     localtime=time.asctime(time.localtime(time.time()))
     lst1=localtime.split(' ')
     if(lst1[3]=='11:31:00'):
         subprocess.call(["Notepad","/s","/t","7"])
         q=driver.find(["Notepad"])
         q.sendk
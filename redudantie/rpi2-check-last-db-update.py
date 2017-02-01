import os
import time
import subprocess

while True:
    st = os.stat('/home/pi/IDP-Waterkering/applicatie/db.sqlite3')
    age = (time.time() - st.st_mtime)
    print(round(age, 2))

    if age > 60:
        subprocess.call('python3 /home/pi/IDP-Waterkering/applicatie/manage.py runserver', shell=True)
        print('File hasent been updated for more than 60 seconds, starting own server.')
        break
    time.sleep(20)

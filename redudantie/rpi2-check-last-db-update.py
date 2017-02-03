import os
import time
import subprocess

while True:
#dit print uit hoe lang geleden het is geupdate de path moet worden aangepast natuurlijk. de tijd wordt berekend door de huidige tijd van de laatste aanpassing tijd af te trekken.
#Je kunt dit testen door de eerste pi het programma compleet stop te zetten met control C
    st = os.stat('/home/pi/IDP-Waterkering/applicatie/db.sqlite3')
    age = (time.time() - st.st_mtime)
    print(round(age, 2))
	#hoe lang hij wacht voordat hij gaat activeren
    if age > 60:
	#hier moet ook je eerste file
        subprocess.call('python3 /home/pi/IDP-Waterkering/applicatie/manage.py runserver', shell=True)
        print('File hasent been updated for more than 60 seconds, starting own server.')
        break
    time.sleep(20)

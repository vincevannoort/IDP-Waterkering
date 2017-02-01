import os
import time

while True:
    os.system('scp ~/IDP-Waterkering/applicatie/db.sqlite3 pi@192.168.137.2:~/IDP-Waterkering/applicatie/db.sqlite3')
    print('DB is copied.')
    time.sleep(20)

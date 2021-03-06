# IDP-Waterkering
De applicatie voor de IDP Waterkering levert een Proof of Concept voor een waterkering op schaal. De waterkering meet door middel van een ultrasonische sensor de waterstand. Indien het water te hoog staat worden waterkeringdeuren gesloten door stappenmotoren. Wanneer het water daarna weer op normaal niveau is, worden de waterkeringdeuren weer geopend. Door een failover systeem wordt gegarandeerd dat de waterkering altijd zal werken.

## Benodigdheden (hardware)
- HC-SR04 ultrasonische sensor - 1x
- 28byj-48 stappenmotor - 2x
- Raspberry Pi - 2x
- Jumper Wires (MM, MF, FF)
- Resistors (330ohm & 470ohm)
- Breadboard
- UTP netwerkkabel

## Installatie (software op beide Raspberry Pi's)
1. **Configureer Raspberry Pi's**  
   Formateer beide SD-cards via Win32DiskImager. Installeer Raspbian met behulp van een iso bestand. Verdere instructies te lezen op: [Raspbian install](https://www.raspberrypi.org/documentation/installation/installing-images/)
   
2. **Configureer verbinding Raspberry Pi's met sensoren en motoren**  
   Om de Raspberry Pi's met de sensors en motoren te verbinden in een schema gemaakt in Fritzing. Met de benodigdheden kun je de sensors en motoren aan het breadboard koppelen en het breadboard aan de twee Raspberry Pi's. [Fritzing instructie](http://i.imgur.com/pFn06OUg.png)

3. **Configureer netwerk**  
   Om de Raspberry Pi's met elkaar verbinding te kunnen laten maken, moet ervoor worden gezorgt dat de Raspberry Pi's een statisch IP hebben. Hiervoor moeten op beide Raspberry Pi's het netwerk interface bestand worden aangepast.  

   Raspberry Pi 1
   ```
   sudo nano /etc/network/interfaces
   ```
   ```
   auto eth0
   iface eth0 inet static
   address 192.137.0.1
   netmask 255.255.255.0
   ```
   Sla op met `ctrl+o`, `enter` gevolgd door `ctrl+x`  

   Raspberry Pi 2
   ```
   sudo nano /etc/network/interfaces
   ```
   ```
   auto eth0
   iface eth0 inet static
   address 192.137.0.2
   netmask 255.255.255.0
   ```
   Sla op met `ctrl+o`, `enter` gevolgd door `ctrl+x`
   Hierna kun je de verbinding testen door op Raspberry Pi 1 te pingen door ```ping 192.168.137.2``` in te voeren en vanaf Raspberry Pi 2 te pingen door ```ping 192.168.137.1``` in te voeren.

4. **Configureer SSH op beide Raspberry Pi's**  
   Om de applicatie verbinding te laten maken met de Raspberry Pi's wordt een SSH verbinding gebruikt. Deze moet op beide Raspberry Pi's worden ingesteld. Voer op beide Raspberry Pi's het onderstaande commando in.
   ```
   sudo ssh-keygen
   ```
   ```
   sudo raspi-config
   ```  
   Raspberry Pi 1
   ```
   ssh-copy-id -i ~/.ssh/id_rsa.pub 192.137.0.2
   ```  
   Raspberry Pi 2
   ```
   ssh-copy-id -i ~/.ssh/id_rsa.pub 192.137.0.1
   ```  
   Hierna kun je de verbinding testen door op Raspberry Pi 1 het commando ```ssh 192.137.0.2``` in te voeren en vanaf Raspberry Pi 2 het commando ```ssh 192.137.0.1``` in te voeren.

5. **Installeer Django en Django Channels**  
   Raspbian komt geisntalleerd met Python3 en de package manager pip. Door middel van pip kun je de juiste packages installeren die ervoor zorgen dat de webserver kan draaien.
   ```
   sudo pip3 install Django
   ```
   ```
   sudo pip3 install -U channels
   ```

6. **Download applicatie naar beide Raspberry Pi's**  
   Om alle bestanden op de Raspberry Pi's te krijgen, kan de repository met git worden gekopieerd.
   ```
   git clone 'https://github.com/vincevannoort/IDP-Waterkering.git'
   ```

7. **Applicatie starten op beide Raspberry Pi's**  
   Op beide Raspberry Pi's moet de applicatie draaien. Op de eerste moet de Django server draaien, en op de tweede het failover script.  

   Raspberry Pi 1
   ```
   cd IDP-Waterkering/applicatie
   ```
   ```
   sudo python3 manage.py runserver
   ```  

   Raspberry Pi 2
   ```
   cd IDP-Waterkering/redudantie
   ```
   ```
   sudo python3 rpi2-check-last-db-update.py
   ```

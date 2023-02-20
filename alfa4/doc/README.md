## P2P DICTIONARY
Author: Tran Ngoc Tuan

Date: 19. 2. 2023

Contact: tranngoc@spsejecna.cz

School: SPSE Jecna

#
# About
This is a project for school.

This project simulates a p2p architecture.

# 
# Requirements
1. windown/linux
2. python compiler
3. putty/telnet

#
# Configuration
!The program is always listening on localhost on port 65532.

in the folder /config there are two files.

slovnik.txt = is for words and their translation.

ipAporty.txt = is for range of IP addresses and ports

# windows
you configure the two files in /config and run the alfa4/src/main.py and its done


# linux
you configure the two files in /config to your liking

After that you make configure it to run in the background

you make a new service file
```
sudo nano /lib/systemd/system/<name>.service
```

in the file write
```
[Unit]
Description=My Python script
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /path/to/my-script.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

after that reload the daemon and start you service

```
sudo systemctl daemon-reload
sudo systemctl start <name>.serivce
sudo systemctl status <name>.serivce
```
and its done

#
# Run program
in windown go to cmd and type 
```
python /path/to/script/main.py
```
afther that open putty and connect to the server
note: nothing should happen in the console after that

#

in linux if made as a daemon
```
systemctl start <name>.serivce
```
and if not as a daemon
```
python /path/to/script/main.py
```
and in new terminal open putty or telnet

#
# Controls
you run the program and start putty/tellnet
you connect to your server and send one of the 3 commands

1. TRANSLATEPING"something"
2. TRANSLATELOCL"word for translation"
3. TRANSLATESCAN"word for translation"


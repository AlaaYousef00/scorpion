import requests, sys
print("""
   _____  .__                  _____.___.                           _____ 
  /  _  \ |  | _____  _____    \__  |   | ____  __ __  ______ _____/ ____\
 /  /_\  \|  | \__  \ \__  \    /   |   |/  _ \|  |  \/  ___// __ \   __\ 
/    |    \  |__/ __ \_/ __ \_  \____   (  <_> )  |  /\___ \\  ___/|  |   
\____|__  /____(____  (____  /  / ______|\____/|____//____  >\___  >__|   
        \/          \/     \/   \/                        \/     \/       
   _____                           _               
  / ____|                         (_)              
 | (___    ___  ___   _ __  _ __   _   ___   _ __  
  \___ \  / __|/ _ \ | '__|| '_ \ | | / _ \ | '_ \ 
  ____) || (__| (_) || |   | |_) || || (_) || | | |
 |_____/  \___|\___/ |_|   | .__/ |_| \___/ |_| |_|
                           | |                     
                           |_|                    
""")

fo = input("###### enter your list : ")
fs = input("###### enter save list : ")
http = input('##### Enter protocol : ')
fc = open(fs, "w")
f = open(fo, "r")
frl = f.readlines()
for link in frl:
    if len(http) > 0:
        if len(link.strip()) != 0:
            link = http + "://" + link.strip()
        else:
            continue
    else:
        link = link.strip()
    try:
        r = requests.get(link, allow_redirects=True, timeout=5)
        if r.status_code == 200:
            print(r.url)
            fc.write(r.url + "\n")
        else:
            print(link+ "========incorrect subdomain")
    except (requests.ConnectionError, requests.TooManyRedirects, requests.exceptions.Timeout) as e:
        pass

f.close()
fc.close()
print("###################################\n ### finish process ### \n ###################################")

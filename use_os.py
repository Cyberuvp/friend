import socket
import os
import requests
import time
import platform

print(f'{"-"*80}')
def iseeverything():
    
    victim = input("enter website name ==> ")
    
    print(f"{victim}")
    print(f'{"-"*80}\n')

    try:
            print("DNSLOOKUP :\n")
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)
            



            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print("IPGEO :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)

            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+victim
            info = requests.get(subnet)
            print("SUBNET :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)



            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print("PAGELINK :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)

            zone = 'https://api.hackertarget.com/zonetransfer/?q='+victim
            info = requests.get(zone)
            print("ZONE :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)

            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print("HEADER :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)


            iplt = 'https://ipinfo.io/'+victim+'/json'
            info = requests.get(iplt)
            print("IPLT :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)

            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print("SHARED :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)


            robots ='http://'+victim+'/robots.txt'
            info = requests.get(robots)
            print("ROBOTS.TXT :\n")
            print('\033[91m',info.text)
            print(f'{"-"*80}\n')
            time.sleep(1)



            




    except socket.gaierror:
         
           print('Name or service not known!\033[93m')
           print()
           iseeverything()
    except UnboundLocalError:
         print('The information you entered is incorrect')
         print()
         iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
         print('?')
         print()
         iseeverything()
   


iseeverything()


            



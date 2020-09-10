from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<─────────────── v.1.2 ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m  786 => bismi-llāhir-raḥmānir-raḥīm')")
           print("\033[1;93m")
           print("  <───────[ Termux && Ringo ]───────>")
           print("")
           try:
                player_user = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                player_pwd = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if player_user == "admin" and player_pwd =="admin":
                   print('wait...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + player_user + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
menu()

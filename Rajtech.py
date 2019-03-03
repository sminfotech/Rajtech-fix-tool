import os
import sys
from time import sleep as timeout
from core.rajmcore import *
from core.deepmcore import *
from multiprocessing import Process


def menu():
    while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<─────────────── Rajtech tool 2.O ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m  OM => JaiMataDi')")
           print("\033[1;93m")
           print("  <───────[ Abhishek Mishra]───────>")
           print("")
           try:
  

>>CREATED BY: RajTech

>>Subscribe Rajtechhub<<
>>>Wellcom<<<

===============================================
1. Account Hacking
2. Information Gathering
3. Website Hacking
4. Termux
5. Error Fixer
6. Update
7. About
8. DeepStore
9. Generate Payload
================================================
10. EXIT
""", 'green'))

loop = True

while loop:
    menu()
    Rajtech = raw_input("Rajtech > ")
    
    if Rajtech == "1":
    	  os.system("clear")
          achacking() 
    elif Rajtech == "2":
    	  os.system("clear")
          info()
    elif Rajtech == "3":
    	  os.system("clear")
          webhacking()
    elif Rajtech == "4":
    	  os.system("clear")
    	  termux()
    elif Rajtech == "5":
    	  os.system("clear")
          Fix()
    elif Rajtech == "6":
          os.system("chmod +x update")
	  os.system("./update")
    elif Rajtech == "7":
          About()
    elif Rajtech == "8":
     	 os.system("clear")
         deepstore()
    elif Rajtech == "9":
    	 print (colored("under progress...", 'green'))
	 timeout(3)
         restartprogram()
    elif Rajtech == "10":
    	sys.exit()
    elif Rajtech == "0":
          restartprogram()
    else:
		  print  (colored("ERROR: WRONG COMMAND Bhai =.?", 'red'))
		  timeout(2)
		  restartprogram()

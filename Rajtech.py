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
    stark = raw_input("stark > ")
    
    if stark == "1":
    	  os.system("clear")
          achacking() 
    elif stark == "2":
    	  os.system("clear")
          info()
    elif stark == "3":
    	  os.system("clear")
          webhacking()
    elif stark == "4":
    	  os.system("clear")
    	  termux()
    elif stark == "5":
    	  os.system("clear")
          Fix()
    elif stark == "6":
          os.system("chmod +x update")
	  os.system("./update")
    elif stark == "7":
          About()
    elif stark == "8":
     	 os.system("clear")
         deepstore()
    elif stark == "9":
    	 print (colored("under progress...", 'green'))
	 timeout(3)
         restartprogram()
    elif stark == "10":
    	sys.exit()
    elif stark == "0":
          restartprogram()
    else:
		  print  (colored("ERROR: WRONG COMMAND Bhai =.?", 'red'))
		  timeout(2)
		  restartprogram()

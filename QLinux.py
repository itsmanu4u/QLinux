print('\n ==========================================================')
print('''\n
#    /$$$$$$  /$$       /$$                              
#   /$$__  $$| $$      |__/                              
#  | $$  \ $$| $$       /$$ /$$$$$$$  /$$   /$$ /$$   /$$
#  | $$  | $$| $$      | $$| $$__  $$| $$  | $$|  $$ /$$/
#  | $$  | $$| $$      | $$| $$  \ $$| $$  | $$ \  $$$$/ 
#  | $$/$$ $$| $$      | $$| $$  | $$| $$  | $$  >$$  $$ 
#  |  $$$$$$/| $$$$$$$$| $$| $$  | $$|  $$$$$$/ /$$/\  $$
#   \____ $$$|________/|__/|__/  |__/ \______/ |__/  \__/
#        \__/                                            
#                                                        
\n''')
print(' ============= Sometime Shortcuts Works Smart ==============  \n')

print('''\t "1" To update your System \t"2" Your system info \t "3" Check Rootkit/trojan/viruss \t"4" To check USB Devices\n
\t "0" To Go Back to Home Screen \t "10" To Quit \t''')

#program code starts here

import subprocess #for invoking system process
count = 0
while True:
	try:
		inu=int(input('\n\n Enter your number # '))
	
		if inu == 1:
			subprocess.call(["sudo", "apt-get", "update"])  #adding Commands to Invoked System process.
			continue
		elif inu == 2:
			subprocess.call(["lscpu"])
			continue
		elif inu == 3:
			subprocess.call(["chkrootkit"])
			continue
		elif inu == 4:
			subprocess.call(["lserrr"])
			continue
		elif inu == 0:
			subprocess.call(["clear"])
			subprocess.call(["python3", "QLinux.py"])
			continue
		elif inu == 10:
			print(' \n\n\t\t Good Bye...\n\n')
			break
		
		else:
			print('\n\nYou Enterd:',inu,' #Are Trying to be Oversmart Now?, Get Out!!\n\n')
			break
	except ValueError:
		
		print('You Didn\'t Enter Anything, My Friend!! \n')
		count += 1
		if count > 2:
			print('You didn\'t Enter anything',count,'TIMES ???','Nothing can Help YOU Lazy, Get Lost!!')
			break
		else:
			continue
	except KeyboardInterrupt:
		print("This Operating (Ctrl+C) is Not Allowed, My Friend")
	except EOFError:
		print("This Operating (Ctrl+D) is Not Allowed, My Friend")

	# End of program, Hope you like it buddy!




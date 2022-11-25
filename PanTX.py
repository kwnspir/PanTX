from os import system

while(True):
	try:
		from art import tprint
		tprint("This   is   PanTX   start   menu...")
	except:
		print("\n\nThis is PanTX start menu...\n\n")

	print("1. Info")
	print("2. Non OFDM")
	print("3. OFDM (bpsk, bpsk)")
	print("4. OFDM (bpsk, qpsk)")
	print("5. OFDM (bpsk, 8-psk)")
	print("6. OFDM (qpsk, bpsk)")
	print("7. OFDM (qpsk, qpsk)")
	print("8. OFDM (qpsk, 8-psk)")
	print("9. quit")
	x=int(input(""));
	if(x==1):
		#info
		pass
	elif(x==2):
		system('python3 ../PanTX_betaA/PanTX_betaA.py')
	elif(x==3):
		system('python3 ../PanTX_betaB/PanTX_betaB.py')
	elif(x==4):
		system('python3 ../PanTX_betaC/Pan_betaC.py')
	elif(x==5):
		system('python3 ../PanTX_betaD/PanTX_betaD.py')
	elif(x==6):
		system('python3 ../PanTX_betaE/PanTX_betaE.py')
	elif(x==7):
		system('python3 ../PanTX_betaF/PanTX_betaF.py')
	elif(x==8):
		system('python3 ../PanTX_betaG/PanTX_betaG.py')
	elif(x==9):
		quit()
	else:
		print("Error\n")

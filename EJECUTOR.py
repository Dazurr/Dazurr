import os
import threading


def per1 ():
	os.system("python perfil1.py")
	
def per2 ():
	os.system("python perfil2.py")
	
def per3 ():
	os.system("python perfil3.py")
	
def per4 ():
	os.system("python perfil4.py")
	
def per5 ():
	os.system("python perfil5.py")
	
def per6 ():
	os.system("python perfil6.py")
	
def per7 ():
	os.system("python perfil7.py")
	
	
threading.Thread(target=per1).start()

threading.Thread(target=per2).start()
			
threading.Thread(target=per3).start()

threading.Thread(target=per4).start()
			
threading.Thread(target=per5).start()
	
threading.Thread(target=per6).start()
							
threading.Thread(target=per7).start()
																																																											
																																																																																																																				
print("SCRIPT ACTIVADO")																																																																																																																																																																														
																																																																																																																																																																																																																																								
																																																																																																																																																																																																																																																																																																																																																												

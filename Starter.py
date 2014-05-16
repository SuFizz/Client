import os
if __name__ ==”__main__”:
	for i in range(10,51):
		os.system(“vncviewer 192.168.42.%s -p /home/pi/.vnc/passwd ”%i)

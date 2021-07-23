import time
from datetime import datetime as dt
import os

print(dt.now().hour)


websites_to_be_blocked = ['www.google.com','google.com','youtube.com','www.youtube.com']
origional_lines = "##" + "\n" + "# Host Database" + "\n" + "#" + "\n" + "# localhost is used to configure the loopback interface" + "\n" + "# when the system is booting.  Do not change this entry." + "\n" + "##" + "\n" + "127.0.0.1	localhost" +"\n" + "255.255.255.255	broadcasthost" + "\n" + "::1             localhost" 
file_path = "C:\\Windows\\System32\\drivers\\etc"
# temp_path = "/Users/mymac/Desktop/python_test/hosts"
temp_path = "C:\\Windows\\System32\\drivers\\etc1"
redirect = "127.0.0.1"
# os.system("touch "+temp_path)
with open(file_path,"r") as f:
	content = f.read()
	print(content)
	# lines_to_be_added = content + "\n"

while True:
	if dt.now().hour > 6 and dt.now().hour < 19:
		with open(file_path,"r") as f:
			content = f.read()
			# print(content)
			lines_to_be_added = content + "\n"
		for i in websites_to_be_blocked:
			if i not in content:
				lines_to_be_added = lines_to_be_added + redirect  + " " + i + "\n"
		with open(temp_path , "wt") as yoyo:
			# temp_line = yoyo.read()
			yoyo.write(lines_to_be_added)

	else:
		with open(temp_path , "wt") as yoyo:
			yoyo.write(origional_lines)


	os.system("sudo mv "+ temp_path + " " + file_path)

	time.sleep(5)





# import os

# os.system("sudo pip3 install pandas")
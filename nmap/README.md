# TryHackMe walkthrough

## Nmap

> _kblagoev | May 13, 2021_

----------------------------------------

### TASK 1. Deploy

<div align="center"><b>Press the green button to deploy the machine!</b></div><div align="center"><i>Please Note: This machine is for scanning purposes only. You do not need to log into it, or exploit any vulnerabilities to gain access.</i></div><div align="center"><i><br /></i></div><div align="center">If you are using the TryHackMe AttackBox then you will need to deploy this separately. <br /><i></i><br /></div>

----------------------------------------

### QUESTIONS:
5
----------------------------------------

1. Deploy the attached VM<br />

```
OK
```

----------------------------------------

### TASK 2. Introduction

<p>When it comes to hacking, knowledge is power. The more knowledge you have about a target system or network, the more options you have available. This makes it imperative that proper enumeration is carried out before any exploitation attempts are made.</p>
<p>Say we have been given an IP (or multiple IP addresses) to perform a security audit on. Before we do anything else, we need to get an idea of the “landscape” we are attacking. What this means is that we need to establish which services are running on the targets. For example, perhaps one of them is running a webserver, and another is acting as a Windows Active Directory Domain Controller. The first stage in establishing this “map” of the landscape is something called port scanning. When a computer runs a network service, it opens a networking construct called a “port” to receive the connection.  Ports are necessary for making multiple network requests or having multiple services available. For example, when you load several webpages at once in a web browser, the program must have some way of determining which tab is loading which web page. This is done by establishing connections to the remote webservers using different ports on your local machine. Equally, if you want a server to be able to run more than one service (for example, perhaps you want your webserver to run both HTTP and HTTPS versions of the site), then you need some way to direct the traffic to the appropriate service. Once again, ports are the solution to this. Network connections are made between two ports – an open port listening on the server and a randomly selected port on your own computer. For example, when you connect to a web page, your computer may open port 49534 to connect to the server’s port 443.</p>
<p><img src="https://i.imgur.com/3XAfRpI.png" alt /></p>
<p>As in the previous example, the diagram shows what happens when you connect to numerous websites at the same time. Your computer opens up a different, high-numbered port (at random), which it uses for all its communications with the remote server.</p>
<p>Every computer has a total of 65535 available ports; however, many of these are registered as standard ports. For example, a HTTP Webservice can nearly always be found on port 80 of the server. A HTTPS Webservice can be found on port 443. Windows NETBIOS can be found on port 139 and SMB can be found on port 445. It is important to note; however, that especially in a CTF setting, it is not unheard of for even these standard ports to be altered, making it even more imperative that we perform appropriate enumeration on the target.</p>
<p>If we do not know which of these ports a server has open, then we do not have a hope of successfully attacking the target; thus, it is crucial that we begin any attack with a port scan. This can be accomplished in a variety of ways – usually using a tool called nmap, which is the focus of this room. Nmap can be used to perform many different kinds of port scan – the most common of these will be introduced in upcoming tasks; however, the basic theory is this: nmap will connect to each port of the target in turn. Depending on how the port responds, it can be determined as being open, closed, or filtered (usually by a firewall). Once we know which ports are open, we can then look at enumerating which services are running on each port – either manually, or more commonly using nmap.</p>
<p>So, why nmap? The short answer is that it's currently the industry standard for a reason: no other port scanning tool comes close to matching its functionality (although some newcomers are now matching it for speed). It is an extremely powerful tool – made even more powerful by its scripting engine which can be used to scan for vulnerabilities, and in some cases even perform the exploit directly! Once again, this will be covered more in upcoming tasks.</p>
<p>For now, it is important that you understand: what port scanning is; why it is necessary; and that nmap is the tool of choice for any kind of initial enumeration.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What networking constructs are used to direct traffic to the right application on a server?</p>


```
Ports
```

2. <p>How many of these are available on any network-enabled computer?</p>


```
65535
```

3. <p><strong>[Research]</strong> How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)</p>


```
1024
```

----------------------------------------

### TASK 3. Nmap Switches

<p>Like most pentesting tools, nmap is run from the terminal. There are versions available for both Windows and Linux. For this room we will assume that you are using Linux; however, the switches should be identical. Nmap is installed by default in both Kali Linux and the <a href="https://tryhackme.com/my-machine">TryHackMe Attack Box.</a></p>
<p>Nmap can be accessed by typing <code>nmap</code> into the terminal command line, followed by some of the "switches" (command arguments which tell a program to do different things) we will be covering below.</p>
<p>All you'll need for this is the help menu for nmap (accessed with <code>nmap -h</code>) and/or the nmap man page (access with <code>man nmap</code>). For each answer, include all parts of the switch unless otherwise specified. This includes the hyphen at the start (<code>-</code>).</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?</p>


```
-sS
```

2. <p>Which switch would you use for a "UDP scan"?</p>


```
-sU
```

3. <p>If you wanted to detect which operating system the target is running on, which switch would you use?</p>


```
-O
```

4. <p>Nmap provides a switch to detect the version of the services running on the target. What is this switch?</p>


```
-sV
```

5. <p>The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?</p>


```
-v
```

6. <p>Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?<br />
(<strong>Note</strong>: it's highly advisable to always use <em>at least</em> this option)</p>


```
-vv
```

7. <p>We should always save the output of our scans -- this means that we only need to run the scan once (reducing network traffic and thus chance of detection), and gives us a reference to use when writing reports for clients.</p>
<p>What switch would you use to save the nmap results in three major formats?</p>


```
-oA
```

8. <p>What switch would you use to save the nmap results in a "normal" format?</p>


```
-oN
```

9. <p>A very useful output format: how would you save results in a "grepable" format?</p>


```
-oG
```

10. <p>Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning.</p>
<p>How would you activate this setting?</p>


```
-A
```

11. <p>Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors!</p>
<p>How would you set the timing template to level 5?</p>


```
-T5
```

12. <p>We can also choose which port(s) to scan.</p>
<p>How would you tell nmap to only scan port 80?</p>


```
-p 80
```

13. <p>How would you tell nmap to scan ports 1000-1500?</p>


```
-p 1000-1500
```

14. <p>A very useful option that should not be ignored:</p>
<p>How would you tell nmap to scan <em>all</em> ports?</p>


```
-p-
```

15. <p>How would you activate a script from the nmap scripting library (lots more on this later!)?</p>


```
--script
```

16. <p>How would you activate all of the scripts in the "vuln" category?</p>


```
--script=vuln
```

----------------------------------------

### TASK 4. <span class="badge badge-soft-info size-16">Scan Types</span> Overview

<p>When port scanning with Nmap, there are three basic scan types. These are:</p>
<ul>
<li>TCP Connect Scans (<code>-sT</code>)</li>
<li>SYN "Half-open" Scans (<code>-sS</code>)</li>
<li>UDP Scans (<code>-sU</code>)</li>
</ul>
<p>Additionally there are several less common port scan types, some of which we will also cover (albeit in less detail). These are:</p>
<ul>
<li>TCP Null Scans (<code>-sN</code>)</li>
<li>TCP FIN Scans (<code>-sF</code>)</li>
<li>TCP Xmas Scans (<code>-sX</code>)</li>
</ul>
<p>Most of these (with the exception of UDP scans) are used for very similar purposes, however, the way that they work differs between each scan. This means that, whilst one of the first three scans are likely to be your go-to in most situations, it's worth bearing in mind that other scan types exist.</p>
<p>In terms of network scanning, we will also look briefly at ICMP (or "ping") scanning.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the Scan Types Introduction.</p>


```
OK
```

----------------------------------------

### TASK 5. <span class="badge badge-soft-info size-16">Scan Types</span> TCP Connect Scans

<p>To understand TCP Connect scans (<code>-sT</code>), it's important that you're comfortable with the <em>TCP three-way handshake</em>. If this term is new to you then completing <a href="https://tryhackme.com/room/introtonetworking">Introductory Networking</a> before continuing would be advisable.</p>
<p>As a brief recap, the three-way handshake consists of three stages. First the connecting terminal (our attacking machine, in this instance) sends a TCP request to the target server with the SYN flag set. The server then acknowledges this packet with a TCP response containing the SYN flag, as well as the ACK flag. Finally, our terminal completes the handshake by sending a TCP request with the ACK flag set.<br />
<img style="float:left;padding:20px;width:300px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-2.png" alt /><br />
<img src="https://i.imgur.com/ngzBWID.png" alt /></p>
<p>This is one of the fundamental principles of TCP/IP networking, but how does it relate to Nmap?</p>
<p>Well, as the name suggests, a TCP Connect scan works by performing the three-way handshake with each target port in turn. In other words, Nmap tries to connect to each specified TCP port, and determines whether the service is open by the response it receives.</p>
<hr />
<p>For example, if a port is closed, <a href="https://tools.ietf.org/html/rfc793">RFC 793</a> states that:</p>
<p><em>"... If the connection does not exist (CLOSED) then a reset is sent in response to any incoming segment except another reset.  In particular, SYNs addressed to a non-existent connection are rejected by this means."</em></p>
<p>In other words, if Nmap sends a TCP request with the <em>SYN</em> flag set to a <b><em>closed</em></b> port, the target server will respond with a TCP packet with the <em>RST</em> (Reset) flag set. By this response, Nmap can establish that the port is closed.</p>
<p><img src="https://i.imgur.com/vUQL9SK.png" alt /></p>
<p>If, however, the request is sent to an <em>open</em> port, the target will respond with a TCP packet with the SYN/ACK flags set. Nmap then marks this port as being <em>open</em> (and completes the handshake by sending back a TCP packet with ACK set).</p>
<hr />
<p>This is all well and good, however, there is a third possibility.</p>
<p>What if the port is open, but hidden behind a firewall?</p>
<p>Many firewalls are configured to simply <strong>drop</strong> incoming packets. Nmap sends a TCP SYN request, and receives nothing back. This indicates that the port is being protected by a firewall and thus the port is considered to be <em>filtered</em>.</p>
<p>That said, it is very easy to configure a firewall to respond with a RST TCP packet. For example, in IPtables for Linux, a simple version of the command would be as follows:</p>
<p><code>iptables -I INPUT -p tcp --dport &lt;port&gt; -j REJECT --reject-with tcp-reset</code></p>
<p>This can make it extremely difficult (if not impossible) to get an accurate reading of the target(s).</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Which RFC defines the appropriate behaviour for the TCP protocol?</p>


```
RFC 793
```

2. <p>If a port is closed, which flag should the server send back to indicate this?</p>


```
RST
```

----------------------------------------

### TASK 6. <span class="badge badge-soft-info size-16">Scan Types</span> SYN Scans

<p>As with TCP scans, SYN scans (<code>-sS</code>) are used to scan the TCP port-range of a target or targets; however, the two scan types work slightly differently. SYN scans are sometimes referred to as "<i>Half-open" </i>scans, or <i>"Stealth"</i> scans.<br /></p><p>Where TCP scans perform a full three-way handshake with the target, SYN scans sends back a RST TCP packet after receiving a SYN/ACK from the server (this prevents the server from repeatedly trying to make the request). In other words, the sequence for scanning an <b>open</b> port looks like this:</p><p><img style="width:272px" src="https://i.imgur.com/cPzF0kU.png" /></p><p><img style="width:1076px" src="https://i.imgur.com/bcgeZmI.png" /><br /></p><p></p><p>This has a variety of advantages for us as hackers:</p><ul><li>It can be used to bypass older Intrusion Detection systems as they are looking out for a full three way handshake. This is often no longer the case with modern IDS solutions; it is for this reason that SYN scans are still frequently referred to as "stealth" scans. </li><li>SYN scans are often not logged by applications listening on open ports, as standard practice is to log a connection once it's been fully established. Again, this plays into the idea of SYN scans being stealthy.</li><li>Without having to bother about completing (and disconnecting from) a three-way handshake for every port, SYN scans are significantly faster than a standard TCP Connect scan.</li></ul><p>There are, however, a couple of disadvantages to SYN scans, namely:</p><ul><li>They require sudo permissions<sup>[1]</sup> in order to work correctly in Linux. This is because SYN scans require the ability to create raw packets (as opposed to the full TCP handshake), which is a privilege only the root user has by default. </li><li>Unstable services are sometimes brought down by SYN scans, which could prove problematic if a client has provided a production environment for the test.</li></ul><p>All in all, the pros outweigh the cons.</p><p>For this reason, SYN scans are the default scans used by Nmap <i>if run with sudo permissions</i>. If run <b>without</b> sudo permissions, Nmap defaults to the TCP Connect scan we saw in the previous task.</p><hr /><p>When using a SYN scan to identify closed and filtered ports, the exact same rules as with a TCP Connect scan apply.</p><p>If a port is closed then the server responds with a RST TCP packet. If the port is filtered by a firewall then the TCP SYN packet is either dropped, or spoofed with a TCP reset.</p><p>In this regard, the two scans are identical: the big difference is in how they handle <i>open</i> ports.</p><hr /><p>[1] SYN scans can also be made to work by giving Nmap the CAP_NET_RAW, CAP_NET_ADMIN and CAP_NET_BIND_SERVICE capabilities; however, this may not allow many of the NSE scripts to run properly.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. There are two other names for a SYN scan, what are they?<br />

```
Half-Open, Stealth
```

2. <p>Can Nmap use a SYN scan without Sudo permissions (Y/N)?<br /></p>

```
N
```

----------------------------------------

### TASK 7. <span class="badge badge-soft-info size-16">Scan Types</span> UDP Scans

<p>Unlike TCP, UDP connections are <i>stateless</i>. This means that, rather than initiating a connection with a back-and-forth "handshake", UDP connections rely on sending packets to a target port and essentially hoping that they make it. This makes UDP superb for connections which rely on speed over quality (e.g. video sharing), but the lack of acknowledgement makes UDP significantly more difficult (and much slower) to scan. The switch for an Nmap UDP scan is (<code>-sU</code>)<br /></p><p>When a packet is sent to an open UDP port, there should be no response. When this happens, Nmap refers to the port as being <code>open|filtered</code>. In other words, it suspects that the port is open, but it could be firewalled. If it gets a UDP response (which is very unusual), then the port is marked as <i>open</i>. More commonly there is no response, in which case the request is sent a second time as a double-check. If there is still no response then the port is marked <i>open|filtered</i> and Nmap moves on.<br /></p><p>When a packet is sent to a <i>closed</i> UDP port, the target should respond with an ICMP (ping) packet containing a message that the port is unreachable. This clearly identifies closed ports, which Nmap marks as such and moves on.<br /></p><hr /><p>Due to this difficulty in identifying whether a UDP port is actually open, UDP scans tend to be incredibly slow in comparison to the various TCP scans (in the region of 20 minutes to scan the first 1000 ports, with a good connection). For this reason it's usually good practice to run an Nmap scan with <code>--top-ports &lt;number&gt;</code> enabled. For example, scanning with  <code>nmap -sU --top-ports 20 &lt;target&gt;</code>. Will scan the top 20 most commonly used UDP ports, resulting in a much more acceptable scan time.</p><hr /><p>When scanning UDP ports, Nmap usually sends completely empty requests -- just raw UDP packets. That said, for ports which are usually occupied by well-known services, it will instead send a protocol-specific payload which is more likely to elicit a response from which a more accurate result can be drawn.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. If a UDP port doesn't respond to an Nmap scan, what will it be marked as?<br />

```
open|filtered
```

2. <p>When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?<br /></p>

```
ICMP
```

----------------------------------------

### TASK 8. <span class="badge badge-soft-info size-16">Scan Types</span> NULL, FIN and Xmas

<p>NULL, FIN and Xmas TCP port scans are less commonly used than any of the others we've covered already, so we will not go into a huge amount of depth here. All three are interlinked and are used primarily as they tend to be even stealthier, relatively speaking, than a SYN "stealth" scan. Beginning with NULL scans:</p><ul><li>As the name suggests, NULL scans (<code>-sN</code>) are when the TCP request is sent with no flags set at all. As per the RFC, the target host should respond with a RST if the port is closed.<br /><img style="width:1020px" src="https://i.imgur.com/ABCxAwf.png" /><br /><br /><br /><br /><br /></li><li>FIN scans (<code>-sF</code>) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a RST if the port is closed.<br /><img style="width:1017px" src="https://i.imgur.com/gIzKbEk.png" /><br /><br /><br /><br /><br /></li><li>As with the other two scans in this class, Xmas scans (<code>-sX</code>) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark. <br /><img style="width:1076px" src="https://i.imgur.com/gKVkGug.png" /><br /></li></ul><p><br /></p><p><br /></p><p>The expected response for <i>open</i> ports with these scans is also identical, and is very similar to that of a UDP scan. If the port is open then there is no response to the malformed packet. Unfortunately (as with open UDP ports), that is <i>also </i>an expected behaviour if the port is protected by a firewall, so NULL, FIN and Xmas scans will only ever identify ports as being <i>open|filtered</i>, <i>closed</i>, or <i>filtered</i>. If a port is identified as filtered with one of these scans then it is usually because the target has responded with an ICMP unreachable packet.<br /></p><p>It's also worth noting that while RFC 793 mandates that network hosts respond to malformed packets with a RST TCP packet for closed ports, and don't respond at all for open ports; this is not always the case in practice. In particular Microsoft Windows (and a lot of Cisco network devices) are known to respond with a RST to any malformed TCP packet -- regardless of whether the port is actually open or not. This results in all ports showing up as being closed.<br /></p><p>That said, the goal here is, of course, firewall evasion. Many firewalls are configured to drop incoming TCP packets to blocked ports which have the SYN flag set (thus blocking new connection initiation requests). By sending requests which do not contain the SYN flag, we effectively bypass this kind of firewall. Whilst this is good in theory, most modern IDS solutions are savvy to these scan types, so don't rely on them to be 100% effective when dealing with modern systems.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Which of the three shown scan types uses the URG flag?<br />

```
xmas
```

2. <p>Why are NULL, FIN and Xmas scans generally used?<br /></p>

```
Firewall Evasion
```

3. <p>Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?<br /></p>

```
Microsoft Windows
```

----------------------------------------

### TASK 9. <span class="badge badge-soft-info size-16">Scan Types</span> ICMP Network Scanning

<p>On first connection to a target network in a black box assignment, our first objective is to obtain a "map" of the network structure -- or, in other words, we want to see which IP addresses contain active hosts, and which do not.</p><p>One way to do this is by using Nmap to perform a so called "ping sweep". This is exactly as the name suggests: Nmap sends an ICMP packet to each possible IP address for the specified network. When it receives a response, it marks the IP address that responded as being alive. For reasons we'll see in a later task, this is not always accurate; however, it can provide something of a baseline and thus is worth covering.</p><p>To perform a ping sweep, we use the <code>-sn</code> switch in conjunction with IP ranges which can be specified with either a hypen (<code>-</code>) or CIDR notation. i.e. we could scan the <code>192.168.0.x</code> network using:</p><ul><li><code>nmap -sn 192.168.0.1-254</code></li></ul><p>or</p><ul><li><code>nmap -sn 192.168.0.0/24</code></li></ul><p><br /></p><p>The <code>-sn</code> switch tells Nmap not to scan any ports -- forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network, if run with sudo or directly as the root user) to identify targets. In addition to the ICMP echo requests, the <code>-sn</code> switch will also cause nmap to send a TCP SYN packet to port 443 of the target, as well as a TCP ACK (or TCP SYN if not run as root) packet to port 80 of the target.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)<br />

```
nmap -sn 172.16.0.0/16
```

----------------------------------------

### TASK 10. <span class="badge badge-soft-warning size-16">NSE Scripts</span> Overview

<p>The <b>N</b>map <b>S</b>cripting <b>E</b>ngine (NSE) is an incredibly powerful addition to Nmap, extending its functionality quite considerably. NSE Scripts are written in the <i>Lua </i>programming language, and can be used to do a variety of things: from scanning for vulnerabilities, to automating exploits for them. The NSE is particularly useful for reconnaisance, however, it is well worth bearing in mind how extensive the script library is.</p><p>There are many categories available. Some useful categories include:</p><ul><li><code>safe</code>:- Won't affect the target</li><li><code>intrusive</code>:- Not safe: likely to affect the target<br /></li><li><code>vuln</code>:- Scan for vulnerabilities</li><li><code>exploit</code>:- Attempt to exploit a vulnerability</li><li><code>auth</code>:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)</li><li><code>brute</code>:- Attempt to bruteforce credentials for running services</li><li><code>discovery</code>:- Attempt to query running services for further information about the network (e.g. query an SNMP server).</li></ul><p>A more exhaustive list can be found <a href="https://nmap.org/book/nse-usage.html" target="_blank">here</a>.</p><p>In the next task we'll look at how to interact with the NSE and make use of the scripts in these categories. <br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What language are NSE scripts written in?<br />

```
Lua
```

2. <p>Which category of scripts would be a <i>very</i> bad idea to run in a production environment?<br /></p>

```
intrusive
```

----------------------------------------

### TASK 11. <span class="badge badge-soft-warning size-16">NSE Scripts</span> Working with the NSE

<p>In Task 3 we looked very briefly at the <code>--script</code> switch for activating NSE scripts from the <code>vuln</code> category using <code>--script=vuln</code>. It should come as no surprise that the other categories work in exactly the same way. If the command <code>--script=safe</code> is run, then any applicable safe scripts will be run against the target (Note: only scripts which target an active service will be activated).</p>
<hr />
<p>To run a specific script, we would use <code>--script=&lt;script-name&gt; </code> , e.g. <code>--script=http-fileupload-exploiter</code>.</p>
<p>Multiple scripts can be run simultaneously in this fashion by separating them by a comma. For example: <code>--script=smb-enum-users,smb-enum-shares</code>.</p>
<p>Some scripts require arguments (for example, credentials, if they're exploiting an authenticated vulnerability). These can be given with the <code>--script-args</code> Nmap switch. An example of this would be with the <code>http-put</code> script (used to upload files using the PUT method). This takes two arguments: the URL to upload the file to, and the file's location on disk.  For example:</p>
<p><code>nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'</code></p>
<p>Note that the arguments are separated by commas, and connected to the corresponding script with periods (i.e.  <code>&lt;script-name&gt;.&lt;argument&gt;</code>).</p>
<p>A full list of scripts and their corresponding arguments (along with example use cases) can be found <a href="https://nmap.org/nsedoc/">here</a>.</p>
<hr />
<p>Nmap scripts come with built-in help menus, which can be accessed using <code>nmap --script-help &lt;script-name&gt;</code>. This tends not to be as extensive as in the link given above, however, it can still be useful when working locally.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What optional argument can the <code>ftp-anon.nse</code> script take?</p>


```
maxlist
```

----------------------------------------

### TASK 12. <span class="badge badge-soft-warning size-16">NSE Scripts</span> Searching for Scripts

<p></p><p>Ok, so we know how to use the scripts in Nmap, but we don't yet know how to <i>find</i> these scripts.</p><p>We have two options for this, which should ideally be used in conjunction with each other. The first is the page on the <a href="https://nmap.org/nsedoc/" target="_blank">Nmap website</a> (mentioned in the previous task) which contains a list of all official scripts. The second is the local storage on your attacking machine. Nmap stores its scripts on Linux at <code>/usr/share/nmap/scripts</code>. All of the NSE scripts are stored in this directory by default -- this is where Nmap looks for scripts when you specify them. </p><p>There are two ways to search for installed scripts. One is by using the <code>/usr/share/nmap/scripts/script.db</code> file. Despite the extension, this isn't actually a database so much as a formatted text file containing filenames and categories for each available script.</p><p><img style="width:729px" src="https://i.imgur.com/aJdVSAP.png" /><br /></p><p> Nmap uses this file to keep track of (and utilise) scripts for the scripting engine; however, we can also <i>grep </i>through it to look for scripts. For example: <code>grep "ftp" /usr/share/nmap/scripts/script.db</code>.<br /></p><p><img style="width:928px" src="https://i.imgur.com/ijAhZsy.png" /><br /></p><p>The second way to search for scripts is quite simply to use the <code>ls</code> command. For example, we could get the same results as in the previous screenshot by using <code>ls -l /usr/share/nmap/scripts/*ftp*</code>:</p><p><img style="width:728px" src="https://i.imgur.com/7GV9Wzi.png" /><br /></p><p><i>Note the use of asterisks</i> (<code>*</code>) <i>on either side of the search term</i></p><p>The same techniques can also be used to search for categories of script. For example:<br /><code>grep "safe" /usr/share/nmap/scripts/script.db</code><br /></p><p><img style="width:766px" src="https://i.imgur.com/352GgTj.png" /><br /></p><p></p><hr /><p><u><i>Installing New Scripts</i></u></p><p>We mentioned previously that the Nmap website contains a list of scripts, so, what happens if one of these is missing in the <code>scripts</code> directory locally? A standard <code>sudo apt update &amp;&amp; sudo apt install nmap</code> should fix this; however, it's also possible to install the scripts manually by downloading the script from Nmap (<code>sudo wget -O /usr/share/nmap/scripts/&lt;script-name&gt;.nse https://svn.nmap.org/nmap/scripts/&lt;script-name&gt;.nse</code>). This must then be followed up with <code>nmap --script-updatedb</code>, which updates the <code>script.db</code> file to contain the newly downloaded script.</p><p>It's worth noting that you would require the same "updatedb" command if you were to make your own NSE script and add it into Nmap -- a more than manageable task with some basic knowledge of Lua! <br /></p><p></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Search for "smb" scripts in the <code>/usr/share/nmap/scripts/</code> directory using either of the demonstrated methods. <br />What is the filename of the script which determines the underlying OS of the SMB server?<br />

```
smb-os-discovery.nse
```

2. <p>Read through this script. What does it depend on?<br /></p>

```
smb-brute
```

----------------------------------------

### TASK 13. Firewall Evasion

<p>We have already seen some techniques for bypassing firewalls (think stealth scans, along with NULL, FIN and Xmas scans); however, there is another very common firewall configuration which it's imperative we know how to bypass.</p><p>Your typical Windows host will, with its default firewall, block all ICMP packets. This presents a problem: not only do we often use <i>ping</i> to manually establish the activity of a target, Nmap does the same thing by default. This means that Nmap will register a host with this firewall configuration as dead and not bother scanning it at all. </p><p>So, we need a way to get around this configuration. Fortunately Nmap provides an option for this: <code>-Pn</code>, which tells Nmap to not bother pinging the host before scanning it. This means that Nmap will always treat the target host(s) as being alive, effectively bypassing the ICMP block; however, it comes at the price of potentially taking a very long time to complete the scan (if the host really is dead then Nmap will still be checking and double checking every specified port). </p><p>It's worth noting that if you're already directly on the local network, Nmap can also use ARP requests to determine host activity. </p><hr /><p>There are a variety of other switches which Nmap considers useful for firewall evasion. We will not go through these in detail, however, they can be found <a href="https://nmap.org/book/man-bypass-firewalls-ids.html" target="_blank">here</a>.</p><p>The following switches are of particular note:</p><ul><li><code>-f</code>:- Used to fragment the packets (i.e. split them into smaller pieces) making it less likely that the packets will be detected by a firewall or IDS. </li><li>An alternative to <code>-f</code>, but providing more control over the size of the packets: <code>--mtu &lt;number&gt;</code>, accepts a maximum transmission unit size to use for the packets sent. This <i>must</i> be a multiple of 8.</li><li><code>--scan-delay &lt;time&gt;ms</code>:- used to add a delay between packets sent. This is very useful if the network is unstable, but also for evading any time-based firewall/IDS triggers which may be in place.</li><li><code>--badsum</code>:- this is used to generate in invalid checksum for packets. Any real TCP/IP stack would drop this packet, however, firewalls may potentially respond automatically, without bothering to check the checksum of the packet. As such, this switch can be used to determine the presence of a firewall/IDS.<br /></li></ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the <code>-Pn</code> switch?<br />

```
ICMP
```

2. <p><b>[Research]</b> Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?<br /></p>

```
--data-length
```

----------------------------------------

### TASK 14. Practical

<p align="center">Use what you've learnt to scan the target machine and answer the following questions!</p><p align="center">(<b>Note:</b> If you're not a subscriber, make sure that this machine has had around ten minutes to start)<br /></p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Does the target (<code>MACHINE_IP</code>)respond to ICMP (ping) requests (Y/N)?</p>


```
N
```

2. <p>Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?</p>


```
999
```

3. <p>There is a reason given for this -- what is it?</p>
<p><strong>Note:</strong> The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!</p>


```
No Response
```

4. <p>Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?</p>


```
5
```

5. <p>Open Wireshark (see <a href="https://tryhackme.com/p/Cryillic">Cryillic's</a> <a href="https://tryhackme.com/room/wireshark">Wireshark Room</a> for instructions) and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on.</p>


```
OK
```

6. <p>Deploy the <code>ftp-anon</code> script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)</p>


```
Y
```

----------------------------------------

### TASK 15. Conclusion

<p>You have now completed the Further Nmap room -- hopefully you enjoyed it, and learnt something new!</p><p>There are lots of great resources for learning more about Nmap on your own. Front and center are Nmaps own (highly extensive) <a href="https://nmap.org/book/" target="_blank">docs</a> which have already been mentioned several times throughout the room. These are a superb resource, so, whilst reading through them line-by-line and learning them by rote is entirely unnecessary, it would be highly advisable to use them as a point of reference, should you need it.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the conclusion.<br />

```
OK
```


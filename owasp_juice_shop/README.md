# TryHackMe walkthrough

## OWASP Juice Shop

> _kblagoev | May 13, 2021_

----------------------------------------

### TASK 1. Open for business!

<p style="text-align:center">Within this room, we will look at <a href="https://owasp.org/www-project-top-ten/" target="_blank">OWASP's TOP 10 vulnerabilities</a> in web applications. You will find these in all types in all types of web applications. But for today we will be looking at OWASP's own creation, Juice Shop!<br /></p><p style="text-align:center"><img src="https://i.imgur.com/vjfcwid.png" style="width:126px;height:151.2px" /><br /></p><p style="text-align:center"><i>We will be using Burp Suite, so if you haven't already got it set up, here is a link to the '</i><span style="text-align:left"><i><a href="https://tryhackme.com/room/rpburpsuite" target="_blank">Burp Suite</a></i></span><i>' room.</i></p><p style="text-align:center"><u>[The <span style="font-size:1rem">'</span><span style="font-size:1rem;text-align:left"><a href="https://tryhackme.com/room/rpburpsuite" target="_blank">Burp Suite</a></span><span style="font-size:1rem">' room is a <b>subscriber-only room</b>, meaning you will require a TryHackMe subscription in order to access it]</span></u></p><p style="text-align:center"><i>In addition, it's highly recommended to check out the '<a href="https://tryhackme.com/room/webfundamentals" target="_blank">Web Fundamentals</a>' room. </i></p><p style="text-align:center"><u>[The '<a href="https://tryhackme.com/room/webfundamentals" target="_blank">Web Fundamentals</a>' room<span style="font-size:1rem"> is a<b> free room</b>, meaning that, like this room, anyone is able to complete it]</span></u><i><br /></i></p><p style="text-align:center">Juice Shop is a large application so we will not be covering every topic from the top 10.<br /></p><p style="text-align:center">We will, however, cover the following topics which we recommend you take a look at as you progress through this room.</p><p style="text-align:center">&lt;-------------------------------------------------&gt;</p><p style="text-align:center"><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection" target="_blank">Injection</a></p><p style="text-align:center"><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A2-Broken_Authentication" target="_blank">Broken Authentication</a></p><p style="text-align:center"><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A3-Sensitive_Data_Exposure" target="_blank">Sensitive Data Exposure</a></p><p style="text-align:center"><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A5-Broken_Access_Control" target="_blank">Broken Access Control</a></p><p style="text-align:center"><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A7-Cross-Site_Scripting_(XSS)" target="_blank">Cross-Site Scripting XSS</a></p><p style="text-align:center">&lt;-------------------------------------------------&gt;</p><p style="text-align:center"><b>[Task 3] and onwards will require a flag, which will be displayed on completion of the task.</b></p><p style="text-align:center"><img src="https://i.imgur.com/t4KAlh2.png" style="width:930px;height:188.893px" /><b><br /></b></p><p style="text-align:center"><b><span style="font-size:24px"><u><br /></u></span></b></p><p style="text-align:center"><b><span style="font-size:24px"><u>Troubleshooting</u></span></b></p><p style="text-align:center">Temporarily disable burp in your proxy settings for the current browser. Refresh the page and the flag will be shown. </p><p style="text-align:center"><i>This is not an issue with the application but an issue with burp stopping the flag from being shown.</i> <br /></p><p style="text-align:center">If you are doing the XSS Tasks and they are not working. Clear your cookies and site data, as this can sometimes be an issue. </p><p style="text-align:center">If you are sure that you have completed the task but it's still not working. Go to <b>[Task 8]</b>, as this will allow you to check its completion.</p><p style="text-align:center"><br /></p><p style="text-align:center"><i><span style=";text-align:left">Credits to </span><a href="https://www.owasp.org/index.php/Main_Page">OWASP</a><span style=";text-align:left"> and </span><a href="https://twitter.com/bkimminich">Bjorn Kimminich</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Deploy the VM attached to this task to get started! You can access this machine by using your <a href="https://tryhackme.com/my-machine" target="_blank">browser-based machine</a>, or if you're connected through <a href="https://tryhackme.com/access" target="_blank">OpenVPN</a>.

```
OK
```

2. <p>Once the machine has loaded, access it by copying and pasting its IP into your browser; if you're using the browser-based machine, paste the machines IP into a browser on that machine.</p>

```
OK
```

----------------------------------------

### TASK 2. Let's go on an adventure!

<p style="text-align:center">             <img src="https://i.imgur.com/7R1O1CF.png" style="width:785px;height:438.49px" /><br /></p><p>Before we get into the actual hacking part, it's good to have a look around. In Burp, set the Intercept mode to off and then browse around the site. This allows Burp to log different requests from the server that may be helpful later. </p><p style="text-align:center">This is called <b>walking through</b> the application, which is also a form of <b>reconnaissance</b>!</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p><span style="background-;;font-weight:bolder;text-align:center;font-size:1rem">Question #1: What's the Administrator's email address?</span></p><p style="text-align:center"><img src="https://i.imgur.com/hPXolAn.png" style="width:639px" /><span style="background-;;font-weight:bolder;text-align:center;font-size:1rem"></span></p><p style="text-align:center">The reviews show each user's email address. Which, by clicking on the Apple Juice product, shows us the Admin email!</p><p style="text-align:center"><img src="https://i.imgur.com/YFWDP5v.png" style="width:493px" /></p>

```
admin@juice-sh.op
```

2. <p><b style=";background-;text-align:center;font-size:1rem">Question #2: What parameter is used for searching? </b></p><p style="text-align:center"><img src="https://i.imgur.com/pZLtWQl.png" style="width:223px" /></p><p style="text-align:center">Click on the magnifying glass in the top right of the application will pop out a search bar.</p><p style="text-align:center"><img src="https://i.imgur.com/bFgw6uS.png" style="width:256px" /></p><p style="text-align:center">We can then input some text and by pressing <b>Enter</b> will search for the text which was just inputted.</p><p style="text-align:center">Now pay attention to the URL which will now update with the text we just entered.</p><p style="text-align:center"><img src="https://i.imgur.com/AzJ3FAM.png" style="width:273px" /></p><p style="text-align:center">We can now see the search parameter after the <b>/#/search? </b>the letter <b>q</b></p>

```
q
```

3. <p><span style="background-;;font-size:1rem;font-weight:bolder;text-align:center">Question #3: What show does Jim reference in his review? </span><br /></p><p style="text-align:center">Jim did a review on the Green Smoothie product. We can see that he mentions a replicator. </p><p style="text-align:center"><img src="https://i.imgur.com/RCFw2tB.png" style="width:367.362px;height:376.25px" /></p><p style="text-align:center">If we google "<b>replicator</b>" we will get the results indicating that it is from a TV show called Star Trek</p><p style="text-align:center"><img src="https://i.imgur.com/Sp8ymGR.png" style="width:553px" /></p>

```
Star Trek
```

----------------------------------------

### TASK 3. Inject the juice

<p style="text-align:center;"><img src="https://i.imgur.com/uwXqDdH.png" style="width:705.004px;height:429.063px" /><br /></p><p style="text-align:center;">This task will be focusing on injection vulnerabilities. Injection vulnerabilities are quite dangerous to a company as they can potentially cause downtime and/or loss of data. Identifying injection points within a web application is usually quite simple, as most of them will return an error. There are many types of injection attacks, some of them are:</p><table class="table table-bordered"><tbody><tr><td><span style="font-weight:700;text-align:left">SQL Injection</span><br /></td><td><span style="text-align:left">SQL Injection is when an attacker enters a malicious or malformed query to either retrieve or tamper data from a database. And in some cases, log into accounts.</span><br /></td></tr><tr><td><span style="font-weight:700;text-align:left">Command Injection</span><br /></td><td><span style="text-align:left">Command Injection is when web applications take input or user-controlled data and run them as system commands. An attacker may tamper with this data to execute their own system commands. This can be seen in applications that perform misconfigured ping tests. </span><br /></td></tr><tr><td><span style="font-weight:700;text-align:left">Email Injection</span><br /></td><td><span style="text-align:left">Email injection is a security vulnerability that allows malicious users to send email messages without prior authorization by the email server. These occur when the attacker adds extra data to fields, which are not interpreted by the server correctly. </span><br /></td></tr></tbody></table><p style=""><br /></p><div style="text-align:center"><span style="font-size:1rem">But in our case, we will be using </span><b style="font-size:1rem">SQL Injection</b><span style="font-size:1rem">.</span></div><p></p><p style="text-align:center;">For more information: <a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection" target="_blank">Injection</a><b><br /></b></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p style="text-align:left"><span style="font-weight:bolder;text-align:center;background-;">Question #1: Log into the administrator account!</span><br /></p><p style="text-align:center">After we navigate to the login page, enter some data into the email and password fields.</p><p style="text-align:center"><img src="https://i.imgur.com/4XHHSof.png" style="width:122px" /></p><p style="text-align:center"> <span style="font-weight:bolder">Before </span>clicking submit, make sure <span style="font-weight:bolder">Intercept mode is</span> <span style="font-weight:bolder">on</span>. </p><p style="text-align:center">This will allow us to see the data been sent to the server!</p><p style="text-align:center"><span style="font-size:1rem"><br /></span></p><p style="text-align:center"><img src="https://i.imgur.com/6gyZ7Vr.png" style="width:880.284px;height:273.711px" /><span style="font-size:1rem"><br /></span></p><p style="text-align:center"><br /></p><p style="text-align:center">We will now change the "<b>a</b>" next to the email to: <span style="font-weight:bold">' or 1=1-- </span>and forward it to the server.</p><p style="text-align:center"><img src="https://i.imgur.com/tPFJnmC.png" style="width:50%" /></p><p style="text-align:center"><b>Why does this work?</b></p><ol><li style="text-align:center;margin-bottom:1rem;">The character <b>'</b> will close the brackets in the SQL query</li><li style="text-align:center;margin-bottom:1rem;">'<b>OR</b>' in a SQL statement will return true if either side of it is true. As <span style="font-weight:bolder">1=1 is always true</span>, the whole statement is true. Thus it will tell the server that the email is valid, and log us into <span style="font-weight:bolder">user id 0</span>, which happens to be the administrator account.</li><li style="text-align:center;margin-bottom:1rem;">The <span style="font-weight:bolder">--</span> character is used in SQL to comment out data, any restrictions on the login will no longer work as they are interpreted as a comment. This is like the <span style="font-weight:bolder"># </span>and <span style="font-weight:bolder">// </span>comment in python and javascript respectively.</li></ol><p style="text-align:center"><br /></p><p style="text-align:center;margin-bottom:1rem">                      <img src="https://i.imgur.com/Y7xYGjp.png" style="width:620.397px;height:352.753px" /></p>

```
32a5e0f21372bcc1000a6088b93b458e41f0e02a
```

2. <p style="text-align:left"><span style="background-"><span style="font-weight:bolder;text-align:center">Question #2: Log into the Bender account!</span><br /></span></p><p style="text-align:center">Similar to what we did in <span style="font-weight:bolder"><u>Question #1</u></span>, we will now log into Bender's account! Capture the login request again, but this time we will put: <span style="font-weight:bolder">bender@juice-sh.op'-- </span>as the email. </p><p style="text-align:center"><img src="https://i.imgur.com/1F1ufc3.png" style="width:100%" /></p><p></p><p style="text-align:center">Now, forward that to the server!<br /></p><p style="text-align:center">But why don't we put the <span style="font-weight:bolder">1=1</span>?</p><p style="text-align:center"> Well, as the email address is valid (which will return <span style="font-weight:bolder">true</span>), we do not need to force it to be <span style="font-weight:bolder">true</span>. Thus we are able to use <b>'-- </b>to bypass the login system. Note the <b>1=1 </b>can be used when the email or username is not known or invalid.</p><p style="text-align:center;margin-bottom:1rem">                     <img src="https://i.imgur.com/Rznz31B.png" style="width:639.25px;height:400.193px;float:none" />  </p>

```
fb364762a3c102b2db932069c0e6b78e738d4066
```

----------------------------------------

### TASK 4. Who broke my lock?!

<p style="text-align:center;">                          <img src="https://i.imgur.com/OM71q2D.png" style="width:640.188px;height:387.094px" /><br /></p><p style="text-align:center;">In this task, we will look at exploiting authentication through different flaws. When talking about flaws within authentication, we include mechanisms that are vulnerable to manipulation. These mechanisms, listed below, are what we will be exploiting. </p><p style="text-align:center;"><span style="font-size:1rem">Weak passwords in high privileged accounts</span></p><p style="text-align:center;"><span style="font-size:1rem">Forgotten password pages</span></p><div style="text-align:center"><span style=""> More information: </span><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A2-Broken_Authentication" target="_blank">Broken Authentication</a></div><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p style="text-align:left"><span style=";font-weight:700;background-">Question #1: Bruteforce the Administrator account's password!</span><br /></p><p style=""><span style=";font-size:1rem">We have used SQL Injection to log into the Administrator account but we still don't know the password. Let's try a brute-force attack! We will once again capture a login request, but instead of sending it through the proxy, we will send it to Intruder.</span></p><p style="">Goto Positions and then select the <span style="font-weight:bolder">Clear § </span>button. In the password field place two § inside the quotes. It should look like the image below. </p><p style=""><img src="https://i.imgur.com/I96sO28.png" style="width:1006px;height:329.232px" /><span style=";font-size:1rem"><br /></span></p><p style=""><span style=";font-size:1rem">For the payload, we will be using the <span style="font-weight:bolder">best1050.txt from Seclists</span>. (Which can be installed via: <b>apt-get install seclists</b>)</span></p><p style=""><i>You can load the list from /usr/share/seclists/Passwords/Common-Credentials/best1050.txt</i></p><p style="">Once the file is loaded into Burp, start the attack. You will want to filter for the request by status.</p><p style="">A <span style="font-weight:bolder">failed </span>request will receive a <span style="font-weight:bolder">401 Unauthorized</span>   <img src="https://i.imgur.com/HcUs6eW.png" style="width:80px" /></p><p style="">Whereas a <span style="font-weight:bolder">successful </span>request will return a <span style="font-weight:bolder">200 OK</span>. <img src="https://i.imgur.com/q5jcfIA.png" style="width:80px" /></p><p style="margin-bottom:1rem;;text-align:center">Once completed, login to the account with the password.</p>

```
c2110d06dc6f81c67cd8099ff0ba601241f1ac0e
```

2. <p style="text-align:left"><span style="font-size:1rem;background-;;font-weight:700">Question #2: </span><span style="text-align:center;font-weight:bolder"><span style="font-size:1rem;background-;">Reset Jim's password!</span></span><br /></p><p></p><div style="text-align:center;"><span style="">Believe it or not, the reset password mechanism can also be exploited! When inputted into the email field in the Forgot Password page, Jim's security question is set to <i>"Your eldest siblings middle name?"</i>. In Task 2, we found that Jim might have something to do with <span style="font-weight:bolder">Star Trek</span>. Googling "Jim Star Trek" gives us a wiki page for <span style="font-weight:bolder">Jame T. Kirk</span> from Star Trek. </span></div><div style="text-align:center;">       <img src="https://i.imgur.com/axsRMp2.png" style="width:873px;height:282.493px" /><span style=""><br /></span></div><div style="text-align:center;"><span style=""><br /></span></div><div style=";text-align:center">Looking through the wiki page we find that he has a brother.</div><div style=";text-align:center"><img src="https://i.imgur.com/PfHXA1h.png" style="width:358px" /></div><div style=";text-align:center">Looks like his brother's middle name is <b>Samuel</b></div><div style=";text-align:center">Inputting that into the Forgot Password page allows you to successfully change his password.</div><div style=";text-align:center">You can change it to anything you want!</div><div style=";text-align:center"><img src="https://i.imgur.com/uRS3kJr.png" style="width:469px" /></div><div style=";text-align:center"><br /></div>

```
094fbc9b48e525150ba97d05b942bbf114987257
```

----------------------------------------

### TASK 5. AH! Don't look!

<p style="text-align:center">                <img src="https://i.imgur.com/XlbJl1E.png" style="width:741px;height:273.302px" /><span style=""><br /></span></p><p style="text-align:center"><span style="">A web application should store and transmit sensitive data safely and securely. But in some cases, the developer may not correctly protect their sensitive data, making it vulnerable. </span></p><p style="text-align:center"><span style="">Most of the time, data protection is not applied consistently across the web application making certain pages accessible to the public. Other times information is leaked to the public without the knowledge of the developer, making the web application vulnerable to an attack. </span></p><p style="text-align:center"><span style="font-size:1rem;">More information: </span><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A3-Sensitive_Data_Exposure" target="_blank">Sensitive Data Exposure</a></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <div style="text-align:left"><span style="font-size:1rem;background-;;font-weight:700">Question #1: </span><span style="text-align:center;font-weight:bolder"><span style="font-size:1rem;background-;">Access the Confidential Document!</span></span><br /></div><div style="text-align:center"><span style="font-weight:bolder"><span style="font-size:1rem;background-;"><br /></span></span></div><div style=";text-align:center"><img src="https://i.imgur.com/M1s8jfu.png" style="width:50%" /><u><span style="font-weight:bolder"><span style=";font-size:1rem"></span></span></u></div><div style="text-align:center"><span style="font-size:1rem">Navigate to the </span><span style="font-size:1rem;font-weight:bolder">About Us</span><span style="font-size:1rem"> page, and hover over the </span><i>"Check out our terms of use"</i><span style="font-size:1rem">.</span></div><div style="text-align:center"><span style="font-size:1rem"><br /></span></div><div style="text-align:center"><span style="font-size:1rem"> </span></div><div style="text-align:center"><img src="https://i.imgur.com/5PsmlD4.png" style="width:1001px" /><span style="font-size:1rem"></span></div><div style="text-align:center"><span style="font-size:1rem"><br /></span></div><div style="text-align:center"><span style="font-size:1rem">You will see that it links to </span><span style="font-size:1rem;"> </span><a href="http://machine_ip/ftp/legal.md">http://MACHINE_IP</a><span style="font-size:1rem"><a href="http://machine_ip/ftp/legal.md">/ftp/legal.md</a></span><span style="font-size:1rem">. Navigating to that <b>/ftp/</b> directory reveals that it is exposed to the public!</span></div><div style="text-align:center"><img src="https://i.imgur.com/EY664PR.png" style="width:200px" /><br /></div><p style="text-align:center;"><img src="https://i.imgur.com/Xp2aZJW.png" style="width:1046px" /><span style=""><br /></span></p><p style="text-align:center;margin-bottom:1rem;"><span style="">We will download the </span><span style="font-weight:bolder">acquisitions.md </span>and save it. It looks like there are other files of interest here as well. </p><p style="text-align:center;margin-bottom:1rem;">After downloading it, navigate to the <b>home page</b> to receive the flag!</p>

```
edf9281222395a1c5fee9b89e32175f1ccf50c5b
```

2. <p style="text-align:left"><span style="font-size:1rem;background-;;font-weight:700">Question #2: </span><span style="text-align:center;font-weight:bolder;background-;">Log into MC SafeSearch's account!</span><br /></p><p style="text-align:center;">                  <iframe frameborder="0" src="https://www.youtube.com/embed/v59CX2DiX0Y" width="640" height="360" class="note-video-clip"></iframe><br /></p><p style="text-align:center;margin-bottom:1rem;">After watching the video there are certain parts of the song that stand out. </p><p style="text-align:center;margin-bottom:1rem;">He notes that his password is "<span style="font-weight:bolder">Mr. Noodles</span>" but he has replaced some "<span style="font-weight:bolder">vowels into zeros</span>", meaning that he just replaced the o's into 0's. </p><p style="text-align:center;margin-bottom:1rem;">We now know the password to the <i>mc.safesearch@juice-sh.op</i> account is "<b>Mr. N00dles</b>"</p>

```
66bdcffad9e698fd534003fbb3cc7e2b7b55d7f0
```

3. <p style="text-align:left"><span style="font-size:1rem;background-;;font-weight:700">Question #3: </span><span style="text-align:center;font-weight:bolder;background-;">Download the Backup file!</span><br /></p><p style="text-align:center;"><span style="font-size:1rem;">We will now go back to the </span><span style="font-size:1rem"> </span><a href="http://machine_ip/ftp/">http://MACHINE_IP</a><span style="font-size:1rem;"><a href="http://machine_ip/ftp/">/ftp/</a> folder and try to download </span><span style="font-size:1rem;font-weight:bolder;">package.json.bak</span><span style="font-size:1rem;">. But it seems we are met with a 403 which says that only .md and .pdf files can be downloaded. </span></p><p style="text-align:center;"><img src="https://i.imgur.com/LDUkDBQ.png" style="width:1046px" /><span style="font-size:1rem;"><br /></span></p><p style="text-align:center;"><span style="font-size:1rem;">To get around this, we will use a character bypass called "</span><span style="font-weight:bolder">Poison Null Byte</span><span style=";font-size:1rem">". A </span>Poison Null Byte looks like this: <i><span style="font-weight:bolder">%00</span></i>. </p><p style="text-align:center;"><span style=";font-size:1rem">Note that we can download it using the url, so we will encode this into a url encoded format.</span></p><p style="text-align:center"><span style=";font-size:1rem">The </span><span style="font-size:1rem">Poison Null Byte will now look like this: <i><span style="font-weight:bolder;">%2500</span>. </i></span><span style=";font-size:1rem">Adding this and then a <b>.md</b> to the end will bypass the 403 error!</span></p><p style="text-align:center"><img src="https://i.imgur.com/2qugsl5.png" style="width:356px" /><span style=";font-size:1rem"></span></p><p style="text-align:center"><span style="font-size:1rem"><b>Why does this work? </b></span></p><p style="text-align:center;margin-bottom:1rem;"><span style=";font-size:1rem">A </span>Poison Null Byte is actually a <span style="font-weight:bolder">NULL terminator</span>. By placing a NULL character in the string at a certain byte, the string will tell the server to terminate at that point, nulling the rest of the string. </p>

```
bfc1e6b4a16579e85e06fee4c36ff8c02fb13795
```

----------------------------------------

### TASK 6. Who's flying this thing?

<p></p><p style="text-align:center"><img src="https://i.imgur.com/r2qq6de.png" style="width:840.146px;height:422.094px" /></p><p style="text-align:left">Modern-day systems will allow for multiple users to have access to different pages. Administrators most commonly use an administration page to edit, add and remove different elements of a website. <span style="font-size:1rem">You might use these when you are building a website with programs such as Weebly or Wix.  </span></p><p style="text-align:left">When Broken Access Control exploits or bugs are found, it will be categorised into one of <b>two types</b>:</p><table class="table table-bordered"><tbody><tr><td><b>Horizontal </b>Privilege Escalation<br /></td><td>Occurs when a user can perform an action or access data of another user with the <b>same </b>level of permissions.<br /></td></tr><tr><td><b>Vertical </b>Privilege Escalation<br /></td><td>Occurs when a user can perform an action or access data of another user with a <span style="font-weight:bolder">higher </span>level of permissions.<br /></td></tr></tbody></table><br /><p></p><p></p><div style="text-align:center"><img src="https://i.imgur.com/bJ9WKY4.png" style="font-size:1rem;width:471px" /></div><span style="font-size:11px"><div style="text-align:center"><i>Credits: Packetlabs.net</i></div></span><p></p><p style="text-align:center">More information: <a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A5-Broken_Access_Control" target="_blank">Broken Access Control</a><br /></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p style="text-align:left"><span style="font-size:1rem;background-;;font-weight:700">Question #1: </span><span style="font-size:1rem;text-align:center"><span style="font-weight:bolder;background-;">Access the administration page!</span></span><br /></p><p style=";text-align:center">First, we are going to open the <b>Debugger </b>on <span style="font-weight:bolder">Firefox</span>. </p><p style=";text-align:center">(Or <b>Sources</b> on <b>Chrome</b>.)</p><p style=";text-align:center">This can be done by navigating to it in the Web Developers menu. </p><p style=";text-align:center"><img src="https://i.imgur.com/rvhCm6V.png" style="width:50%" /><img src="https://i.imgur.com/oWJI6Yi.png" style="width:50%" /><br /></p><p style=";text-align:center">We are then going to refresh the page and look for a javascript file for <span style="font-weight:bolder">main-es2015.js</span></p><p style=";text-align:center">We will then go to that page at: <a href="http://machine_ip/">http://MACHINE_IP</a>/<span style="text-align:left">main-es2015.js</span></p><p style=";text-align:center"><img src="https://i.imgur.com/wF55kiO.png" style="width:639px" /><br /></p><p style=";text-align:center">To get this into a format we can read, click the { } button at the bottom  <img src="https://i.imgur.com/93xvM6I.png" style="width:84px" /></p><p style=";text-align:center">Now search for the term "admin" </p><p style=";text-align:center">You will come across a couple of different words containing "admin" but the one we are looking for is "path: administration"</p><p style=";text-align:center"><img src="https://i.imgur.com/AS1YVjU.png" style="width:639px" /><br /></p><p style=";text-align:center">This hints towards a page called "<b>/#/administration</b>" as can be seen by the <b>about </b>path a couple lines below, but going there while not logged in doesn't work. </p><p style="margin-bottom:1rem;;text-align:center">As this is an Administrator page, it makes sense that we need to be in the <b>Admin account </b>in order to view it.</p><p style="margin-bottom:1rem;;text-align:center">A good way to stop users from accessing this is to only load parts of the application that need to be used by them. This stops sensitive information such as an admin page from been leaked or viewed.<br /></p>

```
946a799363226a24822008503f5d1324536629a0
```

2. <p style="text-align:left;"><span style="font-size:1rem;background-;font-weight:700">Question #2: </span><span style="text-align:center;font-weight:bold;background-">View another user's shopping basket!</span><br /></p><p style=";text-align:center">Login to the Admin account and click on 'Your Basket'. Make sure Burp is running so you can capture the request!</p><p style=";text-align:center">Forward each request until you see: <i>GET /rest/basket/1 HTTP/1.1</i></p><p style=";text-align:center"><img src="https://i.imgur.com/wlS88AU.png" style="width:851px;height:301.938px" /><br /></p><p style=";text-align:center">Now, we are going to change the number <b>1</b> after /basket/ to <b>2</b></p><p style=";text-align:center"><img src="https://i.imgur.com/ugsRunL.png" style="width:50%" /><b></b></p><p style="margin-bottom:1rem;;text-align:center">It will now show you the basket of UserID 2. You can do this for other UserIDs as well, provided that they have one!</p><p style="margin-bottom:1rem;;text-align:center"><img src="https://i.imgur.com/yR4xFo3.png" style="width:758px" /></p>

```
41b997a36cc33fbe4f0ba018474e19ae5ce52121
```

3. <div style="text-align:left"><span style="background-"><b>Question #3: Remove all 5-star reviews!</b></span><br /></div><div style=";text-align:center"><span style="font-weight:bold"><br /></span></div><div style=";text-align:center">Navigate to the <span style="font-size:1rem"><a href="http://machine_ip/#/administration"> </a></span><a href="http://machine_ip/#/administration">http://MACHINE_IP</a><span style="font-size:1rem"><a href="http://machine_ip/#/administration">/#/administration</a></span><span style="font-size:1rem"> page again and </span><span style="font-size:1rem">click the bin icon next to the review with 5 stars!</span></div><div style=";text-align:center"><br /></div><div style=";text-align:center"><img src="https://i.imgur.com/cI2sSyx.png" style="width:560.547px;height:515.703px" /></div><div style=";text-align:center"><br /></div>

```
50c97bcce0b895e446d61c83a21df371ac2266ef
```

----------------------------------------

### TASK 7. Where did that come from?

<p style="text-align:center">      <img src="https://i.imgur.com/qBdgNKC.png" style="width:941px;height:415.708px" /><br /></p><p style="text-align:center">XSS or Cross-site scripting is a vulnerability that allows attackers to run javascript in web applications. These are one of the most found bugs in web applications. Their complexity ranges from easy to extremely hard, as each web application parses the queries in a different way. </p><p style="text-align:center"><b>There are three major types of XSS attacks:</b></p><table class="table table-bordered"><tbody><tr><td><u>DOM (Special)</u><br /></td><td><span style="font-weight:bolder">DOM XSS</span> <i>(Document Object Model-based Cross-site Scripting)</i> uses the HTML environment to execute malicious javascript. This type of attack commonly uses the <i>&lt;script&gt;&lt;/script&gt;</i> HTML tag.<br /></td></tr><tr><td><u>Persistent (Server-side)</u><br /></td><td><span style="font-weight:bolder">Persistent XSS</span> is javascript that is run when the server loads the page containing it. These can occur when the server does not sanitise the user data when it is <b>uploaded </b>to a page. These are commonly found on blog posts. <br /></td></tr><tr><td><u>Reflected (Client-side)</u><br /></td><td><span style="font-weight:bolder">Reflected XSS</span> is javascript that is run on the client-side end of the web application. These are most commonly found when the server doesn't sanitise <b>search </b>data. <br /></td></tr></tbody></table><p style="text-align:center"><span style="font-size:1rem"><br />More information: </span><a href="https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A7-Cross-Site_Scripting_(XSS)" target="_blank">Cross-Site Scripting XSS</a></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p style="text-align:left;"><span style="font-size:1rem;background-;font-weight:700">Question #1: </span><span style="text-align:center;font-weight:bolder"><span style="font-size:1rem;background-">Perform a DOM XSS!</span></span><br /></p><p style=";text-align:center"><img src="https://i.imgur.com/AMz9jps.png" style="width:571px" /></p><p style=";text-align:center">We will be using the iframe element with a javascript alert tag: </p><p style=";text-align:center"><i>&lt;iframe src="javascript:alert(`xss`)"&gt; </i></p><p style="margin-bottom:1rem;;text-align:center">Inputting this into the <b>search bar</b> will trigger the alert.</p><p style="margin-bottom:1rem;;text-align:center"><img src="https://i.imgur.com/rKEx3aR.png" style="width:297px" /></p><p style="margin-bottom:1rem;;text-align:center"> </p><p style="margin-bottom:1rem;;text-align:center">Note that we are using <b>iframe </b>which is a common HTML element found in many web applications, there are others which also produce the same result. </p><p style="margin-bottom:1rem;;text-align:center">This type of XSS is also called XFS (Cross-Frame Scripting), is one of the most common forms of detecting XSS within web applications. </p><p style="margin-bottom:1rem;;text-align:center">Websites that allow the user to modify the iframe or other DOM elements will most likely be vulnerable to XSS.   </p><p style="margin-bottom:1rem;;text-align:center"><b>Why does this work?</b></p><p style="margin-bottom:1rem;;text-align:center">It is common practice that the search bar will send a request to the server in which it will then send back the related information, but this is where the flaw lies. Without correct input sanitation, we are able to perform an XSS attack against the search bar. </p>

```
9aaf4bbea5c30d00a1f5bbcfce4db6d4b0efe0bf
```

2. <p style="text-align:left;"><span style="font-size:1rem;background-;font-weight:700">Question #2: </span><span style="text-align:center;font-weight:bolder"><span style="font-size:1rem;background-">Perform a persistent XSS!</span></span><span style="font-size:1rem"><br /></span></p><p style=";text-align:center"><span style="font-size:1rem">First, login to the <b>admin </b>account.</span></p><p style=";text-align:center"><span style="font-size:1rem">We are going to navigate to the "<b>Last Login IP</b>" page for this attack.</span><br /></p><p style=";text-align:center"> <img src="https://i.imgur.com/YTIzhh0.png" style="width:485px" /></p><p style=";text-align:center">It should say the last IP Address is 0.0.0.0 or 10.x.x.x </p><p style="text-align:center;">As it logs the 'last' login IP we will now logout so that it logs the 'new' IP.</p><p style="text-align:center;"><img src="https://i.imgur.com/4XHHSof.png" style="width:122px" /></p><p style="text-align:center;"> </p><p style="text-align:center;">Make sure that Burp <b>intercept is on</b>, so it will catch the logout request.</p><p style="text-align:center;">We will then head over to the Headers tab where we will add a new header:</p><table class="table table-bordered" style="text-align:center;width:1046px"><tbody><tr><td><i>True-Client-IP</i><br /></td><td><i>&lt;iframe src="javascript:alert(`xss`)"&gt;</i><br /></td></tr></tbody></table><p style="margin-bottom:1rem;;text-align:center"><img src="https://i.imgur.com/VLd2Fga.png" style="width:1046px" /></p><p style="margin-bottom:1rem;;text-align:center">Then forward the request to the server!<br />When <b>signing back into the admin account</b> and navigating to the Last Login IP page again, we will see the XSS alert!</p><p style="margin-bottom:1rem;;text-align:center"><img src="https://i.imgur.com/rKEx3aR.png" style="width:297px" /></p><p style="margin-bottom:1rem;;text-align:center"><b>Why do we have to send this Header?</b></p><p style="margin-bottom:1rem;text-align:center">The <i>True-Client-IP  </i><span style="font-size:1rem">header is similar to the </span><i>X-Forwarded-For </i><span style=";font-size:1rem">header, both tell the server or proxy what the IP of the client is. Due to there being no sanitation in the header we are able to perform an XSS attack. </span></p>

```
149aa8ce13d7a4a8a931472308e269c94dc5f156
```

3. <p style="text-align:left;"><span style="font-size:1rem;background-;font-weight:700">Question #3: </span><span style="text-align:center;font-weight:bolder;background-"><span style="font-size:1rem">Perform a r</span><span style="font-size:1rem">eflected XSS!</span></span><br /></p><p style=";text-align:center">First, we are going to need to be on the right page t<span style=";font-size:1rem">o perform the reflected XSS!</span></p><p style=";text-align:center"><span style=";font-size:1rem"><b>Login </b>into the <b>admin account</b> and navigate to the '<span style="font-weight:bolder">Order History</span>' page. </span></p><p style="">                            <img src="https://i.imgur.com/hBy4O1L.png" style="width:513.704px;height:364.391px;float:none" />  </p><p style=";text-align:center">From there you will see a "<span style="font-weight:bolder">Truck</span>" icon, clicking on that will bring you to the track result page. You will also see that there is an id paired with the order.   <img src="https://i.imgur.com/kQdIKyL.png" style="width:384px" /></p><p style=";text-align:center">We will use the iframe XSS, <i>&lt;iframe src="javascript:alert(`xss`)"&gt;, </i>in the place of the <i>5267-f73dcd000abcc353</i></p><p style="margin-bottom:1rem;;text-align:center">After submitting the URL, refresh the page and you will then get an alert saying XSS!</p><p style="margin-bottom:1rem;;text-align:center"><img src="https://i.imgur.com/rKEx3aR.png" style="width:297px" /></p><p style="margin-bottom:1rem;;text-align:center"><b>Why does this work?</b></p><p style="margin-bottom:1rem;;text-align:center">The server will have a lookup table or database (depending on the type of server) for each tracking ID. As the 'id' parameter is not sanitised before it is sent to the server, we are able to perform an XSS attack.  </p>

```
23cefee1527bde039295b2616eeb29e1edc660a0
```

----------------------------------------

### TASK 8. Exploration!

<p style="text-align:center"><img src="https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part1/img/score-board_partly.png" style="width:894px;height:447px;float:none" /><br /></p><p style="text-align:center">If you wish to tackle some of the <b>harder </b>challenges that were not covered within this room, check out the <b>/#/score-board/</b> section on Juice-shop. Here you can see your completed tasks as well as other tasks in varying difficulty.</p><p style="text-align:center"><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <b style="background-">Access the <span style="text-align:center">/#/score-board/ </span><span style="text-align:center">page</span></b>

```
7efd3174f9dd5baa03a7882027f2824d2f72d86e
```


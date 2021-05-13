# TryHackMe walkthrough

## Introductory Researching

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Introduction



  
  
  
  

Without a doubt, the ability to research effectively is <em>the</em> most important quality for a hacker to have. By its very nature, hacking requires a <em>vast</em> knowledge base -- because how are you supposed to break into something if you don't know how it works? The thing is: no one knows everything. Everyone (professional or amateur, experienced or totally new to the subject) will encounter problems which they don't automatically know how to solve. This is where research comes in, as, in the real world, you can't ever expect to simply be handed the answers to your questions.<br /><br />As your experience level increases, you will find that the things you're researching scale in their difficulty accordingly; however, in the field of information security, there will never come a point where you don't need to look things up.<br /><br />This room will serve as a brief overview of some of the most important resources available to you, and will hopefully aid you in the process of building a research methodology that works for you.<br /><br />We will be looking at the following topics:<br />• An example of a research question<br />• Vulnerability Searching tools<br />• Linux Manual Pages<br /><br />Let's begin.

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the Introduction<br /></p>

```
OK
```

----------------------------------------

### TASK 2. Example Research Question

<p>

  
  
  
  

We'll begin by looking at a typical research question: the kind that you're likely to find when working through a CTF on TryHackMe.<br /><br />Let's say you've downloaded a JPEG image from a remote server. You suspect that there's something hidden inside it, but how can you get it out?<br />How about we start by searching for “hiding things inside images” in Google:<br /><img /></p><p><img style="width:982.797px;height:740.328px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/GoogleSearch1.png" /><br /><br />Notice that the second link down gives us the title of a technique: “Steganography”. You can then click that link and read the document, which will teach you <em>how</em> files are hidden inside images.<br /><br />Ok, so we know how it's done, let's try searching for a way to extract files using steganography:<br /><img /></p><p><img style="width:907.95px;height:695px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/GoogleSearch2.png" /><br /><br />Already virtually every link is pointing to something useful. The first link contains a collection of useful tools, the second is more instructions on how to perform steganography in the first place. Realistically any of these links could prove useful, but let's take a look at that first one (<a href="https://0xrick.github.io/lists/stego/">https://0xrick.github.io/lists/stego/</a>):<br /><br /><img /><img style="width:963.5px;height:546.099px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/0xRick.png" /><br /><br />The very first tool there looks to be useful. It can be used to extract embedded data from JPEG files -- exactly what we need it to do! This page also tells you that steghide can be installed using something called “apt”.<br />Let's search that up next!<br /><br /><img /><img style="width:929.5px;height:392.174px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/AptSearch.png" /><br /><br />Great -- so apt is a package manager that lets us install tools on Linux distributions like Ubuntu (or Kali!).<br />How can we install packages using apt? Let's search it!<br /><img /></p><p><img style="width:774.5px;height:340.849px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/AptSyntax.png" /><br /></p><p><br />Perfect -- right at the top of the page we're given instructions. We know that our package is called steghide, so we can go ahead and install that:<br /><img /></p><p><img style="width:755.5px;height:300.349px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/AptInstallation.png" /><br /><br />Now, let's switch back to that collection of steganography tools we were looking at before. Did you notice that there were instructions on how to use steghide right there?<br /><br /><img /><img style="width:742.5px;height:93.964px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/SteghideSyntax.png" /><br /><br />There we go! That's how we can extract an image from a file. Our research has paid off and we can now go and complete the task.</p><hr /><p>Notice the methodology here. We started with nothing, but gradually built up a picture of what we needed to do. We had a question (How can I extract data from this image). We searched for an answer to that question, then continued to query each of the answers we were given until we had a full understanding of the topic. This is a really good way to conduct research: Start with a question; get an initial understanding of the topic; then look into more advanced aspects as needed.<br /><br />Now it's your turn. See if you can answer the following questions using your research skills. The first three questions have appropriate search queries in the hints:</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>

  
  
  
  

In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)?</p>

```
Repeater
```

2. <p>What hash format are modern Windows login passwords stored in?<br /></p>

```
NTLM
```

3. <p>What are automated tasks called in Linux?</p>

```
Cron Jobs
```

4. <p>What number base could you use as a shorthand for base 2 (binary)?</p>

```
Base 16
```

5. <p>If a password hash starts with $6$, what format is it (Unix variant)?</p>

```
sha512crypt
```

----------------------------------------

### TASK 3. Vulnerability Searching

<p>Often in hacking you'll come across software that might be open to exploitation. For example, Content Management Systems (such as Wordpress, FuelCMS, Ghost, etc) are frequently used to make setting up a website easier, and many of these are vulnerable to various attacks. So where would we look if we wanted to exploit specific software?</p><p>The answer to that question lies in websites such as:</p><ul><li><a href="https://www.exploit-db.com" target="_blank">ExploitDB</a></li><li><a href="https://nvd.nist.gov/vuln/search" target="_blank">NVD</a></li><li><a href="https://cve.mitre.org" target="_blank">CVE Mitre</a></li></ul><p>NVD keeps track of CVEs (<b>C</b>ommon <b>V</b>ulnerabilities and <b>E</b>xposures) -- whether or not there is an exploit publicly available -- so it's a really good place to look if you're researching vulnerabilities in a specific piece of software. CVEs take the form: CVE-YEAR-IDNUMBER<br />(<i>Hint Hint: It's going to be really useful in the questions!)</i></p><p><a href="https://www.exploit-db.com" target="_blank">ExploitDB</a> tends to be very useful for hackers, as it often actually contains exploits that can be downloaded and used straight out of the box. It tends to be one of the first stops when you encounter software in a CTF or pentest.</p><p>If you're inclined towards the CLI on Linux, Kali comes pre-installed with a tool called "searchsploit" which allows you to search ExploitDB from your own machine. This is offline, and works using a downloaded version of the database, meaning that you already have all of the exploits already on your Kali Linux!</p><hr /><p><span style="font-size:1rem">Let's take an example. Say we're playing a CTF and we come across a website:</span><br /></p><p><img src="https://i.imgur.com/8fhG8ZO.png" alt="FuelCMS home page" style="width:961.5px;height:398.71px" /></p><p>Well, this is quite obviously FuelCMS. Usually it won't be <i>this</i> obvious, but hey, we'll work with what we've got!</p><p>We know the software, so let's search for it in ExploitDB. <br />(<i>Note: I'm going to use the CLI tool in Kali, as it tends to be quicker from a workflow perspective -- however, you are welcome to use the website)</i></p><p>I'm using the command <code>searchsploit fuel cms</code> to search for exploits:</p><p><img alt="Searchsploit results for FuelCMS" src="https://i.imgur.com/pu2kdrm.png" style="width:963.09px;height:58.625px" /></p><p>If you prefer doing things in the website, here are the results from there:</p><p><img alt="ExploitDB results for FuelCMS" src="https://i.imgur.com/8MksLin.png" style="width:960.5px;height:311.735px" /></p><p>Success! We've got an exploit that we can now use against the website!</p><p>Actually using the exploit is outwith the scope of this room, but you can see the process. </p><p>If you click on the title you'll be given a bit more of an explanation about the exploit:</p><p><img alt="Information about a remote code execution in FuelCMS 1.4.1" src="https://i.imgur.com/7DMp9h1.png" style="width:981.5px;height:219.234px" /></p><p>Pay particular attention to the CVE numbers; you'll need them for the questions!<br />The format will be like so: <code>CVE-YEAR-NUMBER</code><br /><code></code></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?</p>

```
CVE-2020-10385
```

2. <p>There was a Local Privilege Escalation vulnerability found in the <i>Debian</i> version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability?</p>

```
CVE-2016-1240
```

3. <p>What is the very first CVE found in the VLC media player?</p>

```
CVE-2007-0017
```

4. <p>If you wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would you use?</p>

```
CVE-2019-18634
```

----------------------------------------

### TASK 4. Manual Pages

<p>If you haven't already worked in Linux, take a look at the <a href="https://tryhackme.com/room/linux1" target="_blank">Learn Linux</a> rooms. Linux (usually Kali Linux) is without a doubt the most ubiquitous operating system used in hacking, so it pays to be familiar with it!</p><p>One of the many useful features of Linux is the inbuilt <code>man</code> command, which gives you access to the manual pages for most tools directly inside your terminal. Occasionally you'll find a tool that doesn't have a manual entry; however, this is rare. Generally speaking, when you don't know how to use a tool, <code>man</code> should be your first port of call.</p><p>Let's give this a shot!</p><p>Say we want to connect to a remote computer using SSH, but we don't know the syntax. We can try <code>man ssh</code> to get the manual page for SSH:</p><p><img src="https://i.imgur.com/WgjMwFZ.png" style="width:993.5px;height:239.856px" /></p><p>Awesome!</p><p>We can see in the description that the syntax for using SSH is &lt;user&gt;@&lt;host&gt;:</p><p><img src="https://i.imgur.com/uFricVE.png" style="width:987.5px;height:30.0186px" /></p><p>We can also use the man pages to look for special switches in programs that make the program do other things. An example of this would be that (from our very first example) steghide can be used to both extract and embed files inside an image, based on the switches that you give it. </p><p>For example, if you wanted to display the version number for SSH, you would scroll down in the <code>man</code> page until you found an appropriate switch:</p><p><img src="https://i.imgur.com/0yvbE8H.png" style="width:404px" /></p><p>Then use it:</p><p><img src="https://i.imgur.com/oxwiNxv.png" style="width:489px" /></p><p>Another way to find that switch would have been to search the <code>man</code> page for the correct switch using grep:</p><p><img src="https://i.imgur.com/cpFNlQu.png" style="width:483px" /></p><hr /><p>Now your turn! Answer the following questions using the <code>man</code> command:</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>SCP is a tool used to copy files from one computer to another. <br /><i>What switch would you use to copy an entire directory?</i></p>

```
-r
```

2. <p>fdisk is a command used to view and alter the partitioning scheme used on your hard drive.<br /><i>What switch would you use to list the current partitions?</i></p>

```
-l
```

3. <p>nano is an easy-to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with.<br /><i>What switch would you use to make a backup when opening a file with nano?</i></p>

```
-B
```

4. <p>Netcat is a basic tool used to manually send and receive network requests. <br /><i>What <b>command</b> would you use to start netcat in listen mode, using port 12345?</i></p>

```
nc -l -p 12345
```

----------------------------------------

### TASK 5. Final Thoughts

<p><span style="font-size:1rem">You may have been told in school that there are good sources and bad sources of information. That may be true when it comes to essays and referencing information; however, it's my pleasure to state that it does not apply here. Any information can potentially be useful -- so feel free to use blogs, wikipedia, or anything else that contains what you're looking for! Blogs especially can often be very valuable for learning when it comes to information security, as many security researchers keep a blog.</span><br /></p><p>Having completed this room, you hopefully now have established the basis of a methodology to tackle research questions that you come across by yourself. The vast majority of rooms on TryHackMe can be solved purely using knowledge found on Google, so please take the opportunity to improve your skills by Googling any problems you come across!</p><p style="margin-bottom:1rem">As a follow-up to this room, complete CMNatic's <a href="https://tryhackme.com/room/googledorking" target="_blank">Google Dorking</a> room to learn some advanced Google tricks!</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Research Complete!</p>

```
OK
```


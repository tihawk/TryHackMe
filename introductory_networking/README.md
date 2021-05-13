# TryHackMe walkthrough

## Introductory Networking

> _kblagoev | May 13, 2021_

----------------------------------------

### TASK 1. Introduction

<p>The aim of this room is to provide a beginner's introduction to the basic principles of networking. Networking is a <i>massive</i> topic, so this really will just be a brief overview; however, it will hopefully give you some foundational knowledge of the topic, which you can build upon for yourself<em>.</em></p><p>The topics that we're going to cover in this room are:</p><ul><li>The OSI Model</li><li>The TCP/IP Model</li><li>How these models look in practice</li><li>An introduction to basic networking tools</li></ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Let's get started!</p>

```
OK
```

----------------------------------------

### TASK 2. The OSI Model: An Overview

<p>The OSI (<b>O</b>pen <b>S</b>ystems <b>I</b>nterconnection) Model is a standardised model which we use to demonstrate the theory behind computer networking. In practice, it's actually the more compact TCP/IP model that real-world networking is based off; however the OSI model, in many ways, is easier to get an initial understanding from.</p><p>The OSI model consists of seven layers:</p><p><img style="width:134px" alt="Table showing the OSI layers: Application, Presentation, Session, Transport, Network, Data Link, Physical" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/02/OSI-Table.png" /></p><p>There are many mnemonics floating around to help you learn the layers of the OSI model -- search around until you find one that you like.</p><p>I personally favour: <b>A</b>nxious <b>P</b>ale <b>S</b>hakespeare <b>T</b>reated <b>N</b>ervous <b>D</b>runks <b>P</b>atiently</p><p>Let's briefly take a look at each of these in turn:</p><p><u>Layer 7 -- Application</u><u>:</u></p><p>The application layer of the OSI model essentially provides networking options to programs running on a computer. It works almost exclusively with applications, providing an interface for them to use in order to transmit data. When data is given to the application layer, it is passed down into the presentation layer.<br /></p><p><u>Layer 6 -- Presentation</u><u>:</u></p><p>The presentation layer receives data from the application layer. This data tends to be in a format that the application understands, but it's not necessarily in a standardised format that could be understood by the application layer in the <i>receiving</i> computer. The presentation layer translates the data into a standardised format, as well as handling any encryption, compression or other transformations to the data. With this complete, the data is passed down to the session layer.</p><p><u>Layer 5 -- Session</u><u>:</u></p><p>When the session layer receives the correctly formatted data from the presentation layer, it looks to see if it can set up a connection with the other computer across the network. If it can't then it sends back an error and the process goes no further. If a session <i>can</i> be established then it's the job of the session layer to maintain it, as well as co-operate with the session layer of the remote computer in order to synchronise communications. The session layer is particularly important as the session that it creates is unique to the communication in question. This is what allows you to make multiple requests to different endpoints simultaneously without all the data getting mixed up (think about opening two tabs in a web browser at the same time)! When the session layer has successfully logged a connection between the host and remote computer the data is passed down to Layer 4: the transport Layer.</p><p><u>Layer 4 -- Transport</u><u>:</u></p><p>The transport layer is a very interesting layer that serves numerous important functions. Its first purpose is to choose the protocol over which the data is to be transmitted. The two most common protocols in the transport layer are TCP (<b>T</b>ransmission <b>C</b>ontrol <b>P</b>rotocol) and UDP (<b>U</b>ser <b>D</b>atagram<b> P</b>rotocol); with TCP the transmission is <i>connection-based</i> which means that a connection between the computers is established and maintained for the duration of the request. This allows for a reliable transmission, as the connection can be used to ensure that the packets <i>all</i> get to the right place. A TCP connection allows the two computers to remain in constant communication to ensure that the data is sent at an acceptable speed, and that any lost data is re-sent. With UDP, the opposite is true; packets of data are essentially thrown at the receiving computer -- if it can't keep up then that's <i>its </i>problem (this is why a video transmission over something like Skype can be pixelated if the connection is bad). What this means is that TCP would usually be chosen for situations where accuracy is favoured over speed (e.g. file transfer, or loading a webpage), and UDP would be used in situations where speed is more important (e.g. video streaming).</p><p>With a protocol selected, the transport layer then divides the transmission up into bite-sized pieces (over TCP these are called <i>segments</i>, over UDP they're called <i>datagrams</i>), which makes it easier to transmit the message successfully. </p><p><u>Layer 3 -- Network:</u></p><p>The network layer is responsible for locating the destination of your request. For example, the Internet is a huge network; when you want to request information from a webpage, it's the network layer that takes the IP address for the page and figures out the best route to take. At this stage we're working with what is referred to as <i>Logical </i>addressing (i.e. IP addresses) which are still software controlled. Logical addresses are used to provide order to networks, categorising them and allowing us to properly sort them. Currently the most common form of logical addressing is the IPV4 format, which you'll likely already be familiar with (i.e 192.168.1.1 is a common address for a home router).</p><p><u>Layer 2 -- Data Link:</u></p><p>The data link layer focuses on the <i>physical </i>addressing of the transmission. It receives a packet from the network layer (that includes the IP address for the remote computer) and adds in the physical (MAC) address of the receiving endpoint. I<span style="font-size:1rem">nside every network enabled computer is a </span><span style="font-size:1rem;font-weight:bolder">N</span><span style="font-size:1rem">etwork </span><span style="font-size:1rem;font-weight:bolder">I</span><span style="font-size:1rem">nterface </span><span style="font-size:1rem;font-weight:bolder">C</span><span style="font-size:1rem">ard (NIC) which comes with a unique MAC (</span><span style="font-size:1rem;font-weight:bolder">M</span><span style="font-size:1rem">edia </span><span style="font-size:1rem;font-weight:bolder">A</span><span style="font-size:1rem">ccess </span><span style="font-size:1rem;font-weight:bolder">C</span><span style="font-size:1rem">ontrol) address to identify it. </span></p><p><span style="font-size:1rem">MAC addresses are set by the manufacturer and literally burnt into the card; they can't be changed -- although they </span><i>can</i><span style="font-size:1rem"> be spoofed. When information is sent across a network, it's actually the physical address that is used to identify where exactly to send the information.</span></p><p><span style="font-size:1rem"> </span></p><p><span style="font-size:1rem">Additionally, it's also the job of the data link layer to present the data in a format suitable for transmission.</span></p><p><span style="font-size:1rem">The data link layer also serves an important function when it receives data, as it checks the received information to make sure that it hasn't been corrupted during transmission, which could well happen when the data is transmitted by layer 1: the physical layer. </span></p><p><u>Layer 1 -- Physical:</u></p><p>The physical layer is right down to the hardware of the computer. This is where the electrical pulses that make up data transfer over a network are sent and received. It's the job of the physical layer to convert the binary data of the transmission into signals and transmit them across the network, as well as receiving incoming signals and converting them back into binary data.</p><hr /><p><i><b>For the "Which Layer" Questions below, answer using the layer number (1-7)</b></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Which layer would choose to send data over TCP or UDP?</p>

```
4
```

2. <p>Which layer checks received packets to make sure that they haven't been corrupted?</p>

```
2
```

3. <p>In which layer would data be formatted in preparation for transmission?</p>

```
2
```

4. <p>Which layer transmits and receives data?</p>

```
1
```

5. <p>Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format?</p>

```
6
```

6. <p>Which layer tracks communications between the host and receiving computers?</p>

```
5
```

7. <p>Which layer accepts communication requests from applications?</p>

```
7
```

8. <p>Which layer handles logical addressing?</p>

```
3
```

9. <p>When sending data over TCP, what would you call the "bite-sized" pieces of data? <br /></p>

```
Segments
```

10. <p><b>[Research]</b> Which layer would the FTP protocol communicate with?<br /></p>

```
7
```

11. <p>Which transport layer protocol would be best suited to transmit a live video?</p>

```
UDP
```

----------------------------------------

### TASK 3. Encapsulation

<p style="margin-bottom:1rem">As the data is passed down each layer of the model, more information containing details specific to the layer in question is added on to the start of the transmission. As an example, the header added by the Network Layer would include things like the source and destination IP addresses, and the header added by the Transport Layer would include (amongst other things) information specific to the protocol being used. <span style="font-size:1rem">The data link layer also adds a piece on at the </span><i>end</i><span style="font-size:1rem"> of the transmission, which is used to verify that the data has not been corrupted on transmission; this also has the added bonus of increased security, as the data can't be intercepted and tampered with without breaking the trailer. </span><span style="font-size:1rem">This whole process is referred to as </span><i>encapsulation; </i><span style="font-size:1rem">the process by which data can be sent from one computer to another.</span></p><p style="margin-bottom:1rem"><img alt="Encapsulation process" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/02/image.jpeg" style="width:869px;float:none" /></p><p style="margin-bottom:1rem">Notice that the encapsulated data is given a different name at different steps of the process. In layers 7,6 and 5, the data is simply referred to as data. In the transport layer the encapsulated data is referred to as a segment or a datagram (depending on whether TCP or UDP has been selected as a transmission protocol). At the Network Layer, the data is referred to as a packet. When the packet gets passed down to the Data Link layer it becomes a frame, and by the time it's transmitted across a network the frame has been broken down into bits.</p><p style="margin-bottom:1rem">When the message is received by the second computer, it reverses the process -- starting at the physical layer and working up until it reaches the application layer, stripping off the added information as it goes. This is referred to as <i>de-encapsulation. </i>As such you can think of the layers of the OSI model as existing inside every computer with network capabilities. Whilst it's not actually as clear cut in practice, computers all follow the same process of encapsulation to send data and de-encapsulation upon receiving it.</p><p style="margin-bottom:1rem">The processes of encapsulation and de-encapsulation are very important -- not least because of their practical use, but also because they give us a standardised method for sending data. This means that all transmissions will consistently follow the same methodology, allowing any network enabled device to send a request to any other reachable device and be sure that it will be understood -- regardless of whether they are from the same manufacturer; use the same operating system; or any other factors.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?</p>

```
Frames
```

2. <p>How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?</p>

```
Datagrams
```

3. <p>What process would a computer perform on a received message?</p>

```
De-encapsulation
```

4. <p>Which is the only layer of the OSI model to add a <i>trailer</i> during encapsulation?</p>

```
Data Link
```

5. <p>Does encapsulation provide an extra layer of security <b>(Aye/Nay)</b>?</p>

```
Aye
```

----------------------------------------

### TASK 4. The TCP/IP Model

<p><span style="font-size:1rem">The TCP/IP model is, in many ways, very similar to the OSI model. It's a few years older, and serves as the basis for real-world networking. </span><span style="font-size:1rem">The TCP/IP model consists of four layers: Application, Transport, Internet and Network Interface. Between them, these cover the same range of functions as the seven layers of the OSI Model.</span></p><p><img alt="The layesrs of the TCP/IP model: Application, Transport,Internet, Network Interface" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/02/image-4.png" style="width:153px" /></p><p><i><b>Note: </b>Some recent sources split the TCP/IP model into five layers -- breaking the Network Interface layer into Data Link and Physical layers (as with the OSI model). This is accepted and well-known; however, it is not officially defined (unlike the original four layers which are defined in RFC1122). It's up to you which version you use -- both are generally considered valid.</i><br /></p><p>You would be justified in asking why we bother with the OSI model if it's not actually used for anything in the real-world. The answer to that question is quite simply that the OSI model (due to being less condensed and more rigid than the TCP/IP model) tends to be easier for learning the initial theory of networking. <br /></p><p>The two models match up something like this:</p><p><img alt="Comparison between the TCP/IP and OSI models." src="https://muirlandoracle.co.uk/wp-content/uploads/2020/02/image-3.png" style="width:259px" /></p><p>The processes of encapsulation and de-encapsulation work in exactly the same way with the TCP/IP model as they do with the OSI model. At each layer of the TCP/IP model a header is added during encapsulation, and removed during de-encapsulation.</p><hr /><p>Now let's get down to the practical side of things.</p><p>A layered model is great as a visual aid -- it shows us the general process of how data can be encapsulated and sent across a network, but how does it actually happen?</p><p>When we talk about TCP/IP, it's all well and good to think about a table with four layers in it, but we're actually talking about a suite of protocols -- sets of rules that define how an action is to be carried out. TCP/IP takes its name from the two most important of these: the <b>T</b>ransmission <b>C</b>ontrol <b>P</b>rotocol (which we touched upon earlier in the OSI model) that controls the flow of data between two endpoints, and the <b>I</b>nternet <b>P</b>rotocol, which controls how packets are addressed and sent. There are many more protocols that make up the TCP/IP suite; we will cover some of these in later tasks. For now though, let's talk about TCP.</p><p>As mentioned earlier, TCP is a <i>connection-based</i> protocol. In other words, before you send any data via TCP, you must first form a stable connection between the two computers. The process of forming this connection is called the <i>three-way handshake</i>. </p><p>When you attempt to make a connection, your computer first sends a special request to the remote server indicating that it wants to initialise a connection. This request contains something called a <i>SYN</i> (short for <i>synchronise</i>) bit, which essentially makes first contact in starting the connection process. The server will then respond with a packet containing the SYN bit, as well as another "acknowledgement" bit, called <i>ACK</i>. Finally, your computer will send a packet that contains the ACK bit by itself, confirming that the connection has been setup successfully. With the three-way handshake successfully completed, data can be reliably transmitted between the two computers. Any data that is lost or corrupted on transmission is re-sent, thus leading to a connection which appears to be lossless.</p><p><img alt="The three way handshake" style="width:50%" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-2.png" /></p><p><br /></p><p><img alt="Frank Syn-acktra -- humour value only" style="width:50%" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/02/syn-acktra.jpeg" /></p><p><i>(Credit Kieran Smith, Abertay University)</i></p><p>We're not going to go into exactly <i>how</i> this works on a step-to-step level -- not in this room at any rate. It is sufficient to know that the three-way handshake must be carried out before a connection can be established using TCP.</p><hr /><p><b><u>History:</u></b></p><p>It's important to understand exactly <i>why</i> the TCP/IP and OSI models were originally created. To begin with there was no standardisation -- different manufacturers followed their own methodologies, and consequently systems made by different manufacturers were completely incompatible when it came to networking. The TCP/IP model was introduced by the American DoD in 1982 to provide a standard -- something for all of the different manufacturers to follow. This sorted out the inconsistency problems. Later the OSI model was also introduced by the International Organisation for Standardisation (<a href="https://www.iso.org/home.html" target="_blank">ISO</a>); however, it's mainly used as a more comprehensive guide for learning, as the TCP/IP model is still the standard upon which modern networking is based.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Which model was introduced first, OSI or TCP/IP?</p>

```
TCP/IP
```

2. <p>Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model <b>(Full Name)</b>?<br /></p>

```
Transport
```

3. <p>Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model <b>(Full Name)</b>?<br /></p>

```
Application
```

4. <p>The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. <b>(Full Name)</b>?<br /></p>

```
Physical
```

5. <p><span style="font-size:1rem">Which layer of the TCP/IP model handles the functionality of the OSI network layer?</span><br /></p>

```
Internet
```

6. <p>What kind of protocol is TCP?<br /></p>

```
Connection-based
```

7. <p>What is SYN short for?<br /></p>

```
Synchronise
```

8. <p>What is the second step of the three way handshake?</p>

```
SYN/ACK
```

9. <p>What is the short name for the "Acknowledgement" segment in the three-way handshake?</p>

```
ACK
```

----------------------------------------

### TASK 5. <span class="badge badge-soft-warning size-16">Networking Tools</span> Ping

<p>

  
  
  
  

  
  
  
  

At this stage, hopefully all of the theory has made sense and you now understand the basic models behind computer networking. For the rest of the room we're going to be taking a look at some of the command line networking tools that we can use in practical applications. Many of these tools do work on other operating systems, but for the sake of simplicity, I'm going to assume that you're running Linux for the rest of this room. The first tool that we're going to look at will be the <code>ping</code> command.</p><hr /><p>

  
  
  
  

  
  
  
  

The ping command is used when we want to test whether a connection to a remote resource is possible. Usually this will be a website on the internet, but it could also be for a computer on your home network if you want to check if it's configured correctly. Ping works using the ICMP protocol, which is one of the slightly less well-known TCP/IP  protocols that were mentioned earlier. The ICMP protocol works on the Network layer of the OSI Model, and thus the Internet layer of the TCP/IP model. The basic syntax for ping is <code>ping &lt;target&gt;</code>. In this example we are using ping to test whether a network connection to Google is possible:</p><p><img alt="Pinging Google -- it is possible" style="width:507px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-14.png" /></p><p>

  
  
  
  

  
  
  
  

Notice that the ping command actually returned the IP address for the Google server that it connected to, rather than the URL that was requested. This is a handy secondary application for ping, as it can be used to determine the IP address of the server hosting a website. One of the big advantages of ping is that it's pretty much ubiquitous to any network enabled device. All operating systems support it out of the box, and even most embedded devices can use ping!<br />

  
  
  
  

</p><p>Have a go at the following questions. Any questions about syntax can be answered using the man page for ping (<code>man ping</code> on Linux).</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What command would you use to ping the bbc.co.uk website?</p>

```
ping bbc.co.uk
```

2. <p>Ping <i>muirlandoracle.co.uk</i><br />What is the IPv4 address?<br /></p>

```
217.160.0.152
```

3. <p>What switch lets you change the interval of sent ping requests?<br /></p>

```
-i
```

4. <p>What switch would allow you to restrict requests to IPv4?<br /></p>

```
-4
```

5. <p>What switch would give you a more verbose output?<br /></p>

```
-v
```

----------------------------------------

### TASK 6. <span class="badge badge-soft-warning size-16">Networking Tools</span> Traceroute

<p>

  
  
  
  

The logical follow-up to the ping command is 'traceroute'. Traceroute can be used to map the path your request takes as it heads to the target machine.<br /><br />The internet is made up of many, many different servers and end-points, all networked up to each other. This means that, in order to get to the content you actually want, you first need to go through a bunch of other servers. Traceroute allows you to see each of these connections -- it allows you to see every intermediate step between your computer and the resource that you requested. The basic syntax for traceroute on Linux is this: <code>traceroute &lt;destination&gt;</code></p><p>By default, the Windows traceroute utility (<code>tracert</code>) operates using the same ICMP protocol that ping utilises, and the Unix equivalent operates over UDP. This can be altered with switches in both instances.</p><p><img alt="Performing a traceroute to Google.com" style="width:910px" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-15.png" /></p><p>You can see that it took 13 hops to get from my router (<code>_gateway</code>) to the Google server at 216.58.205.46</p><p>Now it's your turn. As with before, all questions about switches can be answered with the man page for traceroute<br />(<code>man traceroute</code>).<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Use traceroute on tryhackme.com<br />Can you see the path your request has taken?</p>

```
OK
```

2. <p>What switch would you use to specify an interface when using Traceroute?<br /></p>

```
-i
```

3. <p>What switch would you use if you wanted to use TCP SYN requests when tracing the route?<br /></p>

```
-T
```

4. <p><b>[Lateral Thinking] </b>Which layer of the <i><b>TCP/IP</b></i> model will traceroute run on by default (Windows)?</p>

```
Internet
```

----------------------------------------

### TASK 7. <span class="badge badge-soft-warning size-16">Networking Tools</span> WHOIS

<p>Domain Names -- the unsung saviours of the internet.</p><p>Can you imagine how it would feel to remember the IP address of every website you want to visit? Horrible thought.</p><p>Fortunately, we've got domains.</p><p>We'll talk a little bit more about how this works in the next task, but for now suffice to know that a domain translates into an IP address so that we don't need to remember it (e.g. you can type tryhackme.com, rather than the TryHackMe IP address). Domains are leased out by companies called Domain Registrars. If you want a domain, you go and register with a registrar, then lease the domain for a certain length of time. </p><p>Enter Whois.</p><p>Whois essentially allows you to query who a domain name is registered to. In Europe personal details are redacted; <span style="font-size:1rem">however, elsewhere you can potentially get a great deal of information from a whois search.</span></p><p>There is a <a href="https://www.whois.com/whois/" target="_blank">web version</a> of the whois tool if you're particularly adverse to the command line. Either way, let's get started!</p><p><i>(Note: You may need to install whois before using it. On Debian based systems this can be done with </i><code>sudo apt update &amp;&amp; sudo apt-get install whois</code><i>)</i></p><p>Whois lookups are very easy to perform. Just use <code>whois &lt;domain&gt;</code> to get a list of available information about the domain registration:</p><p><img style="width:100%" alt="Performing a whois lookup on bbc.co.uk" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-16.png" /></p><p>This is comparatively a very small amount of information as can often be found. Notice that we've got the domain name, the company that registered the domain, the last renewal, and when it's next due, and a bunch of information about nameservers (which we'll look at in the next task).</p><p>Your Turn</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Perform a whois search on facebook.com</p>

```
OK
```

2. <p>What is the registrant postal code for facebook.com?</p>

```
94025
```

3. <p>When was the facebook.com domain first registered?</p>

```
29/03/1997
```

4. <p>Perform a whois search on microsoft.com</p>

```
OK
```

5. <p>Which city is the registrant based in?</p>

```
Redmond
```

6. <p><b>[OSINT] </b>What is the name of the golf course that is near the registrant address for microsoft.com?</p>

```
Bellevue Golf Course
```

7. <p>What is the registered Tech Email for microsoft.com?</p>

```
msnhst@microsoft.com
```

----------------------------------------

### TASK 8. <span class="badge badge-soft-warning size-16">Networking Tools</span> Dig

<p>We talked about domains in the previous task -- now lets talk about how they work.</p>
<p>Ever wondered how a URL gets converted into an IP address that your computer can understand? The answer is a TCP/IP protocol called DNS (<strong>D</strong>omain <strong>N</strong>ame <strong>S</strong>ystem).</p>
<p>At the most basic level, DNS allows us to ask a special server to give us the IP address of the website we're trying to access. For example, if we made a request to www.google.com, our computer would first send a request to a special DNS server (which your computer already knows how to find). The server would then go looking for the IP address for Google and send it back to us. Our computer could then send the request to the IP of the Google server.</p>
<hr />
<p><span class="size" style="font-size:1rem">Let's break this down a bit.</span></p>
<p>You make a request to a website. The first thing that your computer does is check its local cache to see if it's already got an IP address stored for the website; if it does, great. If not, it goes to the next stage of the process.</p>
<p>Assuming the address hasn't already been found, your computer will then send a request to what's known as a <em>recursive</em> DNS server. These will automatically be known to the router on your network. Many Internet Service Providers (ISPs) maintain their own recursive servers, but companies such as Google and OpenDNS also control recursive servers. This is how your computer automatically knows where to send the request for information: details for a recursive DNS server are stored in your router. This server will also maintain a cache of results for popular domains; however, if the website you've requested isn't stored in the cache, the recursive server will pass the request on to a <em>root name</em> server.</p>
<p>There are precisely 13 root name DNS servers in the world. The root name servers essentially keep track of the DNS servers in the next level down, choosing an appropriate one to redirect your request to. These lower level servers are called <em>Top-Level</em> <em>Domain</em> servers.</p>
<p>Top-Level Domain (TLD) servers are split up into extensions. So, for example, if you were searching for tryhackme**.com** your request would be redirected to a TLD server that handled <code>.com</code> domains. If you were searching for bbc**.co.uk** your request would be redirected to a TLD server that handles <code>.co.uk</code> domains. As with root name servers, TLD servers keep track of the next level down: <em>Authoritative name servers</em>. When a TLD server receives your request for information, the server passes it down to an appropriate Authoritative name server.</p>
<p>Authoritative name servers are used to store DNS records for domains directly. In other words, every domain in the world will have its DNS records stored on an Authoritative name server somewhere or another; they are the source of the information. When your request reaches the authoritative name server for the domain you're querying, it will send the relevant information back to you, allowing your computer to connect to the IP address behind the domain you requested.</p>
<hr />
<p><span class="size" style="font-size:1rem">When you visit a website in your web browser this all happens automatically, but we can also do it manually with a tool called </span><code>dig</code><span class="size" style="font-size:1rem"> . Like ping and traceroute, dig should be installed automatically on Linux systems.</span></p>
<p><span class="size" style="font-size:1rem">Dig allows us to manually query recursive DNS servers of our choice for information about domains:</span><br />
<code>dig &lt;domain&gt; @&lt;dns-server-ip&gt;</code><span class="size" style="font-size:1rem"></span></p>
<p>It is a very useful tool for network troubleshooting.</p>
<p><img alt="Performing a DIG DNS lookup on google.com" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/dig-demo.png" /><span class="size" style="font-size:1rem"></span></p>
<p>This is a <em>lot</em> of information. We're currently most interested in the <code>ANSWER</code> section for this room; however, taking the time to learn what the rest of this means is a very good idea. In summary, that information is telling us that we sent it one query and successfully (i.e. No Errors) received one full answer -- which, as expected, contains the IP address for the domain name that we queried.</p>
<p>Another interesting piece of information that dig gives us is the TTL (<strong>T</strong>ime <strong>T</strong>o <strong>L</strong>ive) of the queried DNS record. As mentioned previously, when your computer queries a domain name, it stores the results in its local cache. The TTL of the record tells your computer when to stop considering the record as being valid -- i.e. when it should request the data again, rather than relying on the cached copy.</p>
<p>The TTL can be found in the second column of the answer section:</p>
<p><img alt="Results demonstrating that the TTL of the DNS record is 157" src="https://muirlandoracle.co.uk/wp-content/uploads/2020/03/TTL.png" /></p>
<p>It's important to remember that TTL (in the context of DNS caching) is measured in <em>seconds,</em> so the record in the example will expire in two minutes and thirty-seven seconds.</p>
<p>Have a go at some questions about DNS and dig.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is DNS short for?</p>


```
Domain Name System
```

2. <p>What is the first type of DNS server your computer would query when you search for a domain?</p>


```
Recursive
```

3. <p>What type of DNS server contains records specific to domain extensions (i.e. <em>.com,</em> .co.uk*, etc)*? Use the long version of the name.</p>


```
Top-Level Domain
```

4. <p>Where is the very first place your computer would look to find the IP address of a domain?</p>


```
Local Cache
```

5. <p><strong>[Research]</strong> <span class="size" style="font-size:1rem">Google runs two public DNS servers. One of them can be queried with the IP 8.8.8.8, what is the IP address of the other one?</span></p>


```
8.8.4.4
```

6. <p>If a DNS query has a TTL of 24 hours, what number would the dig query show?</p>


```
86400
```

----------------------------------------

### TASK 9. Further Reading

<p>That's us completed our whirlwind tour of networking basics. Hopefully you've found it informative!</p><p>Networking is one of those things that you just need to learn. We've covered the very basics, but it would be a very good idea to continue to learn by yourself.</p><p>In terms of further information, feel free to reach out in the TryHackMe Discord if you want any help with the contents of this room. Additionally, if you want to expand your knowledge of networking theory, the <a href="https://www.amazon.co.uk/Interconnecting-Cisco-Network-Devices-ICND1/dp/1587054620/ref=sr_1_1?keywords=Interconnecting+Cisco+Network+Devices%2C+Part+1&amp;qid=1583683766&amp;sr=8-1" target="_blank">CISCO Self Study Guide by Steve McQuerry</a> is a great resource to work from. There may be a more up to date version available; however, this edition is cheap, readily available, and most importantly, still very relevant. Whilst it is designed to as a study guide for the CCNA exam, that book serves equally well as a very rounded introduction to networking principles.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the final thoughts<br /></p>

```
OK
```


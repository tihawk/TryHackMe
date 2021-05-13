# TryHackMe walkthrough

## Burp Suite

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Intro

<p>Burp Suite, a framework of web application pentesting tools, is widely regarded as the de facto tool to use when performing web app testing. Throughout this room, we'll take a look at the basics of installing and using this tool as well as it's various major components. Reference links to the associated documentation per section have been provided at the bottom of most tasks throughout this room. </p><p style="text-align:center"><img src="https://i.imgur.com/Y75lHH6.png" style="width:402.5px;float:none;height:90.5602px" /></p><p style="text-align:center"><span style="color:rgb(33, 37, 41);font-size:1rem">-----------------------------------------</span></p><p style="color:rgb(33, 37, 41);text-align:center"><span style="font-size:1rem"><i>Prior to attempting this room, I highly recommend checking out the '<a href="https://tryhackme.com/room/webfundamentals" target="_blank">Web Fundamentals</a>' room. If you are familiar with basic web request structure and SQL injection, you're already set!</i></span></p><p style="color:rgb(33, 37, 41);text-align:center"><i><span style="font-size:12px">Enjoy the room! For future rooms and write-ups, follow </span><a href="https://twitter.com/darkstar7471"><span style="font-size:12px">@darkstar7471</span></a><span style="font-size:12px"> on Twitter.</span></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the overview and continue on into installation!</p>

```
OK
```

----------------------------------------

### TASK 2. Installation

<p>Before we can dive into the pretty amazing tool that is Burp Suite, we'll first have to install it. Lucky for us, if you're doing this room on Kali Linux you'll already have Burp Suite installed. Since this room is entirely do-able on Windows as well, we'll briefly touch on obtaining Burp Suite (community edition) for any system as it's fairly painless. <b>You can also use <u>deploy your own <a href="https://tryhackme.com/my-machine" target="_blank">in-browser machine</a></u> with BurpSuite already installed!</b></p><p>If you'll be installing Burp (as it's commonly referred to) from scratch, you'll need to first visit this link: <a href="https://portswigger.net/burp/communitydownload">https://portswigger.net/burp/communitydownload</a><a href="https://portswigger.net/burp/communitydownload"></a><br /><br /></p><p style="text-align:center;"><img src="https://i.imgur.com/eC0QU3m.png" style="width:25%;" /><br /></p><p style="text-align:center;"><i><br />We'll use the Burp Suite Community Edition throughout this lab, however, I'll be covering some paid features briefly as well to help you prepare for eventually using the Professional version.</i></p><p style="text-align:center;"><i>Burp Suite Getting Started Documentation: </i><a href="https://portswigger.net/burp/documentation/desktop/getting-started" target="_blank"><i>Link</i></a></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p><span style="color:rgb(0, 0, 0);">If you'll be installing Burp (as it's commonly referred to) from scratch, you'll need to first visit this link: </span><a href="https://portswigger.net/burp/communitydownload">https://portswigger.net/burp/communitydownload</a><br /></p>

```
OK
```

2. <p>Once you've reached the Port Swigger downloads page, go ahead and download the appropriate version for your operating system</p>

```
OK
```

3. <p>Burp Suite requires Java JRE in order to run. Download and install Java here: <a href="https://www.java.com/en/download/">https://www.java.com/en/download/</a><a href="https://www.java.com/en/download/"></a></p><p><span style="font-size:1rem;">Once you've got everything setup move onto our next task, Gettin' [CA] Certified!</span><br /></p>

```
OK
```

----------------------------------------

### TASK 3. Gettin' [CA] Certified

<p style="text-align:center;">Before we can start using our new installation (or preinstalled) Burp Suite, we'll have to fix a certificate warning. We need to install a CA certificate as BurpSuite acts as a proxy between your browser and sending it through the internet - It allows the BurpSuite Application to read and send on HTTPS data. </p><p style="text-align:center;"><img src="https://i.imgur.com/lGnJ2ym.png" style="width:738px;height:272.958px;" /></p><p style="text-align:center;"><i>A certificate warning that will appear unless we install Burp's CA Certificate.</i></p><p style="text-align:center;"><b>One quick note, in this lab I'll be using Firefox and Foxy Proxy</b> (which you can find <a href="https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/" target="_blank">here</a>). I use Firefox in this instance as it's a little bit easier to work with when using Burp Suite. </p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>First, let's go ahead and launch Burp. We can do this on Kali via the icon on the left side. In the image below it's the seventh icon from the top on the left-hand side. <b>If your Kali desktop doesn't look like the screenshot below, click on 'Applications' and type in Burp Suite. Click on the Burp Suite icon that appears.</b></p><p><img src="https://i.imgur.com/CWK5CAr.png" style="width:619px;float:none;height:348.014px;" /></p><p>Launch Burp!</p>

```
OK
```

2. <p>Once you've launched Burp, you'll be greeted with the following screen:</p><p><img src="https://i.imgur.com/khINgRw.png" style="width:625px;height:402.151px;" /></p><p>Once this pops-up, click 'Temporary project' and then 'Next'.</p><p><i>*Now as you likely noticed both 'New project on disk' and 'Open existing project' are both grayed out. As annotated at the top of this window saving projects is a feature associated with Burp Suite Professional as it's pretty common to save and come back to a multi-day web application test. </i></p>

```
OK
```

3. <p>Next, we'll be prompted to ask for what configuration we'd like to use. For now, select 'Use Burp defaults'.</p><p><img src="https://i.imgur.com/mdX4629.png" style="width:635px;height:404.575px;" /></p><p><i>This option is included as it can be incredibly useful to create a custom configuration file for your proxy or other settings, especially depending on how your network configuration and/or if Burp Suite is being launched remotely such as via <a href="https://www.youtube.com/watch?v=auePeI8vZA8" target="_blank">x11 forwarding</a>. </i><br /></p>

```
OK
```

4. <p>Finally, let's go ahead and Start Burp! Click 'Start Burp' now!</p>

```
OK
```

5. <p>You'll now see a screen that looks similar to this:</p><p><img src="https://i.imgur.com/L1Fzfwa.png" style="width:642px;height:318.552px;" /></p><p>Since we now have Burp Suite running, the proxy service will have started by default with it. In order to fully leverage this proxy, we'll have to install the CA certificate included with Burp Suite (otherwise we won't be able to load anything with SSL). To do this, let's launch Firefox now!</p><p><i>*You can do this part with your browser of choice, however, I'll be using Firefox for this room.</i></p>

```
OK
```

6. <p>Now that we've started Burp, let's add an extension to our web browser to allow up to easily route or traffic through it! For this room, we'll be using 'FoxyProxy Standard' on Firefox.</p><p><img src="https://i.imgur.com/kiMG1am.png" style="width:638px;height:299.754px;" /></p><p>Navigate to the following link to install FoxyProxy Standard: <a href="https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/" target="_blank">Link</a></p><p>Go ahead and install this now!</p>

```
OK
```

7. <p>Next, click on FoxyProxy among your extensions. </p><p><img src="https://i.imgur.com/zbh4iYt.png" style="width:216px;" /></p><p>After that, click on 'Options'.</p><p><img src="https://i.imgur.com/V4bvfeC.png" style="font-size:1rem;width:368px;" /><br /></p><p>After that, click 'Add' in the top left. </p><p><img src="https://i.imgur.com/tAhmMgv.png" style="width:108px;" /><br /><br /></p><p>Enter in the following settings and then click 'Save'</p><p><img src="https://i.imgur.com/WGLIDVh.png" style="width:750px;" /></p><p>Finally, click on the FoxyProxy extension icon again and select 'Burp'.</p><p><img src="https://i.imgur.com/V4bvfeC.png" style="width:368px;" /></p><p><i>In the image above Burp isn't selected. Make sure it is in yours!</i></p><p>Next, we'll move onto adding the certificate for Burp!</p>

```
OK
```

8. <p>With Firefox, navigate to the following address: http://localhost:8080<br /></p>

```
OK
```

9. <p>You'll be greeted with the following website:</p><p><img src="https://i.imgur.com/mjmAT34.png" style="font-size:1rem;width:750px;" /><br /></p><p>Click on 'CA Certificate' in the top right to download and save the CA Certificate.</p>

```
OK
```

10. <p>Now that we've downloaded the CA Certificate, move over to the settings menu in Firefox. Search for 'Certificates' in the search bar.</p><p><img src="https://i.imgur.com/RHihhWS.png" style="width:750px;" /></p><p>Click on 'View Certificates'</p>

```
OK
```

11. <p>Next, in the Authorities tab click on 'Import'<br /></p>

```
OK
```

12. <p>Navigate to where you saved the CA Certificate we downloaded previously. Click 'OK' once you've selected this certificate.<br /></p>

```
OK
```

13. <p>Finally, select the following two options seen in this photo:</p><p><img src="https://i.imgur.com/gULEdau.png" style="width:691px;height:366.291px;" /></p><p>Select 'OK' once you've done this. Congrats, we've now installed the Burp Suite CA Certificate!</p>

```
OK
```

----------------------------------------

### TASK 4. Overview of Features

<p>Now that we've set up Burp, let's take a look at everything it has to offer. Web application pentesting can be a messy affair but Burp has something for every step of the way. </p><p style="text-align:center;"><img src="https://i.imgur.com/n9ftVf5.jpg" style="width:397.5px;height:298.125px;" /><br /><i><a href="https://dribbble.com/shots/4887261-Tools" target="_blank"><span style="font-size:12px;">Tools by Ana Miminoshvili on Dribbble</span></a></i></p><p>Throughout this room, we'll be taking a look at these components of Burp Suite. Here's a quick overview of each section covered:</p><ul><li><b>Proxy</b> - What allows us to funnel traffic through Burp Suite for further analysis</li><li><b>Target</b> - How we set the scope of our project. We can also use this to effectively create a site map of the application we are testing.</li><li><b>Intruder</b> - Incredibly powerful tool for everything from field fuzzing to credential stuffing and more</li><li><b>Repeater</b> - Allows us to 'repeat' requests that have previously been made with or without modification. Often used in a precursor step to fuzzing with the aforementioned Intruder</li><li><b>Sequencer</b> - Analyzes the 'randomness' present in parts of the web app which are intended to be unpredictable. This is commonly used for testing session cookies</li><li><b>Decoder</b> - As the name suggests, Decoder is a tool that allows us to perform various transforms on pieces of data. These transforms vary from decoding/encoding to various bases or URL encoding.</li><li><b>Comparer</b> - Comparer as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site maps or proxy histories (awesome for access control issue testing). This is very similar to the Linux tool diff.</li><li><b>Extender</b> - Similar to adding mods to a game like Minecraft, Extender allows us to add components such as tool integrations, additional scan definitions, and more!</li><li><b>Scanner</b> - Automated web vulnerability scanner that can highlight areas of the application for further manual investigation or possible exploitation with another section of Burp. This feature, while not in the community edition of Burp Suite, is still a key facet of performing a web application test.</li></ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Which tool in Burp Suite can we use to perform a 'diff' on responses and other pieces of data?</p>

```
Comparer
```

2. <p>What tool could we use to analyze randomness in different pieces of data such as password reset tokens?</p>

```
Sequencer
```

3. <p>Which tool can we use to set the scope of our project?</p>

```
Target
```

4. <p>While only available in the premium versions of Burp Suite, which tool can we use to automatically identify different vulnerabilities in the application we are examining?</p>

```
Scanner
```

5. Encoding or decoding data can be particularly useful when examining URL parameters or protections on a form, which tool allows us to do just that?

```
Decoder
```

6. <p>Which tool allows us to redirect our web traffic into Burp for further examination?</p>

```
Proxy
```

7. Simple in concept but powerful in execution, which tool allows us to reissue requests?

```
Repeater
```

8. <p>With four modes, which tool in Burp can we use for a variety of purposes such as field fuzzing?</p>

```
Intruder
```

9. <p>Last but certainly not least, which tool allows us to modify Burp Suite via the addition of extensions?</p>

```
Extender
```

----------------------------------------

### TASK 5. Engage Dark Mode 

<p>Working on a project late at night? Fear no more! In this task we'll cover how to enable dark mode in Burp Suite!</p><p style="text-align:center;"><img src="https://i.imgur.com/bYTco2N.jpg" style="width:361.5px;height:271.125px;" /><br /><i><a href="https://dribbble.com/shots/10374655-Work-Hard" target="_blank"><span style="font-size:12px;">Work Hard by Uran on Dribbble</span></a></i></p><p><i><b>This task is optional! You can simply click 'Complete' on all of the questions if you'd like to skip it. This section is purely for 'quality of life' improvements while using Burp Suite throughout this room. You can see what dark mode looks like in question three of task eight.</b></i></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>With Burp Suite launched, let's first navigate to the 'User options' tab. </p><p><img src="https://i.imgur.com/X1taDml.png" style="width:227px;" /></p>

```
OK
```

2. <p>Next, click on the 'Display' sub-tab. </p><p><img src="https://i.imgur.com/qBjFHIJ.png" style="width:255px;" /></p>

```
OK
```

3. <p>Now, click on the 'Look and feel' drop-down menu. Select 'Darcula'. </p><p><img src="https://i.imgur.com/AKfuDZt.png" style="width:412px;" /></p>

```
OK
```

4. <p>Finally, close and relaunch Burp Suite to have dark theme (or whichever theme you picked) take effect.</p>

```
OK
```

----------------------------------------

### TASK 6. Proxy

<p>Generally speaking, proxy servers by definition allow us to relay our traffic through an alternative route to the internet. This can be done for a variety of reasons ranging from educational filtering (common in schools where restricted content must be blocked) to accessing content that may be otherwise unavailable due to region locking or a ban. Using a proxy, however, for web application testing allows us to view and modify traffic inline at a granular level. Throughout this task, we'll explore the major components of the Burp proxy including interception, request history, and the various configuration options we have access to. </p><p style="text-align:center;"><img src="https://i.imgur.com/WTibvB7.png" style="width:50%;" /></p><p style="text-align:center;"><i>Basic diagram of how communications are relayed through a proxy - <a href="https://en.wikipedia.org/wiki/Proxy_server" target="_blank">Wikipedia - Proxy Servers</a></i></p><p></p><p>In task three, Gettin' [CA] Certified, we configured our web traffic to route through our instance of Burp Suite. By default, Burp will be set to 'intercept' our traffic. This means a few things:</p><p>1. Requests will by default require our authorization to be sent.</p><p>2. We can modify our requests in-line similar to what you might see in a man-in-the-middle attack and then send them on.</p><p>3. We can also drop requests we don't want to be sent. This can be useful to see the request attempt after clicking a button or performing another action on the website. </p><p>4. And last but not least, we can send these requests to other tools such as Repeater and Intruder for modification and manipulation to induce vulnerabilities. </p><p style="text-align:center;"><i>Burp Suite reference documentation for Proxy: <a href="https://portswigger.net/burp/documentation/desktop/tools/proxy" target="_blank">Link</a></i></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Deploy the VM attached to this task!</p><p>To complete this task you need to connect to the TryHackMe network through <a href="https://tryhackme.com/connect" target="_blank">OpenVPN</a>. If you're using the <a href="https://tryhackme.com/my-machine" target="_blank">in-browser</a> machine this isn't needed (but make sure you're accessing the machine and using Burp inside the in-browser machine).</p>

```
OK
```

2. <p>By default, the Burp Suite proxy listens on only one interface. What is it? <i>Use the format of IP:PORT</i><br /></p>

```
127.0.0.1:8080
```

3. In Burp Suite, navigate to the Intercept sub-tab of the Proxy section. Enable Intercept

```
OK
```

4. <p>Return to your web browser and navigate to the web application hosted on the VM we deployed just a bit ago. Note that the page appears to be continuously loading. Change back to Burp Suite, we now have a request that's waiting in our intercept tab. Take a look at the actions, which <b>shortcut</b> allows us to forward the request to Repeater?<br /></p>

```
CTRL-R
```

5. <p>How about if we wanted to forward our request to Intruder?</p>

```
CTRL-I
```

6. <p>Burp Suite saves the history of requests sent through the proxy along with their varying details. This can be especially useful when we need to have proof of our actions throughout a penetration test or we want to modify and resend a request we sent a while back. What is the name of the first section wherein general web requests (GET/POST) are saved?</p>

```
HTTP history
```

7. <p>Defined in RFC 6455 as a low-latency communication protocol that doesn't require HTTP encapsulation, what is the name of the second section of our saved history in Burp Suite? These are commonly used in collaborate application which require real-time updates (Google Docs is an excellent example here).</p>

```
WebSockets history
```

8. <p>Before we move onto exploring our target definition, let's take a look at some of the advanced customization we can utilize in the Burp proxy. Move over to the Options section of the Proxy tab and scroll down to Intercept Client Requests. Here we can apply further fine-grained rules to define which requests we would like to intercept. Perhaps the most useful out of the default rules is our only AND rule. What is it's match type?</p>

```
URL
```

9. <p>How about it's 'Relationship'? <i>In this situation, enabling this match rule can be incredibly useful following target definition as we can effectively leave intercept on permanently (unless we need to navigate without intercept) as it won't disturb sites which are outside of our scope - something which is particularly nice if we need to Google something in the same browser.</i></p>

```
Is in target scope
```

----------------------------------------

### TASK 7. Target Definition

<p>Perhaps the most important feature in Burp Suite, we'll now be turning our focus to the Target tab!</p><p style="text-align:center"><img src="https://i.imgur.com/7y8S1zs.jpg" style="width:308.438px;height:231.328px" /><br /><i><a href="https://dribbble.com/shots/2363233-Lock-On-Target" target="_blank"><span style="font-size:12px">Lock on Target by </span></a></i><span style="text-align:left;font-size:12px"><i><a href="https://dribbble.com/shots/2363233-Lock-On-Target" target="_blank">Alexei Vella on Dribbble</a></i></span></p><p>The Target tab in Burp allows us to perform arguably some of the most important parts of a web application penetration test: defining our scope, viewing a site map, and specifying our issue definitions (although this is more useful within report generation and scanning). </p><p>When starting a web application test you'll very likely be provided a few things:</p><p style="margin-left:25px">- The application URL (hopefully for dev/test and not prod)<br /><span style="font-size:1rem">- A list of the different user roles within the application<br /></span><span style="font-size:1rem">- Various test accounts and associated credentials for those accounts<br /></span><span style="font-size:1rem">- A list of pieces/forms in the application which are out-of-scope for testing and should be avoided</span></p><p>From this information, we can now start to build our scope within Burp, something which is incredibly important in the case we are planning on performing any automated testing. Typically this is done in a tiered approach wherein we work our way up from the lowest privileged account (this includes unauthenticated access), browsing the site as a normal user would. Browsing like this to discover the full extent of the site is commonly referenced as the 'happy path'. Following the creation of a site map via browsing the happy path, we can go through and start removing various items from the scope. These items typically fit one of these criteria:</p><p style="margin-left:25px">- The item (page, form, etc) has been designated as out of scope in the provided documentation from the client<br /><span style="font-size:1rem">- Automated exploitation of the item (especially in a credentialed manner) would cause a huge mess (like sending hundreds of password reset emails - If you've done a web app professionally you've probably done this at one point)<br /></span><span style="font-size:1rem">- Automated exploitation of the item (especially in a credentialed manner) would lead to damaging and potentially crashing the web app</span></p><p>Once we've removed any restricted or otherwise potentially dangerous items from our scope, we can move onto other areas of testing with the various tools within Burp Suite.</p><p style="text-align:center"><i>Burp Suite reference documentation for Target: <a href="https://portswigger.net/burp/documentation/desktop/tools/target" target="_blank">Link</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Before leaving the Proxy tab, switch Intercept to disabled. We'll still see the pages we navigate to in our history and the target tab, just having Intercept constantly stopping our requests for this next bit will get old fast.</p>

```
OK
```

2. <p>Navigate to the Target tab in Burp. In our last task, Proxy, we browsed to the website on our target machine (in this case OWASP Juice Shop). Find our target site in this list and right-click on it. Select 'Add to scope'. <br /></p>

```
OK
```

3. <p>Clicking 'Add to scope' will trigger a pop-up. This will stop Burp from sending out-of-scope items to our site map.</p>

```
OK
```

4. Select 'Yes' to close the popup.

```
OK
```

5. <p>Browse around the rest of the application to build out our page structure in the target tab. Once you've visited most of the pages of the site return to Burp Suite and expand the various levels of the application directory. What do we call this representation of the collective web application?</p>

```
site map
```

6. <p>What is the term for browsing the application as a normal user prior to examining it further?</p>

```
happy path
```

7. One last thing before moving on. Within the target tab, you may have noticed a sub-tab for issue definitions. Click into that now.

```
OK
```

8. <p>The issue definitions found here are how Burp Suite defines issues within reporting. While getting started, these issue definitions can be particularly helpful for understanding and categorizing various findings we might have. Which poisoning issue arises when an application behind a cache process input that is not included in the cache key?<br /></p>

```
Web cache poisoning
```

----------------------------------------

### TASK 8. Puttin' it on Repeat[er]

<p>As the name suggests, Repeater allows us to repeat requests we've already made. These requests can either be reissued as-is or with modifications. In contrast to Intruder, Repeater is typically used for the purposes of experimentation or more fine-tuned exploitation wherein automation may not be desired. We'll be checking out Repeater with the goal of finding a proof of concept demonstrating that Juice Shop is vulnerable to SQL injection.</p><p style="text-align:center;"><img src="https://i.imgur.com/V4JaiLm.png" style="width:351.104px;height:263.328px;" /><br /><i><a href="https://dribbble.com/shots/10090741-Record-Player" target="_blank"><span style="font-size:12px;">Record Player by Briton Baker on Dribbble</span></a></i></p><p style="text-align:center;"><i>Burp Suite reference documentation for Repeater: <a href="https://portswigger.net/burp/documentation/desktop/tools/repeater" target="_blank">Link</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>To start, click 'Account' (this might be 'Login' depending on the version of Juice Shop) in the top right corner of Juice Shop in order to navigate to the login page.</p><p><img src="https://i.imgur.com/73ONVlh.png" style="width:132px;" /></p>

```
OK
```

2. <p>Try logging in with invalid credentials. What error is generated when login fails?</p><p><img src="https://i.imgur.com/52rkIqO.png" style="width:451.643px;height:417px;" /></p>

```
Invalid email or password.
```

3. <p>But wait, didn't we want to send that request to Repeater? Even though we didn't send it to Repeater initially via intercept, we can still find the request in our history. Switch over to the HTTP sub-tab of Proxy. Look through these requests until you find our failed login attempt. <b>Right-click on this request and send it to Repeater and then send it to Intruder, too!</b></p><p><img src="https://i.imgur.com/o0NcPLH.png" style="width:600px;" /><b></b></p>

```
OK
```

4. <p>Now that we've sent the request to Repeater, let's try adjusting the request such that we are sending a single quote (') as both the email and password. What error is generated from this request?</p><p><img src="https://i.imgur.com/GgRXizc.png" style="width:583px;" /></p>

```
SQLITE_ERROR
```

5. <p>Now that we've leveraged Repeater to gain proof of concept that Juice Shop's login is vulnerable to SQLi, let's try something a little more mischievous and attempt to leave a devastating zero-star review. First, click on the drawer button in the top-left of the application. <b>If this isn't present for you, just skip to the next question.</b></p><p><img src="https://i.imgur.com/eu0bjOY.png" style="width:78px;" /></p>

```
OK
```

6. <p>Next, click on 'Customer Feedback' (depending on the version of Juice Shop this also might be along the top of the page next to 'Login' under 'Contact Us')</p><p><img src="https://i.imgur.com/Nj3fuuZ.png" style="width:285px;" /></p>

```
OK
```

7. <p>With the Burp proxy on submit feedback. Once this is done, find the POST request in your HTTP History in Burp and send it to Repeater.</p>

```
OK
```

8. <p>What field do we have to modify in order to submit a zero-star review?</p>

```
rating
```

9. <p>Submit a zero-star review and complete this challenge in Juice Shop!</p>

```
OK
```

----------------------------------------

### TASK 9. Help! There's an Intruder!

<p>Arguably the most powerful tool in Burp Suite, Intruder can be used for many things ranging from fuzzing to brute-forcing. At its core, Intruder serves one purpose: automation. </p><p>While Repeater best handles experimentation or one-off testing, Intruder is meant for repeat testing once a proof of concept has been established. Per the <a href="https://portswigger.net/burp/documentation/desktop/tools/intruder/using" target="_blank">Burp Suite documentation</a>, some common uses are as follows:</p><p style="margin-left:25px;">- Enumerating identifiers such as usernames, cycling through predictable session/password recovery tokens, and attempting simple password guessing<br /><span style="font-size:1rem;">- Harvesting useful data from user profiles or other pages of interest via grepping our responses<br /></span><span style="font-size:1rem;">- Fuzzing for vulnerabilities such as SQL injection, cross-site scripting (XSS), and file path traversal</span></p><p style="text-align:center;"><img src="https://i.imgur.com/hBUkjo9.jpg" style="width:385.771px;height:289.328px;" /><br /><i><span style="font-size:12px;"><a href="https://dribbble.com/shots/2384392-The-Overcoat-Nikolai-Gogol-Illustration" target="_blank">The Overcoat by Chill Desk on Dribbble</a></span></i></p><p><span style="font-size:1rem;">To accomplish these various use cases, Intruder has <a href="https://portswigger.net/burp/documentation/desktop/tools/intruder/positions" target="_blank">four</a> different attack types:</span><br /></p><p>1. <i>Sniper</i> - The most popular attack type, this cycles through our selected positions, putting the next available payload (item from our wordlist) in each position in turn. This uses only one set of payloads (one wordlist).</p><p>2. <i>Battering Ram</i> - Similar to Sniper, Battering Ram uses only one set of payloads. Unlike Sniper, Battering Ram puts every payload into every selected position. Think about how a battering ram makes contact across a large surface with a single surface, hence the name battering ram for this attack type.</p><p>3. <i>Pitchfork</i> - The Pitchfork attack type allows us to use multiple payload sets (one per position selected) and iterate through both payload sets <i>simultaneously</i>. For example, if we selected two positions (say a username field and a password field), we can provide a username and password payload list. Intruder will then cycle through the combinations of usernames and passwords, resulting in a total number of combinations equalling the smallest payload set provided.<i> </i></p><p>4. <i>Cluster Bomb</i> - <span style="font-size:1rem;">The Cluster Bomb attack type allows us to use multiple payload sets</span><span style="font-size:1rem;"> </span><span style="font-size:1rem;">(one per position selected)</span><span style="font-size:1rem;"> and iterate through all combinations of the payload lists we provide. For example, if we selected two positions (say a username field and a password field), we can provide a username and password payload list. Intruder will then cycle through the combinations of usernames and passwords, resulting in a total number of combinations equalling usernames x passwords.</span><span style="font-size:1rem;"> </span><i>Do note, this can get pretty lengthy if you are using the community edition of Burp. </i></p><p style="text-align:center;"><img src="https://i.imgur.com/cYXHREg.png" style="width:238px;" /><br /><i>Intruder Attack Type Selection</i></p><p>For our purposes, we'll be returning to the SQL injection vulnerability we previously discovered through using Repeater. </p><p style="text-align:center;"><i>For some additional practice on using Intruder, check out the older <a href="https://tryhackme.com/room/learnburp" target="_blank">Learn Burp Suite room</a> here on TryHackMe</i></p><p style="text-align:center;"><i>Burp Suite reference documentation for Intruder: <a href="https://portswigger.net/burp/documentation/desktop/tools/intruder" target="_blank">Link</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Which attack type allows us to select multiple payload sets (one per position) and iterate through them simultaneously?</p>

```
Pitchfork
```

2. How about the attack type which allows us to use one payload set in every single position we've selected simultaneously?

```
Battering Ram
```

3. <p>Which attack type allows us to select multiple payload sets (one per position) and iterate through all possible combinations?<br /></p>

```
Cluster Bomb
```

4. <p>Perhaps the most commonly used, which attack type allows us to cycle through our payload set, <span style="color:rgb(0, 0, 0);font-size:1rem;">putting the next available payload in each position in turn?</span></p>

```
Sniper
```

5. <p>Download the wordlist attached to this room, this is a shortened version of the <a href="https://github.com/fuzzdb-project/fuzzdb/blob/master/attack/sql-injection/detect/xplatform.txt" target="_blank">fuzzdb SQLi platform detection list</a>.</p>

```
OK
```

6. <p>Return to the Intruder in Burp. In our previous task, we passed our failed login attempt to both Repeater and Intruder for further examination. Open up the Positions sub-tab in the Intruder tab with this request now and verify that 'Sniper' is selected as our attack type.</p><p><img src="https://i.imgur.com/Derove4.png" style="width:180px;" /></p>

```
OK
```

7. <p>Burp attempts to automatically highlight possible fields of interest for Intruder, however, it doesn't have it quite right for what we'll be looking at in this instance. Hit 'Clear' on the right-hand side to clear all selected fields.</p><p><img src="https://i.imgur.com/C8Yect8.png" style="width:131px;" /></p>

```
OK
```

8. <p>Next, let's highlight the email field between the double quotes ("). <i>This will be whatever you entered in the email field for our previous failed login attempt.</i></p><p><img src="https://i.imgur.com/zVrLe4O.png" style="width:884px;" /><i></i></p>

```
OK
```

9. <p>Now click 'Add' to select our email field as a position for our payloads.</p><p><img src="https://i.imgur.com/3Y0CErR.png" style="width:130px;" /></p>

```
OK
```

10. <p>Next, let's switch to the payloads sub-tab of Intruder. Once there, hit 'Load' and select the wordlist you previously downloaded in question five that is attached to this task.</p><p><img src="https://i.imgur.com/PJ2d8UP.png" style="width:570px;" /></p>

```
OK
```

11. <p>Almost there! Scroll down and uncheck 'URL-encode these characters'. We don't want to have the characters sent in our payloads to be encoded as they otherwise won't be recognized by SQL.</p><p><img src="https://i.imgur.com/IuHzsZO.png" style="width:840px;" /></p>

```
OK
```

12. <p>Finally, click 'Start attack'. What is the first payload that returns a 200 status code, showing that we have successfully bypassed authentication?</p>

```
a' OR 1=1--
```

----------------------------------------

### TASK 10. As it turns out the machines are better at math than us

<p>While not as commonly used in a practice environment, Sequencer represents a core tool in a proper web application pentest. Burp's Sequencer, <a href="https://portswigger.net/burp/documentation/desktop/tools/sequencer/getting-started" target="_blank">per the Burp documentation</a>, is a tool for analyzing the quality of randomness in an application's sessions tokens and other important data items that are otherwise intended to be unpredictable. Some commonly analyzed items include:</p><p style="margin-left:25px">- Session tokens<br /><span style="font-size:1rem">- Anti-CSRF (Cross-Site Request Forgery) tokens<br /></span><span style="font-size:1rem">- Password reset tokens (sent with password resets that in theory uniquely tie users with their password reset requests)</span></p><p>We'll take a quick peek at how we can use Sequencer to examine the session cookies which Juice Shop issues.</p><p style="text-align:center"><img src="https://i.imgur.com/Rf03DAu.png" style="width:351.5px;height:263.625px" /><br /><i><span style="font-size:12px"><a href="https://dribbble.com/shots/4033707-SEO-Friendly-Progressive-Web-Applications-with-Angular-Universal" target="_blank">SEO Friendly Progressive Web Applications with Angular Universal by Maxime Bourgeois on Dribbble</a></span></i></p><p style="text-align:center"><i>Burp Suite reference documentation for Sequencer: <a href="https://portswigger.net/burp/documentation/desktop/tools/sequencer" target="_blank">Link</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Switch over to the HTTP history sub-tab of Proxy. </p>

```
OK
```

2. <p>We're going to dig for a <b>response</b> which issues a cookie. Parse through the various responses we've received from Juice Shop until you find one that includes a 'Set-Cookie' header. <br /></p>

```
OK
```

3. <p>Once you've found a request response that issues a cookie, right-click on the request and select 'Send to Sequencer'.</p>

```
OK
```

4. <p>Change over Sequencer and select 'Start live capture'</p>

```
OK
```

5. <p>Let Sequencer run and collect ~10,000 requests. Once it hits roughly that amount hit 'Pause' and then 'Analyze now'</p>

```
OK
```

6. <p>Parse through the results. What is the effective estimated entropy measured in?</p>

```
bits
```

7. <p>In order to find the usable bits of entropy we often have to make some adjustments to have a normalized dataset. What item is converted in this process?</p>

```
token
```

8. <p>Read through the remaining results of the token analysis</p>

```
OK
```

----------------------------------------

### TASK 11. Decoder and Comparer

<p>Decoder and Comparer, while lesser tools within Burp Suite, are still essential to understand and leverage as part of being a proficient web app tester. </p><p>As the name suggests, Decoder is a tool that allows us to perform various transforms on pieces of data. These transforms vary from decoding/encoding to various bases or URL encoding. We chain these transforms together and Decoder will automatically spawn an additional tier each time we select a decoder, encoder, or hash.<i> This tool ultimately functions very similarly to <a href="https://gchq.github.io/CyberChef/" target="_blank">CyberChef</a>, albeit slightly less powerful.</i></p><p style="text-align:center;"><img src="https://i.imgur.com/81fJqyC.png" style="width:391.5px;height:293.625px;" /><br /><i><span style="font-size:12px;"><a href="https://dribbble.com/shots/6549514-Encryption" target="_blank">Encryption by Muriel on Dribbble</a></span></i></p><p>Similarly, Comparer, as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site maps or proxy histories (awesome for access control issue testing). This is very similar to the Linux tool diff.</p><p>Per the Burp <a href="https://portswigger.net/burp/documentation/desktop/tools/comparer" target="_blank">documentation</a>, some common uses for Comparer are as follows:</p><p>- When looking for username enumeration conditions, you can compare responses to failed logins using valid and invalid usernames, looking for subtle differences in responses. <i>This is also sometimes useful for when enumerating password recovery forms or another similar recovery/account access mechanism. </i></p><p>- When an Intruder attack has resulted in some very large responses with different lengths than the base response, you can compare these to quickly see where the differences lie.</p><p>- When comparing the site maps or Proxy history entries generated by different types of users, you can compare pairs of similar requests to see where the differences lie that give rise to different application behavior. This may reveal possible access control issues in the application wherein lower privileged users can access pages they really shouldn't be able to.</p><p>- When testing for blind SQL injection bugs using Boolean condition injection and other similar tests, you can compare two responses to see whether injecting different conditions has resulted in a relevant difference in responses.</p><p><i>*These examples are taken nearly in their entirety from the Burp docs simply to provide a broader set of examples to consider when using Comparer.</i></p><p style="text-align:center;"><img src="https://i.imgur.com/xUTJWS6.png" style="width:369.5px;height:277.125px;" /><br /><i><span style="font-size:12px;"><a href="https://dribbble.com/shots/3551926-JavaScript-Arrays-in-Depth" target="_blank">JavaScript Arrays in Depth by Maxime Bourgeois on Dribbble</a></span></i></p><p style="text-align:center;"><i>Burp Suite reference documentation for <a href="https://portswigger.net/burp/documentation/desktop/tools/decoder" target="_blank">Decoder</a> and <a href="https://portswigger.net/burp/documentation/desktop/tools/comparer" target="_blank">Comparer</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Let's first take a look at decoder by revisiting an old friend. Previously we discovered the scoreboard within the site JavaScript. Return to our target tab and find the API endpoint highlighted in the following request:</p><p><img src="https://i.imgur.com/8gU45ZO.png" style="width:227px;" /></p>

```
OK
```

2. <p>Copy the first line of that request and paste it into Decoder. Next, select 'Decode as ...' URL</p>

```
OK
```

3. <p>What character does the %20 in the request we copied into Decoder decode as?</p>

```
Space
```

4. <p>Similar to CyberChef, Decoder also has a 'Magic' mode where it will automatically attempt to decode the input it is provided. What is this mode called? </p>

```
Smart Decode
```

5. <p>What can we load into Comparer to see differences in what various user roles can access? <i>This is very useful to check for access control issues.</i></p>

```
site maps
```

6. <p>Comparer can perform a diff against two different metrics, which one allows us to examine the data loaded in as-is rather than breaking it down into bytes?</p>

```
Words
```

----------------------------------------

### TASK 12. Installing some Mods [Extender]

<p><span style="color:rgb(33, 37, 41);">Similar to adding mods to a game like Minecraft, Extender allows us to add components such as tool integrations, additional scan definitions, and more! Here are some of the most popular extensions I suggest checking out (not all of these are free but I suggest looking into them all the same):</span><br /></p><ul><li><a href="https://portswigger.net/bappstore/470b7057b86f41c396a97903377f3d81" target="_blank">Logger++</a> - Adds enhanced logging to all requests and responses from all Burp Suite tools, enable this one before you need it ;)</li><li><a href="https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646" target="_blank">Request Smuggler</a> - A relatively new extension, this allows you to attempt to smuggle requests to backend servers. See this talk by James Kettle for more details: <a href="https://www.youtube.com/watch?v=_A04msdplXs" target="_blank">Link</a></li><li><a href="https://portswigger.net/bappstore/f9bbac8c4acf4aefa4d7dc92a991af2f" target="_blank">Autorize</a> - Useful for authentication testing in web app tests. These tests typically revolve around navigating to restricted pages or issuing restricted GET requests with the session cookies of low-privileged users</li><li><a href="https://github.com/Static-Flow/BurpSuite-Team-Extension" target="_blank">Burp Teams Server</a> - Allows for collaboration on a Burp project amongst team members. Project details are shared in a chatroom-like format</li><li><a href="https://portswigger.net/bappstore/36238b534a78494db9bf2d03f112265c" target="_blank">Retire.js</a> - Adds scanner checks for outdated JavaScript libraries that contain vulnerabilities, this is a premium extension</li><li><a href="https://portswigger.net/bappstore/7ec6d429fed04cdcb6243d8ba7358880" target="_blank">J2EEScan</a> - Adds scanner test coverage for J2EE (java platform for web development) applications, this is a premium extension</li><li><a href="https://portswigger.net/bappstore/56675bcf2a804d3096465b2868ec1d65" target="_blank">Request Timer</a> - Captures response times for requests made by all Burp tools, useful for discovering timing attack vectors </li></ul><p style="text-align:center;"><img src="https://i.imgur.com/t7BWVla.png" style="width:302.219px;height:226.664px;" /><br /><i><span style="font-size:12px;"><a href="https://dribbble.com/shots/3870703-Contributing" target="_blank">Contributing by Matt Scribner on Dribbble</a></span></i></p><p>A prerequisite for many of the extensions offered for Burp, we'll walk through the installation of Jython, the Java implementation of Python.</p><p style="text-align:center;"><img src="https://i.imgur.com/0ByhGaM.png" style="width:318.5px;height:194.398px;" /><br /></p><p style="text-align:center;"><i>Burp Suite reference documentation for Extender: <a href="https://portswigger.net/burp/documentation/desktop/tools/extender" target="_blank">Link</a></i></p><p style="text-align:center;"><i>Article on some of the top extensions for Burp Suite: <a href="https://portswigger.net/testers/penetration-testing-tools" target="_blank">Link</a></i><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>To start, let's go ahead and switch over to the Options sub-tab of the Extender tab. </p>

```
OK
```

2. <p>Scroll down until you reach the 'Python Environment' section. Note, Burp requires the standalone edition of Jython.</p>

```
OK
```

3. <p>Download the standalone version of Jython from here: <a href="https://www.jython.org/download.html" target="_blank">Link</a> - <i>I suggest saving this or moving it to your Documents folder</i></p>

```
OK
```

4. <p>Return back to Burp and hit 'Select file' under the Python Environment subsection for Jython standalone. Navigate to where you just downloaded this file and select it. </p>

```
OK
```

5. <p>Burp is now set to go for installing extensions. Switch to the BApp Store sub-tab of Extender and look through the various extensions offered.</p>

```
OK
```

6. <p>Which extension allows us too bookmark various requests?</p>

```
Bookmarks
```

----------------------------------------

### TASK 13. But wait, there's more!

<p>Before we conclude, let's take a quick look into the features that Burp Suite Professional offers: The Burp Suite Scanner and Collaborator Client!</p><p style="text-align:center;"><img src="https://i.imgur.com/zD8MMWe.jpg" style="width:293.125px;height:219.844px;" /><br /><i><a href="https://dribbble.com/shots/3988968-Engage" target="_blank"><span style="font-size:12px;">Engage by Todd Zlab on Dribbble</span></a></i></p><p><span style="font-size:1rem;">Arguably the most powerful feature in Burp Suite, the Burp Suite Scanner allows us to passively and actively scan and spider the website we are testing for vulnerabilities. In Burp 2.0's task-based model, we can launch these scans (Scanner and Spider) from the dashboard and let them run in the background while we continue to examine the web app. In this case, I've run an unauthenticated scan against Juice Shop and have attached it to this task. These reports can provide a starting place for further enumeration and exploitation via the other tools in Burp Suite.</span></p><p style="text-align:center;"><img src="https://i.imgur.com/KR0UAOe.png" style="width:887px;height:421.678px;" /></p><p style="text-align:center;"><i>A Preview of the Report Attached to this Task Created with Burp Professional</i></p><p>Commonly used in manual tests, Burp Collaborator Client allows us to gain insight into issues that may otherwise seem to produce no output. Often during testing, we may come across items which, either due to timing/slowness of the web app or a lack of any reaction, are likely vulnerable but don't produce any sure-fire indicators. With Burp Collaborator, however, we can produce out-of-band alerts via generating payloads that reach back to Burp Suite's servers for us.</p><p style="text-align:center;"><img src="https://i.imgur.com/xymdmu0.png" style="width:911px;height:750.08px;" /><br /></p><p style="text-align:center;"><i><span style="font-size:1rem;">Burp Suite reference documentation for</span><span style="font-size:1rem;"> <a href="https://portswigger.net/burp/documentation/scanner" target="_blank">Scanner</a> and <a href="https://portswigger.net/burp/documentation/desktop/tools/collaborator-client" target="_blank">Collaborator Client</a></span></i></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Download the report attached to this task. What is the only critical issue?</p>

```
Cross-origin resource sharing: arbitrary origin trusted
```

2. <p>How many 'Certain' low issues did Burp find?</p>

```
12
```

----------------------------------------

### TASK 14. Extra Credit

<p>Want to learn more? You're in luck! Port Swigger, the makers of Burp Suite, have a (mostly) free online Web Security Academy! This online training is excellent for learning more about web exploitation techniques and putting your newly minted Burp skills to the test! Pretty much all of this training is <b>free</b> with the only exceptions being a few labs that require the professional version of Burp Suite.</p><p>You can find the Port Swigger Web Security Academy training here: <a href="https://portswigger.net/web-security">https://portswigger.net/web-security</a></p><p style="text-align:center"><img src="https://i.imgur.com/DgiwoVB.png" style="width:50%" /></p><p style="text-align:center"><span style="text-align:left;font-size:1rem">In addition to Port Swigger's training, SANS offers excellent web application pentesting courses. A few of these include SANS </span><a href="https://www.sans.org/course/web-app-penetration-testing-ethical-hacking" target="_blank">SEC 542</a><span style="text-align:left;font-size:1rem"> and </span><a href="https://www.sans.org/course/advanced-web-app-penetration-testing-ethical-hacking" target="_blank">SEC 642</a><span style="text-align:left;font-size:1rem">. Note, these training courses are paid and can be fairly pricy. That being said, they are of incredibly high quality and are worth checking out. </span><br /></p><p style="text-align:center"><img src="https://i.imgur.com/rWF7AEa.png" style="width:159.047px;height:159.047px" /></p><p style="text-align:center">Last but not least, you can keep learning with OWASP Juice Shop in its room here on TryHackMe! <a href="https://tryhackme.com/room/owaspjuiceshop" target="_blank">Link</a></p><p style="text-align:center"><img src="https://i.imgur.com/uBguaF8.png" style="width:148.335px;height:178px" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Check out the provided links and keep learning!

```
OK
```


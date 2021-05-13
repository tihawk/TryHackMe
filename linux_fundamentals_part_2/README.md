# TryHackMe walkthrough

## Linux Fundamentals Part 2

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Intro

<p>This room is the second part in the Linux Fundamental rooms designed to teach you about various Linux concepts, and in-built tools. This room covers the following topics:</p>
<ul>
<li>Linux Operators</li>
<li>Advanced File Operators</li>
</ul>
<p>Deploy the machine and SSH into the room as explained in the tasks below using the following credentials (these credentials will be available from the last task of the <a href="https://tryhackme.com/room/linux1">Linux Fundamentals Part 1</a> room):</p>
<ul>
<li>username: shiba2</li>
<li>password: pinguftw</li></ul><p><i>Please note, unlike the first Linux room you will need to SSH into the machine (there isn't a browser-based machine). Learn how to do this with task 2 and 3.</i></p><ul>
</ul>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>


```
OK
```

2. <p>Deploy the machine attached to this task!</p>
<p><strong>NOTE:</strong> <b><em>If you have a machine open in the Welcome room (or any other room) please go to that room and terminate it before deploying the machine attached to this task. These machines are not the same, and only the one attached to this room will work.</em></b></p>


```
OK
```

----------------------------------------

### TASK 2. SSH - Intro

<p>SSH is the act of remotely accessing a machine. SSH allows you to run commands interactively on the remote machine. This is done through the use of a program on the target machine, which allows the ssh client to interface with the target host.</p><p><span style="font-size:1rem">While the most common usage of a regular operating system is graphical(allowing you to see pictures, web browsers, file managers etc.) SSH works through a command line, meaning anything done on the target machine will be done through a command prompt similar to this.</span><br /></p><p><img src="https://imgur.com/4QD2LNB.png" style="width:333px" /></p><p><span style="font-size:1rem">It may look intimidating at first, but you'll soon find out you can do much of the same functionality that you're able to do using graphical user interfaces!</span><br /></p><p> <span style="font-size:1rem">It is an invaluable tool, and how you </span><span style="font-size:1rem">will be accessing this machine to learn and to do the challenges. Depending on the operating system there are different ways of SSHing into a machine. This section will purely focus on the windows way(PuTTY), and after we learn more about linux commands, and how they work, we'll return back to this section and learn about the linux method.</span></p><p><br /><span style="font-size:1rem"><span style="font-size:1rem"><i><span style="font-weight:bolder">NOTE: Please do not try to SSH into the VM from the Welcome room. You can </span></i><span style="font-weight:bolder">only<i> access the content in this room from the VM provided in Task One. If you forgot to terminate any other machines, please do so, then press the green button to deploy the Learn Linux VM provided in Task One.</i></span></span></span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above

```
OK
```

----------------------------------------

### TASK 3. Putty and SSH

<p>Disclaimer: please do not use putty if you are already on Linux. Use the instructions for the ssh binary down below.</p><p><br /></p><p>The download for putty can be found <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" target="_blank">here</a>, once you download it go through the install process. Once you've installed it, open it and you should see this screen</p><p><img src="https://imgur.com/LN2dIZG.png" style="width:444px" /></p><p>The field that we are most interested in is "Host Name (or IP Address)". This is where the <code style="font-size:14px">MACHINE_IP</code> that you got when you deployed the machine comes into play. That's because the format of SSH connections is &lt;user&gt;@&lt;host&gt;, and in this case host is equal to <code style="font-size:14px">MACHINE_IP</code>. The user for this trial will be shiba2, so the completed "Host Name" field should like this (<b>please note that the image uses shiba1 however shiba2 is the correct username)</b>.</p><p><img src="https://imgur.com/ADpZspQ.jpg" style="width:449px" /></p><p>(Note: the 10.10.10.10 is just an example, and you should replace that with <code style="font-size:14px">MACHINE_IP</code>)</p><p>From there click open, and you'll be greeted with </p><p><img src="https://imgur.com/nlzlrun.jpg" style="width:661px" /></p><p>Click yes(this prompt is purely for verification purposes) and you'll be prompted for a password <span style="font-size:1rem">(</span><span style="font-size:1rem;font-weight:bolder">please note that the image uses shiba1 however shiba2 is the correct username)</span><span style="font-size:1rem">:</span></p><p><img src="https://imgur.com/9mMhNv4.jpg" style="width:639px" /></p><p>Enter "<span style="font-size:1rem"><b>pinguftw</b></span><span style="font-size:1rem">" and click enter, and you'll have logged in! </span><span style="font-size:1rem">(</span><span style="font-size:1rem;font-weight:bolder">please note that the image uses shiba1 however shiba2 is the correct username)</span></p><p><img src="https://imgur.com/v0N82PO.jpg" style="width:650px" /></p><p><span style="font-size:1rem">Note: sometimes putty just may not work, in that case follow the ssh binary guide listed below!</span></p><p><span style="font-size:1rem"><br /></span></p><p><span style="font-size:1rem">As an alternative to putty, you may have an ssh binary on your computer. That binary is accessed by going to your terminal(cmd/MacOS Terminal), and typing ssh.</span><br /></p><p><img src="https://imgur.com/SNNCMwf.jpg" style="width:768px" /></p><p><span style="font-size:1rem">The syntax on how to use this command is </span><code style="font-size:14px">ssh &lt;user&gt;@&lt;host&gt;</code><span style="font-size:1rem">. So to ssh into the machine you'll need to type in </span><code style="font-size:14px">ssh shiba2@MACHINE_IP</code><span style="font-size:1rem">. It will prompt you for the user password, which in this case is also </span><span style="font-size:1rem">pinguftw</span><span style="font-size:1rem">. </span></p><p><img src="https://imgur.com/VO2Q6qc.png" style="width:744px" /><br /></p><p><span style="font-size:1rem">That's it, you can now run commands interactively!!! :)))</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. SSH into the server

```
OK
```

----------------------------------------

### TASK 4. [Section 4: Linux Operators]: "&&"

<p>&amp;&amp; means as you might expect "and". Meaning &amp;&amp; allows you to execute a second command after the first one has executed <i>successfully</i>. Meaning <code>ls &amp;&amp; echo hello</code> will work fine, but <code>dljahfrsdkjlhfsdhjklfsdhkljfh &amp;&amp; echo hello</code> will fail.</p><p><img style="width:655px;" src="https://imgur.com/2LcM4I3.jpg" /></p><p><span style="font-size:1rem;">Note: Since the second command happens after the first command, you can use something created in the first command in the second command.</span><br /></p><p><img style="width:593px;" src="https://imgur.com/1XjZbLe.jpg" /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above

```
OK
```

----------------------------------------

### TASK 5. [Section 4: Linux Operators]: "&"

<p>Much unlike &amp;&amp;, &amp; has nothing to do with and at all(try saying that 10 times fast). &amp; is a background operator, meaning say you run a command that takes 10 seconds to run, normally you wouldn't be able to run commands during that period; however, with &amp; that command will still execute and you'll be able to run other commands.</p><p><img src="https://imgur.com/5XPAUBq.jpg" style="font-size:1rem;width:271px;" /><br /></p><p>Note: I can't exactly show time in an image, but trust me I really did wait the 5 seconds :)</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 6. [Section 4: Linux Operators]: "$"

<p>The $ is an unusually special operator, as it is used to denote environment variables. These are variables set by the computer(you can set them yourself but we'll get into that) that are used to affect different processes and how they work. Meaning that if you edit these variables you can change how certain processes work on your computer. For example your current user is always stored in an environment variable called $USER. You can view these variables with the echo command.</p><p><span style="box-sizing:inherit;clip:rect(0px, 0px, 0px, 0px);color:rgb(255, 255, 255);font-family:Proxima Nova Regular,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;-ms-user-select:text;orphans:2;position:fixed;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;top:0px;-webkit-text-stroke-width:0px;white-space:pre;word-spacing:0px;">https://imgur.com/bEGpRfG</span></p><p><img style="width:598px;" src="https://imgur.com/bEGpRfG.jpg" /><strike><br /></strike></p><p>Naturally this means environment variables can be used as input for other commands as well, for example say I wanted to create a file which is the name of our current user, I could do <code>touch $USER</code>.<strike><br /></strike></p><p><img style="width:435px;" src="https://imgur.com/81jNcME.jpg" /><strike><br /></strike></p><p>Recall that the &gt;&gt; operator appends output to a file.</p><p><span style="font-size:1rem;">Environment variables can also be set pretty easily, just running </span><code> export &lt;varname&gt;=&lt;value&gt;</code><span style="font-size:1rem;"> will set that as an environment variable</span><br /></p><p><strike><br /></strike><img style="width:449px;" src="https://imgur.com/qjCpT08.jpg" /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you set nootnoot equal to 1111</p>

```
export nootnoot=1111
```

2. <p>What is the value of the home environment variable</p>

```
/home/shiba2
```

----------------------------------------

### TASK 7. [Section 4: Linux Operators]: "|"

<p>Continuing with the trend of very special operators, we have the pipe. The pipe is unique because while operators like &gt;&gt; allow you to store the output of a command, the | operator allows you to take the output of a command and use it as input for a second command.</p><p><span style="font-size:1rem;">For example, I can use </span><code>cat </code><span style="font-size:1rem;">to get the output of a file, and pipe that into </span><code>grep</code><span style="font-size:1rem;"> to search for a specific string(Note: We will learn more about grep later, but for now just know that it's a command used to find specific strings in an input).  </span></p><p><img style="width:529px;" src="https://imgur.com/psOTao5.jpg" /> </p><p>It is worth noting that not all commands support the pipe, and some that do support it require you to use - instead of input, for example <code>cat -</code>. So always check to see if the command does support it  </p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above!</p>

```
OK
```

----------------------------------------

### TASK 8. [Section 4: Linux Operators] - ";"

<p>The ; operator works a lot like &amp;&amp;, however it does not require the first command to execute successfully. This means that you can do <code>dkhsgffgsafgfasdgfasfghkgdsgfs; ls</code> and you would still see the output of ls.</p><p><img style="width:591px;" src="https://imgur.com/3FjiVnU.jpg" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>

```
OK
```

----------------------------------------

### TASK 9. [Section 4: Linux Operators]: ">" 

<p>&gt; is the operator for output redirection. Meaning that you can redirect the output of any command to a file. For example if I were to run echo hello &gt; file, then instead of outputting hello to the console, it would save that output to a file called file.</p><p><img src="https://imgur.com/subOGoB.jpg" style="font-size:1rem;width:467px;" /><br /></p><p><span style="font-size:1rem;">It is worth noting that if you were to use this operator on a file that already exists, it would completely erase the contents of that file and replace it with the output from your command</span><br /></p><p><img src="https://imgur.com/qpvaaLO.jpg" style="font-size:1rem;width:538px;" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you output twenty to a file called test</p>

```
echo twenty > test
```

----------------------------------------

### TASK 10. [Section 4: Linux Operators]: ">>"

<p>&gt;&gt; does mainly the same thing as &gt;, with one key difference. &gt;&gt; appends the output of a command to a file, instead of erasing it.</p><p><img src="https://imgur.com/QHZHCdt.jpg" style="font-size:1rem;width:447px;" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 11. Binary - shiba2

<p>This challenge is pretty simple. The binary is checking to see if the environment variable "test1234" exists, and if it's set equal to the current $USER environment variable.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is shiba3's password?</p>

```
happynootnoises
```

----------------------------------------

### TASK 12. [Section 5 - Advanced File Operations]: Intro

<p>Much like windows, files have a lot of complexity to them. Multiple different parameters have to be modified to allow certain users to read to files, write to files, and execute certain files. This section will cover modifying these parameters.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>

```
OK
```

----------------------------------------

### TASK 13. [Section 5 - Advanced File Operators]: A bit of background.

<p>Recall that ls has different flags that allow you to view information about different types of files.</p><p><img style="width:552px;" src="https://imgur.com/uqIivIH.jpg" /></p><p>This image has all of the attributes that will be covered in this section. More specifically we're interested in these three.</p><p><img src="https://imgur.com/eetqAI3.jpg" style="font-size:1rem;width:561px;" /><br /></p><p><span style="font-size:1rem;">These attributes are(in order) the file permissions, owner of the file, and group that the file is in.</span><br /></p><p><span style="font-size:1rem;">The next few tasks will go over the command to modify these attributes.</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above!</p>

```
OK
```

----------------------------------------

### TASK 14. [Section 5: Advanced File Operations]: chown

<p>Recall that ls shows us our username twice.</p>
<p><img src="https://imgur.com/8kYdiUp.jpg" alt /></p>
<p>These attributes are the user, and group attributes resepectively. Recall that we can edit the permissions for these attributes, so it stands to reason that we can also change these attributes. That is done using the chown command, which allows us to change the user and group for any file. The syntax for this command is chown user:group file. For example if we wanted to change the owner of file to shiba2 as well as the group to shiba2, we could use<code>chown shiba2:shiba2 file</code>.</p>
<p><span class="size" style="font-size:1rem">Note: You can only use chown if you are "above" that other user, meaning that chown is best done with the root(administrator) user.</span></p>
<p><img src="https://imgur.com/Q0NwmUk.jpg" alt /></p>
<p><span class="size" style="font-size:1rem">You can also use chown without specifying a group. So you can just use chown user file if you only wanted to change the user but keep the group.</span></p>
<p><img src="https://imgur.com/kFWp8pL.jpg" alt /></p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you change the owner of file to paradox</p>


```
chown paradox file
```

2. <p>What about the owner and the group of file to paradox</p>


```
chown paradox:paradox file
```

3. <p>What flag allows you to operate on every file in the directory at once?</p>


```
-R
```

----------------------------------------

### TASK 15. [Section 5: Advanced File Operations]: chmod

<p>chmod allows you to set the different permissions for a file, and control who can read it. The syntax of this command is typically <code>chmod &lt;permissions&gt; &lt;file&gt; </code>. </p><p><span style="font-size:1rem;">The interesting part is how the permissions are set. They're set using a three digit number, where each digit controls a specific permission, meaning the first digit controls the permissions for a user, the second digit controls the permission for a group, the third digit controls permissions for everyone that's not a part of the user or group.</span><br /></p><p><span style="font-size:1rem;">Now the value of the digits control whether they can read, write or execute it or do all three, and to properly calculate it some math needs to be done.</span></p><table class="table table-bordered"><tbody><tr><td>Digit</td><td>Meaning</td></tr><tr><td>1</td><td>That file can be executed</td></tr><tr><td>2</td><td>That file can be written to</td></tr><tr><td>3</td><td>That file can be executed and written to</td></tr><tr><td>4</td><td>That file can be read</td></tr><tr><td>5</td><td>That file can be read and executed</td></tr><tr><td>6</td><td>That file can be written to and read</td></tr><tr><td>7</td><td>That file can be read, written to, and executed</td></tr></tbody></table><p><br />The way these values are calculated is this. The digit 1 means the file can be executed, the digit 2 means it can be written to, and the digit 4 means it can be read. You get the different permissions by adding these digits together. For example 1+2 is 3 meaning that file can be executed and written to. Now let's see how it all works in perspective.</p><table class="table table-bordered"><tbody><tr><td>Command:</td><td>Meaning</td></tr><tr><td>chmod 341 file</td><td><p>The file can be executed and written to <span style="display:inline;float:none;background-color:rgb(255, 255, 255);color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:center;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">by the user that owns the file</span></p><p>The file can be read <span style="display:inline;float:none;background-color:rgb(255, 255, 255);color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:center;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">by the group that owns the file</span></p><p>The file can be executed by everyone else.</p></td></tr><tr><td>chmod 777 file</td><td><p>The file can be read, written to, and executed <span style="display:inline;float:none;background-color:rgb(255, 255, 255);color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:center;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">by the user that owns the file</span></p><p style="box-sizing:border-box;color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;margin-bottom:1rem;margin-top:0px;orphans:2;text-align:center;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">The file can be read, written to, and executed <span style="display:inline;float:none;background-color:rgb(255, 255, 255);color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:center;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">by the group that owns the file</span></p><p style="box-sizing:border-box;color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;margin-bottom:1rem;margin-top:0px;orphans:2;text-align:center;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">The file can be read, written to, and executed by everyone else</p><p><b></b><i></i><u></u><sup></sup><strike></strike><br /></p></td></tr><tr><td>chmod 455</td><td><p>The file can be read by the user that owns the file</p><p>The file can be read and executed by the group that owns the file</p><p>The file can be read to and executed by everyone else</p></td></tr></tbody></table><p><br /></p><p><br /></p><p>ls provides a helpful way of viewing the permissions of files in the current directory.</p><p><img style="width:561px;" src="https://imgur.com/MPSlodl.jpg" /></p><p>Recall that file permissions are divided into three sections, user and group and everyone else. The same is true here; however, everything starts from the second hyphen not the first, so we can just forget the first hyphen for now. Note that everything is in sequential order, so the first three characters control permissions for the user, the second three characters control permissions for the group, and the final three characters control permissions for everyone else</p><p><img style="width:568px;" src="https://imgur.com/ZNaY6Iw.jpg" /><br /></p><p>(Forgive the artist's rendition. U = user, G = group, E = everyone else)</p><p>rw means as you might expect "read and write", meaning the user has read write perms to the file. Following that logic, that means members of the group and everyone else have only read perms. To convert that to numbers the permissions for that file in number form are 644. We can test this by trying to change the permissions</p><p><img style="width:701px;" src="https://imgur.com/hu9mkJC.jpg" /><br /></p><p><span style="font-size:1rem;">When we try to change the perms to 644 nothing happens because the perms are already 644. The interesting part is while we can write data to .profile with echo while the perms are 644, we can't when we change the perms to 544, because we took away our own write perms. Following that logic, that means we can completely lock ourselves out of writing to a file we already own!</span><br /></p><p><span style="font-size:1rem;">Note: It is possible to give someone no perms to a file, You can just put 0 as the digit. 770 Means that everyone that isnt a part of the user or group cant do anything to the file.</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What permissions mean the user can read the file, the group can read and write to the file, and no one else can read, write or execute the file?</p>

```
460
```

2. <p style="box-sizing:border-box;color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;margin-bottom:0px;margin-top:0px;orphans:2;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">What permissions mean the user can read, write, and execute the file, the group can <span style="display:inline;float:none;background-color:rgb(255, 255, 255);color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">read, write, and execut</span>e the file, and everyone else can <span style="display:inline;float:none;background-color:rgb(255, 255, 255);color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">read, write, and execute the file.</span></p><p><b></b><i></i><u></u><sup></sup><strike></strike><b></b><i></i><u></u><sup></sup><strike></strike><br /></p>

```
777
```

----------------------------------------

### TASK 16. [Section 5: Advanced File Operations]: rm

<p>Let's take a break from all the permissions and math, and look at something that can completely destroy your whole Linux system if used carelessly! rm as you might have guessed means remove, and that's exactly what it does.</p>
<p><img src="https://imgur.com/UOEEgzo.jpg" alt /></p>
<p><span class="size" style="font-size:1rem">As you can imagine this is incredibly dangerous, as you can remove some very important files, and render your system completely unusable. It is not worth noting that you need write permissions to the file to deleted so you cant just delete any file if you're a regular user.</span></p>
<p><img src="https://imgur.com/UkPkxAh.png" alt /></p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What flag deletes every file in a directory</p>


```
-r
```

2. <p>How do you suppress all warning prompts</p>


```
-f
```

----------------------------------------

### TASK 17. [Section 5: Advanced File Operations]: mv

<p>mv allows you to move files from one place to another. The syntax for the command is <code>mv &lt;file&gt; &lt;destination&gt;</code>. so if I wanted to move a file to my home directory I could type <code>mv file ~</code>.</p>
<p><img src="https://imgur.com/2TQwVJj.jpg" alt /></p>
<p><span class="size" style="font-size:1rem">Note: You can also use mv to change the name of file, </span><code>mv file ~/ghfds</code><span class="size" style="font-size:1rem"> will rename file to ghfds. </span></p>
<p><img src="https://imgur.com/8LhG68n.png" alt /></p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you move file to /tmp</p>


```
mv file /tmp
```

----------------------------------------

### TASK 18. Linux Fundamentals 3

<p>Now that you have some intermediate knowledge to using Linux, finish the Linux series and join the <a href="https://tryhackme.com/room/linux3">Linux Fundamentals 3</a> room.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Join the Linux Fundamentals 3 room, and finish learning Linux: <a href="https://tryhackme.com/room/linux3">https://tryhackme.com/room/linux3</a></p>


```
OK
```


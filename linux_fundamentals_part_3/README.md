# TryHackMe walkthrough

## Linux Fundamentals Part 3

> _kblagoev | May 13, 2021_

----------------------------------------

### TASK 1. Intro

<p>This room is the third part in the Linux Fundamental rooms designed to teach you about various Linux concepts, and in-built tools. This room covers the following topics:</p>
<ul>
<li>Advanced File Operators (Continued From <a href="https://tryhackme.com/room/linux2">Linux Fundamentals Part 2)</a></li>
<li>Users &amp; Groups</li>
<li>Introduction To Shell Scripting</li>
</ul>
<p>Deploy the machine and SSH into the room using the following credentials (these credentials will be available from the last task of the <a href="https://tryhackme.com/room/linux2">Linux Fundamentals Part</a>2 room):</p>
<ul>
<li>username: shiba3</li>
<li>password: happynootnoises</li>
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

### TASK 2. [Section 5: Advanced File Operations] - cp

<p>cp does mainly the same thing as mv, except instead of moving the file it duplicates(copies) it. The syntax is also the same as mv, meaning the syntax is <code>cp &lt;file&gt; &lt;destination&gt; </code> .</p><p><img style="width:618px" src="https://i.imgur.com/B958Kyj.png" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p><br /></p>

```
OK
```

----------------------------------------

### TASK 3. [Section 5: Advanced file Operations] - cd &amp;&amp; mkdir

<p>In windows there are folders. Folders allow you to store multiple files in a single group, which makes them easier to organize and access. Linux has the exact same thing, except they're called directories. </p><p><span style="font-size:1rem">Linux allows you to change the location of the current directory through the use of the cd command. The syntax of the cd command is this, </span><code>cd &lt;directory&gt;</code><span style="font-size:1rem">.</span><br /></p><p><img src="https://imgur.com/4ToyThJ.jpg" style="width:323px" /></p><p><span style="font-size:1rem">Relative Paths are supported, as well as absolute paths. Our command line provides a nice section for seeing exactly what directory you're in, so you'll never be lost!</span><br /></p><p><span style="font-size:1rem">This brings us to mkdir, occasionally you'll want to make a new directory to store files in, and that is done using mkdir, the syntax of mkdir is </span><code>mkdir &lt;directory name&gt;</code><span style="font-size:1rem">.</span><br /></p><p><img src="https://imgur.com/Wd1D6H4.jpg" style="width:276px" /></p><p><span style="font-size:1rem">Note: As you might have noticed, ls shows directories aswell</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Using relative paths, how would you cd to your home directory.

```
cd ~
```

2. <p>Using absolute paths how would you make a directory called test in /tmp</p>

```
mkdir /tmp/test
```

----------------------------------------

### TASK 4. [Section 5: Advanced File Operations] ln

<p>ln is a weird one, because it has two different main uses. One of those is what's known as "hard linking", which completely duplicates the file, and links the duplicate to the original copy. Meaning What ever is done to the created link, is also done to the original file. The ln syntax is <code>ln source destination</code>.<br /></p><p><br /></p><p><img style="width:524px;" src="https://imgur.com/GFFFO2u.jpg" /></p><p><span style="font-size:1rem;">It's important to be very careful with hard links, as depending on what you're doing it can be very easy to erase data from a file.</span><br /></p><p><span style="font-size:1rem;">The next form of linking is symbolic linking(symlink). While a hard linked file contains the data in the original file, a symbolic link is just a glorified reference. Meaning that the actual symbolic link has no data in it at all, it's just a reference to another file.</span><br /></p><p>The syntax for a symbolic link is the exact same, but it uses the -s flag, so to create a symbolic link, you would run <code>ln -s &lt;file&gt; &lt;destination&gt;</code>.</p><p><img style="width:522px;" src="https://imgur.com/9E6e92K.jpg" /><br /></p><p><span style="font-size:1rem;">ls even shows that its a symbolic link with the arrow pointing to what the link is referencing. It is important to note the permissions on the symlink. It has full 777 perms meaning that in theory you can execute the symlink, however since it is just a reference, in reality it has the same perms as the original file.</span><br /></p><p><img style="width:467px;" src="https://imgur.com/7r8Jmow.jpg" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would I link /home/test/testfile to /tmp/test</p>

```
ln /home/test/testfile /tmp/test
```

----------------------------------------

### TASK 5. [Section 5 - Advanced File Operations]: find

<p>find is an incredibly powerful, but incredibly simple command. It allows you to do just as it says, find files. It does this by listing every file in the current directory, so if you ran find /tmp it would list every file in /tmp. </p><p><img src="https://imgur.com/3zcvXKh.jpg" style="width:1046px;" /></p><p><span style="font-size:1rem;">It is worth noting that find is recursive, so it searches every directory that is in the original directory you provided. Meaning that if you were to run </span><code>find /</code><span style="font-size:1rem;">, it would list every file on the OS. Another thing worth noting is that it can only list files in directories that you have permission to access, meaning you cant just list every file as every user.</span><br /></p><p><span style="font-size:1rem;">The </span><span style="font-size:1rem;">true power of this command though comes from the parameters you can provide it. You can use </span><code>find dir -user</code><span style="font-size:1rem;"> , to list every file owned by a specific user; you can use </span><code>find dir -group</code><span style="font-size:1rem;"> to list every file owned by a specific group. The sheer customizability of the command is it's most powerful feature.</span><br /></p><p><img src="https://imgur.com/Ckqt2ax.jpg" style="width:1046px;" /></p><p>This is one command I highly recommend reading the manual page on to learn all of it's options. This command is invaluable when working with files.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How do you find files that have specific permissions?</p>

```
-perm
```

2. <p>How would you find all the files in /home</p>

```
find /home
```

3. <p>How would you find all the files owned by paradox on the whole system</p>

```
find / -user paradox
```

----------------------------------------

### TASK 6. [Section 5: Advanced File Operations] - grep

<p>I can say without reservation that grep is one of the most useful commands to learn. It allows you find data inside of data. When working with large files, or a large output, it is arguably the best way to narrow the output down to better find what your looking for. The syntax of the command is <code>grep &lt;string&gt; &lt;file&gt;</code> however file is optional if you're using piping.</p><p><span style="font-size:1rem">Note: You can search multiple files at the same time, meaning you can theoretically do </span><code>grep &lt;string&gt; &lt;file&gt; &lt;file2&gt;</code><br /></p><p><span style="font-size:1rem">For instance let's say you know have the file name of test1234, but you don't know where it is on the system. find can be used to list every file on the OS, and grep can be used to find the actual file.</span></p><p><img style="width:459px" src="https://imgur.com/IR7M08S.jpg" /></p><p>grep comes and saves the day! What about if you have a bunch of data, and you wanna see if the string hello is in it, and if so what line number it's at.</p><p><img style="width:412px" src="https://imgur.com/xPWWXQe.jpg" /></p><p>I'm sure you can see just how useful this command is. When searching logs for the cause of an error message, when parsing large amounts of data for that specific piece, when searching every file in a directory for that one line that you may need to change.</p><p><span style="font-size:1rem">Another important thing to note is that grep supports regular expressions, you see I wasn't being entirely truthful with you(props if you get the reference) when I says the syntax is </span><code>grep &lt;string&gt; &lt;file&gt;</code><span style="font-size:1rem">, the syntax is actually </span><code>grep &lt;regular expression&gt; &lt;file&gt;</code><span style="font-size:1rem">. Unfortunately regular expressions are out of the scope of this room, but I highly encourage you to read up on regular expressions, as they increase the power of grep tenfold.</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What flag lists line numbers for every string found?</p>

```
-n
```

2. <p>How would I search for the string boop in the file aaaa in the directory /tmp</p>

```
grep boop /tmp/aaaa
```

----------------------------------------

### TASK 7. Binary - Shiba3 

<p>We've been through a lot in this section, and the challenge for this binary will reflect that. The first step is actually finding the binary, I'm not heartless though, so I'll give you the name of the binary. The name of the binary is shiba4.</p><p><span style="font-size:1rem;">The actual binary will check for two things, it will be checking that there's a directory called test in your home directory, how you create that is up to you. It will also be checking that inside the directory there's a file called test1234.</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is shiba4's password</p>

```
test1234
```

----------------------------------------

### TASK 8. [Section 6: Miscellaneous]: Intro

Even though we've gone over how the Linux operating system works, and some of it's most useful features and commands, there are some useful commands and concepts that haven't been covered in previous sections. So this section is dedicated to all those miscellaneous commands and concepts that are useful to know.

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 9. [Section 6: Miscellaneous]: sudo

<p>Throughout this room you might have seen me mention the root user. The root user is the equivalent of the administrator user on Windows, and like Windows certain commands, and certain things you download from the internet will require admin permissions.</p><p><span style="font-size:1rem;">That's where sudo comes in. sudo is Linux's run as administrator button, and the syntax goes </span><code>sudo &lt;command&gt;</code><span style="font-size:1rem;">.</span></p><p><img style="width:299px;" src="https://imgur.com/ejD2Dib.jpg" />  </p><p>Note: whoami is just a command that states your current user.</p><p><span style="font-size:1rem;">As you can see when using sudo the command is run as root. It is important to note that you need to have your current user's password to use it. Again like Windows, not every user has permission to use sudo, but most Linux OS' set up a user that has permissions when you install it. </span><br /></p><p><span style="font-size:1rem;">Assuming you create a new user that you also want to give sudo permissions to, the man page for sudo has a section on how to add user permissions. It is also worth noting you can configure sudo to run commands as other users, again the man page has a section on that(sudo has a very nice man page)</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How do you specify which user you want to run a command as.</p>

```
-u
```

2. <p>How would I run whoami as user jen?</p>

```
sudo -u jen whoami
```

3. <p>How do you list your current sudo privileges(what commands you can run, who you can run them as etc.)    </p>

```
-l
```

----------------------------------------

### TASK 10. [Section 6: Miscellaneous]: Adding users and groups

<p>You know about how to modify permissions for users and groups, therefore it's helpful to know how to create them. Luckily Linux provides a nice helpful way to do this, with <code>adduser </code>and <code>addgroup</code>. The syntax for both of these commands are <code>adduser username</code> and <code>addgroup groupname</code>.</p><p><img style="width:515px;" src="https://imgur.com/wWwteJA.jpg" /></p><p><img style="width:711px;" src="https://imgur.com/sEWC06K.jpg" /><br /></p><p>It's important to note that only root has permissions to add users and groups, as seen with the failure when I attempted to run the commands without sudo. You may be wondering how to add a user to a group. that is done with the usermod command, the syntax for that is <code>usermod -a -G &lt;groups seperated by commas&gt; &lt;user&gt;</code>. Meaning if I wanted to add the user noot to b I would run <code>usermod -a -G b noot</code>.</p><p><img style="width:552px;" src="https://imgur.com/vmxNa4e.jpg" /></p><p>Note: id is a command that allows you to view basic information about a user.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would I add the user test to the group test</p>

```
sudo usermod -a -G test test
```

----------------------------------------

### TASK 11. [Section 6: Miscellaneous]: nano

<p>Up until this point you may have seen me only using &gt;&gt; to add content to a file. Luckily that's not the only way to do things, nano is a terminal based text editor. The syntax for nano is <code>nano &lt;file you want to write to&gt;</code>. For example typing nano test will take you to this screen.</p><p><img style="width:810px;" src="https://imgur.com/s0uJCNT.png" /></p><p>From here type until your heart's content!</p><p><img style="width:830px;" src="https://imgur.com/Kj5VuJW.png" /></p><p>Nano has alot of commands inside of it's text editor, and the text editor as a whole probably warrants a room on it's own, but 99.9 percent of the time you're gonna wanna use <code>ctrl+x</code></p><p>Note: ^X means ctrl+x, most of the time you see ^&lt;key&gt; the ^ means control</p><p>Once you press ctrl +x you'll be prompted with this screen</p><p><img style="width:833px;" src="https://imgur.com/XqkoQbk.png" /></p><p>From there press Y and you'll be asked what you want to name the file.</p><p><img style="width:895px;" src="https://imgur.com/ao053v7.png" /></p><p>Type whatever you want the file to be named, press enter and you'll be greeted with your terminal screen! You'll notice the file is there and everything you typed is there.</p><p><img style="width:936px;" src="https://imgur.com/xlMG3H7.png" /></p><p><span style="font-size:1rem;">Now you can actually edit text files! :)</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 12. [Section 6: Miscellaneous]: Basic shell scripting

<p>Linux provides us a way to run commands one after another without using any special operators. This is done by storing the commands you want to run in a file with a .sh extension</p><p><img style="width:1046px" src="https://imgur.com/HODFyrK.png" /></p><p>If we save and run <code>bash s.sh</code> it executes those commands in order.</p><p><img style="width:484px" src="https://imgur.com/EGB71ea.png" /></p><p>It echoed out hello, then it echoed out whoami, then it ran whoami exactly as the file said it should. Congratulations that's your first bash script!</p><p>It is worth noting that the sh extension isn't technically needed if you provide a shebang(#!) , and then the path to the shell we want to use to run our command<span style="box-sizing:inherit;clip:rect(0px, 0px, 0px, 0px);color:rgb(255, 255, 255);font-family:Proxima Nova Regular,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;-ms-user-select:text;orphans:2;position:fixed;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;top:0px;-webkit-text-stroke-width:0px;white-space:pre;word-spacing:0px"> Ahttps://imgur.com/a5AX8U4</span>.</p><p><img style="width:951px" src="https://imgur.com/a5AX8U4.png" /></p><p>From there we can remove the sh extension, and make the file executable.</p><p><img style="width:354px" src="https://imgur.com/UH9LQkO.png" /></p><p><span style="font-size:1rem">Note: The shebang MUST be in the beginning of the file</span><br /></p><p><span style="box-sizing:inherit;clip:rect(0px, 0px, 0px, 0px);color:rgb(255, 255, 255);font-family:Proxima Nova Regular,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;-ms-user-select:text;orphans:2;position:fixed;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;top:0px;-webkit-text-stroke-width:0px;white-space:pre;word-spacing:0px"><br /></span></p><p><span style="box-sizing:inherit;clip:rect(0px, 0px, 0px, 0px);color:rgb(255, 255, 255);font-family:Proxima Nova Regular,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;-ms-user-select:text;orphans:2;position:fixed;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;top:0px;-webkit-text-stroke-width:0px;white-space:pre;word-spacing:0px"><br /></span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>

```
OK
```

----------------------------------------

### TASK 13. [Section 6: Miscellaneous]: Important Files and Directories

<p>Throughout this room you've seen a lot of files and directories, so I'm using this task to define what the most important of those files and directories do. </p><p>Before that however, it is worth noting exactly how the linux file system works. Everything on the linux file system extends from "/". / is the equivalent of C: in Windows. Meaning that for example if you were to delete "/", you would delete every file on your system.<br /></p><p><b style="font-size:1rem;">/etc/passwd - Stores user information - Often used to see all the users on a system</b><br /></p><p>    <img style="width:825px;" src="https://imgur.com/EhQNy3H.png" /></p><p><b style="font-size:1rem;">/etc/shadow - Has all the passwords of these users</b><br /></p><p>    Not showing for obvious reasons</p><p><b>/tmp - Every file inside it gets deleted upon shutdown - used for temporary files</b></p><p>    <img style="width:793px;" src="https://imgur.com/SEtC1rs.png" /><b><br /></b></p><p><b style="font-size:1rem;">/etc/sudoers - Used to control the sudo permissions of every user on the system -</b><br /></p><p>    <b>   </b><span style="box-sizing:inherit;clip:rect(0px, 0px, 0px, 0px);color:rgb(255, 255, 255);font-family:Proxima Nova Regular,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;-ms-user-select:text;orphans:2;position:fixed;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;top:0px;-webkit-text-stroke-width:0px;white-space:pre;word-spacing:0px;">https://imgur.com/SEtC1rs</span>Too Long to show</p><p><b>/home - The directory where all your downloads, documents etc are. - The equivalent on Windows is </b><a>C:\Users\</a>&lt;user&gt;</p><p>    <img style="width:665px;" src="https://imgur.com/YQnZLbJ.png" /><b><br /></b></p><p><b>/root - The root user's home directory - The equivilent on Windows is </b><a>C:\Users\Administrator</a></p><p>       Not showing because of spoiler ;)</p><p><b>/usr - Where all your software is installed</b> </p><p>        <img style="width:501px;" src="https://imgur.com/e0l4Ybh.png" /><br /></p><p><span style="box-sizing:inherit;clip:rect(0px, 0px, 0px, 0px);color:rgb(255, 255, 255);font-family:Proxima Nova Regular,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;-ms-user-select:text;orphans:2;position:fixed;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;top:0px;-webkit-text-stroke-width:0px;white-space:pre;word-spacing:0px;">https://imgur.com/e0l4Ybh</span><b></b><i></i><u></u><sup></sup><strike></strike><b>/bin and /sbin - Used for system critical files - DO NOT DELETE</b></p><p>    Too big to show, but contains all of the basic programs needed for linux to function</p><p><b style="font-size:1rem;">/var - The Linux miscellaneous directory, a myriad of processes store data in /var</b><br /></p><p>    <img style="width:793px;" src="https://imgur.com/tyIiCeg.png" /><b><br /></b></p><p><b>$PATH - Stores all the binaries you're able to run - same as $PATH on Windows</b></p><p>    $PATH is an environment variable that contains all the binaries you're able to execute. </p><p>    <img src="https://imgur.com/vQYYnlr.png" style="width:889px;" /><b><br /></b></p><p>    It is worth noting that the paths in $PATH(hah!) are separated by colons. Every executable file that is in any of those paths you are able to run just by typing the name of the executable instead of the full path.</p><p>    <img src="https://imgur.com/8csjrPX.png" style="width:998px;" /><br /></p><p>     Note: which is just a command that shows you where an executable is in any of the PATH directories.</p><p><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 14. [Section 6 - Miscellaneous]: Installing packages(apt)

<p>This is a bit hard to make a task on because depending on the Linux OS you install, this information may be entirely worthless. Therefore, I have deemed it best to show how to install packages using the most popular package manager, that being apt. A package is essentially a program, you can think of it like an exe file on windows. To install packages you need root permissions, as each package will likely modify some system critical directories such as /usr. The syntax to install packages is <code>apt install package</code>.</p><p><img style="width:810px;" src="https://imgur.com/VaGFf6H.png" /></p><p>Note: python-dev is a random package and just the first one that came to mind</p><p>apt downloads the package from a repository(list of programs). It then installs it and gives you your command prompt </p><p>back, much like when you install a program on Windows.</p><p><img style="width:637px;" src="https://imgur.com/OfsAQ6N.png" /></p><p>apt has a lot of sub commands, and again warrants a room on it's own but most of the time you're going to be googling what you want and you'll find the name of the package to install.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 15. [Section 6: Miscellaneous]: Processes

<p>Every binary you execute on linux, is a process while it's run. A process is just another word for a running program. A list of user created processes can be viewed with the <code>ps</code> command</p><p><img src="https://imgur.com/pP9hnen.png" style="width:335px;" /></p><p>While this is technically all the user created processes, it's likely not the information you're looking for if you're going to be examining processes. To view a list of all system processes, you have to use the <code>-ef</code> flag</p><p><img src="https://imgur.com/WiLQ5Rq.png" style="width:1046px;" /></p><p>Every process that is currently running on the system is listed, along with some basic information about the process. Arguably the most interesting part about that list is the second column, the 3-5 digit numbers. Those are known as Process ID's(PID's) and they're how you interact with the processes. 90% of the time you'll likely be wanting to stop these processes and that's done with the <code>kill</code> command(an apt choice of naming I know). </p><p><br />The syntax of kill is <code>kill &lt;PID&gt;</code>.</p><p><img src="https://imgur.com/o8u8nhh.png" style="width:948px;" /></p><p><img src="https://imgur.com/UKq8sEN.png" style="width:867px;" /></p><p><br />After running kill, the process no longer shows up! Another useful way to interact with PID's is through the command top. top shows you what processes are taking up the most system resources, which allows you to manage the resource allocation on your system by killing unneeded processes.</p><p><img src="https://imgur.com/E3OeMWn.png" style="width:905px;" /></p><p><span style="font-size:1rem;">Note: The top man page has descriptions for what every value means, and how they affect your system; I highly recommend reading it!</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above!</p>

```
OK
```


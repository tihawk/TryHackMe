# TryHackMe walkthrough

## Linux Fundamentals Part 1

> _kblagoev | May 13, 2021_

----------------------------------------

### TASK 1. Intro

<p>This room is the first part in the Linux Fundamental rooms designed to teach you about various Linux concepts, and in-built tools. This room covers the following topics:</p>
<ul>
<li>Introduction To Linux</li>
<li>Executing Commands and Man Pages</li>
<li>Basic File Operators</li>
</ul>
<p>Deploy the machine attached to this task to get started.</p>


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

### TASK 2. Methodology

<p>After careful consideration, I've deemed the best way to go about this is to introduce various concepts in sections, with each section being more complex and requiring knowledge from the previous section. To better enable the transition between section, I've split each section into different users in the VM; when you finish a section you'll have to complete a challenge and then you'll be able to move onto the next section.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>

```
OK
```

----------------------------------------

### TASK 3. [Section 2: Running Commands] - Basic Command Execution

<p>Now that you've logged into the server, you're gonna wanna do things, and everything that can be done over SSH is done by running commands. To start out, we'll take a look at some of the basic commands, and the first command will be <code>echo</code>. Type <code>echo hello</code>, and press enter and you'll see your input echoed back at you.</p><p><br /></p><p><img style="width:660px;" src="https://imgur.com/QGPXIFc.jpg" /></p><p>Much like the word it's named after, <code>echo </code>returns whatever is inputted into it. Congratulations, you've just ran your first Linux command!</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above</p>

```
OK
```

----------------------------------------

### TASK 4. [Section 2: Running Commands] - Manual Pages and Flags

<p>Most of the commands you'll learn about have a lot of options that are not immediately known at first glance, these options are known as flags, and have the format <code>&lt;command&gt; &lt;flag&gt; &lt;input&gt;</code>. These flags can be learned about using the <code>man</code> command. The man command has the format <code>man &lt;command&gt;</code>. Therefore, to learn about flags for the echo command, we would type <code>man echo</code>. Typing that shows us a nicely formatted document:</p><p><img style="width:1046px;" src="https://imgur.com/FixWl4Y.jpg" /></p><p>We get alot of information, but the flags are stored in the description section. For example the flag to remove the newline is -n. So to output "<code>Shiba</code>" without the newline you would type <code>echo -n Shiba</code>.        </p><p><span style="font-size:1rem;">Note: Some commands support the -h flag, meaning you can type </span><code>&lt;command&gt; -h</code><span style="font-size:1rem;"> and get a list of flags and other useful information without using </span><code>man</code><span style="font-size:1rem;">.           </span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you output hello without a newline</p>

```
echo -n hello
```

----------------------------------------

### TASK 5. [Section 3: Basic File Operations] - ls

<p>ls is a command that lists information about every file/directory in the directory. Just running the ls command outputs the name of every file in the directory.</p><p><img style="width:180px;" src="https://imgur.com/AMpO7qK.jpg" /></p><p>As with other commands ls has many flags that can manipulate the output.  For example <code>ls -a</code> shows all files/directories including ones that start with <code>.</code></p><p><img style="width:635px;" src="https://imgur.com/Wp9M8pF.jpg" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What flag outputs all entries</p>

```
-a
```

2. <p>What flag outputs things in a "long list" format    </p>

```
-l
```

----------------------------------------

### TASK 6. [Section 3: Basic File Operations] - cat

<p>cat short for concatenate, does exactly that, it outputs the contents of files to the console. For example, given a file called a.txt which contains the data "hello", <code>cat a.txt</code> would output hello.</p><p><img style="width:243px;" src="https://imgur.com/fFfe9tz.jpg" /></p><p><span style="font-size:1rem;">Note: cat supports the --help flag meaning that you can see useful flags without going to the man page!</span><br /></p><p><img style="width:664px;" src="https://imgur.com/vzjsPck.jpg" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What flag numbers all output lines?    </p>

```
-n
```

----------------------------------------

### TASK 7. [Section 3: Basic File Operations] - touch

<p>touch is a pretty simple command, it creates files. Given the command <code>touch b.txt</code>, b.txt would be created.</p><p><img style="width:372px;" src="https://imgur.com/4Yw3YKY.png" /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above!</p>

```
OK
```

----------------------------------------

### TASK 8. [Section 3: Basic File Operations] - Running A Binary

<p>Occasionally there will be times when you want to run downloaded or user created programs. This is done by providing the full path to the binary, for example say you download a binary that outputs noot, providing the full path to that binary will execute it. </p><p><img style="width:380px;" src="https://imgur.com/PKDp1eF.jpg" /></p><p>Note: A binary is just executable code, think a windows exe file</p><p><span style="font-size:1rem;">This seems like a good time to mention Relative Paths! Every time you intend on running the binary, you don't need to provide a full path, you can use Relative Paths.</span><br /></p><p>Relative Paths:</p><p>The chart below will assume the current path is /tmp/aa </p><table class="table table-bordered"><tbody><tr><td>Relative Path</td><td>Meaning</td><td>Absolute Path</td><td>Relative Path</td><td>Running a binary with a Relative Path</td><td>Running A Binary with an Absolute Path</td></tr><tr><td>.</td><td>Current Directory</td><td>/tmp/aa </td><td>.</td><td>./hello</td><td>/tmp/aa/hello</td></tr><tr><td>..</td><td>Directory before the current directory</td><td>/tmp</td><td>..</td><td>../hello</td><td>/tmp/hello</td></tr><tr><td>~</td><td>The user's home directory</td><td>/home/&lt;current user&gt;</td><td>~</td><td>~/hello</td><td>/home/&lt;user&gt;/hello</td></tr></tbody></table><p><br /></p><p>These shortcuts are incredibly efficient, and save time. These shortcuts for every command, so if I were to run <code>ls .</code> it would be the same as running <code>ls &lt;current directory&gt;</code>   </p><p><img style="width:328px;" src="https://imgur.com/hfre7mJ.jpg" /><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>How would you run a binary called hello using the directory shortcut . ?</p>

```
./hello
```

2. <p><span style="display:inline;float:none;background-color:transparent;color:rgb(33, 37, 41);font-family:ubuntu mono,monospace;font-size:16px;font-style:normal;font-variant:normal;font-weight:400;letter-spacing:normal;orphans:2;text-align:left;text-decoration:none;text-indent:0px;text-transform:none;-webkit-text-stroke-width:0px;white-space:normal;word-spacing:0px;">How would you run a binary called hello in your home directory using the shortcut ~ ?</span><br /></p>

```
~/hello
```

3. <p>How would you run a binary called hello in the previous directory using the shortcut .. ?</p>

```
../hello
```

----------------------------------------

### TASK 9. Binary - Shiba1

<p>Now that you've learned basic file operations, you can solve the first challenge! This challenge is pretty simple, create a file called noot.txt.</p><p><span style="font-size:1rem;">Once you're done run the binary and you'll be given the password for the user shiba2!</span></p><p><span style="font-size:1rem;"><br /></span></p><p><span style="font-size:1rem;">Note: the name of the binary is shiba1, as shown in the title</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What's the password for shiba2        </p>

```
pinguftw
```

----------------------------------------

### TASK 10. su

<p>Now that we have our next user password, it seems like a good time to cover su. su is a command that allows you to change the user, without logging out and logging back in again. For example if you wanted to switch to shiba2 while you're the user shiba1, you would type <code>su shiba2</code> . You would then be prompted for a password and if you entered shiba2's password you would then become shiba2</p><p><img style="width:246px" src="https://imgur.com/iZhPtJf.jpg" /></p><p><span style="font-size:1rem">Note: Typing </span><code>su</code><span style="font-size:1rem"> on its own is equivalent to typing </span><code>su root</code><span style="font-size:1rem">. </span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>

```
OK
```

----------------------------------------

### TASK 11. Linux Fundamentals 2

<p>Now that you have some beginner knowledge to using Linux, its time you take it a step further and join the <a href="https://tryhackme.com/room/linux2">Linux Fundamentals 2</a> room.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Join the Linux Fundamentals 2 room, and continue your learning journey: <a href="https://tryhackme.com/room/linux2">https://tryhackme.com/room/linux2</a></p>


```
OK
```

2. <p>Terminate the machine.</p>

```
OK
```


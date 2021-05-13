# TryHackMe walkthrough

## John The Ripper

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. John who? 

<h4>Welcome</h4><p>John the Ripper is one of the most well known, well-loved and versatile hash cracking tools out there. It combines a fast cracking speed, with an extraordinary range of compatible hash types. This room will assume no previous knowledge, so we must first cover some basic terms and concepts before we move into practical hash cracking. </p><p><br /></p><h4>What are Hashes?</h4><p>A hash is a way of taking a piece of data of any length and  representing it in another form that is a fixed length. This masks the original value of the data. This is done by running the original data through a hashing algorithm. There are many popular hashing algorithms, such as MD4,MD5, SHA1 and NTLM. Lets try and show this with an example:</p><p>If we take "polo", a string of 4 characters- and run it through an MD5 hashing algorithm, we end up with an output of: b53759f3ce692de7aff1b5779d3964da a standard 32 character MD5 hash. </p><p>Likewise, if we take "polomints", a string of 9 characters- and run it through the same MD5 hashing algorithm, we end up with an output of: 584b6e4f4586e136bc280f27f9c64f3b another standard 32 character MD5 hash. </p><p><br /></p><h4>What makes Hashes secure?</h4><p>Hashing algorithms are designed so that they only operate one way. This means that a calculated hash cannot be reversed using just the output given. This ties back to a fundamental mathematical problem known as the <a href="https://en.wikipedia.org/wiki/P_versus_NP_problem" target="_blank">P vs NP relationship</a> . </p><p>While this is an extremely interesting mathematical concept that proves fundamental to computing and cryptography I am in no way qualified to try and explain it in detail here; but abstractly it means that the algorithm to hash the value will be "NP" and can therefore be calculated reasonably. However an un-hashing algorithm would be "P" and intractable to solve- meaning that it cannot be computed in a reasonable time using standard computers. </p><p><br /></p><h4>Where John Comes in...</h4><p>Even though the algorithm itself is not feasibly reversible. That doesn't mean that cracking the hashes is impossible. If you have the hashed version of a password, for example- and you know the hashing algorithm- you can use that hashing algorithm to hash a large number of words, called a dictionary. You can then compare these hashes to the one you're trying to crack, to see if any of them match. If they do, you now know what word corresponds to that hash- you've cracked it!</p><p>This process is called a <b>dictionary attack </b>and John the Ripper, or John as it's commonly shortened to, is a tool to allow you to conduct fast brute force attacks on a large array of different hash types.</p><p><br /></p><h4>Learning More</h4><p>For some more in-depth material on specific hashing and Encryption methods I'd recommend checking out <a class="green-link" href="https://tryhackme.com/p/NinjaJc01">NinjaJc01</a>'s amazing room covering these topics: <a href="https://tryhackme.com/room/encryptioncrypto101" target="_blank">encryptioncrypto101</a> <br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read and understand the basic concepts of hashing and hash cracking <br />

```
OK
```

----------------------------------------

### TASK 2. Setting up John the Ripper 

<h4>Setting Up John The Ripper</h4><p>John the Ripper is supported on many different Operating Systems, not just Linux Distributions. As a note before we go through this, there are multiple versions of John, the standard "core" distribution, as well as multiple community editions- which extend the feature set of the original John distribution. The most popular of these distributions is the "Jumbo John"- which we will be using specific features of later. </p><p><br /></p><h4>Parrot, Kali and AttackBox </h4><p>If you're using Parrot OS, Kali Linux or TryHackMe's own AttackBox- you should already have Jumbo John installed. You can double check this by typing <code>john</code> into the terminal. You should be met with a usage guide for john, with the first line reading: "John the Ripper 1.9.0-jumbo-1" or similar with a different version number. If not, you can use <code>sudo apt install john</code> to install it. <br /></p><p><br /></p><h4>Blackarch</h4><p>If you're using Blackarch, or the Blackarch repositories you may or may not have Jumbo John installed, to check if you do, use the command <code>pacman -Qe | grep "john"</code> You should be met with an output similar to "john 1.9.0.jumbo1-5" or similar with a different version number. If you do not have it installed, you can simply use <code>pacman -S john</code> to install it. </p><p><br /></p><h4>Building from Source for Linux</h4><p>If you wish to build the package from source to meet your system requirements, you can do this in five fairly straightforward steps. Further advice on the installation process and how to configure your build from source can be found <a href="https://github.com/openwall/john/blob/bleeding-jumbo/doc/INSTALL" target="_blank">here.</a> <br /></p><ol><li> Use <code>git clone https://github.com/openwall/john -b bleeding-jumbo john</code> to clone the jumbo john repository to your current working</li><li> Then <code>cd john/src/</code> to change your current directory to where the source code is.  </li><li>Once you're in this directory, use <code>./configure</code> to check the required dependencies and options that have been configured. </li><li>If you're happy with this output, and have installed any required dependencies that are needed, use <code>make -s clean &amp;&amp; make -sj4</code> to build a binary of john. This binary will be in the above run directory, which you can change to with <code>cd ../run</code></li><li>You can test this binary using ./john --test</li></ol><p><br /></p><h4>Installing on Windows<br /></h4><p>To install Jumbo John the Ripper on Windows, you just need to download and install the zipped binary for either 64 bit systems <a href="https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip" target="_blank">here</a> or for 32 bit systems <a href="https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip" target="_blank">here</a>.<br /></p><h4> </h4>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the most popular extended version of John the Ripper?<br />

```
Jumbo John
```

----------------------------------------

### TASK 3. Wordlists

<h4>Wordlists</h4><p>As we explained in the first task, in order to in order to dictionary attack hashes, you need a list of words that you can hash and compare, unsurprisingly this is called a wordlist. There are many different wordlists out there, a good collection to use can be found in the <a href="https://github.com/danielmiessler/SecLists" target="_blank">SecLists</a> repository. There are a few places you can look for wordlists on your attacking system of choice, we will quickly run through where you can find them. </p><p><br /></p><h4>Parrot, Kali and AttackBox </h4><p>On Parrot, Kali and TryHackMe's AttackBox- you can find a series of amazing wordlists in the <code>/usr/share/wordlists</code> directory.</p><p><br /></p><h4>RockYou </h4><p>For all of the tasks in this room, we will be using the infamous rockyou.txt wordlist- which is a very large common password wordlist, obtained from a data breach on a website called rockyou.com in 2009. If you are not using any of the above distributions, you can get the rockyou.txt wordlist from the <a href="https://github.com/danielmiessler/SecLists" target="_blank">SecLists</a> repository under the <code>/Passwords/Leaked-Databases</code> subsection. You may need to extract it from .tar.gz format, using <code>tar xvzf rockyou.txt.tar.gz</code>.</p><p><br /></p><p>Now that we have our hash cracker and wordlists all set up, lets move onto some hash cracking!<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What website was the rockyou.txt wordlist created from a breach on?<br />

```
rockyou.com
```

----------------------------------------

### TASK 4. Cracking Basic Hashes

<h4>Cracking Basic Hashes</h4><p>There are multiple ways to use John the Ripper to crack simple hashes, we're going to walk through a few, before moving on to cracking some ourselves. </p><p><br /></p><h4>John Basic Syntax</h4><p>The basic syntax of John the Ripper commands is as follows. We will cover the specific options and modifiers used as we use them.<br /></p><p><code>john [options] [path to file]</code></p><p><code>john</code> - Invokes the John the Ripper program </p><p><code>[path to file]</code> - The file containing the hash you're trying
 to crack, if it's in the same directory you won't need to name a path, 
just the file.</p><p><br /></p><h4>Automatic Cracking<br /></h4><p>John has built-in features to detect what type of hash it's being given, and to select appropriate rules and formats to crack it for you, this isn't always the best idea as it can be unreliable- but if you can't identify what hash type you're working with and just want to try cracking it, it can be a good option! To do this we use the following syntax:</p><p><code>john --wordlist=[path to wordlist] [path to file]<br /></code></p><p><code>--wordlist=</code> - Specifies using wordlist mode, reading from the file that you supply in the following path...</p><p><code>[path to wordlist]</code> - The path to the wordlist you're using, as described in the previous task.</p><p><b>Example Usage:</b></p><p>john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt<br /><b></b><br /><b><br /></b></p><h4>Identifying Hashes</h4><p>Sometimes John won't play nicely with automatically recognising and loading hashes, that's okay! We're able to use other tools to identify the hash, and then set john to use a specific format. There are multiple ways to do this, such as using an online hash identifier like <a href="https://hashes.com/en/tools/hash_identifier" target="_blank">this</a> one. I like to use a tool called <a href="https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master" target="_blank">hash-identifier</a>, a Python tool that is super easy to use and will tell you what different types of hashes the one you enter is likely to be, giving you more options if the first one fails. </p><p>To use hash-identifier, you can just pull the python file from gitlab using:<code> wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py</code>. </p><p>Then simply launch it with <code>python3 hash-identifier.py</code> and then enter the hash you're trying to identify- and it will give you possible formats! </p><h4><br /></h4><h4>Format-Specific Cracking</h4><p>Once you have identified the hash that you're dealing with, you can tell john to use it while cracking the provided hash using the following syntax:</p><p><code>john --format=[format] --wordlist=[path to wordlist] [path to file]</code></p><p><code>--format=</code> - This is the flag to tell John that you're giving it a hash of a specific format, and to use the following format to crack it<br /></p><p><code>[format]</code> - The format that the hash is in<br /></p><p><b>Example Usage:</b></p><p>john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt<b> </b>hash_to_crack.txt</p><p><b>A Note on Formats:</b></p><p>When you are telling john to use formats, if you're dealing with a standard hash type, e.g. md5 as in the example above, you have to prefix it with<code> raw-</code> to tell john you're just dealing with a standard hash type, though this doesn't always apply. To check if you need to add the prefix or not, you can list all of John's formats using <code>john --list=formats</code> and either check manually, or grep for your hash type using something like <code>john --list=formats | grep -iF "md5"</code>.<br /></p><h4><br /></h4><h4>Practical</h4><p>Now you know the syntax, modifiers and methods to crack basic hashes, try it yourself! Download the attached .txt files that <br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What type of hash is hash1.txt?<br />

```
md5
```

2. <p>What is the cracked value of hash1.txt?<br /></p>

```
biscuit
```

3. <p>What type of hash is hash2.txt?</p>

```
sha1
```

4. <p>What is the cracked value of hash2.txt<br /></p>

```
kangeroo
```

5. <p>What type of hash is hash3.txt?</p>

```
sha256
```

6. <p>What is the cracked value of hash3.txt</p>

```
microphone
```

7. <p>What type of hash is hash4.txt?</p>

```
whirlpool
```

8. <p>What is the cracked value of hash4.txt</p>

```
colossal
```

----------------------------------------

### TASK 5. Cracking Windows Authentication Hashes

<h4>Cracking Windows Hashes</h4><p>Now that we understand the basic syntax and usage of John the Ripper- lets move on to cracking something a little bit more difficult, something that you may even want to attempt if you're on a real Penetration Test or Red Team engagement. Authentication hashes are the hashed versions of passwords that are stored by operating systems, it is sometimes possible to crack them using the brute-force methods that we're using. To get your hands on these hashes, you must often already be a privileged user- so we will explain some of the hashes that we plan on cracking as we attempt them. </p><h4><br /></h4><h4>NTHash / NTLM </h4><p>NThash is the hash format that modern Windows Operating System machines will store user and service passwords in. It's also commonly referred to as "NTLM" which references the previous version of Windows format for hashing passwords known as "LM", thus "NT/LM".</p><p> A little bit of history, the NT designation for Windows products originally meant "New Technology", and was used- starting with <a href="https://en.wikipedia.org/wiki/Windows_NT" target="_blank">Windows NT</a>, to denote products that were not built up from the MS-DOS Operating System. Eventually, the "NT" line became the standard Operating System type to be released by Microsoft and the name was dropped, but it still lives on in the names of some Microsoft technologies.  </p><p>You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, by using a tool like Mimikatz or from the Active Directory database: NTDS.dit. You may not have to crack the hash to continue privilege escalation- as you can often conduct a "pass the hash" attack instead, but sometimes hash cracking is a viable option if there is a weak password policy.</p><h4><br /></h4><h4>Practical</h4><p>Now that you know the theory behind it, see if you can use the techniques we practiced in the last task, and the knowledge of what type of hash this is to crack the ntlm.txt file! <br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What do we need to set the "format" flag to, in order to crack this?<br />

```
nt
```

2. <p>What is the cracked value of this password?<br /></p>

```
mushroom
```

----------------------------------------

### TASK 6. Cracking /etc/shadow Hashes

<h4>Cracking Hashes from /etc/shadow</h4><p>The /etc/shadow file is the file on Linux machines where password hashes are stored. <span style="color:#000000">It also stores other information, such as the date of last password change and password expiration information. </span><span style="color:#000000"></span><span style="color:#000000">It contains one entry 
per line for each user or user account of the system. This file is usually only accessible by the root user- so in order to get your hands on the hashes you must have sufficient privileges, but if you do- there is a chance that you will be able to crack some of the hashes.<br /></span></p><p><span style="color:#000000"> </span></p><p><br /></p><h4>Unshadowing</h4><p>John can be very particular about the formats it needs data in to be able to work with it, for this reason- in order to crack /etc/shadow passwords, you must combine it with the /etc/passwd file in order for John to understand the data it's being given. To do this, we use a tool built into the John suite of tools called unshadow. The basic syntax of unshadow is as follows:</p><p><code>unshadow [path to passwd] [path to shadow]</code></p><p><code>unshadow</code> - Invokes the unshadow tool <br /></p><p><code>[path to passwd]</code> - The file that contains the copy of the /etc/passwd file you've taken from the target machine <br /></p><p><code>[path to shadow]</code> - The file that contains the copy of the /etc/shadow file you've taken from the target machine </p><p><b>Example Usage:</b></p><p>unshadow local_passwd local_shadow &gt; unshadowed.txt</p><p><b>Note on the files</b></p><p>When using unshadow, you can either use the entire /etc/passwd and /etc/shadow file- if you have them available, or you can use the relevant line from each, for example:</p><p><b>FILE 1 - local_passwd<br /></b></p><p>Contains the /etc/passwd line for the root user:</p><p>root:x:0:0::/root:/bin/bash</p><p><b>FILE 2 - local_shadow</b></p><p>Contains the /etc/shadow line for the root user:<br /></p><p>root:$6$2nwjN454g.dv4HN/$m9Z/r2xVfweYVkrr.v5Ft8Ws3/YYksfNwq96UL1FX0OJjY1L6l.DS3KEVsZ9rOVLB/ldTeEL/OIhJZ4GMFMGA0:18576::::::</p><h4><br /></h4><h4>Cracking</h4><p>We're then able to feed the output from unshadow, in our example use case called "unshadowed.txt" directly into John. We should not need to specify a mode here as we have made the input specifically for John, however in some cases you will need to specify the format as we have done previously using: <code>--format=sha512crypt</code></p><p><code>john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt</code></p><h4><br /></h4><h4>Practical</h4><p>Now, see if you can follow the process to crack the password hash of the root user that is provided in the "etc_hashes.txt" file. Good luck!<br /></p><p><span style="color:#000000"></span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the root password?<br />

```
1234
```

----------------------------------------

### TASK 7. Single Crack Mode

<p></p><h4>Single Crack Mode</h4><p>So far we've been using John's wordlist mode to deal with brute forcing simple., and not so simple hashes. But John also has another mode, called Single Crack mode. In this mode, John uses only the information provided in the username, to try and work out possible passwords heuristically, by slightly changing the letters and numbers contained within the username.</p><p><br /></p><h4>Word Mangling<br /></h4><p>The best way to show what Single Crack mode is,  and what word mangling is, is to actually go through an example:</p><p>If we take the username: Markus </p><p>Some possible passwords could be:</p><ul><li>Markus1, Markus2, Markus3 (etc.)</li><li>MArkus, MARkus, MARKus (etc.)</li><li>Markus!, Markus$, Markus* (etc.)</li></ul><p>This technique is called word mangling. John is building it's own dictionary based on the information that it has been fed and uses a set of rules called "mangling rules" which define how it can mutate the word it started with to generate a wordlist based off of relevant factors for the target you're trying to crack. This is exploiting how poor passwords can be based off of information about the username, or the service they're logging into.<br /></p><h4><br /></h4><h4>GECOS</h4><p>John's implementation of word mangling also features compatibility with the Gecos fields of the UNIX operating system, and other UNIX-like operating systems such as Linux. So what are Gecos? Remember in the last task where we were looking at the entries of both /etc/shadow and /etc/passwd? Well if you look closely You can see that each field is seperated by a colon ":". Each one of the fields that these records are split into are called Gecos fields. John can take information stored in those records, such as full name and home directory name to add in to the wordlist it generates when cracking /etc/shadow hashes with single crack mode.</p><p><br /></p><h4>Using Single Crack Mode</h4><p>To use single crack mode, we use roughly the same syntax that we've used to so far, for example if we wanted to crack the password of the user named "Mike", using single mode, we'd use:<br /></p><p><code>john --single --format=[format] [path to file] </code></p><p><code>--single</code> - This flag lets john know you want to use the single hash cracking mode.</p><p><b>Example Usage:</b></p><p></p><p>john --single --format=raw-sha256 hashes.txt</p><p><b>A Note on File Formats in Single Crack Mode:</b></p><p>If you're cracking hashes in single crack mode, you need to change the file format that you're feeding john for it to understand what data to create a wordlist from. You do this by prepending the hash with the username that the hash belongs to, so according to the above example- we would change the file hashes.txt </p><p><b>From: <span></span> </b><span><br /></span></p><p><span></span>1efee03cdcb96d90ad48ccc7b8666033</p><p><b>To </b></p><p>mike:1efee03cdcb96d90ad48ccc7b8666033</p><h4><br /></h4><h4>Practical</h4><p>Now you're familiar with the Syntax for John's single crack mode, download the attached hash and crack it, assuming that the user it belongs to is called "Joker".</p><p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is Joker's password?<br />

```
Jok3r
```

----------------------------------------

### TASK 8. Custom Rules

<h4>What are Custom Rules?<br /></h4><p>As we journeyed through our exploration of what John can do in Single Crack Mode- you may have some ideas about what some good mangling patterns would be, or what patterns your passwords often use- that could be replicated with a certain mangling pattern. The good news is you can define your own sets of rules, which John will use to dynamically create passwords. This is especially useful when you know more information about the password structure of whatever your target is. </p><p><br /></p><h4>Common Custom Rules</h4><p>Many organisations will require a certain level of password complexity to try and combat dictionary attacks, meaning that if you create an account somewhere, go to create a password and enter:</p><p>polopassword</p><p>You may receive a prompt telling you that passwords have to contain at least one of the following:</p><ul><li> Capital letter</li><li>Number</li><li>Symbol</li></ul><p>This is good! However, we can exploit the fact that most users will be predictable in the location of these symbols. For the above criteria, many users will use something like the following:</p><p>Polopassword1!</p><p>A password with the capital letter first, and a number followed by a symbol at the end. This pattern of the familiar password, appended and prepended by modifiers (such as the capital letter or symbols) is a memorable pattern that people will use, and reuse when they create passwords. This pattern can let us exploit password complexity predictability.<br /></p><p>Now this does meet the password complexity requirements, however as an attacker we can exploit the fact we know the likely position of these added elements to create dynamic passwords from our wordlists.</p><p><br /></p><h4>How to create Custom Rules</h4><p>Custom rules are defined in the <code>john.conf</code> file, usually located in <code>/etc/john/john.conf</code> if you have installed John using a package manager or built from source with <code>make</code> and in <code>/opt/john/john.conf</code> on the TryHackMe Attackbox.<br /></p><p>Let's go over the syntax of these custom rules, using the example above as our target pattern. Note that there is a massive level of granular control that you can define in these rules, I would suggest taking a look at the wiki <a href="https://www.openwall.com/john/doc/RULES.shtml" target="_blank">here</a> in order to get a full view of the types of modifier you can use, as well as more examples of rule implementation. </p><p><br /></p><p>The first line:</p><p><code>[List.Rules:THMRules]</code> - Is used to define the name of your rule, this is what you will use to call your custom rule as a John argument.</p><p>We then use a regex style pattern match to define where in the word will be modified, again- we will only cover the basic and most common modifiers here:</p><p><code>Az</code> - Takes the word and appends it with the characters you define <br /></p><p><code>A0</code> - Takes the word and prepends it with the characters you define<br /></p><p><code>c</code> - Capitalises the character positionally</p><p><br /></p><p>These can be used in combination to define where and what in the word you want to modify.</p><p>Lastly, we then need to define what characters should be appended, prepended or otherwise included, we do this by adding character sets in square brackets <code>[ ]</code> in the order they should be used. These directly follow the modifier patterns inside of double quotes <code>" "</code>. Here are some common examples:</p><p><br /></p><p><code>[0-9]</code> - Will include numbers 0-9<br /></p><p><code>[0]</code> - Will include only the number 0<br /></p><p><code>[A-z]</code> - Will include both upper and lowercase <br /></p><p><code>[A-Z]</code> - Will include only uppercase letters<br /></p><p><code>[a-z]</code> - Will include only lowercase letters <br /></p><p><code>[a]</code> - Will include only a<br /></p><p><code>[!£$%@]</code> - Will include the symbols !£$%@<br /></p><p><br /></p><p>Putting this all together, in order to generate a wordlist from the rules that would match the example password "Polopassword1!" (assuming the word polopassword was in our wordlist) we would create a rule entry that looks like this:</p><p><code>[List.Rules:PoloPassword]</code></p><p><code>cAz"[0-9] [!£$%@]"</code></p><p><br /></p><p>In order to: </p><p>Capitalise the first  letter - <code>c</code></p><p>Append to the end of the word - <code>Az</code></p><p>A number in the range 0-9 - <code>[0-9]</code></p><p>Followed by a symbol that is one of <code>[!£$%@]</code></p><p><br /></p><h4>Using Custom Rules</h4><p>We could then call this custom rule as a John argument using the  <code>--rule=PoloPassword</code> flag.<br /></p><p>As a full command: <code>john --wordlist=[path to wordlist] --rule=PoloPassword [path to file] </code></p><p><br /></p><p>As a note I find it helpful to talk out the patterns if you're writing a rule- as shown above, the same applies to writing RegEx patterns too.<br /></p><p>Jumbo John already comes with a large list of custom rules, which contain modifiers for use almost all cases. If you get stuck, try looking at those rules [around line 678] if your syntax isn't working properly.</p><p><br /></p><p>Now, time for you to have a go!<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What do custom rules allow us to exploit?<br />

```
Password complexity predictability
```

2. <p>What rule would we use to add all capital letters to the end of the word?</p>

```
Az"[A-Z]"
```

3. What flag would we use to call a custom rule called "THMRules"<br />

```
--rule=THMRules
```

----------------------------------------

### TASK 9. Cracking Password Protected Zip Files

<h4>Cracking a Password Protected Zip File </h4><p>Yes! You read that right. We can use John to crack the password on password protected Zip files. Again, we're going to be using a separate part of the john suite of tools to convert the zip file into a format that John will understand, but for all intents and purposes, we're going to be using the syntax that you're already pretty familiar with by now. </p><p><br /></p><h4>Zip2John</h4><p>Similarly to the unshadow tool that we used previously, we're going to be using the zip2john tool to convert the zip file into a hash format that John is able to understand, and hopefully crack. The basic usage is like this:</p><p><code>zip2john [options] [zip file] &gt; [output file]<br /></code></p><p><code>[options]</code> - Allows you to pass specific checksum options to zip2john, this shouldn't often be necessary <br /></p><p><code>[zip file]</code> - The path to the zip file you wish to get the hash of</p><p><code>&gt;</code> - This is the output director, we're using this to send the output from this file to the...<br /></p><p><code>[output file]</code> - This is the file that will store the output from <br /></p><p><b>Example Usage</b></p><p>zip2john zipfile.zip &gt; zip_hash.txt</p><h4><br /></h4><h4>Cracking</h4><p>We're then able to take the file we output from zip2john in
 our example use case called "zip_hash.txt" and, as we did with unshadow, feed it directly into John as we have made the input 
specifically for it.</p><p><code>john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt</code></p><br /><h4>Practical</h4><p>Now have a go at cracking the attached "secure" zip file!<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the password for the secure.zip file?<br />

```
pass123
```

2. <p>What is the contents of the flag inside the zip file?<br /></p>

```
THM{w3ll_d0n3_h4sh_r0y4l}
```

----------------------------------------

### TASK 10. Cracking Password Protected RAR Archives

<p></p><h4>Cracking a Password Protected RAR Archive </h4><p>We can use a similar process to the one we used in the last task to obtain the password for rar archives. If you aren't familiar, rar archives are compressed files created by the Winrar archive manager. Just like zip files they compress a wide variety of folders and files. </p><h4><br /></h4><h4>Rar2John </h4><p>Almost identical to the zip2john tool that we just used, we're going 
to use the rar2john tool to convert the rar file into a hash format
 that John is able to understand. The basic syntax is as follows:<br /></p><p><code>rar2john [rar file] &gt; [output file]<br /></code></p><p><code>rar2john</code> - Invokes the rar2john tool<br /></p><p><code>[rar file]</code> - The path to the rar file you wish to get the hash of</p><p><code>&gt;</code> - This is the output director, we're using this to send the output from this file to the...<br /></p><code>[output file]</code> - This is the file that will store the output from <p></p><p></p><p><b>Example Usage</b></p><p>rar2john rarfile.rar &gt; rar_hash.txt</p><p><br /></p><h4>Cracking</h4><p>Once again, we're then able to take the file we output from rar2john in
 our example use case called "rar_hash.txt" and, as we did with zip2john we can feed it directly into John..</p><p><code>john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt</code></p><br /><h4>Practical</h4>Now have a go at cracking the attached "secure" rar file!<p></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the password for the secure.rar file?

```
```

2. <p>What is the contents of the flag inside the zip file?</p>

```
```

----------------------------------------

### TASK 11. Cracking SSH Keys with John 

<h4>Cracking SSH Key Passwords<br /></h4>Okay, okay I hear you, no more file archives! Fine! Let's explore one more use of John that comes up semi-frequently in CTF challenges. Using John to crack the SSH private key password of id_rsa files. Unless configured otherwise, you authenticate your SSH login using a password. However, you can configure key-based authentication, which lets you use your private key, id_rsa, as an authentication key to login to a remote machine over SSH. However, doing so will often require a password- here we will be using John to crack this password to allow authentication over SSH using the key. <br /><h4><br /></h4><h4>SSH2John </h4><p>Who could have guessed it, another conversion tool? Well, that's what working with John is all about. As the name suggests ssh2john converts the id_rsa private key that you use to login to the SSH session into hash format that john can work with. Jokes aside, it's another beautiful example of John's versatility. The syntax is about what you'd expect. Note that if you don't have ssh2john installed, you can use ssh2john.py, which is located in the /opt/john/ssh2john.py. If you're doing this, replace the <code>ssh2john</code> command with <code>python3 /opt/ssh2john.py</code> or on Kali, <code> python /usr/share/john/ssh2john.py</code>.</p><p><code>ssh2john [id_rsa private key file] &gt; [output file]<br /></code></p><p>ssh2john - Invokes the ssh2john tool<br /></p><p><code>[id_rsa private key file]</code> - The path to the id_rsa file you wish to get the hash of</p><p><code>&gt;</code> - This is the output director, we're using this to send the output from this file to the...<br /></p><code>[output file]</code> - This is the file that will store the output from <p><b><br /></b></p><p><b>Example Usage</b></p><p>ssh2john id_rsa &gt; id_rsa_hash.txt</p><p><br /></p><h4>Cracking</h4><p>For the final time, we're feeding the file we output from ssh2john, which in our example use case is called "id_rsa_hash.txt" and, as we did with rar2john we can use this seamlessly with John:<br /></p><p><code>john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt</code></p><br /><h4>Practical</h4>Now I'd like you to crack the hash of the id_rsa file that's attached to this task!<br />

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What is the SSH private key password?<br />

```
```

----------------------------------------

### TASK 12. Further Reading

<h4><span style="font-size:1rem">Thank you for completing this room on John the Ripper! I hope you've learnt a lot along the way. I'm sure by now you understand the basic principles and the pattern that there is to using John with even the most obscure supported hashes. I'd recommend checking out the Openwall Wiki </span><a href="https://www.openwall.com/john/" target="_blank">here</a><span style="font-size:1rem"> for more information about using John, and advice, updates or news about the tool.</span><br /></h4>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Read the above.

```
```


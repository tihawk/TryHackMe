# TryHackMe walkthrough

## Encryption - Crypto 101

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. What will this room cover?

<h3>This room will cover:</h3>
<ul>
<li>Why cryptography matters for security and CTFs</li>
<li>The two main classes of cryptography and their uses</li>
<li>RSA, and some of the uses of RSA</li>
<li>2 methods of Key Exchange</li>
<li>Notes about the future of encryption with the rise of Quantum Computing</li></ul><p>Note: This room expects some familiarity with tools, and some research into how to use them yourself!<br />I recommend completing <a href="https://tryhackme.com/room/ccpentesting" target="_blank">CC Pentesting</a> first for some familiarity with John The Ripper.</p><ul>
</ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. I'm ready to learn about encryption

```
OK
```

----------------------------------------

### TASK 2. Key terms

<p>Many of these key terms are shared with <a href="https://tryhackme.com/room/hashingcrypto101">https://tryhackme.com/room/hashingcrypto101</a>, so you might
    be able to skip over some if you're already familiar.<br /></p>
<p><b>Ciphertext</b> - The result of encrypting a plaintext, encrypted data</p>
<p><b>Cipher</b> - A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are many non
    cryptographic ciphers like Caesar.</p>
<p><b>Plaintext</b> - Data before encryption, often text but not always. Could be a photograph or other file</p>
<p><b>Encryption</b> - Transforming data into ciphertext, using a cipher.</p>
<p><b>Encoding</b> - NOT a form of encryption, just a form of data representation like base64. Immediately reversible.
</p>
<p><b>Key</b> - Some information that is needed to correctly decrypt the ciphertext and obtain the plaintext.</p>
<p><b>Passphrase </b>- Separate to the key, a passphrase is similar to a password and used to protect a key.</p>
<p><b>Asymmetric encryption</b> - Uses different keys to encrypt and decrypt.</p>
<p><b>Symmetric encryption</b> - Uses the same key to encrypt and decrypt</p>
<p><b>Brute force</b> - Attacking cryptography by trying every different password or every different key</p>
<p><b>Cryptanalysis</b> - Attacking cryptography by finding a weakness in the underlying maths</p>
<p><b>Alice and Bob</b> - Used to represent 2 people who generally want to communicate. They’re named Alice and Bob
    because this gives them the initials A and B. <a href="https://en.wikipedia.org/wiki/Alice_and_Bob" target="_blank">https://en.wikipedia.org/wiki/Alice_and_Bob</a><span style="font-size:1rem"></span> for more information, as these extend through the alphabet to represent many
        different people involved in communication.</p><p><b>WARNING:</b> This room is very theory heavy. Cryptography is a big topic, and this room is designed to just scratch the surface.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>I agree not to complain too much about how theory heavy this room is.</p>

```
OK
```

2. <p>Are SSH keys protected with a passphrase or a password?</p>

```
passphrase
```

----------------------------------------

### TASK 3. Why is Encryption important?

<p>Cryptography is used to protect confidentiality, ensure integrity, ensure authenticity. You use cryptography every
    day most likely, and you’re almost certainly reading this now over an encrypted connection.</p>
<p>When logging into TryHackMe, your credentials were sent to the server. These were encrypted, otherwise someone
    would be able to capture them by snooping on your connection.</p>
<p>When you connect to SSH, your client and the server establish an encrypted tunnel so that no one can snoop on your
    session.</p>
<p>When you connect to your bank, there’s a certificate that uses cryptography to prove that it is actually your bank
    rather than a hacker.</p>
<p>When you download a file, how do you check if it downloaded right? You can use cryptography here to verify a
    checksum of the data.</p>
<p>You rarely have to interact directly with cryptography, but it silently protects almost everything you do
    digitally.</p>
<p>Whenever sensitive user data needs to be stored, it should be encrypted. Standards like <a href="https://www.pcisecuritystandards.org/documents/PCI_DSS_for_Large_Organizations_v1.pdf" target="_blank">PCI-DSS</a> state that the data
    should be encrypted both at rest (in storage) AND while being transmitted. If you’re handling payment card details,
    you need to comply with these PCI regulations. Medical data has similar standards. With legislation like GDPR and California’s data protection, data breaches
    are extremely costly and dangerous to you as either a consumer or a business.</p>
<p><b>DO NOT</b> encrypt passwords unless you’re doing something like a password manager. Passwords should not be stored in plaintext, and
    you should use hashing to manage them safely.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What does SSH stand for?

```
Secure Shell
```

2. <p>How do webservers prove their identity?<br /></p>

```
certificates
```

3. <p>What is the main set of standards you need to comply with if you store or process payment card details?</p>

```
PCI-DSS
```

----------------------------------------

### TASK 4. Crucial Crypto Maths

<p>There's a little bit of math(s) that comes up relatively often in cryptography. The Modulo operator. Pretty much every programming language implements this operator, or has it available through a library. When you need to work with large numbers, use a programming language. Python is good for this as integers are unlimited in size, and you can easily get an interpreter.</p>
<p>When learning division for the first time, you were probably taught to use remainders in your answer. X % Y is the
    remainder when X is divided by Y.</p>
<h3>Examples</h3>
<p>25 % 5 = 0 (5*5 = 25 so it divides exactly with no remainder)</p>
<p>23 % 6 = 5 (23 does not divide evenly by 6, there would be a remainder of 5)</p>
<p>An important thing to remember about modulo is that it’s not reversible. If I gave you an equation: x % 5 = 4, there
    are infinite values of x that will be valid.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. What's 30 % 5?

```
0
```

2. <p>What's 25 % 7</p>

```
4
```

3. <p>What's 118613842 % 9091<br /></p>

```
3565
```

----------------------------------------

### TASK 5. Types of Encryption

<p>The two main categories of Encryption are symmetric and asymmetric.</p><p><b>Symmetric encryption</b> uses the same key to encrypt and decrypt the data. Examples of Symmetric encryption are DES (Broken) and AES. These algorithms tend to be faster than asymmetric cryptography, and use smaller keys (128 or 256 bit keys are common for AES, DES keys are 56 bits long).</p><p><b>Asymmetric encryption</b> uses a pair of keys, one to encrypt and the other in the pair to decrypt. Examples are RSA and Elliptic Curve Cryptography. Normally these keys are referred to as a public key and a private key. Data encrypted with the private key can be decrypted with the public key, and vice versa. Your private key needs to be kept private, hence the name. Asymmetric encryption tends to be slower and uses larger keys, for example RSA typically uses 2048 to 4096 bit keys.</p><p>RSA and Elliptic Curve cryptography are based around different mathematically difficult (intractable) problems, which give them their strength. More about RSA later.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Should you trust DES? Yea/Nay

```
Nay
```

2. <p>What was the result of the attempt to make DES more secure so that it could be used for longer?</p>

```
Triple DES
```

3. <p>Is it ok to share your public key? Yea/Nay</p>

```
Yea
```

----------------------------------------

### TASK 6. RSA - Rivest Shamir Adleman

<h3>The math(s) side</h3>
<p>RSA is based on the mathematically difficult problem of working out the factors of a large number. It’s very quick
    to multiply two prime numbers together, say 17*23 = 391, but it’s quite difficult to work out what two prime numbers
    multiply together to make 14351 (113x127 for reference).</p>
<h3>The attacking side</h3>
<p>The maths behind RSA seems to come up relatively often in CTFs, normally requiring you to calculate variables or
    break some encryption based on them. The wikipedia page for RSA seems complicated at first, but will give you almost
    all of the information you need in order to complete challenges.</p><p>There are some excellent tools for defeating RSA
    challenges in CTFs, and my personal favorite is <a href="https://github.com/Ganapati/RsaCtfTool" target="_blank">https://github.com/Ganapati/RsaCtfTool</a> which has worked very well
    for me. I’ve also had some success with <a href="https://github.com/ius/rsatool" target="_blank">https://github.com/ius/rsatool</a>.</p>
<p>The key variables that you need to know about for RSA in CTFs are p, q, m, n, e, d, and c.</p>
<p>“p” and “q” are large prime numbers, “n” is the product of p and q.</p>
<p>The public key is n and e, the private key is n and d.</p>
<p>“m” is used to represent the message (in plaintext) and “c” represents the ciphertext (encrypted text).</p>

<h3>CTFs involving RSA</h3>

<p>Crypto CTF challenges often present you with a set of these values, and you need to break the encryption and
    decrypt a message to retrieve the flag.</p>

<p>There’s a lot more maths to RSA, and it gets quite complicated fairly quickly. If you want to learn the maths behind it, I
    recommend reading MuirlandOracle’s blog post here: <a href="https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/">https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/</a>.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. p = 4391, q = 6659. What is n?

```
29239669
```

2. <p>I understand enough about RSA to move on, and I know where to look to learn more if I want to.</p>

```
OK
```

----------------------------------------

### TASK 7. Establishing Keys Using Asymmetric Cryptography

<p>A very common use of asymmetric cryptography is exchanging keys for symmetric encryption.</p>
<p>Asymmetric encryption tends to be slower, so for things like HTTPS symmetric encryption is better.</p>
<p>But the question is, how do you agree a key with the server without transmitting the key for people snooping to
    see?</p>
<h3>Metaphor time</h3>
<p>Imagine you have a secret code, and instructions for how to use the secret code. If you want to send your friend
    the instructions without anyone else being able to read it, what you could do is ask your friend for a lock.</p>
<p>Only they have the key for this lock, and we’ll assume you have an indestructible box that you can lock with it.
</p>
<p>If you send the instructions in a locked box to your friend, they can unlock it once it reaches them and read the
    instructions.</p>
<p>After that, you can communicate in the secret code without risk of people snooping.</p>
<p>In this metaphor, the secret code represents a symmetric encryption key, the lock represents the server’s public
    key, and the key represents the server’s private key.</p>
<p>You’ve only used asymmetric cryptography once, so it’s fast, and you can now communicate privately with symmetric
    encryption.</p>
<h3>The Real World</h3>
<p>In reality, you need a little more cryptography to verify the person you’re talking to is who they say
    they are, which is done using digital signatures and certificates. You can find a lot more detail on how HTTPS (one example where you need to exchange keys) really works from this excellent blog post. <a href="https://robertheaton.com/2014/03/27/how-does-https-actually-work/" target="_blank">https://robertheaton.com/2014/03/27/how-does-https-actually-work/</a></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. I understand how keys can be established using Public Key (asymmetric) cryptography.

```
OK
```

----------------------------------------

### TASK 8. Digital signatures and Certificates

<h3>What's a Digital Signature?</h3>
<p>Digital signatures are a way to prove the authenticity of files, to prove who created or modified them. Using
    asymmetric cryptography, you produce a signature with your private key and it can be verified using your public key.
    As only you should have access to your private key, this proves you signed the file. Digital signatures and physical
    signatures have the same value in the UK, legally.</p>

<p>The simplest form of digital signature would be encrypting the document with your private key, and then if someone
    wanted to verify this signature they would decrypt it with your public key and check if the files match.</p>
<h3>Certificates - Prove who you are!</h3>
<p>Certificates are also a key use of public key cryptography, linked to digital signatures.
A common place where they’re used is for HTTPS. How
    does your web browser know that the server you’re talking to is the real tryhackme.com?</p>
<p>The answer is certificates. The web server has a certificate that says it is the real tryhackme.com. The
    certificates have a chain of trust, starting with a root CA (certificate authority). Root CAs are automatically
    trusted by your device, OS, or browser from install. Certs below that are trusted because the Root CAs say they
    trust that organisation. Certificates below that are trusted because the organisation is trusted by the Root CA and
    so on. There are long chains of trust. Again, this blog post explains this much better than I can. <a href="https://robertheaton.com/2014/03/27/how-does-https-actually-work/" target="_blank">https://robertheaton.com/2014/03/27/how-does-https-actually-work/</a></p>

<p>You can get your own HTTPS certificates for domains you own using Let’s Encrypt for free. If you run a website,
    it’s worth setting it up.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. What company is TryHackMe's certificate issued to?

```
Cloudflare
```

----------------------------------------

### TASK 9. SSH Authentication

<h3>Encryption and SSH authentication</h3>
<p>By default, SSH is authenticated using usernames and passwords in the same way that you would log in to the
    physical machine.</p>
<p>At some point, you’re almost certain to hit a machine that has SSH configured with key authentication instead. This
    uses public and private keys to prove that the client is a valid and authorised user on the server. By default, SSH
    keys are RSA keys. You can choose which algorithm to generate, and/or add a passphrase to encrypt the SSH key.
    <code>ssh-keygen</code> is the program used to generate pairs of keys most of the time.</p>

<h3>SSH Private Keys</h3>
<p>You should treat your private SSH keys like passwords. Don’t share them, they’re called private keys for a reason.
    If someone has your private key, they can use it to log in to servers that will accept it unless the key is
    encrypted.</p>
<p>It’s very important to mention that the passphrase to decrypt the key isn’t used to identify you to the
    server at all, all it does is decrypt the SSH key. The passphrase is never transmitted, and never leaves your
    system.</p>
<p>Using tools like John the Ripper, you can attack an encrypted SSH key to attempt to find the passphrase,
    which highlights the importance of using a secure passphrase and keeping your private key private.</p>
<p>When generating an SSH key to log in to a remote machine, you should generate the keys on your machine and then copy the public key over as this means the private
    key never exists on the target machine. For temporary keys generated for access to CTF boxes, this doesn't matter as much.</p>

<h3>How do I use these keys?</h3>
<p>The ~/.ssh folder is the default place to store these keys for OpenSSH. The <code>authorized_keys</code> (note the US English
    spelling) file in this directory holds public keys that are allowed to access the server if key authentication is enabled. By default on many distros, key authentication is enabled as it is more secure than using a password to authenticate. Normally for the root user, only key authentication is enabled.</p>
<p>In order to use a private SSH key, the permissions must be set up correctly otherwise your SSH client will ignore the file with a warning. Only the owner should be able to read or write to the private key (600 or stricter). <code>ssh -i keyNameGoesHere user@host</code> is how you specify a key for the standard Linux OpenSSH client.</p>

<h3>Using SSH keys to get a better shell</h3>
<p>SSH keys are an excellent way to “upgrade” a reverse shell, assuming the user has login enabled (www-data normally
    does not, but regular users and root will). Leaving an SSH key in authorized_keys on a box can be a useful backdoor, and you don't need to deal with any of the issues of unstabilised reverse shells like Control-C or lack of tab completion.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>I recommend giving this a go yourself. Deploy a VM, like <a href="https://tryhackme.com/room/linux2" target="_blank">Linux Fundamentals 2</a> and try to add an SSH key and log in with the private key.</p>

```
OK
```

2. <p>Download the SSH Private Key attached to this room.</p>

```
OK
```

3. <p>What algorithm does the key use?</p>

```
RSA
```

4. <p>Crack the password with John The Ripper and rockyou, what's the passphrase for the key?</p>

```bash
# ssh2john is broken for python3
sed 's/decodestring/decodebytes/' /usr/bin/ssh2john | python3 - id_rsa > forJohn
john forJohn --wordlist /opt/rockyou.txt
```

```
delicious
```

----------------------------------------

### TASK 10. Explaining Diffie Hellman Key Exchange

<h3>What is Key Exchange?</h3>
<p>Key exchange allows 2 people/parties to establish a set of common cryptographic keys without an observer being able
    to get these keys. Generally, to establish common symmetric keys.</p>

<h3>How does Diffie Hellman Key Exchange work?</h3>
<p>Alice and Bob want to talk securely. They want to establish a common key, so they can use symmetric cryptography,
    but they don’t want to use key exchange with asymmetric cryptography. This is where DH Key Exchange comes in.</p>
<p>Alice and Bob both have secrets that they generate, let’s call these A and B. They also have some common material
    that’s public, let’s call this C.</p>
<p>We need to make some assumptions. Firstly, whenever we combine secrets/material it’s impossible or very very
    difficult to separate. Secondly, the order that they're combined in doesn’t matter.</p>
<p>Alice and Bob will combine their secrets with the common material, and form AC and BC. They will then send these to
    each other, and combine that with their secrets to form two identical keys, both ABC. Now they can use this key to
    communicate.</p>

<h3>Extra Resources</h3>
<p>An excellent video if you want a visual explanation is available here. <a href="https://www.youtube.com/watch?v=NmM9HA2MQGI" target="_blank">https://www.youtube.com/watch?v=NmM9HA2MQGI</a></p>
<p>DH Key Exchange is often used alongside RSA public key cryptography, to prove the identity of the person you’re
    talking to with digital signing. This prevents someone from attacking the connection with a man-in-the-middle attack
    by pretending to be Bob.</p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. I understand how Diffie Hellman Key Exchange works at a basic level

```
OK
```

----------------------------------------

### TASK 11. PGP, GPG and AES

<h3>What is PGP?</h3>
<p>PGP stands for Pretty Good Privacy. It’s a software that implements encryption for
    encrypting files, performing digital signing and more.</p>
<h3>What is GPG?</h3>
<p><a href="https://gnupg.org/" target="_blank">GnuPG or GPG</a> is an Open Source implementation of PGP from the GNU project. You may need to use GPG to decrypt files
    in CTFs. With PGP/GPG, private keys can be protected with passphrases in a similar way to SSH private keys. If the key is passphrase protected, you can
    attempt to crack this passphrase using John The Ripper and gpg2john. The key provided in this task is <u>not</u> protected with a passphrase.</p><p>The man page for GPG can be found online <a href="https://www.gnupg.org/gph/de/manual/r1023.html" target="_blank">here</a>.</p>
<h3>What about AES?</h3>
<p>AES, sometimes called Rijndael after its creators, stands for Advanced Encryption Standard. It was a replacement
    for DES which had short keys and other cryptographic flaws.
</p><p>AES and DES both operate on blocks of data (a block is a
    fixed size series of bits).</p>
<p>AES is complicated to explain, and doesn’t seem to come up as often. If you’d like to
    learn how it works, here’s an excellent video from Computerphile <a href="https://www.youtube.com/watch?v=O4xNJsjtN6E">https://www.youtube.com/watch?v=O4xNJsjtN6E</a></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. Time to try some GPG. Download the archive attached and extract it somewhere sensible.

```
OK
```

2. <p>You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?</p>

```
unzip zip
gpg --import tryhackme.key
gpg --decrypt message.gpg
```

```
Pineapple
```

----------------------------------------

### TASK 12. The Future - Quantum Computers and Encryption

<p>Quantum computers will soon be a problem for many types of encryption.</p>

<h3>Asymmetric and Quantum</h3>
<p>While it’s unlikely we’ll have sufficiently powerful quantum computers until around 2030, once these exist
    encryption that uses RSA or Elliptical Curve Cryptography will be very fast to break. This is because quantum
    computers can very efficiently solve the mathematical problems that these algorithms rely on for their strength.
</p>

<h3>AES/DES and Quantum</h3>
<p>AES with 128 bit keys is also likely to be broken by quantum computers in the near future, but 256 bit AES can’t be
    broken as easily. Triple DES is also vulnerable to attacks from quantum computers.</p>

<h3>Current Recommendations</h3>
<p>The NSA recommends using RSA-3072 or better for asymmetric encryption and AES-256 or better for symmetric
    encryption. There are several competitions currently running for quantum safe cryptographic algorithms, and it’s
    likely that we will have a new encryption standard before quantum computers become a threat to RSA and AES.</p>

<h3>Learn More about Quantum Computers and Cryptography</h3>
<p>If you’d like to learn more about this, NIST has resources that detail what the issues with current encryption is
    and the currently proposed solutions for these. <a href="https://doi.org/10.6028/NIST.IR.8105">https://doi.org/10.6028/NIST.IR.8105</a></p> 
<p>I also recommend the book "Cryptography Apocalypse" By Roger A. Grimes, as this was my introduction to quantum computing and quantum safe cryptography.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. I understand that quantum computers affect the future of encryption. I know where to look if I want to learn more.

```
OK
```


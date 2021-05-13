# TryHackMe challenge

## Pickle Rick

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. Pickle Rick 

<p style="text-align:center;"><img src="https://i.imgur.com/o9pyhyU.jpg" style="width:161.484px;height:161.484px;" /><br /></p><p style="text-align:center;">This Rick and Morty themed challenge requires you to exploit a webserver to find 3 ingredients that will<span style="font-size:1rem;"> help Rick make his potion to transform himself back into a human from a pickle.</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Deploy the virtual machine on this task and explore the web application.</p><p>What is the first <span style="font-size:1rem;">ingredient Rick needs?</span></p>

```bash
export IP=10.10.241.78

nmap -sC -sV -vvv -oN nmap/initial $IP
```

```html
  <!--

    Note to self, remember username!

    Username: R1ckRul3s

  -->
```

```bash
# robots.txt

Wubbalubbadubdub
```
```
http://10.10.241.78/login.php
```

`strings Sup3rS3cretPickl3Ingred.txt`

```
mr. meeseek hair
```

2. <p>Whats the second ingredient Rick needs?<br /></p>

`strings /home/rick/second\ ingredients`

```
1 jerry tear
```

3. <p>Whats the final ingredient Rick needs?<br /></p>

`sudo -l`
`sudo strings /root/3rd.txt`

```
fleeb juice
```


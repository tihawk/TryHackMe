# TryHackMe challenge

## Intro to x86-64

> _tihawk | May 17, 2021_

----------------------------------------

### TASK 1. Description and Objectives

<p><span style="font-family:&quot;Arial Black&quot;"><span style="font-family:Arial">This room will look at the basic primitives of Intel's x86-64 assembly language, and will use these primitives to understand the construction of basic programs using loops, functions and procedures. The tasks attached to this room will use the</span> </span><a href="https://github.com/radare/radare2"><span style="font-family:Arial">r2 reverse engineering framework</span></a><span style="font-family:Arial">, which will come installed in the machine attached to this room. The username of the machine attached to the next task is <b>tryhackme</b> and the password is <b>reismyfavl33t</b>. To access the machine, SSH into it on port 22. </span></p><p><span style="font-family:Arial">Here are a few things to note before beginning the room:</span></p><ul><li><span style="font-family:Arial">this room will use the AT&amp;T syntax. In general, people either use the AT&amp;T syntax or the Intel Syntax(differences are highlighted </span><a href="http://web.mit.edu/rhel-doc/3/rhel-as-en-3/i386-syntax.html"><span style="font-family:Arial">here</span></a><span style="font-family:Arial">).</span></li><li><span style="font-family:Arial">This room aims to be a gentle introduction to radare2. While they are not shown here, radare has a lot of powerful features and tools which can be found </span><a href="https://github.com/radare/radare2/blob/master/doc/intro.md"><span style="font-family:Arial">here</span></a><span style="font-family:Arial">, </span><a href="https://gist.github.com/williballenthin/6857590dab3e2a6559d7"><span style="font-family:Arial">here </span></a><span style="font-family:Arial">and </span><a href="https://web.archive.org/web/20180312191821/http://www.radare.org/get/THC2018.pdf" target="_blank"><span style="font-family:Arial">here</span></a></li><li><span style="font-family:Arial">As soon as your start r2, remember to enter e asm.syntax=att to ensure that you are using the AT&amp;T syntax.</span></li><li><span style="font-family:Arial">The addresses shown on the images in the tasks below may be different from the addresses you view when you disassemble the files.</span></li></ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read the above.</p>

```
OK
```

----------------------------------------

### TASK 2. Introduction

<p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">Computers execute machine code, which is encoded as bytes, to carry out tasks on a computer. Since different computers have different processors, the machine code executed on these computers is specific to the processor. In this case, we’ll be looking at the Intel x86-64 instruction set architecture which is most commonly found today. Machine code is usually represented by a more readable form of the code called assembly code. This machine is code is usually produced by a compiler, which takes the source code of a file, and after going through some intermediate stages, produces machine code that can be executed by a computer. Without going into too much detail, Intel first started out by building 16-bit instruction set, followed by 32 bit, after which they finally created 64 bit. All these instruction sets have been created for backward compatibility, so code compiled for 32 bit architecture will run on 64 bit machines. As mentioned earlier, before an executable file is produced, the source code is first compiled into assembly(.s files), after which the assembler converts it into an object program(.o files), and operations with a linker finally make it an executable. </span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">
</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The best way to actually start explaining assembly is by diving in. We’ll be using radare2 to do this - radare2 is a framework for reverse engineering and analysing binaries. It can be used to disassemble binaries(translate machine code to assembly, which is actually readable) and debug said binaries(by allowing a user to step through the execution and view the state of the program). 

</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The first step is to execute the program intro by running</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>./intro</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Which then just shows the following output</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh5.googleusercontent.com/JjT_G7sF5ScGMJWTisYH3N49djt64Dx2_6CkOtXBSezoheO0uo7wlu0FQBLBLTyjA_PsRDHrRYTYrvqtA0NVFG0Kt2EGosxx7QvBf32cEjSMSYEOh85uRFJFKy2AxLhsovfUTT9O" width="363" height="52" style="border:none;" /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">From the execution, it can be seen that the program is creating two variables and switching their values. Time to see what it’s actually doing under the hood!</span></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">
Go to the introduction folder on the virtual machine and run the command:</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>r2 -d intro </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">This will open the binary in debugging mode. Once the binary is open, one of the first things to do is ask r2 to analyze the program, and this can be done by typing in:</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>aa</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Which is the most common analysis command. It analyses all symbols and entry points in the executable.</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The run</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>e asm.syntax=att</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-family:Arial;font-size:14px;">to set the disassembly syntax to AT&amp;T.</span></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">
The analysis in this case involves extracting function names, flow control information and much more! r2 instructions are usually based on a single character, so it is easy to get more information about the commands. For general help, run:</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>?</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">For more specific information, for example, about analysis, run</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>a?</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">
Once the analysis is complete, you would want to know where to start analysing from - most programs have an entry point defined as main. To find a list of the functions run:</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>afl</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh4.googleusercontent.com/OMdwgZHBcZxoBjRON-zmPmdlfeaCcZUstR0S5qev7mofmxTEGwVzkZAenUYlKXEy94wBWA8XoSsWQnXbwAroPPj2gq1rrrytoavs-Vc97PwK9eblUtGx-DBj3EMHS7xXN5Jn2_9f" width="622" height="240" style="border:none;" /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">As seen here, there actually is a function at main. Let’s examine the assembly code at main by running the command</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>pdf @main</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Where pdf means print disassembly function. Doing so will give us the following view</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh4.googleusercontent.com/HometWAQT4JO7lJN5-tipL_tiBL8T270njUm4bTTdIIXIXOm3oEb41YhuUcq1dl0oK5b_y5QfqbzZJlDsPQKQ-G7LMVqPADbpz1uvD6TfCM7UONbEAmAVn_bae7W2Rpj2dfZDJDV" width="624" height="232" style="border:none;" /></span></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">
As we can see from above, the values on the complete left column are memory addresses of the instructions, and these are usually stored in a structure called the stack(which we will talk about later). The middle column contains the instructions encoded in bytes(what is usually the machine code), and the last column actually contains the human readable instructions. </span><br /></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">The core of assembly language involves using registers to do the following:</span><br /></p><ul><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Transfer data between memory and register, and vice versa</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Perform arithmetic operations on registers and data</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Transfer control to other parts of the program</span></p></li></ul><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Since the architecture is x86-64, the registers are 64 bit and Intel has a list of 16 registers:

</span></p><div style="margin-left:0pt;"><table><tbody><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">64 bit</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">32 bit</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rax</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%eax</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rbx</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%ebx</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rcx</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%ecx</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rdx</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%edx</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rsi</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%esi</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rdi</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%edi</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rsp</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%esp</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%rbp</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%ebp</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r8</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r8d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r9</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r9d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r10</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r10d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r11</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r11d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r12</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r12d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r13</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r13d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r14</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r14d</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r15</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">%r15d</span></p></td></tr></tbody></table></div><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">
Even though the registers are 64 bit, meaning they can hold up to 64 bits of data, other parts of the registers can also be referenced. In this case, registers can also be referenced as 32 bit values as shown. What isn’t shown is that registers can be referenced as 16 bit and 8 bit(higher 4 bit and lower 4 bit). </span><br /></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">The first 6 registers are known as general purpose registers. The %rsp is the stack pointer and it points to the top of the stack which contains the most recent memory address. The stack is a data structure that manages memory for programs. %rbp is a frame pointer and points to the frame of the function currently being executed - every function is executed in a new frame. To move data using registers, the following instruction is used:</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>movq source, destination</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">This involves:</span></p><ul><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Transferring constants(which are prefixed using the </span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">$</span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> operator) e.g. </span><code>movq $3 rax</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> would move the constant 3 to the register</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">Transferring values from a register e.g. </span><code>movq %rax %rbx</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:italic;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"> </span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">which involves moving value from rax to rbx</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">Transferring values from memory which is shown by putting registers inside brackets e.g. </span><code>movq %rax (%rbx)</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:italic;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"> </span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">which means move value stored in %rax to memory location represented by %rbx.</span></p></li></ul><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The last letter of the mov instruction represents the size of the data:</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br /></span></p><div style="margin-left:0pt;"><table><tbody><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Intel Data Type</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Suffix</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Size(bytes)</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Byte</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">b</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">1</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Word</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">w</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Double Word</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">l</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Quad Word</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">q</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Quad Word</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">q</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Single Precision</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">s</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p></td></tr><tr><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Double Precision</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">l</span></p></td><td><p style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8</span></p></td></tr></tbody></table></div><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">When dealing with memory manipulation using registers, there are other cases to be considered:</span></p><ul><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">(Rb, Ri) = MemoryLocation[Rb + Ri]</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">D(Rb, Ri) = MemoryLocation[Rb + Ri + D]</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">(Rb, Ri, S) = MemoryLocation(Rb + S * Ri]</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">D(Rb, Ri, S) = MemoryLocation[Rb + S * Ri + D]</span></p></li></ul><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">Some other important instructions are:</span><br /></p><ul><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>leaq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:italic;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: </span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">this instruction sets destination to the address denoted by the expression in source</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>addq source, destination</code><span style="font-style:italic;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: </span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">destination = destination + source</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>subq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: destination = destination - source</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>imulq<i> source, destination</i></code><span style="font-style:italic;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: </span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">destination = destination * source</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>salq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:italic;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: </span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">destination = destination &lt;&lt; source where &lt;&lt; is the left bit shifting operator</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>sarq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: destination = destination &gt;&gt; source where &gt;&gt; is the right bit shifting operator</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>xorq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: destination = destination XOR source</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>andq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: destination = destination &amp; source</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>orq source, destination</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-style:normal;font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;">: destination = destination | source</span></p></li></ul><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">Before understanding how programs work, it is important to understand registers, memory manipulation and some basic instructions. The next sections will have more hands on use of radare2.</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read and experiment with the above.</p>

```
OK
```

----------------------------------------

### TASK 3. If Statements

<p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;">The general format of an if statement is
</span><br /></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>if(condition)</code><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;">{</span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>  do-stuff-here</code></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>}</code><code>else if(condition) //this is an optional condition<span style="font-size:14.6667px;white-space:pre-wrap;background-color:rgb(255, 255, 255);"> </span></code><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;">{</span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>  do-stuff-here</code><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>}</code><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;">else </span><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;">{</span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>  do-stuff-here</code><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>}</code><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">
If statements use 3 important instructions in assembly:</span></p><ul><li style="list-style-type:disc;font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre;"><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>cmpq source2, source1</code><span style="font-size:11pt;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"><i>: </i></span><span style="font-style:normal;font-size:11pt;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">it is like computing a-b without setting destination</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;background-color:transparent;font-style:italic;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre;"><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><code>testq source2, source1</code><span style="font-size:11pt;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-size:11pt;background-color:transparent;font-style:normal;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">: it is like computing a&amp;b without setting destination</span></p></li></ul><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.38;text-align:justify;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Jump instructions are used to transfer control to different instructions, and there are different types of jumps:

</span></p><div style="margin-left:0pt;"><table><tbody><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Jump Type</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Description</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jmp</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Unconditional</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">je</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Equal/Zero</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jne</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Not Equal/Not Zero</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">js</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Negative</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jns</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Nonnegative</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jg</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Greater</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jge</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Greater or Equal</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jl</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Less</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jle</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Less or Equal</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">ja</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Above(unsigned)</span></p></td></tr><tr><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">jb</span></p></td><td><p style="margin-top:0pt;margin-bottom:0pt;line-height:1.2;"><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">Below(unsigned)</span></p></td></tr><tr><td><br /></td><td><br /></td></tr></tbody></table></div><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify;">The last 2 values of the table refer to unsigned integers. Unsigned integers cannot be negative while signed integers represent both positive and negative values. SInce the computer needs to differentiate between them, it uses different methods to interpret these values. For signed integers, it uses something called the two’s complement representation and for unsigned integers it uses normal binary calculations. </span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Read and experiment with the above.<br /></p>

```
OK
```

----------------------------------------

### TASK 4. If Statements Continued

<p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;">Go to the if-statement folder and Start r2 with </span><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;">r2 -d if1</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">And run the following commands:</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>aaa</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>afl</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>pdf @main</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code><br /></code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">This analyses the program, lists the functions and disassembles the main function.</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh4.googleusercontent.com/SWXZLnHK52fyB4BtLsq4b-YC0uucB8P219xVEc4ilFrGiFf0usbMzzzuzx1m3KEF94__4Ox9sCP256VVHkWUOx3DUhVcS9a03eG3FONST3C2gCD9Kt8pCmmM2r-6rl1TFOeMkLGk" width="624" height="209" style="border:none;" /></span></p><p><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">
 We’ll then start by setting a break point on the </span><code>jge</code><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"> and the </span><code>jmp </code><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">instruction by using the command:</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>db 0x55ae52836612</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">(which is the hex address of the </span><code>jge </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">instruction)</span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> </span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><code>db 0x55ae52836618</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">(which is the hex address of the </span><code>jmp </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">instruction)</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">We’ve added breakpoints to stop the execution of the program at those points so we can see the state of the program. </span><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;">Doing so will show the following:</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh6.googleusercontent.com/9aI231aVGvJr4mWImailUL5Z0zjQ-IuOnHgKxybK2jX-bAXp2uHlqggTTdLtwyANTyq_Q1anXDgnUl1Goxe9WhFGi6n5QcKzef9vAfnRdfycB5Q2icI8ZOGrafnmP2PomCjOsOCk" width="624" height="211" style="border:none;" /></span></p><p><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">
We now run </span><code>dc </code><i><span style="font-size:11pt;font-family:Arial;background-color:transparent;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span></i><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">to start execution of the program and the program will start execution and stop at the break point. Let’s examine what has happened before hitting the breakpoint:</span><br /></p><ul><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The first 2 lines are about pushing the frame pointer onto the stack and saving it(this is about how functions are called, and will be examined later)</span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The next 3 lines are about assigning values 3 and 4 to the local arguments/variables var_8h and var_4h. It then stores the value in var_8h in the %eax register. </span></p></li><li style="list-style-type:disc;font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;"><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The </span><code>cmpl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">instruction compares the value of eax with that of the var_8h argument</span></p></li></ul><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">To view the value of the registers, type in: </span><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;">dr</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh5.googleusercontent.com/dIlnkagpBvm0pX7AFwYDStfJp4UqA48PUmOv2qf_BcZwVu7OsgYoKInNZ16iv_k4xbC3XqUxB8IbVbscKtnQ2TmdhHRIpWuTbvezdjd6ZcHfcSv3H1heeD05-K4Se9e_MCi9Qdw1" width="228" height="319" style="border:none;" /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">We can see that the value of rax, which is the 64 bit version of eax contains 3. We saw that the jge instruction is jumping based on whether value of eax is greater than var_4h. To see what’s in var_4h, we can see that at top of the main function, it tells us the position of var_4h. Run the command: </span><code>px @rbp-0x4</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">And that shows the value of 4. 

</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">We know that eax contains 3, and 3 is not greater than 4, so the jump will not execute. Instead it will move to the next instruction. To check this, run the </span><code>ds</code><span style="font-size:11pt;font-family:Arial;color:rgb(0, 0, 0);background-color:transparent;font-weight:400;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre-wrap;"></span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> command which seeks/moves onto the next instruction.</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh4.googleusercontent.com/jGtJeqPVX_GL4UOwOjx0i7KigX69yt2MsROx5vO0k3l5IuM9-MwU7JyD67lbbkTohGZueOMnGYzpUatkXoMTKTtWMe0f8KhwSj7hXcEDcpWZ7I1Vu6-MbVBDG1msi2kya_95eOdt" width="624" height="213" style="border:none;" /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">
The rip(which is the current instruction pointer) shows that it moves onto the next instruction - which shows we are correct. The current instruction then adds 5 to var_8h which is a local argument. To see that this actually happens, first check the value of var_8h, run </span><code>ds</code><span style="background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"></span><span style="background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;"> and check the value again. This will show it increments by 5.
</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><img src="https://lh5.googleusercontent.com/epOtH0brvnOKjW9GLbv8ZgcSUsREsGrMJrcMh0HJkXlBoR_kLhmJp4CDUBb8U6BWkNneIOEkteXP4wH69OgvI8h2Aq3Cufi_TD3huKkJ3FtYDMI47kWwh89IFhyfutypuvQTnf7R" width="624" height="316" style="border:none;" /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Note that because we are checking the exact address, we only need to check to 0 offset. The value stored in memory is stored as hex. </span></p><p><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">
The next instruction is an unconditional jump and it just jumps to clearing the eax register. The </span><code>popq </code><span style="text-align:justify;background-color:transparent;font-size:11pt;font-family:Arial;font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;white-space:pre-wrap;">instruction involves popping a value of the stack and reading it, and the return instruction sets this popped value to the current instruction pointer. In this case, it shows the execution of the program has been completed. To understand better about how an if statement work, you can check the corresponding C file in the same folder.</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">The following questions involve analysing the if2 binary.</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

```
tryhackme@ip-10-10-96-5:~/if-statement$ r2 -d if2
Process with PID 1407 started...
= attach 1407 1407
bin.baddr 0x55abce204000
Using 0x55abce204000
asm.bits 64
 -- Did you know that r2 is 10 years old?
[0x7f308e338090]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x7f308e338090]> pdf @main
/ (fcn) main 68
|   int main (int argc, char **argv, char **envp);
|           ; var int32_t var_ch @ rbp-0xc
|           ; var int32_t var_8h @ rbp-0x8
|           ; var int32_t var_4h @ rbp-0x4
|           ; DATA XREF from entry0 (0x55abce20450d)
|           0x55abce2045fa      55             pushq %rbp
|           0x55abce2045fb      4889e5         movq %rsp, %rbp
|           0x55abce2045fe      c745f4000000.  movl $0, var_ch
|           0x55abce204605      c745f8630000.  movl $0x63, var_8h      ; 'c' ; 99
|           0x55abce20460c      c745fce80300.  movl $0x3e8, var_4h     ; 1000
|           0x55abce204613      8b45f4         movl var_ch, %eax
|           0x55abce204616      3b45f8         cmpl var_8h, %eax
|       ,=< 0x55abce204619      7d0e           jge 0x55abce204629
|       |   0x55abce20461b      8b45f8         movl var_8h, %eax
|       |   0x55abce20461e      3b45fc         cmpl var_4h, %eax
|      ,==< 0x55abce204621      7d0d           jge 0x55abce204630
|      ||   0x55abce204623      8365f864       andl $0x64, var_8h
|     ,===< 0x55abce204627      eb07           jmp 0x55abce204630
|     ||`-> 0x55abce204629      8145f4b00400.  addl $0x4b0, var_ch
|     ||    ; CODE XREF from main (0x55abce204627)
|     ``--> 0x55abce204630      816dfce70300.  subl $0x3e7, var_4h
|           0x55abce204637      b800000000     movl $0, %eax
|           0x55abce20463c      5d             popq %rbp
\           0x55abce20463d      c3             retq
[0x7f308e338090]> db 0x55abce204637
[0x7f308e338090]> dc
hit breakpoint at: 55abce204637
[0x55abce204637]> px @ rbp-0xc
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffd3f3b2564  0000 0000 6000 0000 0100 0000 4046 20ce  ....`.......@F .
0x7ffd3f3b2574  ab55 0000 977b f68d 307f 0000 0100 0000  .U...{..0.......
0x7ffd3f3b2584  0000 0000 5826 3b3f fd7f 0000 0080 0000  ....X&;?........
0x7ffd3f3b2594  0100 0000 fa45 20ce ab55 0000 0000 0000  .....E ..U......
0x7ffd3f3b25a4  0000 0000 b5f6 ca15 99b4 8643 f044 20ce  ...........C.D .
0x7ffd3f3b25b4  ab55 0000 5026 3b3f fd7f 0000 0000 0000  .U..P&;?........
0x7ffd3f3b25c4  0000 0000 0000 0000 0000 0000 b5f6 4ad2  ..............J.
0x7ffd3f3b25d4  af56 2b17 b5f6 d46f 3533 b016 0000 0000  .V+....o53......
0x7ffd3f3b25e4  fd7f 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd3f3b25f4  0000 0000 3377 348e 307f 0000 38d6 328e  ....3w4.0...8.2.
0x7ffd3f3b2604  307f 0000 4506 0900 0000 0000 0000 0000  0...E...........
0x7ffd3f3b2614  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd3f3b2624  0000 0000 f044 20ce ab55 0000 5026 3b3f  .....D ..U..P&;?
0x7ffd3f3b2634  fd7f 0000 1a45 20ce ab55 0000 4826 3b3f  .....E ..U..H&;?
0x7ffd3f3b2644  fd7f 0000 1c00 0000 0000 0000 0100 0000  ................
0x7ffd3f3b2654  0000 0000 7f47 3b3f fd7f 0000 0000 0000  .....G;?........
[0x55abce204637]> px @ rbp-0x8
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffd3f3b2568  6000 0000 0100 0000 4046 20ce ab55 0000  `.......@F ..U..
0x7ffd3f3b2578  977b f68d 307f 0000 0100 0000 0000 0000  .{..0...........
0x7ffd3f3b2588  5826 3b3f fd7f 0000 0080 0000 0100 0000  X&;?............
0x7ffd3f3b2598  fa45 20ce ab55 0000 0000 0000 0000 0000  .E ..U..........
0x7ffd3f3b25a8  b5f6 ca15 99b4 8643 f044 20ce ab55 0000  .......C.D ..U..
0x7ffd3f3b25b8  5026 3b3f fd7f 0000 0000 0000 0000 0000  P&;?............
0x7ffd3f3b25c8  0000 0000 0000 0000 b5f6 4ad2 af56 2b17  ..........J..V+.
0x7ffd3f3b25d8  b5f6 d46f 3533 b016 0000 0000 fd7f 0000  ...o53..........
0x7ffd3f3b25e8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd3f3b25f8  3377 348e 307f 0000 38d6 328e 307f 0000  3w4.0...8.2.0...
0x7ffd3f3b2608  4506 0900 0000 0000 0000 0000 0000 0000  E...............
0x7ffd3f3b2618  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd3f3b2628  f044 20ce ab55 0000 5026 3b3f fd7f 0000  .D ..U..P&;?....
0x7ffd3f3b2638  1a45 20ce ab55 0000 4826 3b3f fd7f 0000  .E ..U..H&;?....
0x7ffd3f3b2648  1c00 0000 0000 0000 0100 0000 0000 0000  ................
0x7ffd3f3b2658  7f47 3b3f fd7f 0000 0000 0000 0000 0000  .G;?............
[0x55abce204637]> px @ rbp-0x4
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffd3f3b256c  0100 0000 4046 20ce ab55 0000 977b f68d  ....@F ..U...{..
0x7ffd3f3b257c  307f 0000 0100 0000 0000 0000 5826 3b3f  0...........X&;?
0x7ffd3f3b258c  fd7f 0000 0080 0000 0100 0000 fa45 20ce  .............E .
0x7ffd3f3b259c  ab55 0000 0000 0000 0000 0000 b5f6 ca15  .U..............
0x7ffd3f3b25ac  99b4 8643 f044 20ce ab55 0000 5026 3b3f  ...C.D ..U..P&;?
0x7ffd3f3b25bc  fd7f 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd3f3b25cc  0000 0000 b5f6 4ad2 af56 2b17 b5f6 d46f  ......J..V+....o
0x7ffd3f3b25dc  3533 b016 0000 0000 fd7f 0000 0000 0000  53..............
0x7ffd3f3b25ec  0000 0000 0000 0000 0000 0000 3377 348e  ............3w4.
0x7ffd3f3b25fc  307f 0000 38d6 328e 307f 0000 4506 0900  0...8.2.0...E...
0x7ffd3f3b260c  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd3f3b261c  0000 0000 0000 0000 0000 0000 f044 20ce  .............D .
0x7ffd3f3b262c  ab55 0000 5026 3b3f fd7f 0000 1a45 20ce  .U..P&;?.....E .
0x7ffd3f3b263c  ab55 0000 4826 3b3f fd7f 0000 1c00 0000  .U..H&;?........
0x7ffd3f3b264c  0000 0000 0100 0000 0000 0000 7f47 3b3f  .............G;?
0x7ffd3f3b265c  fd7f 0000 0000 0000 0000 0000 8547 3b3f  .............G;?
[0x55abce204637]> 
```

1. <p>What is the value of var_8h before the popq and ret instructions?</p>

```
echo 'ibase=16; 60' | bc
```

```
96
```

2. <p>what is the value of var_ch before the popq and ret instructions?</p>

```
0
```

3. <p>What is the value of var_4h before the popq and ret instructions?</p>

```
1
```

4. <span><span style="font-variant-numeric:normal;font-variant-east-asian:normal;vertical-align:baseline;">What operator is used to change the value of var_8h, input the symbol as your answer(symbols include +, -, *, /, &amp;, |):</span></span>

```
&
```

----------------------------------------

### TASK 5. Loops

<p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap">Usually two types of loops are used: for loops and while loops. The general format of a while loops is:</span><br /></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>while(condition){</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">  </span><code>Do-stuff-here</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">  </span><code>Change value used in condition</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>}</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">
The general format of a for loop is</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>for(initialise value: condition; change value used in condition){</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">  </span><code>do-stuff-here</code></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>}</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">
Let’s start looking up loops by entering the loops folder, running r2 with the loops 1 file. After this, analyse everything, list the functions and disassemble the main function. </span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"><img src="https://lh4.googleusercontent.com/OKIkdD0MD_xvJ8zqJpR8LJBnffeOjeoWXRHFQ1uahwqmrfB-t6tctxc-8Nfm1t4gS_nwR61ekl1x4bVvY4mslLbjfaqbtKfs4onYHxaHr7dt1jAbfj59W7xdVtJOjAMXnqGFo67O" width="624" height="168" style="border:none" /></span></p><p><span style="background-color:transparent;font-family:Arial;font-size:11pt;white-space:pre-wrap;text-align:justify">
Let start of by setting a break point at the jmp instruction using the command: </span><span style="background-color:rgb(248, 249, 250);color:rgb(232, 62, 140);font-family:SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;font-size:14px;text-align:justify">db address-of-instruction</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">Doing this allows us to skip the first few lines of instructions, which as we saw using if statements, it just passing in values to local arguments(note that the constant showed by </span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">$0xa</span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"> represents that value of 10 in hex). Once execution reaches the breakpoint at the jmp instruction, run </span><code>ds</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"> to move to the next instruction. Since this is an unconditional jump, it will move to the cmpl instruction.

</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"><img src="https://lh6.googleusercontent.com/mMG7wWP3vWB59e_2EtZuRgl8b_g4PwYklXzn8SaKCL5zLHUZmbmQhnO6JBUEiZvWG5JBQPR2WQUmkZFA5arFafm88l_c2rhjILTlhf064o7wO9Zmg99eq6iqvoqHYdDMebmZuURM" width="624" height="193" style="border:none" />

</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">Here the </span><code>cmpl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction is trying to compare what’s in the local argument var_ch with the value 8. To see what’s in var_ch, check the start of the disassembled function and check the memory. In this case, it is </span><code>rbp-0xc</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"><img src="https://lh3.googleusercontent.com/KL9Y3euzWtQh-FqiylEiSpoEerjE8zHoetxHMqmbth5-mCw0ETwNubCaibWDXV7WIGo9IecXZPjFQ88xy-JC9dPkCTAFO-yBlRb5OG_Yy6jY87MFM-XqF1WI7PFzXDsXJgXIAaiI" width="624" height="175" style="border:none" />

</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">And shows that it contains 4. The next instruction is a </span><code>jle</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"> which is going to check is the value is var-ch is less than or equal to 8. Since 4 is less than 8, it will jump to the </span><code>addl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction. </span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"><img src="https://lh6.googleusercontent.com/W2rtR7Df_6PWd2FiKcixUJA92dPgYb3ISpwgdfA-ONMhfM_WpgrpRVziXBSjDy2fj3pWmHanGfr_Dhck7bIq9__lfH3IgGRJDl-PpRuCn761XBCWTRpaavCSHsTbthx_VTyx_kaL" width="624" height="216" style="border:none" /></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">
The </span><code>addl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction will add 2 to the value of var-ch and continue to go to the </span><code>cmpl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction. Since 2 was added to var_ch, var_ch will now contain 6 which is still less than 8, and it will jump back to the </span><code>addl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction. This can be seeing by continuing execution using the </span><code>ds </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:italic;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">statement. We know this is a loop because the </span><code>addl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction is being executed more than once, and this is in combination with comparing the value of var_ch to 8. So we can infer the structure of the loop to be</span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>while(var_ch &lt; 8){</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>  var_ch = var_ch + 2</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><code>}</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"></span></p><p></p><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;text-align:justify"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">A quicker way to examine the loop would be to add a break point to </span><code>cmpl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction and running </span><code>dc</code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">. Since this is a loop, the program will always break at the </span><code>cmpl </code><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">instruction(because this instruction checks the condition before executing what is inside the loop). You can check the loop1.c file to see the structure of the loop! </span></p><div><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap"><br /></span></div><div><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap">Use the loop2 binary to answer the following questions.</span></div>

----------------------------------------

### QUESTIONS:

----------------------------------------

```
tryhackme@ip-10-10-96-5:~/loops$ r2 -d loop2
Process with PID 1460 started...
= attach 1460 1460
bin.baddr 0x5626d2439000
Using 0x5626d2439000
asm.bits 64
 -- We are surrounded by the enemy. - Excellent, we can attack in any direction!
[0x7f914e60b090]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x7f914e60b090]> afl
0x5626d24394f0    1 42           entry0
0x5626d2639fe0    1 4124         reloc.__libc_start_main
0x5626d2439520    4 50   -> 40   sym.deregister_tm_clones
0x5626d2439560    4 66   -> 57   sym.register_tm_clones
0x5626d24395b0    5 58   -> 51   entry.fini0
0x5626d24394e0    1 6            sym.imp.__cxa_finalize
0x5626d24395f0    1 10           entry.init0
0x5626d24396b0    1 2            sym.__libc_csu_fini
0x5626d24396b4    1 9            sym._fini
0x5626d2439640    4 101          sym.__libc_csu_init
0x5626d24395fa    4 66           main
0x5626d24394b8    3 23           sym._init
[0x7f914e60b090]> pdf @main
/ (fcn) main 66
|   int main (int argc, char **argv, char **envp);
|           ; var int32_t var_ch @ rbp-0xc
|           ; var int32_t var_8h @ rbp-0x8
|           ; var int32_t var_4h @ rbp-0x4
|           ; DATA XREF from entry0 (0x5626d243950d)
|           0x5626d24395fa      55             pushq %rbp
|           0x5626d24395fb      4889e5         movq %rsp, %rbp
|           0x5626d24395fe      c745f4140000.  movl $0x14, var_ch      ; 20
|           0x5626d2439605      c745f8160000.  movl $0x16, var_8h      ; 22
|           0x5626d243960c      c745fc000000.  movl $0, var_4h
|           0x5626d2439613      c745fc040000.  movl $4, var_4h
|       ,=< 0x5626d243961a      eb13           jmp 0x5626d243962f
|      .--> 0x5626d243961c      8365f402       andl $2, var_ch
|      :|   0x5626d2439620      d17df8         sarl $1, var_8h
|      :|   0x5626d2439623      8b55fc         movl var_4h, %edx
|      :|   0x5626d2439626      89d0           movl %edx, %eax
|      :|   0x5626d2439628      01c0           addl %eax, %eax
|      :|   0x5626d243962a      01d0           addl %edx, %eax
|      :|   0x5626d243962c      8945fc         movl %eax, var_4h
|      :|   ; CODE XREF from main (0x5626d243961a)
|      :`-> 0x5626d243962f      837dfc63       cmpl $0x63, var_4h      ; 'c'
|      `==< 0x5626d2439633      7ee7           jle 0x5626d243961c
|           0x5626d2439635      b800000000     movl $0, %eax
|           0x5626d243963a      5d             popq %rbp
\           0x5626d243963b      c3             retq
[0x7f914e60b090]> db 0x5626d243962f
[0x7f914e60b090]> dc
hit breakpoint at: 5626d243962f
[0x5626d243962f]> db 0x5626d2439635
[0x5626d243962f]> dc
hit breakpoint at: 5626d243962f
[0x5626d243962f]> dc
hit breakpoint at: 5626d243962f
[0x5626d243962f]> px @ rbp-0x8
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffc85435e48  0500 0000 2400 0000 4096 43d2 2656 0000  ....$...@.C.&V..
0x7ffc85435e58  97ab 234e 917f 0000 0100 0000 0000 0000  ..#N............
0x7ffc85435e68  385f 4385 fc7f 0000 0080 0000 0100 0000  8_C.............
0x7ffc85435e78  fa95 43d2 2656 0000 0000 0000 0000 0000  ..C.&V..........
0x7ffc85435e88  b91b 0f1b 6a2c 0f28 f094 43d2 2656 0000  ....j,.(..C.&V..
0x7ffc85435e98  305f 4385 fc7f 0000 0000 0000 0000 0000  0_C.............
0x7ffc85435ea8  0000 0000 0000 0000 b91b 4f8b 6b82 bb7b  ..........O.k..{
0x7ffc85435eb8  b91b 1161 aa14 607b 0000 0000 fc7f 0000  ...a..`{........
0x7ffc85435ec8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435ed8  33a7 614e 917f 0000 3806 604e 917f 0000  3.aN....8.`N....
0x7ffc85435ee8  4699 0800 0000 0000 0000 0000 0000 0000  F...............
0x7ffc85435ef8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435f08  f094 43d2 2656 0000 305f 4385 fc7f 0000  ..C.&V..0_C.....
0x7ffc85435f18  1a95 43d2 2656 0000 285f 4385 fc7f 0000  ..C.&V..(_C.....
0x7ffc85435f28  1c00 0000 0000 0000 0100 0000 0000 0000  ................
0x7ffc85435f38  8277 4385 fc7f 0000 0000 0000 0000 0000  .wC.............
[0x5626d243962f]> px @ rbp-0xc
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffc85435e44  0000 0000 0500 0000 2400 0000 4096 43d2  ........$...@.C.
0x7ffc85435e54  2656 0000 97ab 234e 917f 0000 0100 0000  &V....#N........
0x7ffc85435e64  0000 0000 385f 4385 fc7f 0000 0080 0000  ....8_C.........
0x7ffc85435e74  0100 0000 fa95 43d2 2656 0000 0000 0000  ......C.&V......
0x7ffc85435e84  0000 0000 b91b 0f1b 6a2c 0f28 f094 43d2  ........j,.(..C.
0x7ffc85435e94  2656 0000 305f 4385 fc7f 0000 0000 0000  &V..0_C.........
0x7ffc85435ea4  0000 0000 0000 0000 0000 0000 b91b 4f8b  ..............O.
0x7ffc85435eb4  6b82 bb7b b91b 1161 aa14 607b 0000 0000  k..{...a..`{....
0x7ffc85435ec4  fc7f 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435ed4  0000 0000 33a7 614e 917f 0000 3806 604e  ....3.aN....8.`N
0x7ffc85435ee4  917f 0000 4699 0800 0000 0000 0000 0000  ....F...........
0x7ffc85435ef4  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435f04  0000 0000 f094 43d2 2656 0000 305f 4385  ......C.&V..0_C.
0x7ffc85435f14  fc7f 0000 1a95 43d2 2656 0000 285f 4385  ......C.&V..(_C.
0x7ffc85435f24  fc7f 0000 1c00 0000 0000 0000 0100 0000  ................
0x7ffc85435f34  0000 0000 8277 4385 fc7f 0000 0000 0000  .....wC.........
[0x5626d243962f]> dc
hit breakpoint at: 5626d243962f
[0x5626d243962f]> dc
hit breakpoint at: 5626d2439635
[0x5626d243962f]> px @ rbp-0x8
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffc85435e48  0200 0000 6c00 0000 4096 43d2 2656 0000  ....l...@.C.&V..
0x7ffc85435e58  97ab 234e 917f 0000 0100 0000 0000 0000  ..#N............
0x7ffc85435e68  385f 4385 fc7f 0000 0080 0000 0100 0000  8_C.............
0x7ffc85435e78  fa95 43d2 2656 0000 0000 0000 0000 0000  ..C.&V..........
0x7ffc85435e88  b91b 0f1b 6a2c 0f28 f094 43d2 2656 0000  ....j,.(..C.&V..
0x7ffc85435e98  305f 4385 fc7f 0000 0000 0000 0000 0000  0_C.............
0x7ffc85435ea8  0000 0000 0000 0000 b91b 4f8b 6b82 bb7b  ..........O.k..{
0x7ffc85435eb8  b91b 1161 aa14 607b 0000 0000 fc7f 0000  ...a..`{........
0x7ffc85435ec8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435ed8  33a7 614e 917f 0000 3806 604e 917f 0000  3.aN....8.`N....
0x7ffc85435ee8  4699 0800 0000 0000 0000 0000 0000 0000  F...............
0x7ffc85435ef8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435f08  f094 43d2 2656 0000 305f 4385 fc7f 0000  ..C.&V..0_C.....
0x7ffc85435f18  1a95 43d2 2656 0000 285f 4385 fc7f 0000  ..C.&V..(_C.....
0x7ffc85435f28  1c00 0000 0000 0000 0100 0000 0000 0000  ................
0x7ffc85435f38  8277 4385 fc7f 0000 0000 0000 0000 0000  .wC.............
[0x5626d243962f]> px @ rbp-0xc
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffc85435e44  0000 0000 0200 0000 6c00 0000 4096 43d2  ........l...@.C.
0x7ffc85435e54  2656 0000 97ab 234e 917f 0000 0100 0000  &V....#N........
0x7ffc85435e64  0000 0000 385f 4385 fc7f 0000 0080 0000  ....8_C.........
0x7ffc85435e74  0100 0000 fa95 43d2 2656 0000 0000 0000  ......C.&V......
0x7ffc85435e84  0000 0000 b91b 0f1b 6a2c 0f28 f094 43d2  ........j,.(..C.
0x7ffc85435e94  2656 0000 305f 4385 fc7f 0000 0000 0000  &V..0_C.........
0x7ffc85435ea4  0000 0000 0000 0000 0000 0000 b91b 4f8b  ..............O.
0x7ffc85435eb4  6b82 bb7b b91b 1161 aa14 607b 0000 0000  k..{...a..`{....
0x7ffc85435ec4  fc7f 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435ed4  0000 0000 33a7 614e 917f 0000 3806 604e  ....3.aN....8.`N
0x7ffc85435ee4  917f 0000 4699 0800 0000 0000 0000 0000  ....F...........
0x7ffc85435ef4  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffc85435f04  0000 0000 f094 43d2 2656 0000 305f 4385  ......C.&V..0_C.
0x7ffc85435f14  fc7f 0000 1a95 43d2 2656 0000 285f 4385  ......C.&V..(_C.
0x7ffc85435f24  fc7f 0000 1c00 0000 0000 0000 0100 0000  ................
0x7ffc85435f34  0000 0000 8277 4385 fc7f 0000 0000 0000  .....wC.........
[0x5626d243962f]> 

```

1. <p>What is the value of var_8h on the second iteration of the loop?</p>

```
5
```

2. <p>What is the value of var_ch on the second iteration of the loop?</p>

```
0
```

3. <p>What is the value of var_8h at the end of the program?</p>

```
2
```

4. <p>What is the value of var_ch at the end of the program?</p>

```
0
```

----------------------------------------

### TASK 6. crackme1

<p><span style="font-family:Arial;">Go to the crackme folder and analyse the crackme1 binary. This binary checks if the user has a correct password, and this can be done by running the binary and entering the password.</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

```
tryhackme@ip-10-10-96-5:~/crackme$ r2 -d crackme1
Process with PID 1589 started...
= attach 1589 1589
bin.baddr 0x558dc8a56000
Using 0x558dc8a56000
asm.bits 64
 -- Remember that word: C H A I R
[0x7fca3f669090]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x7fca3f669090]> pdf @main
/ (fcn) main 280
|   int main (int argc, char **argv, char **envp);
|           ; var int32_t var_54h @ rbp-0x54
|           ; var int32_t var_50h @ rbp-0x50
|           ; var int32_t var_4ch @ rbp-0x4c
|           ; var int32_t var_48h @ rbp-0x48
|           ; var int32_t var_40h @ rbp-0x40
|           ; var int32_t var_38h @ rbp-0x38
|           ; var int32_t var_30h @ rbp-0x30
|           ; var int32_t var_28h @ rbp-0x28
|           ; var int32_t var_12h @ rbp-0x12
|           ; var int32_t var_8h @ rbp-0x8
|           ; arg int32_t arg_40h @ rbp+0x40
|           ; DATA XREF from entry0 (0x558dc8a5670d)
|           0x558dc8a567fa      55             pushq %rbp
|           0x558dc8a567fb      4889e5         movq %rsp, %rbp
|           0x558dc8a567fe      4883ec60       subq $0x60, %rsp        ; '`'
|           0x558dc8a56802      64488b042528.  movq %fs:0x28, %rax     ; [0x28:8]=-1 ; '(' ; 40
|           0x558dc8a5680b      488945f8       movq %rax, var_8h
|           0x558dc8a5680f      31c0           xorl %eax, %eax
|           0x558dc8a56811      488d3d900100.  leaq str.enter_your_password, %rdi ; 0x558dc8a569a8 ; "enter your password"
|           0x558dc8a56818      e863feffff     callq sym.imp.puts      ; int puts(const char *s)
|           0x558dc8a5681d      488d45ee       leaq var_12h, %rax
|           0x558dc8a56821      4889c6         movq %rax, %rsi
|           0x558dc8a56824      488d3d910100.  leaq 0x558dc8a569bc, %rdi ; "%s"
|           0x558dc8a5682b      b800000000     movl $0, %eax
|           0x558dc8a56830      e89bfeffff     callq sym.imp.__isoc99_scanf ; int scanf(const char *format)
|           0x558dc8a56835      c745ac000000.  movl $0, var_54h
|           0x558dc8a5683c      488d057c0100.  leaq 0x558dc8a569bf, %rax ; "127"
|           0x558dc8a56843      488945c0       movq %rax, var_40h
|           0x558dc8a56847      488d05750100.  leaq str.01., %rax      ; 0x558dc8a569c3 ; u"01.\u7257\u6e6f\u2067\u6150\u7373\u6f77\u6472\u5900\u756f\u7627\u2065\u6f67\u2074\u6874\u2065\u6f63\u7272\u6365\u2074\u6170\u7373\u6f77\u6472\u0100\u031b\u3c3b"
|           0x558dc8a5684e      488945c8       movq %rax, var_38h
|           0x558dc8a56852      488d056a0100.  leaq str.01., %rax      ; 0x558dc8a569c3 ; u"01.\u7257\u6e6f\u2067\u6150\u7373\u6f77\u6472\u5900\u756f\u7627\u2065\u6f67\u2074\u6874\u2065\u6f63\u7272\u6365\u2074\u6170\u7373\u6f77\u6472\u0100\u031b\u3c3b"
|           0x558dc8a56859      488945d0       movq %rax, var_30h
|           0x558dc8a5685d      488d05610100.  leaq 0x558dc8a569c5, %rax ; u"1.\u7257\u6e6f\u2067\u6150\u7373\u6f77\u6472\u5900\u756f\u7627\u2065\u6f67\u2074\u6874\u2065\u6f63\u7272\u6365\u2074\u6170\u7373\u6f77\u6472\u0100\u031b\u3c3b"
|           0x558dc8a56864      488945d8       movq %rax, var_28h
|           0x558dc8a56868      488d45ee       leaq var_12h, %rax
|           0x558dc8a5686c      4889c7         movq %rax, %rdi
|           0x558dc8a5686f      e81cfeffff     callq sym.imp.strlen    ; size_t strlen(const char *s)
|           0x558dc8a56874      8945b0         movl %eax, var_50h
|           0x558dc8a56877      488d45ee       leaq var_12h, %rax
|           0x558dc8a5687b      488d35450100.  leaq 0x558dc8a569c7, %rsi ; "."
|           0x558dc8a56882      4889c7         movq %rax, %rdi
|           0x558dc8a56885      e836feffff     callq sym.imp.strtok    ; char *strtok(char *s1, const char *s2)
|           0x558dc8a5688a      488945b8       movq %rax, var_48h
|       ,=< 0x558dc8a5688e      eb4e           jmp 0x558dc8a568de
|      .--> 0x558dc8a56890      8b45ac         movl var_54h, %eax
|      :|   0x558dc8a56893      4898           cltq
|      :|   0x558dc8a56895      488b54c5c0     movq -0x40(%rbp, %rax, 8), %rdx
|      :|   0x558dc8a5689a      488b45b8       movq var_48h, %rax
|      :|   0x558dc8a5689e      4889d6         movq %rdx, %rsi
|      :|   0x558dc8a568a1      4889c7         movq %rax, %rdi
|      :|   0x558dc8a568a4      e807feffff     callq sym.imp.strcmp    ; int strcmp(const char *s1, const char *s2)
|      :|   0x558dc8a568a9      8945b4         movl %eax, var_4ch
|      :|   0x558dc8a568ac      8345ac01       addl $1, var_54h
|      :|   0x558dc8a568b0      837db400       cmpl $0, var_4ch
|     ,===< 0x558dc8a568b4      7413           je 0x558dc8a568c9
|     |:|   0x558dc8a568b6      488d3d0c0100.  leaq 0x558dc8a569c9, %rdi ; "Wrong Password"
|     |:|   0x558dc8a568bd      e8befdffff     callq sym.imp.puts      ; int puts(const char *s)
|     |:|   0x558dc8a568c2      b8ffffffff     movl $0xffffffff, %eax  ; -1
|    ,====< 0x558dc8a568c7      eb33           jmp 0x558dc8a568fc
|    |`---> 0x558dc8a568c9      488d35f70000.  leaq 0x558dc8a569c7, %rsi ; "."
|    | :|   0x558dc8a568d0      bf00000000     movl $0, %edi
|    | :|   0x558dc8a568d5      e8e6fdffff     callq sym.imp.strtok    ; char *strtok(char *s1, const char *s2)
|    | :|   0x558dc8a568da      488945b8       movq %rax, var_48h
|    | :|   ; CODE XREF from main (0x558dc8a5688e)
|    | :`-> 0x558dc8a568de      48837db800     cmpq $0, var_48h
|    | :,=< 0x558dc8a568e3      7406           je 0x558dc8a568eb
|    | :|   0x558dc8a568e5      837dac03       cmpl $3, var_54h
|    | `==< 0x558dc8a568e9      7ea5           jle 0x558dc8a56890
|    |  `-> 0x558dc8a568eb      488d3de60000.  leaq str.You_ve_got_the_correct_password, %rdi ; 0x558dc8a569d8 ; "You've got the correct password"
|    |      0x558dc8a568f2      e889fdffff     callq sym.imp.puts      ; int puts(const char *s)
|    |      0x558dc8a568f7      b800000000     movl $0, %eax
|    |      ; CODE XREF from main (0x558dc8a568c7)
|    `----> 0x558dc8a568fc      488b4df8       movq var_8h, %rcx
|           0x558dc8a56900      6448330c2528.  xorq %fs:0x28, %rcx
|       ,=< 0x558dc8a56909      7405           je 0x558dc8a56910
|       |   0x558dc8a5690b      e890fdffff     callq sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       `-> 0x558dc8a56910      c9             leave
\           0x558dc8a56911      c3             retq
[0x7fca3f669090]> db 0x558dc8a568a4
[0x7fca3f669090]> dc
enter your password
a
hit breakpoint at: 558dc8a568a4
[0x558dc8a568a4]> dr
rax = 0x7ffecc23c1be
rbx = 0x00000000
rcx = 0x00000001
rdx = 0x558dc8a569bf
r8 = 0x0000000e
r9 = 0x00000000
r10 = 0x00000000
r11 = 0x558dc8a569be
r12 = 0x558dc8a566f0
r13 = 0x7ffecc23c2b0
r14 = 0x00000000
r15 = 0x00000000
rsi = 0x558dc8a569bf
rdi = 0x7ffecc23c1be
rsp = 0x7ffecc23c170
rbp = 0x7ffecc23c1d0
rip = 0x558dc8a568a4
rflags = 0x00000293
orax = 0xffffffffffffffff
[0x558dc8a568a4]> px @ rbp+0x40
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffecc23c210  f066 a5c8 8d55 0000 b0c2 23cc fe7f 0000  .f...U....#.....
0x7ffecc23c220  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffecc23c230  9a18 a0b0 abb8 e421 9a18 fe25 bf5e 8d21  .......!...%.^.!
0x7ffecc23c240  0000 0000 fe7f 0000 0000 0000 0000 0000  ................
0x7ffecc23c250  0000 0000 0000 0000 3387 673f ca7f 0000  ........3.g?....
0x7ffecc23c260  38e6 653f ca7f 0000 7716 0900 0000 0000  8.e?....w.......
0x7ffecc23c270  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffecc23c280  0000 0000 0000 0000 f066 a5c8 8d55 0000  .........f...U..
0x7ffecc23c290  b0c2 23cc fe7f 0000 1a67 a5c8 8d55 0000  ..#......g...U..
0x7ffecc23c2a0  a8c2 23cc fe7f 0000 1c00 0000 0000 0000  ..#.............
0x7ffecc23c2b0  0100 0000 0000 0000 74d7 23cc fe7f 0000  ........t.#.....
0x7ffecc23c2c0  0000 0000 0000 0000 7fd7 23cc fe7f 0000  ..........#.....
0x7ffecc23c2d0  6bdd 23cc fe7f 0000 99dd 23cc fe7f 0000  k.#.......#.....
0x7ffecc23c2e0  bbdd 23cc fe7f 0000 c8dd 23cc fe7f 0000  ..#.......#.....
0x7ffecc23c2f0  d9dd 23cc fe7f 0000 e8dd 23cc fe7f 0000  ..#.......#.....
0x7ffecc23c300  04de 23cc fe7f 0000 19de 23cc fe7f 0000  ..#.......#.....
[0x558dc8a568a4]> pxw @ rbp+0x40
0x7ffecc23c210  0xc8a566f0 0x0000558d 0xcc23c2b0 0x00007ffe  .f...U....#.....
0x7ffecc23c220  0x00000000 0x00000000 0x00000000 0x00000000  ................
0x7ffecc23c230  0xb0a0189a 0x21e4b8ab 0x25fe189a 0x218d5ebf  .......!...%.^.!
0x7ffecc23c240  0x00000000 0x00007ffe 0x00000000 0x00000000  ................
0x7ffecc23c250  0x00000000 0x00000000 0x3f678733 0x00007fca  ........3.g?....
0x7ffecc23c260  0x3f65e638 0x00007fca 0x00091677 0x00000000  8.e?....w.......
0x7ffecc23c270  0x00000000 0x00000000 0x00000000 0x00000000  ................
0x7ffecc23c280  0x00000000 0x00000000 0xc8a566f0 0x0000558d  .........f...U..
0x7ffecc23c290  0xcc23c2b0 0x00007ffe 0xc8a5671a 0x0000558d  ..#......g...U..
0x7ffecc23c2a0  0xcc23c2a8 0x00007ffe 0x0000001c 0x00000000  ..#.............
0x7ffecc23c2b0  0x00000001 0x00000000 0xcc23d774 0x00007ffe  ........t.#.....
0x7ffecc23c2c0  0x00000000 0x00000000 0xcc23d77f 0x00007ffe  ..........#.....
0x7ffecc23c2d0  0xcc23dd6b 0x00007ffe 0xcc23dd99 0x00007ffe  k.#.......#.....
0x7ffecc23c2e0  0xcc23ddbb 0x00007ffe 0xcc23ddc8 0x00007ffe  ..#.......#.....
0x7ffecc23c2f0  0xcc23ddd9 0x00007ffe 0xcc23dde8 0x00007ffe  ..#.......#.....
0x7ffecc23c300  0xcc23de04 0x00007ffe 0xcc23de19 0x00007ffe  ..#.......#.....
[0x558dc8a568a4]> pxw 0x7ffecc23c1be
This block size is too big (0x3200000 < 0x33dc3e42). Did you mean 'px @  0x7ffecc23c1be' instead?
[0x558dc8a568a4]> pxw @ 0x7ffecc23c1be
0x7ffecc23c1be  0xc2b00061 0x7ffecc23 0x65000000 0x3a24da63  a...#......ec.$:
0x7ffecc23c1ce  0x69202108 0x558dc8a5 0x8b970000 0x7fca3f29  .! i...U....)?..
0x7ffecc23c1de  0x00010000 0x00000000 0xc2b80000 0x7ffecc23  ............#...
0x7ffecc23c1ee  0x80000000 0x00010000 0x67fa0000 0x558dc8a5  ...........g...U
0x7ffecc23c1fe  0x00000000 0x00000000 0x189a0000 0xb1a6e120  ............ ...
0x7ffecc23c20e  0x66f07502 0x558dc8a5 0xc2b00000 0x7ffecc23  .u.f...U....#...
0x7ffecc23c21e  0x00000000 0x00000000 0x00000000 0x00000000  ................
0x7ffecc23c22e  0x189a0000 0xb8abb0a0 0x189a21e4 0x5ebf25fe  .........!...%.^
0x7ffecc23c23e  0x0000218d 0x7ffe0000 0x00000000 0x00000000  .!..............
0x7ffecc23c24e  0x00000000 0x00000000 0x87330000 0x7fca3f67  ..........3.g?..
0x7ffecc23c25e  0xe6380000 0x7fca3f65 0x16770000 0x00000009  ..8.e?....w.....
0x7ffecc23c26e  0x00000000 0x00000000 0x00000000 0x00000000  ................
0x7ffecc23c27e  0x00000000 0x00000000 0x66f00000 0x558dc8a5  ...........f...U
0x7ffecc23c28e  0xc2b00000 0x7ffecc23 0x671a0000 0x558dc8a5  ....#......g...U
0x7ffecc23c29e  0xc2a80000 0x7ffecc23 0x001c0000 0x00000000  ....#...........
0x7ffecc23c2ae  0x00010000 0x00000000 0xd7740000 0x7ffecc23  ..........t.#...
[0x558dc8a568a4]> pxw @ 0x558dc8a569bf
0x558dc8a569bf  0x00373231 0x00310030 0x7257002e 0x20676e6f  127.0.1...Wrong 
0x558dc8a569cf  0x73736150 0x64726f77 0x756f5900 0x20657627  Password.You've 
0x558dc8a569df  0x20746f67 0x20656874 0x72726f63 0x20746365  got the correct 
0x558dc8a569ef  0x73736170 0x64726f77 0x031b0100 0x00003c3b  password....;<..
0x558dc8a569ff  0x00000600 0xfffc7800 0x000088ff 0xfffce800  .....x..........
0x558dc8a56a0f  0x0000b0ff 0xfffcf800 0x000058ff 0xfffe0200  .........X......
0x558dc8a56a1f  0x0000c8ff 0xffff2800 0x0000e8ff 0xffff9800  .....(..........
0x558dc8a56a2f  0x000130ff 0x00000000 0x00001400 0x00000000  .0..............
0x558dc8a56a3f  0x527a0100 0x10780100 0x070c1b01 0x07019008  ..zR..x.........
0x558dc8a56a4f  0x00001410 0x00001c00 0xfffc9800 0x00002bff  .............+..
0x558dc8a56a5f  0x00000000 0x00000000 0x00001400 0x00000000  ................
0x558dc8a56a6f  0x527a0100 0x10780100 0x070c1b01 0x00019008  ..zR..x.........
0x558dc8a56a7f  0x00002400 0x00001c00 0xfffbe800 0x000070ff  .$...........p..
0x558dc8a56a8f  0x100e0000 0x4a180e46 0x08770b0f 0x1a3f0080  ....F..J..w...?.
0x558dc8a56a9f  0x24332a3b 0x00000022 0x00001400 0x00004400  ;*3$"........D..
0x558dc8a56aaf  0xfffc3000 0x000008ff 0x00000000 0x00000000  .0..............
[0x558dc8a568a4]> 
```

1. <p>What is the password?</p>

```
127.0.0.1
```

> I'm not entirely sure why...

----------------------------------------

### TASK 7. crackme2

<p><span style="font-family:Arial;">Analyse the crackme2 binary and try find the correct password, as with the previous question.</span></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

```
tryhackme@ip-10-10-96-5:~/crackme$ r2 -d crackme2
Process with PID 1593 started...
= attach 1593 1593
bin.baddr 0x563ca5fc4000
Using 0x563ca5fc4000
asm.bits 64
 -- Step through your seek history with the commands 'u' (undo) and 'U' (redo)
[0x7fcf13658090]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
Warning: Invalid range. Use different search.in=? or anal.in=dbg.maps.x
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x7fcf13658090]> afl
0x563ca5fc46f0    1 42           entry0
0x563ca61c4fe0    1 4124         reloc.__libc_start_main
0x563ca5fc4720    4 50   -> 40   sym.deregister_tm_clones
0x563ca5fc4760    4 66   -> 57   sym.register_tm_clones
0x563ca5fc47b0    5 58   -> 51   entry.fini0
0x563ca5fc46e0    1 6            sym..plt.got
0x563ca5fc47f0    1 10           entry.init0
0x563ca5fc4990    1 2            sym.__libc_csu_fini
0x563ca5fc4994    1 9            sym._fini
0x563ca5fc4920    4 101          sym.__libc_csu_init
0x563ca5fc47fa   12 283          main
0x563ca5fc4650    3 23           sym._init
0x563ca5fc4680    1 6            sym.imp.puts
0x563ca5fc4690    1 6            sym.imp.fread
0x563ca5fc46a0    1 6            sym.imp.strlen
0x563ca5fc46b0    1 6            sym.imp.__stack_chk_fail
0x563ca5fc4000    2 25           map.home_tryhackme_crackme_crackme2.r_x
0x563ca5fc46c0    1 6            sym.imp.fopen
0x563ca5fc46d0    1 6            sym.imp.__isoc99_scanf
[0x7fcf13658090]> pdf @main
/ (fcn) main 283
|   int main (int argc, char **argv, char **envp);
|           ; var int32_t var_44h @ rbp-0x44
|           ; var int32_t var_40h @ rbp-0x40
|           ; var int32_t var_3ch @ rbp-0x3c
|           ; var int32_t var_38h @ rbp-0x38
|           ; var int32_t var_2eh @ rbp-0x2e
|           ; var int32_t var_23h @ rbp-0x23
|           ; var int32_t var_18h @ rbp-0x18
|           ; DATA XREF from entry0 (0x563ca5fc470d)
|           0x563ca5fc47fa      55             pushq %rbp
|           0x563ca5fc47fb      4889e5         movq %rsp, %rbp
|           0x563ca5fc47fe      53             pushq %rbx
|           0x563ca5fc47ff      4883ec48       subq $0x48, %rsp        ; 'H'
|           0x563ca5fc4803      64488b042528.  movq %fs:0x28, %rax     ; [0x28:8]=-1 ; '(' ; 40
|           0x563ca5fc480c      488945e8       movq %rax, var_18h
|           0x563ca5fc4810      31c0           xorl %eax, %eax
|           0x563ca5fc4812      488d358f0100.  leaq 0x563ca5fc49a8, %rsi ; "r"
|           0x563ca5fc4819      488d3d900100.  leaq str.home_tryhackme_install_files_secret.txt, %rdi ; 0x563ca5fc49b0 ; "/home/tryhackme/install-files/secret.txt"
|           0x563ca5fc4820      e89bfeffff     callq sym.imp.fopen     ; file*fopen(const char *filename, const char *mode)
|           0x563ca5fc4825      488945c8       movq %rax, var_38h
|           0x563ca5fc4829      488b55c8       movq var_38h, %rdx
|           0x563ca5fc482d      488d45d2       leaq var_2eh, %rax
|           0x563ca5fc4831      4889d1         movq %rdx, %rcx
|           0x563ca5fc4834      ba0b000000     movl $0xb, %edx         ; 11
|           0x563ca5fc4839      be01000000     movl $1, %esi
|           0x563ca5fc483e      4889c7         movq %rax, %rdi
|           0x563ca5fc4841      e84afeffff     callq sym.imp.fread     ; size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)
|           0x563ca5fc4846      8945c4         movl %eax, var_3ch
|           0x563ca5fc4849      837dc400       cmpl $0, var_3ch
|       ,=< 0x563ca5fc484d      7916           jns 0x563ca5fc4865
|       |   0x563ca5fc484f      488d3d830100.  leaq str.Error_Reading_File, %rdi ; 0x563ca5fc49d9 ; "Error Reading File"
|       |   0x563ca5fc4856      e825feffff     callq sym.imp.puts      ; int puts(const char *s)
|       |   0x563ca5fc485b      b8ffffffff     movl $0xffffffff, %eax  ; -1
|      ,==< 0x563ca5fc4860      e995000000     jmp 0x563ca5fc48fa
|      |`-> 0x563ca5fc4865      488d3d800100.  leaq str.Please_enter_password, %rdi ; 0x563ca5fc49ec ; "Please enter password"
|      |    0x563ca5fc486c      e80ffeffff     callq sym.imp.puts      ; int puts(const char *s)
|      |    0x563ca5fc4871      488d45dd       leaq var_23h, %rax
|      |    0x563ca5fc4875      4889c6         movq %rax, %rsi
|      |    0x563ca5fc4878      488d3d830100.  leaq str.11s, %rdi      ; 0x563ca5fc4a02 ; "%11s"
|      |    0x563ca5fc487f      b800000000     movl $0, %eax
|      |    0x563ca5fc4884      e847feffff     callq sym.imp.__isoc99_scanf ; int scanf(const char *format)
|      |    0x563ca5fc4889      c745bc090000.  movl $9, var_44h
|      |    0x563ca5fc4890      c745c0000000.  movl $0, var_40h
|      |,=< 0x563ca5fc4897      eb33           jmp 0x563ca5fc48cc
|     .---> 0x563ca5fc4899      8b45bc         movl var_44h, %eax
|     :||   0x563ca5fc489c      4898           cltq
|     :||   0x563ca5fc489e      0fb65405d2     movzbl -0x2e(%rbp, %rax), %edx
|     :||   0x563ca5fc48a3      8b45c0         movl var_40h, %eax
|     :||   0x563ca5fc48a6      4898           cltq
|     :||   0x563ca5fc48a8      0fb64405dd     movzbl -0x23(%rbp, %rax), %eax
|     :||   0x563ca5fc48ad      38c2           cmpb %al, %dl
|    ,====< 0x563ca5fc48af      7413           je 0x563ca5fc48c4
|    |:||   0x563ca5fc48b1      488d3d4f0100.  leaq str.Wrong_Password, %rdi ; 0x563ca5fc4a07 ; "Wrong Password"
|    |:||   0x563ca5fc48b8      e8c3fdffff     callq sym.imp.puts      ; int puts(const char *s)
|    |:||   0x563ca5fc48bd      b8ffffffff     movl $0xffffffff, %eax  ; -1
|   ,=====< 0x563ca5fc48c2      eb36           jmp 0x563ca5fc48fa
|   |`----> 0x563ca5fc48c4      836dbc01       subl $1, var_44h
|   | :||   0x563ca5fc48c8      8345c001       addl $1, var_40h
|   | :||   ; CODE XREF from main (0x563ca5fc4897)
|   | :|`-> 0x563ca5fc48cc      837dbc00       cmpl $0, var_44h
|   | :|,=< 0x563ca5fc48d0      7e17           jle 0x563ca5fc48e9
|   | :||   0x563ca5fc48d2      8b45c0         movl var_40h, %eax
|   | :||   0x563ca5fc48d5      4863d8         movslq %eax, %rbx
|   | :||   0x563ca5fc48d8      488d45dd       leaq var_23h, %rax
|   | :||   0x563ca5fc48dc      4889c7         movq %rax, %rdi
|   | :||   0x563ca5fc48df      e8bcfdffff     callq sym.imp.strlen    ; size_t strlen(const char *s)
|   | :||   0x563ca5fc48e4      4839c3         cmpq %rax, %rbx
|   | `===< 0x563ca5fc48e7      72b0           jb 0x563ca5fc4899
|   |  |`-> 0x563ca5fc48e9      488d3d260100.  leaq str.Correct_Password, %rdi ; 0x563ca5fc4a16 ; "Correct Password"
|   |  |    0x563ca5fc48f0      e88bfdffff     callq sym.imp.puts      ; int puts(const char *s)
|   |  |    0x563ca5fc48f5      b800000000     movl $0, %eax
|   |  |    ; CODE XREFS from main (0x563ca5fc4860, 0x563ca5fc48c2)
|   `--`--> 0x563ca5fc48fa      488b4de8       movq var_18h, %rcx
|           0x563ca5fc48fe      6448330c2528.  xorq %fs:0x28, %rcx
|       ,=< 0x563ca5fc4907      7405           je 0x563ca5fc490e
|       |   0x563ca5fc4909      e8a2fdffff     callq sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       `-> 0x563ca5fc490e      4883c448       addq $0x48, %rsp        ; 'H'
|           0x563ca5fc4912      5b             popq %rbx
|           0x563ca5fc4913      5d             popq %rbp
\           0x563ca5fc4914      c3             retq
[0x7fcf13658090]> 
```

```
tryhackme@ip-10-10-96-5:~/crackme$ cat /home/tryhackme/install-files/secret.txt | rev
dwperuc3sv
```

1. <p>What is the correct password?</p>

```
dwperuc3sv
```


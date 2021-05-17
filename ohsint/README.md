# TryHackMe challenge

## OhSINT

> _tihawk | May 17, 2021_

----------------------------------------

### TASK 1. OhSINT

<p style="text-align:center"><span style="font-size:18px">What information can you possible get with just one photo?</span><br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What is this users avatar of?<br /></p>

```
[tihawk@archpenner ohsint]$ /opt/Image-ExifTool-12.25/exiftool task.jpg 
ExifTool Version Number         : 12.25
File Name                       : task.jpg
Directory                       : .
File Size                       : 229 KiB
File Modification Date/Time     : 2021:05:17 22:18:43+03:00
File Access Date/Time           : 2021:05:17 22:20:09+03:00
File Inode Change Date/Time     : 2021:05:17 22:19:05+03:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
XMP Toolkit                     : Image::ExifTool 11.27
GPS Latitude                    : 54 deg 17' 41.27" N
GPS Longitude                   : 2 deg 15' 1.33" W
Copyright                       : OWoodflint
Image Width                     : 1920
Image Height                    : 1080
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1920x1080
Megapixels                      : 2.1
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Position                    : 54 deg 17' 41.27" N, 2 deg 15' 1.33" W
```

[https://twitter.com/owoodflint?lang=en](https://twitter.com/owoodflint?lang=en)

```
cat
```

2. <p>What city is this person in?<br /></p>

[https://github.com/OWoodfl1nt/people_finder](https://github.com/OWoodfl1nt/people_finder)

```
London
```

3. <p>Whats the SSID of the WAP he connected to?<br /></p>

[https://twitter.com/owoodflint?lang=en](https://twitter.com/owoodflint?lang=en)
[wigle](https://wigle.net/mapsearch?maplat=51.508310690434215&maplon=-0.1321514545054625&mapzoom=22)

```
UnileverWiFi
```

4. <p>What is his personal email address?<br /></p>

[https://github.com/OWoodfl1nt/people_finder](https://github.com/OWoodfl1nt/people_finder)

```
OWoodflint@gmail.com
```

5. <p>What site did you find his email address on?</p>

```
GitHub
```

6. <p>Where has he gone on holiday?<br /></p>

[https://oliverwoodflint.wordpress.com/author/owoodflint/](https://oliverwoodflint.wordpress.com/author/owoodflint/)

```
New York
```

7. <p>What is this persons password?<br /></p>

[view-source:https://oliverwoodflint.wordpress.com/](view-source:https://oliverwoodflint.wordpress.com/)

It's in white. Great.

```
pennYDr0pper.!
```


#!/usr/bin/python
import sys
import os
header = """
############################################
[==========      D3n0l Ganz      ==========]
############################################
"""
print header
print
asu = raw_input("Nama File : ")
folder = raw_input("Folder : ")
title = raw_input("Judul : ")
lfont = raw_input("Link Font : ")
nfont = raw_input("Nama Font : ")
ufont = raw_input("Ukuran Font : ")
wfont = raw_input("Warna Font : ")
nick = raw_input("Nickname : ")
team = raw_input("Team : ")
image = raw_input("Link Gambar [Tengah] : ")
bgimage = raw_input("Link Gambar [Background] : ")
lcss  = raw_input("Link Css : ")
ncss = raw_input("Nama Css : ")
text = raw_input("Pesan (Contoh = Pm gan<br>Up gan : ")
musik = raw_input("Link Musik : ")

os.system("cd "folder"")
fo = open(asu,"w")
sc1 = '''<html>
<head>
<title>
'''
sc2 = title
sc3 = '''</title>
</head>
<body bgcolor="black">
<link href="https://fonts.googleapis.com/css?family=VT323|New+Rocker" rel="stylesheet" type="text/css">
<link href="'''
sc4 = lfont
sc5 = '''" rel="stylesheet' type="text/css">
'''
sc6 = '''
<style>
body {
    background-image:url("'''
sc7 = bgimage
sc8 = '''");
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
</style>
'''
sc9 = '''
<br><audio autoplay loop>
<source src="'''
sc10 = musik
sc11 = '''" type="audio/mp3"></audio>
'''
sc12 = '''<font face="'''
sc13 = nfont
sc14 = '''" size="'''
sc15 = ufont
sc16 = '''" color="'''
sc17 = wfont
sc18 = '''">
<center>
<marquee behavior="alternate"
width="10%">>>></marquee>
'''
sc19 = team
sc20 = '''
<marquee behavior="alternate"
width="10%"><<<</marquee>
<br><center>
'''
sc21 = '''<link type="text/css" href="'''
sc22 = lcss
sc23 = '''" rel="stylesheet">
<div class="'''
sc24 = ncss
sc25 = '''">'''
sc26 = '''
<img src="'''
sc27 = image
sc28 = '''" />
</div>
<center>
<font face="New Rocker" size="10" font style="color:black;text-align: center;text-shadow: 0 0 3px #F60000, 0px 0px 5px #FF0000,0 0 5px #FF0D0D,0 0 5px #FF0000;">

'''
sc29 = nick
sc30 = '''<br><br><br>
<font face="'''
sc31 = nfont
sc32 = ''' size="'''
sc33 = ufont
sc34 = '''" color="'''
sc35 = wfont
sc36 = '''">
'''
sc37 = text
sc38 = '''
</center>
</font><br>
<center>
'''
sc39 = '''
<script language="JavaScript">
document.onkeypress = function (event) {
event = (event || window.event);
if (event.keyCode == 123) {
//alert('No F-12');
return false;
}
}
document.onmousedown = function (event) {
event = (event || window.event);
if (event.keyCode == 123) {
//alert('No F-keys');
return false;
}
}
document.onkeydown = function (event) {
event = (event || window.event);
if (event.keyCode == 123) {
//alert('No F-keys');
return false;
}
}
</script>
<script type="text/javascript">
window.oncontextmenu = function () {
return false;
}
$(document).keydown(function (event) {
if (event.keyCode == 123) {
return false;
}
else if ((event.ctrlKey && event.shiftKey && event.keyCode == 73) || (event.ctrlKey && event.shiftKey && event.keyCode == 74)) {
return false;
}
});
</script><br>
<font size="6" face="Jolly Lodger" color="yellow">
<span id="sec">
<div id="foter" class="foter"
style="position: fixed; top: 75px; left: -235px; width: 600px; padding: 10px; font-size: 16px; text-align: center; color: rgb(255, 255, 255); font-family: Jolly Lodger;transform: rotate(-45deg);transform-origin: 50% 0px;-o-transform: rotate(-45deg); -o-transform-origin: 50% 0px;-moz-transform: rotate(-45deg); -moz-transform-origin: 50% 0px; -webkit-transform: rotate(-45deg); -webkit-transform-origin: 50% 0px; background-color: rgb(0, 0, 0); border: 1px solid rgb(170, 170, 170); z-index: 9999; opacity: 0.5;">
<b><font face="Jolly Lodger" size="6">
<marquee width="50%" behavior="alternate" scrollamount="3">
=======>'''
sc40 = nick
sc41 = '''<=======
</marquee></font></center>
</body>
</head>
</html>'''


fo.write(sc1)
fo.write(sc2)
fo.write(sc3)
fo.write(sc4)
fo.write(sc5)
fo.write(sc6)
fo.write(sc7)
fo.write(sc8)
fo.write(sc9)
fo.write(sc10)
fo.write(sc11)
fo.write(sc12)
fo.write(sc13)
fo.write(sc14)
fo.write(sc15)
fo.write(sc16)
fo.write(sc17)
fo.write(sc18)
fo.write(sc19)
fo.write(sc20)
fo.write(sc21)
fo.write(sc22)
fo.write(sc23)
fo.write(sc24)
fo.write(sc25)
fo.write(sc26)
fo.write(sc27)
fo.write(sc28)
fo.write(sc29)
fo.write(sc30)
fo.write(sc31)
fo.write(sc32)
fo.write(sc33)
fo.write(sc34)
fo.write(sc35)
fo.write(sc36)
fo.write(sc37)
fo.write(sc38)
fo.write(sc39)
fo.write(sc40)
fo.write(sc41)

print ""
print "Script Berhasil Di buat!"
print ""
os.system("pkg install apt && apt install curl && curl -T")

fo.close()

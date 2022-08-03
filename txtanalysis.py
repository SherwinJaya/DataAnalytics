import matplotlib.pyplot as plt
import re

austen = [ "A-emma.txt", "A-mansfield.txt", "A-northanger.txt",
"A-persuasion.txt", "A-pride.txt", "A-sense.txt"]
austenlabel = ["EM", "MP", "NA", "PE", "PP", "SS"]
collins = [ "C-afterdark.txt", "C-armadale.txt",
"C-evilgenius.txt", "C-moonstone.txt", "C-noname.txt", "C-womanwhite.txt"]
collinslabel = ["ED", "FH", "PF", "PM", "DC"]

def wordsup (file) :
	f = open (file)
	use = set()
	all = f.read()
	all = re.sub(",", ",,", all)
	for wd in re.findall(r"[.,;] (\w+),", all):
		use.add(wd.lower())
	f.close()
	return use

love=wordsup ("roget-love")
fear = wordsup("roget-fear")

def countw (book):
	ab = open(book).read().lower()
	wds = re.findall(r"\w{4,}", ab)
	lb = len(wds)
	nm = nr = 0
	for w in wds:
		if w in love:
			nm+=1
		if w in fear:
			nr+=1
	return  nm*1000.0/lb, nr*1000.0/lb

xg = []
yg = []
for book in austen:
	xm, ym = countw(book)
	xg.append(xm)
	yg.append(ym)

xt = []
yt = list()
for book in collins:
	xm, ym = countw(book)
	xt.append(xm)
	yt.append(ym)

plt.plot(xg,yg,"r,")
for pt in zip(xg,yg,austenlabel):
	plt.text(pt[0], pt[1], pt[2], color="red")
plt.plot(xt, yt, "b,")
for pt in zip(xt,yt,collinslabel):
	plt.text(pt[0], pt[1], pt[2], color="blue")
plt.xlabel ("Love")
plt.ylabel ("Fear")

plt.title ("Austen: Red, Collins: Blue")
plt.show()
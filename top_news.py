from Adafruit_Thermal import *
import feedparser,textwrap,sys,unicodedata
d=feedparser.parse('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.boldOn()
printer.setSize('L')
printer.println('TOP STORIES')
printer.boldOff()
printer.setSize('S')
for post in d.entries:
	unwrapped_text = unicodedata.normalize('NFKD',post.title).encode('ascii','ignore') + '.'
	wrapped_text = textwrap.fill('* '+unwrapped_text, 32)
	printer.println(wrapped_text)
	print (post.title+"\n")

printer.feed()
printer.feed()


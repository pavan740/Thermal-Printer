from Adafruit_Thermal import *
import sqlite3,textwrap,sys,time
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
ticks=time.asctime( time.localtime(time.time()) )
printer.println(ticks)
thermalp = 'test.db'
conn = sqlite3.connect(thermalp)
c = conn.cursor()
c.execute('select * from printer;')
for row in c.fetchall():
    unwrapped_text = row[0]
    wrapped_text = textwrap.fill(unwrapped_text, 32)
    printer.println(wrapped_text)
conn.close()


# coding=utf-8

from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        # line=line.decode('utf-8') #decoding the binary data to text
        print(line)
        # if "EST" in line or 'EDT' in line: #look for Estern Time
        #   print(line)

# sending email
import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
                From: soothsayer@example.org

               Beware the Ides of March.
               """)
server.quit()

import smtplib
import ssl
import socket

socket.getaddrinfo('127.0.0.1', 8080)

host = "smtp.gmail.com"
port = 465


username = "idanlevy1995@gmail.com"
password = "mevwvfokfyesvudm"

receiver = "idanlevy1995@gmail.com"
my_context = ssl.create_default_context()

message = """
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=my_context)as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

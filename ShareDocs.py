# for implementing the HTTP Web servers
import http.server
# provides access to the BSD socket interface
import socket
# a framework for network servers
import socketserver
# to display a Web-based documents to users
import webbrowser
# to generate qrcode
import pyqrcode
from pyqrcode import QRCode
# to access operating system control
import os


# assigning the appropriate port value
PORT = 8080

# Find the name of the computer user by using env 
os.environ['USERPROFILE']
# changing the directory to access the files desktop with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'Documents')
os.chdir(desktop)

# creating an http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under which Python interpreter is executed
hostname = socket.gethostname()

# Here we find the IP address of our Computer
temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
temp.connect(("8.8.8.8", 80))
IPADDRESS = "http://" + temp.getsockname()[0] + ":" + str(PORT)
myURL = IPADDRESS

# Using pyqrcode module of python to convert the IP address into Qrcode
url = pyqrcode.create(myURL)
# saves the Qrcode inform of svg
url.svg("QRcode.svg", scale=10)
# opens the Qrcode image in the web browser
webbrowser.open('QRcode.svg')

# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print("Server running at port", PORT)
	print("Type this URL in your Browser", IPADDRESS)
	print("or Use the QRCode")
	httpd.serve_forever()

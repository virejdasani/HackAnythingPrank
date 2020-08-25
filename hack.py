# HackAnything - lol
                                  
import getpass
import time

print("""
 MADE BY:_            _   _____                        _ 
 \ \    / (_)        (_) |  __ \                      (_)
  \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _ 
   \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
    \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
     \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
                    _/ |                                 
                   |__/                                  
""")

identity = input("Confirm Identity: \n")

# print("Access Key:")
password = getpass.getpass()


if identity == "root":

    print("\033[1;32;40m\nGRANTED  \n") # This will give a green output
    command0 = input()
    input("Target Name: \n")
    print('wlan0')
    print('wlan1')
    print('wlan')
    print('wep')
    time.sleep(1)


    if command0 == "aircrack-ng":
        print("""\033[1;32;40m\nif sys.version_info[0] >= 3:
	from socketserver import ThreadingTCPServer
	from urllib.request import urlopen, URLError
	from urllib.parse import urlparse, parse_qs
	from http.client import HTTPConnection
	from http.server import SimpleHTTPRequestHandler
else:
	from SocketServer import ThreadingTCPServer
	from urllib2 import urlopen, URLError
	from urlparse import urlparse, parse_qs
	from httplib import HTTPConnection
	from SimpleHTTPServer import SimpleHTTPRequestHandler

	bytes = lambda a, b : a

port = 1337
url = None
cid = None
tls = threading.local()
nets = {}
cracker = None

class ServerHandler(SimpleHTTPRequestHandler):
	def do_GET(s):
		result = s.do_req(s.path)

		if not result:
			return

		s.send_response(200)
		s.send_header("Content-type", "text/plain")
		s.end_headers()
		s.wfile.write(bytes(result, "UTF-8"))
  \n""")
    time.sleep(3)


    print("""\033[1;32;40m\n def do_POST(s):
		POST_failure = True

		# Read data here and pass it, so we can handle chunked encoding
		if ("dict" in s.path) or ("cap" in s.path):

			tmp_file = "/tmp/" + next(tempfile._get_candidate_names())
			with open(tmp_file, "wb") as fid:
				if s.headers.get('Content-Length'):
					cl = int(s.headers['Content-Length'])
					fid.write(s.rfile.read(cl))
					POST_failure = False
				# elif s.headers.get('Transfer-Encoding') and s.headers['Transfer-Encoding'] == "chunked":
				elif s.headers.get('Transfer-Encoding') == "chunked":
					# With Python3, we need to handle chunked encoding
					# If someone has a better solution, I'm all ears

					while True:
						chunk_size_hex = ""

						# Get size
						while True:
							c = s.rfile.read(1)
							if sys.version_info[0] >= 3:
								c = chr(c[0])
							if c == '':
								# Skip next char ('\n')
								c = s.rfile.read(1)
								break
							chunk_size_hex += c

						# If string is empty, that's the end of it
						if not chunk_size_hex:
							break
                            time.sleep(4)
						# Convert from hex to integer
						chunk_size = int(chunk_size_hex, 16)

						# Read the amount of bytes
						fid.write(s.rfile.read(chunk_size))
					POST_failure = False

			if (POST_failure == False):
				if ("dict" in s.path):
					s.do_upload_dict(tmp_file)

				if ("cap" in s.path):
					s.do_upload_cap(tmp_file)
  \n""")
    time.sleep(5)

    print("""\033[1;32;40m\nif sys.version_info[0] >= 3:
	from socketserver import ThreadingTCPServer
	from urllib.request import urlopen, URLError
	from urllib.parse import urlparse, parse_qs
	from http.client import HTTPConnection
	from http.server import SimpleHTTPRequestHandler
else:
	from SocketServer import ThreadingTCPServer
	from urllib2 import urlopen, URLError
	from urlparse import urlparse, parse_qs
	from httplib import HTTPConnection
	from SimpleHTTPServer import SimpleHTTPRequestHandler

	bytes = lambda a, b : a

port = 1337
url = None
cid = None
tls = threading.local()
nets = {	}
cracker = None

class ServerHandler(SimpleHTTPRequestHandler):
	def do_GET(s):
		result = s.do_req(s.path)

		if not result:
			return

		s.send_response(200)
		s.send_header("Content-type", "text/plain")
		s.end_headers()
		s.wfile.write(bytes(result, "UTF-8"))
  \n""")
    time.sleep(6)

    print("FOUND\n")
    print(password + "\n\n")
    

else:
    print("\033[1;31;40m\nDENIED  \n") # This will give a red utput





# Commands:
# aircrack-ng
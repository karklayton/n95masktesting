import network
import uftpd
import usocket as socket




def connect_wifi(ssid = 'Pumpers5_EXT2.4G', password = 'fX-SZ20G/iPb/Vcw41$Xf'):
    uftpd.start(splash=True)
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print('Connection successful')
    print(station.ifconfig())
    uftpd.restart()
    
    
# def web_page():
    # with open('config.txt', 'r') as myfile:
        # velocity = myfile.read()
    # html = """<html><head>
    # <meta name="viewport" content="width=device-width, initial-scale=1"></head>
    # <body><h1>Dr. Brandt's Mask Tester</h1><form>
    # <label for="velo">Enter Velocity:</label>
    # <input type="number" step="any" min="1" max="10" placeholder ={} id="velo" name="velo">
    # </form></body></html>""".format(velocity)
    # return html
  
  
# def web_server():
    # ap = network.WLAN(network.AP_IF)
    # ap.active(True)
    # ssid = 'Mask_Tester'
    # password = 'Dr_Brandt'
    # ap.config(essid=ssid, password=password)
    # while ap.active() == False:
        # pass
    # print('Connection is successful')
    # print(ap.ifconfig())
    
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
    # s.bind(('', 80))
    # s.listen(5)
    # while True:
        # conn, addr = s.accept()
        # print('Got a connection from %s' % str(addr))
        # request = conn.recv(1024)
        # sreq = str(request)
        # print('Content = %s' % sreq)
        # if 'GET /?velo' in sreq:
            # a = sreq.find('GET /?velo=')
            # b = sreq.find(' HTTP')
            # velocity = sreq[a+11:b]
            # print(velocity)
            # if velocity != '':
                # with open('config.txt', 'w') as myfile:
                # myfile.write(velocity)
                
        # response = web_page()
        # conn.send(response)
        # conn.close()
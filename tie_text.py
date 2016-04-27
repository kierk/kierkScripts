#! /bin/sh

#-----------------------------------------------------------
#	Script for controlling e-tie-o-matic from your phone:
#		by kierke@bu.edu
#
#	Usage:
#		Run `sudo python tie_text.py` on Pi microcontroller
#		connected to the e-ink display
#		text number linked to webserver for 
#-----------------------------------------------------------

from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """E-TIE-O-MATIC!"""

    flag_check = request.values.get('Body', None)
    if flag_check is not None and 'Me' in flag_check:
        message = ('Changing...')
        subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/6.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Adin' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/4.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Venus' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/3.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Aphro' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/0.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Saturn' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/2.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Cat' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/1.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Argyle' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/5.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    elif flag_check is not None and 'Arrow' in flag_check:
    	message = ('Changing...')
    	subprocess.call("/home/pi/Desktop/ec535/PlatformWithOS/driver-common/xbm2bin < imgs/7.xbm  > /dev/epd/display", shell=True)
    	subprocess.call("echo U > /dev/epd/command", shell=True)
    else:
        message = "No image for flag: " + flag_check

    message += "\n\nFlags are: Me, Adin, Venus, Aphro, Saturn, Cat, Argyle, Arrow"

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

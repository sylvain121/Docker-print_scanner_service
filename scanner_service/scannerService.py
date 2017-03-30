from flask import Flask
import sane
import time
from PIL import Image

app = Flask(__name__)
base_folder = "/mnt/scanner"

#
# scanner init pixma MP240
#

depth = 8
mode = 'color'

ver = sane.init()
print('SANE version:', ver)

devices = sane.get_devices()
print('Available devices:', devices)

# open first device
dev = sane.open(devices[0][0])
params = dev.get_parameters()

try:
    dev.depth = depth
except:
    print('Cannot set Depth, defaulting to %d' % params[3])

try:
    dev.mode = mode
except:
    print('Cannot set mode, defaulting to %s' % params[0])

params = dev.get_parameters()
print('Device parameters:', params)


img_count = 1

@app.route('/scan')
def scan_image():
    dev.start()
    im = dev.snap()
    filename = "scanned-%s-%05d.jpg" % (time.strftime("%Y-%m-%d-%H%M%S", img_count%10000))
    im.save(os.path.join(base_folder, filename), quality=100)
    img_count += 1
    return "SCANED !!!" 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

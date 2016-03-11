import qrcode
import sys
import oledImage
from OmegaExpansion import oledExp


# check for arguments
if len(sys.argv) < 2:
	print 'ERROR: Expected data to encode!'
	exit()

# load the data 
data = sys.argv[1]

# define the filename for the generated OLED image
imageFile = 'qr-code.lcd'


# setup the QR Code generator
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

print '> Encoding %d characters'%(len(data))
qr.add_data(data)
qr.make(fit=True)

matrix = qr.get_matrix()
print '> Generated QR Code: %dx%d'%(len(matrix[0]), len(matrix) )

# double the QR code size if it's less than half of the OLED size
dMatrix = oledImage.doubleMatrixSize(matrix)
xOffset = oledImage.SCREEN_WIDTH/2 - len(dMatrix[0])/2


## convert the QR code to an OLED image
screen = oledImage.convertToOledImg(dMatrix, xOffset, 0)
#oledImage.printScreen(screen, newlines=False)
oledImage.printToFile(screen, imageFile)


## display the image on the OLED Expansion
oledExp.driverInit()
oledExp.drawFromFile(imageFile)

#qr.print_tty()

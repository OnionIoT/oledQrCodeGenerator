import oledImage
import qrcode
from OmegaExpansion import oledExp

def dispQrCode (data, imageFile='qr-code.lcd'):
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

	matrix 		= qr.get_matrix()
	matrixRows 	= len(matrix)
	matrixCols 	= len(matrix[0])
	print '> Generated QR Code: %dx%d pixels'%(matrixCols, matrixRows )

	# check the size
	if matrixCols > oledImage.SCREEN_WIDTH or matrixRows > oledImage.SCREEN_HEIGHT:
		print 'ERROR: Generated QR code is too large for the OLED Display! Try less text!'
		exit()

	# double the QR code size if it's less than half of the OLED size
	dMatrix = oledImage.doubleMatrixSize(matrix)
	xOffset = oledImage.SCREEN_WIDTH/2 - len(dMatrix[0])/2


	## convert the QR code to an OLED image
	screen = oledImage.convertToOledImg(dMatrix, xOffset, 0)
	oledImage.printToFile(screen, imageFile)


	## display the image on the OLED Expansion
	oledExp.driverInit()			# initialize the screen
	oledExp.setDisplayMode(1)		# invert the colours
	oledExp.drawFromFile(imageFile)	# display the image file



if __name__ == '__main__':  # pragma: no cover
	import sys
	data 	= ""

	# check for arguments
	if len(sys.argv) < 2:
		print 'Expected data to encode!'
		print 'Using default text :)'
		data = 'Onion Omega: Invent the Future'
	else:
		# load the data
		data = sys.argv[1]

	# run the function to generate the qr code and display on the OLED
	dispQrCode(data)


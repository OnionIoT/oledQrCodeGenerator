import sys


SCREEN_WIDTH 		= 128
SCREEN_HEIGHT 		= 64

SCREEN_PAGE_HEIGHT 	= 8
SCREEN_PAGES 		= (SCREEN_HEIGHT/SCREEN_PAGE_HEIGHT)


# print the oled image to the screen
def printScreen (obj, newlines=True):
	sys.stdout.softspace=0
	for row in obj:
		for point in row:
			print '%02x'%point,
		if newlines == True:
			print ' '
	print ' '

# print the oled image to a file
#	1024 bytes in a row
def printToFile(obj, filename):
	out = []
	f = open(filename, 'w')
	for row in obj:
		for point in row:
			if type(point) is int:
				byte = str('%02x'%point)
				f.write(byte)

	f.close()

# convert boolean to a 1 or 0, bitshift the appropriate number of bits
def matrixPointToBit (bool, bitNumber):
	val 	= 0
	if bool == True:
		val = 1 << bitNumber

	return val 


# convert a vertical row of 8 pixels to an OLED byte
def matrixPointsToByte (matrix, X, startingY):
	byte 	= 0
	for i in range(0,8):
		row  = startingY + i
		#print 'matrix(%d,%d)= '%(X, row),
		if (row < len(matrix)-1):
			data = matrix[row][X]
			#print data
		else:
			data = 0
			#print 'ZERO'

		byte |= matrixPointToBit(data, i)

	return byte

# convert a boolean matrix to an oled image
#	matrix 	- the boolean matrix to convert
#	xOffset	- how much to shift the image on the X axis in the OLED image
#	yOffset	- how much to shift the image on the Y axis in the OLED image 
def convertToOledImg (matrix, xOffset, yOffset):
	oled 	= [[0] * SCREEN_WIDTH for x in xrange(SCREEN_PAGES)]

	# loop through the rows (increasing by page size)
	for y in range(0, len(matrix), SCREEN_PAGES):
		yy = yOffset + y
		# loop through each pixel in the row
		for x in range(0, len(matrix[y]) ):
			# convert the 8 vertical pixels to a byte
			byte = matrixPointsToByte(matrix, x, y)
			# set this byte in the oled screen object
			oled[y/SCREEN_PAGES][x + xOffset]	= byte

	return oled

# 
def doubleMatrixSize (matrix):
	rows 	= len(matrix)
	cols 	= len(matrix[0])

	if rows <= (SCREEN_HEIGHT/2):
		dMatrix 	= [[0] * cols*2 for x in xrange(rows*2)]

		for y in range(0, rows):
			for x in range(0, cols):
				# copy this matrix point to 4 new matrix points
				dMatrix[y*2][x*2] 		= matrix[y][x]
				dMatrix[y*2][x*2+1] 	= matrix[y][x]
				dMatrix[y*2+1][x*2] 	= matrix[y][x]
				dMatrix[y*2+1][x*2+1] 	= matrix[y][x]
		print '> Doubled QR Code size: %dx%d'%(len(dMatrix[0]), len(dMatrix) )
	else:
		dMatrix 	= matrix

	return dMatrix










# oled-qr-code-generator
Encode text and display QR Code on OLED Expansion


# Installation 

On your Omega:
```
git clone https://github.com/OnionIoT/oledQrCodeGenerator.git
```


## Required Packages

Install the following packages:
```
opkg update
opkg install git git-http python-light python-codecs pyOledExp
```


# Generating a QR Code

Run the following command:
```
python oledQrCodeGenerator/main.py '<text to encode>'
```

This will create a QR Code with the specified text and display it on the OLED Display.



## Using the Module

The code here can also be used as a module to be included in other scripts.

```
import oledQrCodeGenerator


oledQrCodeGenerator.dispQrCode('Hello!')
```



# Acknowledgements

The code in the `qrcode` directory is a stripped-down version of lincolnloop's `python-qrcode` repo:
https://github.com/lincolnloop/python-qrcode/tree/master/qrcode

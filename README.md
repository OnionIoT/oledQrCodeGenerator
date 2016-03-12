# oled-qr-code-generator
Encode text and display QR Code on OLED Expansion


# Installation 

On your Omega:
```
git clone https://github.com/OnionIoT/oled-qr-code-generator.git
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
python oled-qr-code-generator/display-qr-code.py '<text to encode>'
```

This will create a QR Code with the specified text and display it on the OLED Display.



# Acknowledgements

The code in the `qrcode` directory is a stripped-down version of lincolnloop's `python-qrcode` repo:
https://github.com/lincolnloop/python-qrcode/tree/master/qrcode

# simple qr code generator for more information visit qrcode functions
# qr code is going to save in same directory or folder where file is locates after run the program
import qrcode

img = qrcode.make('https://www.google.com')
type(img)
img.save("google-site.png")
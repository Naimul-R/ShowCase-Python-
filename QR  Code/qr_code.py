import qrcode as qr

img = qr.make("https://www.facebook.com/naimul.rabby.407310/")
img.save("facebook_qr.png")
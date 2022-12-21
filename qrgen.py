import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://www.youtube.com/watch?v=sek3FhByr6w"
qr.add_data(data)
qr.make(fit=True)
qr.make_image(fill="black",back_color="white")
img.save('text.png')  

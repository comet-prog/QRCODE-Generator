import qrcode
Url = input("Enter your text or URL").strip()
filename = input("Enter filename").strip()
qr = qrcode.QRCode(box_size=20, border=5)

qr.add_data(Url)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR saved at {filename}")

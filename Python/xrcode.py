import qrcode

link = "https://drive.google.com/file/d/1vjudUh-F_KMdOnSpZZPLYpNENK6VDk4V/view?usp=sharing"
qr = qrcode.make(link)
qr.save("qr_foto.png")
print("QR berhasil dibuat")
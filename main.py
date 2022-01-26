import pyqrcode

text = str(input("Enter the string :"))
file_name = str(input("Enter a name for QR code file : "))
qr = pyqrcode.create(text)
qr.svg(f"{file_name}.svg",scale=20)

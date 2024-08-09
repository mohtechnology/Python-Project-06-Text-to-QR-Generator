import qrcode

print("Welcome To Text To QR Code Convertor")
text = input("Enter the text here : ")

img = qrcode.make(text)

img.save("image.png")

print("Your QR-Code is generated Successfully")
print("Thank You")

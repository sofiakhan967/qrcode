from ensurepip import version
from turtle import fillcolor
import qrcode #install qrcode
import image #pip install Image
#this is simple qrcode generator

#my_qrcode=qrcode.make("hello ")
#my_qrcode.save("myimg.png")

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
                  box_size=10,
                  border=2)
qr.add_data("") #can pass link 
qr.make(fit=True)

img=qr.make_image(fillcolor="black", back_color="white")
img.save("myprofile.png")

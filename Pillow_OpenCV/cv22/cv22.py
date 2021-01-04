from PIL import Image,ImageDraw,ImageFont,ImageColor,ImageFilter

image = Image.open('C:\\Users\\radis\\Desktop\\me.jpeg')
cr = image.crop((0, 80, 500, 1100))
draw = ImageDraw.Draw(cr)
draw.line((200,230, 180, 480))
font = ImageFont.load_default()
draw.text((200,200),'Mood',font = font,fill='black')
draw.rectangle((100, 650, 230, 490), outline=ImageColor.getrgb("yellow"), width=5)
box=(0, 80, 500, 1100)
blur = cr.filter(ImageFilter.GaussianBlur(5))
cr.paste(blur,box)
cr.save('C:\\Users\\radis\\Desktop\\me.png')
cr.show()



import cv2
Image = cv2.imread('C:\\Users\\radis\\Desktop\\me.jpeg')
th = cv2.threshold(Image,(200,200),0)

cv2.imshow('I',Image)
cv2.rectangle(Image,(100, 750),(230, 590),(0, 255, 255), 10)
cv2.putText(Image,'Mood',(200,200),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 1)
cropped = Image[0:280,500:700]
blurred = cv2.GaussianBlur(cropped, (41,41), 0)
crop = Image[100:300, 100:320]
cv2.imshow("cr", crop)
x_=300
y_=200
Image[y_:y_+cropped.shape[0], x_:x_+cropped.shape[1]] = blurred
cv2.imwrite('C:\\Users\\radis\\Desktop\\me1.jpeg',Image)
cv2.imshow('I+', Image)
cv2.waitKey(0)
cv2.destroyAllWindows()

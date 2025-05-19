import cv2
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np
from PIL import ImageFont, ImageDraw, Image

 
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)


while True:
    try:
        success,img = cap.read()

        text = "أيوب علالي"
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text) 

        fontpath = "arial.ttf" # ==> https://www.freefontspro.com/14454/arial.ttf  

        font = ImageFont.truetype(fontpath, 45)

        img_pil = Image.fromarray(img)

        draw = ImageDraw.Draw(img_pil)
        draw.text((100,100),bidi_text, font = font,fill=(0,255,0))


        img = np.array(img_pil)

        cv2.imshow("Output",img)
        cv2.waitKey(1)
    except:
        pass

cap.release()
cv2.destroyAllWindows()
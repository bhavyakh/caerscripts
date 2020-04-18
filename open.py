import cv2
import sys
vars = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
for j in range(7):
    ff = 'CAER-S/test/' + vars[j] + '/'
    gg = 'face/test/' + vars[j] + '/'
    hh = 'context/test/' + vars[j] + '/'

    for i in range(2999):
        imagePath  = ff + str(i+1).zfill(4)+'.png'
        print(imagePath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.32,
            minNeighbors=6,
            minSize=(80,80)
        )

        
        for (x, y, w, h) in faces:
            
            
            roi_color = image[y:y + h, x:x + w]
            
            print("[INFO] Object found. Saving locally at file number.{}".format(i))
            target = gg + str(i+1).zfill(4) + '.png'
            print(target)
            cv2.imwrite(target, roi_color)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), -1)
            
            break;
        status = cv2.imwrite(hh+ str(i+1).zfill(4) + '.png',image)
            

    
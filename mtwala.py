import cv2 
from mtcnn.mtcnn import MTCNN
vars = ['Neutral']
detector = MTCNN()

for j in range(1):
    ff = 'CAER-S/train/' + vars[j] + '/'
    gg = 'face/train/' + vars[j] + '/'
    hh = 'context/train/' + vars[j] + '/'

    for i in range(7001):
        imagePath  = ff + str(i+1).zfill(4)+'.png'
        print(imagePath)
        image = cv2.imread(imagePath)
        result = detector.detect_faces(image);
        if(len(result)):
            box = result[0]['box'] 
            x1 = abs(box[0])
            y1 = abs(box[1])
            x2 = abs(box[0]+box[2])
            y2 = abs(box[1]+box[3])
            roi_color = image[y1:y2, x1:x2]            
            target = gg + str(i+1).zfill(4) + '.png'
            cv2.imwrite(target, roi_color)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0,0,0), thickness=-1)
            status = cv2.imwrite(hh+ str(i+1).zfill(4) + '.png',image)
        else:
            print('Face not found!')
            

    
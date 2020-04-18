import cv2 as cv2
import dlib
import sys
vars = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
dnnFaceDetector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
        
for j in range(7):
    ff = 'CAER-S/train/' + vars[j] + '/'
    gg = 'face/train/' + vars[j] + '/'
    hh = 'context/train/' + vars[j] + '/'

    for i in range(7001):
        imagePath  = ff + str(i+1).zfill(4)+'.png'
        print(imagePath)
        imagePath = 'CAER-S/train/Happy/1234.png';

        image = cv2.imread(imagePath)
        
        rects = dnnFaceDetector(image, 1)


        if(len(rects)):
            for (pl, rect) in enumerate(rects):
                x1 = rect.rect.left()
                y1 = rect.rect.top()
                x2 = rect.rect.right()
                y2 = rect.rect.bottom()
                roi_color = image[y1:y2, x1:x2]
                
                
                target = gg + str(i+1).zfill(4) + '.png'
                cv2.imwrite(target, roi_color)
                        
                # Rectangle around the face
                cv2.rectangle(image, (x1, y1), (x2, y2), (0,0,0), thickness=-1)
                break;
            status = cv2.imwrite(hh+ str(i+1).zfill(4) + '.png',image)
            

    
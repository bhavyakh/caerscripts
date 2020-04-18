import cv2 
from mtcnn.mtcnn import MTCNN
imagePath = 'CAER-S/train/Happy/1234.png';
detector = MTCNN()
print(imagePath);
image = cv2.imread(imagePath);
result = detector.detect_faces(image);
print(result)
if(len(result)):
    box = result[0]['box'] 
    print(box)
    x1 = box[0]
    y1 = box[1]
    x2 = box[0]+box[2]
    y2 = box[1]+box[3]
    #roi_color = image[box[0]:box[1], box[2]:box[3]]
    roi_color = image[y1:y2, x1:x2]
                
    print(roi_color)
    cv2.imwrite('abhc.png',roi_color)
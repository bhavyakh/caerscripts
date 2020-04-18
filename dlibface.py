import dlib
import cv2
import matplotlib.pyplot as plt

dnnFaceDetector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
imagePath = 'CAER-S/test/Happy/0001.png'
print(imagePath)
image = cv2.imread(imagePath)
rects = dnnFaceDetector(image, 1)
for (i, rect) in enumerate(rects):
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
status = cv2.imwrite('sample.png',image)     
import cv2          

#storing the cars image in a variable
img_file="car3.jpg"

#video=cv2.VideoCapture('carvideo.mp4')


video=cv2.VideoCapture('carpedestrian.mp4')

#our pre trained clasiifier
car_dector_xml_file='cars.xml'
pedestrian_detector_xml_file='haarcascade_fullbody.xml'

#create pedestrian classifier
pedestrian_tracker=cv2.CascadeClassifier(pedestrian_detector_xml_file)

#create car classifier
car_detector=cv2.CascadeClassifier(car_dector_xml_file)

while True:
    
    (read_succesful,frame)=video.read()
    
    #bnwframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #safe coding
    if read_succesful:
        bnwframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    
    #detect cars and pedestrians
    cars=car_detector.detectMultiScale(bnwframe)
    pedestrians=pedestrian_tracker.detectMultiScale(bnwframe)

    #print(cars)

    #draw rectangle around the cars
    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    #draw rectangle around the pedestrians
    for(x,y,w,h) in pedestrians:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    #Display the image with the faces spotted
    cv2.imshow('Clever Programmer Car Detector',frame)

    #Dont autoclose(Wait here in the code and listen for a key press)
    key= cv2.waitKey(1)

    #stop if q key is framed
    if key==81 or key==113:
        break

#release the video capture
video.release()

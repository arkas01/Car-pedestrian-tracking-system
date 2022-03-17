# Car-pedestrian-tracking-system
Car and pedestrian tracking system using python and openCV

Abstract:
The aim of the project is to use computer vision to track cars and pedestrians on the streets using Python and openCV. By using computer vision it is much easier to track the vehicles and the pedestrians on the road rather than using a LIDAR sensor, which is much more costlier and doesn’t provide much decipherable results.So far the main aim of this project is to track cars and pedestrians. But this application is useful for building automated vehicles.`

Approach Used:
The main part of this project is the haar cascade file which is a pre trained car classifier and a pre trained pedestrian classifier. Using the cascade classifier attribute of openCV I’ve used the cascade files to detect and distinguish the vehicles and pedestrians in our project. Also on detecting the cars and pedestrians I’ve distinguished them by drawing rectangles of different colors around them.

Reference links of the haar cascade files:
Pedestrians: https://raw.githubusercontent.com/ope...
Cars: https://raw.githubusercontent.com/and...

  
Conclusion:
There are several drawbacks of the system such as delay in transmission and even false tracking in some incidents, and the accuracy of the model is about 75%.

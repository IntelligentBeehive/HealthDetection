# Hive health detection by only using a simple Camera!

## How to install:

### Install packages
* Python3
* TensorFlow 1.15 (Important to use 1.15)
* OpenCV3
* Numpy

### Run
Run "python3 Main.py" to start the program. It will use images inside the DataSet as input for the classification. 

Run "python3 Main_Demo.py" to visualize the steps the program takes to classify the beehive. 

If you want to use a live camera pointed at your beehive change the cv2.imread function at line 13 in main.py to use your camera. Also change the classify function to get your camera image

## Results

### BeeCounter

#### Input Image
![Image description](https://github.com/IntelligentBeehive/HealthDetection/blob/master/pics/kast1.jpeg)

#### Sectioned part of image
![Image description](https://github.com/IntelligentBeehive/HealthDetection/blob/master/pics/populationCounterSection.png)

#### Final Result
![Image description](https://github.com/IntelligentBeehive/HealthDetection/blob/master/pics/populationCounterResult.png)

### Brood Pattern Classifier
#### Healthy Result
![Image description](https://github.com/IntelligentBeehive/HealthDetection/blob/master/pics/healthy.png)

#### Unhealthy Result
![Image description](https://github.com/IntelligentBeehive/HealthDetection/blob/master/pics/unhealthy.png)







## OLD:
classify the broodpattern using AI trained on the complex features of an healthy and unhealthy broodpattern. Use the confidence as an factor of the state of the brood pattern

Use Computer Vision to calculate the area of bee clusters to calculate the population in the beehive

Store this data inside a DataBase

Calculate trends on this DataBase to find patterns of degrading hive health

Warn bee keeper if there is a trend in which the hive health is degreding,


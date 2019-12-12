Brood Pattern Health Detection By Using AI

this AI can classify wather an image of the brood pattern of a Beehive is Healthy or Unhealthy based on the features it can extract from the image. Example feature could be if an brood cell is capped or not.

Steps:
-  1 DataSet was made from the internet. Two sets are availible:
-- DataSetV1 (Hand picked images of healthy and unhealthy brood pattern) Around 100 images
-- DataSetV2 (Automated image download of healthy and unhealthy brood pattern) Around 600 images (has lots of false images)
- 2 AI was trained on both datasets. MobileNet with DataSetV1 gave best Accuracy. (all other models are also inside this repo
- 3 Script which automatilcy calls AI to calssify boor patern Health at a specific time interval has been made
- 4 Result is given back to the Main.py script which then combines population count to give health state of the entire beehive. 

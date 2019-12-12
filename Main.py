import sys
sys.path.insert(1, 'BroodPatternAI/')
sys.path.insert(2, 'PopulationCounter/')

from Classifier import *
from Demo import *


broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/h1.png"

results = Classify(broodimagepath)

print(results)

#print(run())
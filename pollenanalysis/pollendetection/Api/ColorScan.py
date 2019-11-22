from Domain.Plant import Plant
import csv
import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt


class ColorScan:
    def __init__(self):
        self.plant1 = Plant("Lupin", "#6c2d23", "summer", 108, 45, 35)

    def pixel_compare(self, r, g, b):
        return self.plant1.rgb == {r, g, b}


colorScan = ColorScan()
print(ColorScan.pixel_compare(colorScan, 5, 5, 5))
print(ColorScan.pixel_compare(colorScan, 108, 45, 35))

with open('..\CSV\pollenchart.csv', 'r', encoding="utf-8-sig") as csvDataFile:
    csvReader = csv.DictReader(csvDataFile, delimiter="	")
    print(csvReader.fieldnames)
    for row in csvReader:
        found = ColorScan.pixel_compare(colorScan, row['Red'], row['Green'], row['Blue'])
        if found:
            print(row)

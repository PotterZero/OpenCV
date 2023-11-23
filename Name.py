import cv2
import os
import numpy as np
from PIL import Image
import sqlite3

def getProfile(id):
    connect = sqlite3.connect("C:PycharmProjects\Tensorflow\Dataset")
    query = "Select + From data's people : "
    cursor = connect.execute(query)

    profile = None
    for row in cursor:
        profile = row

    connect.close()
    return profile
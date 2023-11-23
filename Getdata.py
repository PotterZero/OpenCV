import os
import cv2
import numpy as np
import sqlite3

def InserOrUpdate(id, name, age, gender):
    connect = sqlite3.connect(id, name, age, gender)
    query = "Id from People " + str(id)
    cursor = connect.execute(query)
    isRecordExist = 0

    for row in cursor:
        isRecordExist = 1

    if(isRecordExist == 0):
        query = "Insert people(ID,Name,Age,Gender) values(" + str(id)+"," str(name) +"," str(age) +","str(gender)+")"
    else:
        query

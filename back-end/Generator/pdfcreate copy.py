import cv2
import numpy as np
import pandas as pd

data = pd.read_excel("C:/Users/Dev/Desktop/Live_wires_project/CG2/Certificate-Generator/back-end/Generator/cert_data.xlsx ", engine="openpyxl")
print(data)

for i in data['Name']:
    length=len(i)*50
    cert = cv2.imread("C:/Users/Dev/Desktop/Live_wires_project/CG2/Certificate-Generator/back-end/Generator/image.png")
    resized = cv2.resize(cert,(1987,1386))
    cv2.putText(resized,i,(1000-length,727),cv2.FONT_HERSHEY_COMPLEX,5,(0,0,255),1,cv2.LINE_AA)
    cv2.imwrite("C:/Users/Dev/Desktop/Live_wires_project/CG2/Certificate-Generator/back-end/Generator/image{}.png".format(i),resized)
    print("the process for {}".format(i))
        
    
         





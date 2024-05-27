import pandas as pd
import cv2
from PIL import Image , ImageDraw ,ImageFont

names = {'Name':['Rajesh k',"Mohammad Vaseem","Devan S","Nikil Paul","Saravana Kumar"]}

df = pd.DataFrame(names)
# print(df)

font_file = ImageFont.truetype("GreatVibes-Regular.ttf",180)
font_color = "#FFFFFF"

# template = Image.open('template.png')
# Draw = ImageDraw.Draw(template)

# Width, Height = template.size



# length = font_file.getlength("Rajesh")

# start_x = (Width- length)//2.5

# #

# Draw.text((start_x,(Height-250)//2),"Rajesh K", fill=font_color, font=font_file)

# template.save('C:\\Users\\Rajesh\\Desktop\\Workspace\\Python-Development\\LiveWires\\Rajesh.png')
# print('Saving Certificate of:', "Rajesh")  

def generation(Template,  Name):
    template = Image.open(Template)
    Draw = ImageDraw.Draw(template)
    Width, Height = template.size
    length = font_file.getlength(Name)
    start_x = (Width- length)//2
    Draw.text((start_x,(Height-250)//2),Name, fill=font_color, font=font_file)
    template.save(f'C:\\Users\\Rajesh\\Desktop\\Workspace\\Python-Development\\LiveWires\\{Name}.png')
    # print(f"{Name}'s certificate is generated!!!")
    return "Completed"
    


for i in df['Name']:
    generation("template.png",i)
print("completed")

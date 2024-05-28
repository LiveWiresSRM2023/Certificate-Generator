# # import pandas as pd
# # import cv2
# # from PIL import Image , ImageDraw ,ImageFont

# # names = {'Name':['Rajesh k',"Mohammad Vaseem","Devan S","Nikil Paul","Saravana Kumar"]}

# # df = pd.DataFrame(names)
# # # print(df)

# # font_file = ImageFont.truetype("GreatVibes-Regular.ttf",180)
# # font_color = "#FFFFFF"

# # # template = Image.open('template.png')
# # # Draw = ImageDraw.Draw(template)

# # # Width, Height = template.size



# # # length = font_file.getlength("Rajesh")

# # # start_x = (Width- length)//2.5

# # # #

# # # Draw.text((start_x,(Height-250)//2),"Rajesh K", fill=font_color, font=font_file)

# # # template.save('C:\\Users\\Rajesh\\Desktop\\Workspace\\Python-Development\\LiveWires\\Rajesh.png')
# # # print('Saving Certificate of:', "Rajesh")  

# # def generation(Template,  Name):
# #     template = Image.open(Template)
# #     Draw = ImageDraw.Draw(template)
# #     Width, Height = template.size
# #     length = font_file.getlength(Name)
# #     start_x = (Width- length)//2
# #     Draw.text((start_x,(Height-250)//2),Name, fill=font_color, font=font_file)
# #     # template.save(f'C:\\Users\\Rajesh\\Desktop\\Workspace\\Python-Development\\LiveWires\\{Name}.png')
# #     template.save(f'C:\\Users\\Dev\\Desktop\\Certificate_Generator_v1.1\\Certificate-Generator\\CG_PRO\\generator_engine\\{Name}.png')
# #     # print(f"{Name}'s certificate is generated!!!")
# #     return "Completed"
    


# # for i in df['Name']:
# #     generation("template.png",i)
# # print("completed")






# import pandas as pd
# import cv2
# from PIL import Image, ImageDraw, ImageFont
# import os


# class gen_engine():
#     def generate(name):
#         # Define the names dictionary and create DataFrame
#         # names = {'Name': ['Rajesh k', "Mohammad Vaseem", "Devan S", "Nikil Paul", "Saravana Kumar"]}
#         df = pd.DataFrame(name)

#         # Path to the font file
#         font_path = "C:\\Users\\Dev\\Desktop\\CGP_V1.3 ENV\\venv\\Certificate-Generator\\CG_PRO\\generator_engine\\GreatVibes-Regular.ttf"

#         # Check if the font file exists
#         if not os.path.exists(font_path):
#             raise FileNotFoundError(f"The font file {font_path} does not exist.")

#         font_file = ImageFont.truetype(font_path, 180)
#         font_color = "#FFFFFF"

#         # Function to generate certificates
#         def generation(template_path, name):
#             # Check if the template file exists
#             if not os.path.exists(template_path):
#                 raise FileNotFoundError(f"The template file {template_path} does not exist.")
            
#             template = Image.open(template_path)
#             draw = ImageDraw.Draw(template)
#             width, height = template.size
#             length = font_file.getlength(name)
#             start_x = (width - length) // 2
#             draw.text((start_x, (height - 250) // 2), name, fill=font_color, font=font_file)
            
#             # Construct the output path
#             output_path = os.path.join('C:\\Users\\Dev\\Desktop\\CGP_V1.3 ENV\\venv\\Certificate-Generator\\CG_PRO\\generator_engine\\', f'{name}.png')
#             template.save(output_path)
            
#             print(f"{name}'s certificate is generated!!!")
#             return "Completed"

#         # Generate certificates for all names in the DataFrame
#         for name in df['Name']:
#             generation("venv//Certificate-Generator//CG_PRO//generator_engine//template.png", name)
#         print("Completed")








import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

class gen_engine:
    def generate(self, names):
        df = pd.DataFrame(names)

        # Path to the font file
        font_path = "C:\\Users\\Dev\\Desktop\\CGP_V1.3 ENV\\venv\\Certificate-Generator\\CG_PRO\\generator_engine\\GreatVibes-Regular.ttf"

        # Check if the font file exists
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"The font file {font_path} does not exist.")

        font_file = ImageFont.truetype(font_path, 180)
        font_color = "#FFFFFF"

        # Function to generate certificates
        def generation(template_path, name):
            # Check if the template file exists
            if not os.path.exists(template_path):
                raise FileNotFoundError(f"The template file {template_path} does not exist.")
            
            template = Image.open(template_path)
            draw = ImageDraw.Draw(template)
            width, height = template.size
            length = font_file.getlength(name)
            start_x = (width - length) // 2
            draw.text((start_x, (height - 250) // 2), name, fill=font_color, font=font_file)
            
            # Construct the output path
            output_path = os.path.join('C:\\Users\\Dev\\Desktop\\Certificate-Generator\\CG_PRO\\generator_engine\\', f'{name}.png')
            template.save(output_path)
            
            
            print(f"{name}'s certificate is generated!!!")
            return "Completed"

        # Generate certificates for all names in the DataFrame
        
        for name in df['Name']:
            generation("C:\\Users\\Dev\\Desktop\\CGP_V1.3 ENV\\venv\\Certificate-Generator\\CG_PRO\\generator_engine\\template.png", name)
        print("Completed")










# names = {'Name': ['Rajesh k', "Mohammad Vaseem", "Devan S", "Nikil Paul", "Saravana Kumar"]}
# engine=gen_engine()
#     # Call the generate method with the list of names
# engine.generate(names)

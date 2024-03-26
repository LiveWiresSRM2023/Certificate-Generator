# import sqlite3
# import pandas as pd
# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
# cursor.execute("SELECT name from sqlite_master WHERE type='table';")
# names = cursor.fetchall()
# print(names)
# for i in names:
#     print('hi'+i+1)
#     cursor.execute(f"SELECT * FROM {i[0]}")
#     rows = cursor.fetchall()
#     print(row)
#     df = pd.DataFrame(rows, columns=["Name","Register number","evant","email"])
#     print(df)
#     cursor.close()
#     conn.close()


import sqlite3
import pandas as pd

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
names = cursor.fetchall()

detials=[]
for name in names:
    table_name = name[0]
    

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    # print(rows)
    df = pd.DataFrame(rows, columns=["Name", "Register_number", "Event", "Email"])
    data=[i for i in df.values]
    for i in range(len(data)):
        detials.append(data[i])
email='devan333s@gmail.com'

import numpy as np
df=pd.DataFrame(detials,columns=["Name", "Register_number", "Event", "Email"])
# print(df)
dataframe=df[df['Email']==email]
print(dataframe)
final_data=[]
data_=[i for i in dataframe.values]
for i in range(len(data_)):
    final_data.append(data_[i])
return final_data



# print([i for i in dataframe])
# Close the cursor and connection outside the loop

cursor.close()
conn.close()

import psycopg2
import pandas as pd
import sqlalchemy as db 
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import numpy as np
from PIL import Image
from scipy.misc import toimage
import scipy.misc
from scipy.misc import imsave
from datetime import datetime, date


class OperationDatabase():

    engine = db.create_engine('postgresql://postgres:postgres@localhost:5432/TitanLog')
    
    def __init__(self):

        try:
            self.Data = pd.DataFrame(columns = ['face', 'embedding_id', 'embedding', 'start_time', 'end_time', 'cam_id' , 'duration'])
            # self.Data = pd.DataFrame(columns = ['face'])
            self.connection = self.engine.connect()
            print("Database instance is created")
        except Exception as e:
            print("Exception in initiating the database :",e)

    def selectquery(self):

        table = self.connection.execute(f"""SELECT encode(face, 'escape'), embedding_id, encode(embedding, 'escape'), start_time, end_time, cam_id , duration FROM datalog;""")
        # table = self.connection.execute(f"""SELECT encode(face, 'escape') FROM datalog;""")
        # df = pd.read_sql(table, self.connection)
        # print(df)
        dfcount = 0
        for row in table:

            row = list(row)
            self.Data.loc[dfcount] = row
            dfcount += 1
        final_table = self.connection.execute(f"""UPDATE datalog SET duration=end_time-start_time;""")
        # print(final_table)
        # for index, row in self.Data.iterrows():
        #     # t = datetime.now().time()
        #     # seconds = (t.hour * 60 + t.minute) * 60 + t.second
        #     # print(seconds)
        #     print(type(pd.Timestamp(row['end_time'])))
        #     print(pd.Timestamp(row['end_time']) - pd.Timestamp(row['start_time']))
        #     print(type(pd.Timestamp(row['end_time'])))
        #     df["end_time"] = pd.Timestamp(df['end_time'])
        # df["start_time"] = pd.Timestamp(df['start_time'])
        # self.Data['end_time'] =  self.Data['end_time'].apply(pd.Timestamp)
        # self.Data['start_time'] = self.Data['start_time'].apply(pd.Timestamp)
        # self.Data['duration'] = self.Data['end_time'].sub(self.Data['start_time'], axis=0)
        # self.Data['duration'] = self.Data['end_time'].sub(self.Data['start_time'])
        # print(self.Data)
        # print(df)

        # df["end_time"] = pd.Timestamp(df['end_time'])
        # df["start_time"] = pd.Timestamp(df['start_time'])

        # # self.Data["up_duration"] = self.Data["end_time"] - self.Data["start_time"]
        # print(df)


        # for i in range(0, len(self.Data)):
        #     # print(i)
        #     df = self.Data
        #     ith = df.loc[i]

        #     ith["end_time"] = pd.to_datetime(ith['end_time'], errors='coerce')
        #     ith["start_time"] = pd.to_datetime(ith['start_time'], errors='coerce')
        #     start = ith["start_time"].item()
        #     end = ith["end_time"].item()
        #     dur = end - start
        #     print("Duration time is here", dur)



        # self.Data["end_time"] = pd.to_datetime(self.Data['end_time'])
        # self.Data["start_time"] = pd.to_datetime(self.Data['start_time'])
        # self.Data["up_duration"] = self.Data["end_time"] - self.Data["start_time"]
        # print(self.Data)
        # print(type(self.Data["end_time"]))
        self.Data = self.Data.to_json()
        print(self.Data)

        return(self.Data)

OpData = OperationDatabase()
OpData.selectquery()

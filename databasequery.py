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
        dfcount = 0
        for row in table:
            row = list(row)
            self.Data.loc[dfcount] = row
            dfcount += 1
        self.Data = self.Data.to_json()
        return(self.Data)

OpData = OperationDatabase()
OpData.selectquery()

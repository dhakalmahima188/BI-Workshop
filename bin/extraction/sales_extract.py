from lib.Variables import Variables
import sqls
import datetime
from lib.Logger import Logger
v = Variables()

def sales_extract():


    print("Extracting Sales " + str(datetime.datetime.now()))
    Logger.log_message("Extracting Sales " + str(datetime.datetime.now()))

    #load_stage_table for customer table
    table = "SALES"
    sqls.load_stage(table, v)

    print("Extracted Sales " + str(datetime.datetime.now()))
    Logger.log_message("Extracted Sales " + str(datetime.datetime.now()))


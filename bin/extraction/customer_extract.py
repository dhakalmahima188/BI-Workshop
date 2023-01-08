from lib.Variables import Variables
import sqls
import datetime
from lib.Logger import Logger
v = Variables()

def customer_extract():


    print("Extracting Customer " + str(datetime.datetime.now()))
    Logger.log_message("Extracting Customer " + str(datetime.datetime.now()))


    #load_stage_table for customer table
    table = "CUSTOMER"
    sqls.load_stage(table, v)

    print("Extracted Customer " + str(datetime.datetime.now()))
    Logger.log_message("Extracted Customer " + str(datetime.datetime.now()))


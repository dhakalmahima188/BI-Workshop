from lib import Variables
import sqls
import datetime
from lib.Logger import Logger

def customer_load():

    print("Loading to Customer " + str(datetime.datetime.now()))
    Logger.log_message("Loading to Customer " + str(datetime.datetime.now()))

    table = "CUSTOMER"
    sqls.truncate_table("RETAIL_DWH", "TEMP", "TMP", table)
    #load temp table customer from customer stage table
    load_temp_customer = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_{table}(
                    CUSTOMER_ID,
                    CUSTOMER_FST_NM,
                    CUSTOMER_MID_NM,
                    CUSTOMER_LST_NM,
                    CUSTOMER_ADDR
                ) SELECT
                    ID, 
                    CUSTOMER_FIRST_NAME,
                    CUSTOMER_MIDDLE_NAME,
                    CUSTOMER_LAST_NAME,
                    CUSTOMER_ADDRESS 
                FROM RETAIL_DWH.STAGE.STG_CUSTOMER;"""
    sqls.load_table(load_temp_customer, table, 'temp')


    #load dimension table customer
    table = "D_RETAIL_CUSTOMER_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_CUSTOMER"
    update_tgt_customer = f""" UPDATE RETAIL_DWH.TARGET.{table} AS T1
                                       SET T1.CUSTOMER_FST_NM = T2.CUSTOMER_FST_NM ,
                                       T1.CUSTOMER_MID_NM = T2.CUSTOMER_MID_NM, 
                                       T1.CUSTOMER_LST_NM = T2.CUSTOMER_LST_NM,
                                       T1.CUSTOMER_ADDR = T2.CUSTOMER_ADDR , 
                                       ROW_UPDT_TMS = LOCALTIMESTAMP 
                                       FROM {temp_table} AS T2
                                       WHERE T1.CUSTOMER_ID = T2.CUSTOMER_ID;
               """

    sqls.load_table(update_tgt_customer, table, 'target')
    load_tgt_customer = f"""INSERT INTO RETAIL_DWH.TARGET.{table}(
                CUSTOMER_ID,
                CUSTOMER_FST_NM,
                CUSTOMER_MID_NM,
                CUSTOMER_LST_NM,
                CUSTOMER_ADDR,
                OPEN_CLOSE_CD,
                ROW_INSRT_TMS,
                ROW_UPDT_TMS  
            ) SELECT
                CUSTOMER_ID,
                CUSTOMER_FST_NM,
                CUSTOMER_MID_NM,
                CUSTOMER_LST_NM,
                CUSTOMER_ADDR,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP
            FROM RETAIL_DWH.TEMP.TMP_CUSTOMER
WHERE CUSTOMER_ID NOT IN (SELECT DISTINCT CUSTOMER_ID from RETAIL_DWH.TARGET.D_RETAIL_CUSTOMER_T )"""
    sqls.load_table(load_tgt_customer, table, 'target')


    print("Loaded to Customer " + str(datetime.datetime.now()))
    Logger.log_message("Loaded to Customer " + str(datetime.datetime.now()))
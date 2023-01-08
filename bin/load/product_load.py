from lib import Variables
import sqls
import datetime
from lib.Logger import Logger

def product_load():

    print("Loading to Product " + str(datetime.datetime.now()))
    Logger.log_message("Loading to Product " + str(datetime.datetime.now()))


    #load temp table category from category stage table
    table = "CATEGORY"
    sqls.truncate_table("RETAIL_DWH", "TEMP", "TMP", table)
    load_temp_category = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_{table}(
                    CTGRY_ID,
                    CTGRY_DESC
                ) SELECT
                    ID, 
                    CATEGORY_DESC
                    FROM RETAIL_DWH.STAGE.STG_CATEGORY"""
    sqls.load_table(load_temp_category, table, 'temp')

    #load dimension table category
    table = "D_RETAIL_CTGRY_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_CATEGORY"
    update_tgt_category = f""" UPDATE RETAIL_DWH.TARGET.{table} AS T1
                                          SET T1.CTGRY_DESC = T2.CTGRY_DESC,  
                                          ROW_UPDT_TMS = LOCALTIMESTAMP 
                                          FROM {temp_table} AS T2
                                          WHERE T1.CTGRY_ID = T2.CTGRY_ID;
                  """
    sqls.load_table(update_tgt_category, table, 'target')



    load_tgt_category = f"""INSERT INTO RETAIL_DWH.TARGET.{table}(
                CTGRY_ID,
                CTGRY_DESC,
                OPEN_CLOSE_CD,
                ROW_INSRT_TMS,
                ROW_UPDT_TMS
            ) SELECT
                CTGRY_ID,
                CTGRY_DESC,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP
            FROM RETAIL_DWH.TEMP.TMP_CATEGORY
WHERE CTGRY_ID NOT IN (SELECT DISTINCT CTGRY_ID from RETAIL_DWH.TARGET.D_RETAIL_CTGRY_T )"""
    sqls.load_table(load_tgt_category, table, 'target')

    #load temp table subcategory from subcategory stage table
    table = "SUBCATEGORY"
    sqls.truncate_table("RETAIL_DWH", "TEMP", "TMP", table)
    load_temp_subcategory = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_{table}(
                    SUB_CTGRY_ID,
                CTGRY_KY,
                SUB_CTGRY_DESC
            ) SELECT 
                ID,
                CTGRY.CTGRY_KY,
                SUBCATEGORY_DESC
            FROM RETAIL_DWH.STAGE.STG_SUBCATEGORY SUBCTGRY
            LEFT OUTER JOIN RETAIL_DWH.TARGET.D_RETAIL_CTGRY_T CTGRY
            ON SUBCTGRY.CATEGORY_ID=CTGRY.CTGRY_ID;"""
    sqls.load_table(load_temp_subcategory, table, 'temp')


    #load dimension table subcategory
    table = "D_RETAIL_SUB_CTGRY_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_SUBCATEGORY"
    update_tgt_subcategory = f""" UPDATE RETAIL_DWH.TARGET.{table} AS T1
                                      SET T1.CTGRY_KY = T2.CTGRY_KY ,
                                      T1.SUB_CTGRY_DESC = T2.SUB_CTGRY_DESC,  
                                      ROW_UPDT_TMS = LOCALTIMESTAMP 
                                      FROM {temp_table} AS T2
                                      WHERE T1.SUB_CTGRY_ID = T2.SUB_CTGRY_ID;
              """
    sqls.load_table(update_tgt_subcategory, table, 'target')

    load_tgt_subcategory = f"""INSERT INTO RETAIL_DWH.TARGET.{table}(
                SUB_CTGRY_ID,
                CTGRY_KY,
                SUB_CTGRY_DESC,
                OPEN_CLOSE_CD,
                ROW_INSRT_TMS,
                ROW_UPDT_TMS
            ) SELECT 
                SUB_CTGRY_ID,
                CTGRY_KY,
                SUB_CTGRY_DESC,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP
            FROM RETAIL_DWH.TEMP.TMP_SUBCATEGORY
WHERE SUB_CTGRY_ID NOT IN (SELECT DISTINCT SUB_CTGRY_ID from RETAIL_DWH.TARGET.D_RETAIL_SUB_CTGRY_T )"""
    sqls.load_table(load_tgt_subcategory, table, 'target')

    #load temp table product from product stage table
    table = "PRODUCT"
    sqls.truncate_table("RETAIL_DWH", "TEMP", "TMP", table)
    load_temp_product = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_{table}(
                    PDT_ID,
                    SUB_CTGRY_KY,
                    CTGRY_KY,
                    PDT_DESC
                ) SELECT 
                    ID,
                    SUBCTGRY.SUB_CTGRY_KY,
                    SUBCTGRY.CTGRY_KY,
                    PRODUCT_DESC
                    FROM RETAIL_DWH.STAGE.STG_PRODUCT PRDT
                    LEFT OUTER JOIN RETAIL_DWH.TARGET.D_RETAIL_SUB_CTGRY_T SUBCTGRY
                    ON SUBCTGRY.SUB_CTGRY_ID=PRDT.SUBCATEGORY_ID;"""
    sqls.load_table(load_temp_product, table, 'temp')





    #load dimension table product
    table = "D_RETAIL_PDT_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_PRODUCT"
    update_tgt_product = f""" UPDATE RETAIL_DWH.TARGET.{table} AS T1
                                          SET T1.CTGRY_KY = T2.CTGRY_KY ,
                                          T1.SUB_CTGRY_KY = T2.SUB_CTGRY_KY,
                                          T1.PDT_DESC = T2.PDT_DESC,  
                                          ROW_UPDT_TMS = LOCALTIMESTAMP 
                                          FROM {temp_table} AS T2
                                          WHERE T1.PDT_ID = T2.PDT_ID;
                  """
    sqls.load_table(update_tgt_product, table, 'target')
    load_tgt_product = f"""INSERT INTO RETAIL_DWH.TARGET.{table}(
                PDT_ID,
            SUB_CTGRY_KY,
            CTGRY_KY,
            PDT_DESC,
            ACTV_FLG,
            PRICE,
            OPEN_CLOSE_CD,
            ROW_INSRT_TMS,
            ROW_UPDT_TMS
            ) SELECT
                PDT_ID,
                SUB_CTGRY_KY,
                CTGRY_KY,
                PDT_DESC,
                1,
                null,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP
            FROM RETAIL_DWH.TEMP.TMP_PRODUCT
 WHERE PDT_ID NOT IN (SELECT DISTINCT PDT_ID from RETAIL_DWH.TARGET.D_RETAIL_PDT_T )"""
    sqls.load_table(load_tgt_product, table, 'target')

    print("Loaded to Product " + str(datetime.datetime.now()))
    Logger.log_message("Loaded to Product " + str(datetime.datetime.now()))


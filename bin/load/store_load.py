from lib import Variables
import sqls
import datetime
from lib.Logger import Logger



v= Variables.Variables()
def store_load():


    print("Loading to Store " + str(datetime.datetime.now()))
    Logger.log_message("Loading to Store " + str(datetime.datetime.now()))

    #load temp table country from country stage table
    table = "COUNTRY"
    sqls.truncate_table("RETAIL_DWH", "TEMP", "TMP", table)
    load_temp_country = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_COUNTRY(
                    CNTRY_ID, 
                    CNTRY_DESC
                ) SELECT
                    ID,
                    COUNTRY_DESC
                    FROM RETAIL_DWH.STAGE.STG_COUNTRY; """
    sqls.load_table(load_temp_country, table, 'temp')

    #load dimension table country
    table = "D_RETAIL_CNTRY_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_COUNTRY"
    update_tgt_country = sqls.return_update_query('CNTRY',temp_table)
    sqls.load_table(update_tgt_country, table , 'target')
    load_tgt_country = f"""INSERT INTO RETAIL_DWH.TARGET.D_RETAIL_CNTRY_T(
                CNTRY_ID,
                CNTRY_DESC,
                OPEN_CLOSE_CD,
                ROW_INSRT_TMS,
                ROW_UPDT_TMS
            ) SELECT 
                CNTRY_ID,
                CNTRY_DESC,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP 
            FROM RETAIL_DWH.TEMP.TMP_COUNTRY
            WHERE CNTRY_ID NOT IN (SELECT DISTINCT CNTRY_ID from RETAIL_DWH.TARGET.D_RETAIL_CNTRY_T )"""
    sqls.load_table(load_tgt_country, table, 'target')


    #load temp table region from region stage table
    table = "REGION"

    sqls.truncate_table("RETAIL_DWH", "TEMP", "TMP", table)
    print("Sucessfully Truncated TEMP.REGION ")
    load_temp_region = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_REGION(
                    RGN_ID,
                    CNTRY_KY,
                    RGN_DESC
                ) SELECT 
                    ID,
                    CNTRY.CNTRY_KY,
                    REGION_DESC FROM RETAIL_DWH.STAGE.STG_REGION REGN
                    LEFT OUTER JOIN RETAIL_DWH.TARGET.D_RETAIL_CNTRY_T CNTRY
                     ON REGN.COUNTRY_ID = CNTRY.CNTRY_ID ;"""
    sqls.load_table(load_temp_region, table, 'temp')


    #load dimension table region
    table = "D_RETAIL_RGN_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_REGION"
    update_tgt_region = sqls.return_update_query('RGN', temp_table)
    sqls.load_table(update_tgt_region, table, 'target')
    load_tgt_region = f"""INSERT INTO RETAIL_DWH.TARGET.D_RETAIL_RGN_T(
                RGN_ID,
                CNTRY_KY,
                RGN_DESC,
                OPEN_CLOSE_CD,
                ROW_INSRT_TMS,
                ROW_UPDT_TMS
            ) SELECT
                RGN_ID,
                CNTRY_KY,
                RGN_DESC,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP
            FROM RETAIL_DWH.TEMP.TMP_REGION
WHERE RGN_ID NOT IN (SELECT DISTINCT RGN_ID from RETAIL_DWH.TARGET.D_RETAIL_RGN_T )"""
    sqls.load_table(load_tgt_region, table, 'target')


    #load temp table store from store stage table
    table = "STORE"
    sqls.truncate_table("RETAIL_DWH","TEMP","TMP",table)
    load_temp_store = f"""INSERT INTO RETAIL_DWH.TEMP.TMP_STORE(
                    STORE_ID,
                    RGN_KY,
                    CNTRY_KY,
                    STORE_DESC
                ) SELECT 
                    ID,
                    REGN.RGN_KY,
                    REGN.CNTRY_KY,
                    STR.STORE_DESC FROM RETAIL_DWH.STAGE.STG_STORE STR
                    LEFT OUTER JOIN RETAIL_DWH.TARGET.D_RETAIL_RGN_T REGN  on REGN.RGN_ID=STR.REGION_ID"""
    sqls.load_table(load_temp_store, table, 'temp')




    #load dimension table store
    table = "D_RETAIL_LOCN_T"
    temp_table = "RETAIL_DWH.TEMP.TMP_STORE"
    update_tgt_store = f""" UPDATE RETAIL_DWH.TARGET.D_RETAIL_LOCN_T AS T1
                                    SET T1.RGN_KY = T2.RGN_KY ,
                                    T1.CNTRY_KY = T2.CNTRY_KY, 
                                    T1.LOCN_DESC = T2.STORE_DESC, 
                                    ROW_UPDT_TMS = LOCALTIMESTAMP 
                                    FROM {temp_table} AS T2
                                    WHERE T1.LOCN_ID = T2.STORE_ID;
            """

    sqls.load_table(update_tgt_store, table, 'target')

    load_tgt_store = f"""INSERT INTO RETAIL_DWH.TARGET.D_RETAIL_LOCN_T(
                LOCN_ID,
            RGN_KY,
            CNTRY_KY,
            LOCN_DESC,
            LAST_OPEN_TMS,
            ACTV_FLG,
            OPEN_CLOSE_CD,
            ROW_INSRT_TMS,
            ROW_UPDT_TMS    
            ) SELECT
                STORE_ID,
                RGN_KY,
                CNTRY_KY,
                STORE_DESC,
                LOCALTIMESTAMP,
                1,
                1,
                LOCALTIMESTAMP,
                LOCALTIMESTAMP
            FROM RETAIL_DWH.TEMP.TMP_STORE
            WHERE STORE_ID NOT IN (SELECT DISTINCT LOCN_ID from RETAIL_DWH.TARGET.D_RETAIL_LOCN_T )"""
    sqls.load_table(load_tgt_store, table, 'target')

    print("Loaded to Store " + str(datetime.datetime.now()))
    Logger.log_message("Loaded to Store " + str(datetime.datetime.now()))


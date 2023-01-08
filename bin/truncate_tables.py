import sqls
from lib.Variables import Variables

v= Variables()
def truncate():
    database = v.get("DATABASE")

    tables =  {"STAGE" : ['COUNTRY','REGION','STORE','CATEGORY','SUBCATEGORY','PRODUCT','CUSTOMER','SALES'],
                "TEMP": ['COUNTRY','REGION','STORE','CATEGORY','SUBCATEGORY','PRODUCT','CUSTOMER','SALES'], #,'YEAR','HALFYEAR','QUARTER','MONTH','DAY','HOUR','MIN']}
                "TARGET_D_RETAIL": ['CNTRY_T','RGN_T','LOCN_T','CTGRY_T','SUB_CTGRY_T','PDT_T','CUSTOMER_T', 'TIME_YEAR_T','TIME_HALF_YEAR_T','TIME_QUARTER_T','TIME_MONTH_T','TIME_DAY_T','TIME_HOUR_T','TIME_MIN_T','TIME_SEC_T'],
                "TARGET_F_RETAIL": ['SLS_T','AGG_SLS_PLC_MONTH_T']}
        
    for key, values in tables.items():
        if key == "STAGE":
            prefix = "STG"
            schema = key
        elif key == "TEMP":
            prefix = "TMP"
            schema = key
        elif key == "TARGET_D_RETAIL":
            prefix = "D_RETAIL"
            schema = "TARGET"
        else:
            prefix = "F_RETAIL"
            schema = "TARGET"
        for i in values:
            sqls.truncate_table(database,schema,prefix,i)
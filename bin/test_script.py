from lib import connect


def read_country_table():
    read_country_query = f"""
                    SELECT * FROM RETAIL_DWH.SOURCE.COUNTRY
            """
    connect.execute_query(read_country_query)


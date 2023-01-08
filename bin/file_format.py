from lib import connect
from lib.Variables import Variables
v = Variables()

def create_file_format():
    format = v.get("FILE_FORMAT")

    try:
        format = f""" 
        create or replace file format {format}
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
        """
        connect.execute_query(format)
        print("sucessfully created a file format")
        
    except Exception as e:
        print("Failed to create File Format")
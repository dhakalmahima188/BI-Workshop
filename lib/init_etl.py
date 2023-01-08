import sys
sys.path.append('../')

from lib.Logger import Logger
from lib.Variables import Variables
from bin import test_script
from bin.load import sales_load, customer_load, store_load, aggregate_sales_load,  product_load
from bin.extraction import store_extract, customer_extract, product_extract, sales_extract

v=Variables()
Logger.log_initialize()
Logger.log_message("Nightly Batch Started")
#truncate_tables.truncate()
#file_format.create_file_format()

Logger.log_message( "Starting the Extraction Process")
test_script.read_country_table()
#Extraction Block
# product_extract.product_extract()
# store_extract.store_extract()
# customer_extract.customer_extract()
# sales_extract.sales_extract()
# Logger.log_message("Extraction Process Completed")
#
# Logger.log_message(  "Starting the Loading Process")
# #Load_Block
# product_load.product_load()
# store_load.store_load()
# customer_load.customer_load()
# sales_load.sales_load()
# aggregate_sales_load.agg_sales_load()
# Logger.log_message( "Load Process Completed")

Logger.close()
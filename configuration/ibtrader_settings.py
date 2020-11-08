import os
import logging, sys


BUCKET_NAME  = "tradeable"

# NUMERO DE BARRAS ADJACENTES A LA ACTUAL COMO PICOS TANTO PARA PRECIOS COMO PARA INDICADORES 
# IMPORTANTE , O 2 O 1 AHORA 
PEAKS_VALLEYS_PRICE_ = "PRICE"
PEAKS_VALLEYS_INDICATORS_ = "INDICATOR"


SETTINGS_FILE_FORMAT_DATE = "YYYYMMDD"
SETTINGS_FILE_FORMAT_TIME ="HHMM"

SETTINGS_FILE_MONTH_PATTERN = "MONTH"
SETTINGS_FILE_DAY_PATTERN = "DAY"
SETTINGS_FILE_WEEK_PATTERN = "WEEK"

SETTINGS_PATH_STOCK_DATA_OUTPUT = "./output"

SETTINGS_PATH_STOCK_DATA = "./data"
SETTINGS_PATH_STOCK_DATA_MONTH =   SETTINGS_PATH_STOCK_DATA   + "/"   + SETTINGS_FILE_MONTH_PATTERN
SETTINGS_PATH_STOCK_DATA_DAY   =   SETTINGS_PATH_STOCK_DATA   + "/"   + SETTINGS_FILE_DAY_PATTERN
SETTINGS_PATH_STOCK_DATA_WEEK  =   SETTINGS_PATH_STOCK_DATA   + "/"   + SETTINGS_FILE_WEEK_PATTERN


SETTINGS_REALPATH_STOCK_DATA       =  os.path.realpath(SETTINGS_PATH_STOCK_DATA)
SETTINGS_REALPATH_STOCK_DATA_MONTH =  SETTINGS_REALPATH_STOCK_DATA + "/" +  SETTINGS_FILE_MONTH_PATTERN  + "/"
SETTINGS_REALPATH_STOCK_DATA_DAY   =  SETTINGS_REALPATH_STOCK_DATA + "/" +  SETTINGS_FILE_DAY_PATTERN + "/"
SETTINGS_REALPATH_STOCK_DATA_WEEK  =  SETTINGS_REALPATH_STOCK_DATA + "/" +  SETTINGS_FILE_WEEK_PATTERN + "/"

SETTINGS_REALPATH_STOCK_DATA_OUTPUT       =  os.path.realpath(SETTINGS_PATH_STOCK_DATA_OUTPUT)


# Create target Directory if don't exist
if not os.path.exists(SETTINGS_PATH_STOCK_DATA_OUTPUT):
    os.mkdir(SETTINGS_PATH_STOCK_DATA_OUTPUT)
    print("Directory " , SETTINGS_PATH_STOCK_DATA_OUTPUT ,  " Created ")
else:    
    logging.debug("Directory " , SETTINGS_PATH_STOCK_DATA_OUTPUT ,  " already exists")

# Create target Directory if don't exist
if not os.path.exists(SETTINGS_PATH_STOCK_DATA):
    os.mkdir(SETTINGS_PATH_STOCK_DATA)
    print("Directory " , SETTINGS_PATH_STOCK_DATA ,  " Created ")
else:    
    logging.debug("Directory " , SETTINGS_PATH_STOCK_DATA ,  " already exists")

if not os.path.exists(SETTINGS_PATH_STOCK_DATA_MONTH):
    os.mkdir(SETTINGS_PATH_STOCK_DATA_MONTH)
    print("Directory " , SETTINGS_PATH_STOCK_DATA_MONTH ,  " Created ")
else:    
    logging.debug("Directory " , SETTINGS_PATH_STOCK_DATA_MONTH ,  " already exists")

if not os.path.exists(SETTINGS_PATH_STOCK_DATA_DAY):
    os.mkdir(SETTINGS_PATH_STOCK_DATA_DAY)
    print("Directory " , SETTINGS_PATH_STOCK_DATA_DAY ,  " Created ")
else:    
    logging.debug("Directory " , SETTINGS_PATH_STOCK_DATA_DAY ,  " already exists")

if not os.path.exists(SETTINGS_PATH_STOCK_DATA_WEEK):
    os.mkdir(SETTINGS_PATH_STOCK_DATA_WEEK)
    print("Directory " , SETTINGS_PATH_STOCK_DATA_WEEK ,  " Created ")
else:    
    logging.debug("Directory " , SETTINGS_PATH_STOCK_DATA_WEEK ,  " already exists")   







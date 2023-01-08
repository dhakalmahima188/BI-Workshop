import datetime


def year_data_generate(begin_date, end_date):
    #id = 0
    begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    begin_year = begin.year
    end_year = end.year
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_YEAR (YEAR_KY, YEAR_START_DATE, YEAR_END_DATE) VALUES')
    for year in range(begin_year, end_year):
        #id = id + 1
        year_ky = str(year)
        year_start_date = str(year) + '-01-01'
        year_end_date = str(int(year) + 1 ) + '-12-30'
        print('(',year_ky,',',"'"+year_start_date+"'",',',"'"+year_end_date+"'",')',',')

def half_year_data_generate(begin_date, end_date):
    #id = 0
    begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    begin_year = begin.year
    end_year = end.year
    
    print(' INSERT INTO RETAIL_DWH.TEMP.TMP_HALFYEAR (HALF_YEAR_KY, YEAR_KY, HALF_YEAR_START_DATE, HALF_YEAR_END_DATE) VALUES')
    for year in range(begin_year, end_year):
        year_ky = str(year)
        start_month = 1
        end_month = 6   
        for i in range(2): 
            #id = id + 1
            half_year_ky = str(year) + str(i+1).zfill(2)
            half_year_start_date = str(year) + '-' + str(start_month).zfill(2) + '-01'
            half_year_end_date = str(year) + '-' +  str(end_month).zfill(2) + '-30'
            start_month = start_month + 6
            end_month = end_month + 6
            print('(',half_year_ky,',',year_ky,',',"'"+half_year_start_date+"'",',',"'"+half_year_end_date+"'",')',',')    

def quarter_year_data_generator(begin_date, end_date):
    begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    begin_year = begin.year
    end_year = end.year
    #id = 0
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_QUARTER (QUARTER_KY, YEAR_KY, HALF_YEAR_KY, QUARTER_START_DATE, QUARTER_END_DATE) VALUES')
    for year in range(begin_year, end_year):
        year_ky = str(year)
        start_month = 1
        end_month = 3
        for i in range(4):
            #id = id + 1
            quarter_ky = str(year) + str(i+1).zfill(2)
            if i <= 1 :
                half_year_ky = str(year) + '01'
            else:
                half_year_ky = str(year) + '02'

            quarter_start_date = str(year) + '-' + str(start_month).zfill(2) + '-01'
            quarter_end_date = str(year) + '-' + str(end_month).zfill(2) + '-30'
            start_month = start_month + 3
            end_month = end_month + 3
            print('(',quarter_ky,',',year_ky,',',half_year_ky,',',"'"+quarter_start_date+"'",',',"'"+quarter_end_date+"'",')',',')

def month_data_generator(begin_date, end_date):
    begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    begin_year = begin.year
    end_year = end.year
    #id = 0
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_MONTH (MONTH_KY, QUARTER_KY, YEAR_KY, HALF_YEAR_KY, MONTH_START_DATE, MONTH_END_DATE) VALUES')
    for year in range(begin_year, end_year):
        year_ky = str(year)
        for i in range(12):
            #id = id + 1
            month_ky = str(year) + str(i+1).zfill(2)
            if i <= 5:
                half_year_ky = str(year) + '01'
                if i <= 2 :
                    quarter_ky = str(year) + '01'
                else:
                    quarter_ky = str(year) + '02'
            else:
                half_year_ky = str(year) + '02'
                if i <= 8:
                    quarter_ky = str(year) + '03'
                else:
                    quarter_ky = str(year) + '04'
            month_start_date = str(year) + '-' + str(i+1).zfill(2) + '-01'
            if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
                month_end_date = str(year) + '-' + str(i+1).zfill(2) + '-31'
            elif i == 1:
                month_end_date = str(year) + '-' + str(i+1).zfill(2) + '-28'
            else:
                month_end_date = str(year) + '-' + str(i+1).zfill(2) + '-30'
            print('(',month_ky,',',quarter_ky,',',year_ky,',',half_year_ky,',',"'"+month_start_date+"'",',',"'"+month_end_date+"'",')',',')

def day_data_generator(begin_date, end_date):
    begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    begin_year = begin.year
    end_year = end.year
    # id = 0
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_DAY(DAY_KY, MONTH_KY, QUARTER_KY, YEAR_KY, HALF_YEAR_KY, DAY_START_TIME, DAY_END_TIME) VALUES')
    for year in range(begin_year, end_year):
        year_ky = str(year)
        # day_start_time = '07:00:00'
        # day_end_time = '22:00:00'
        for i in range(12):
            month_ky = str(year) + str(i+1).zfill(2)
            if i <= 2:
                quarter_ky = str(year) + '01'
                half_year_ky = str(year) + '01'
            elif 3 <= i <= 5 :
                quarter_ky = str(year) + '02'
                half_year_ky = str(year) + '01'
            elif 6 <= i <= 8  :
                quarter_ky = str(year) + '03'
                half_year_ky = str(year) + '02'
            else:
                quarter_ky = str(year) + '04'
                half_year_ky = str(year) + '02'

            if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
                for day in range(31):
                    day_ky = str(year) + str(i+1).zfill(2) + str(day+1).zfill(2)
                    day_start_time = str(year) + '-' + str(i+1).zfill(2) + '-' + str(day+1).zfill(2) + ' 07:00:00'
                    day_end_time = str(year) + '-' + str(i+1).zfill(2) + '-' + str(day+1).zfill(2) + ' 21:00:00'
                    print('(',day_ky,',',month_ky,',',quarter_ky,',',year_ky,',',half_year_ky,',',"'"+day_start_time+"'",',',"'"+day_end_time+"'",')',',')
            elif i == 1:
                for day in range(28):
                    day_ky = str(year) + str(i+1).zfill(2) + str(day+1).zfill(2)
                    print('(',day_ky,',',month_ky,',',quarter_ky,',',year_ky,',',half_year_ky,',',"'"+day_start_time+"'",',',"'"+day_end_time+"'",')',',')
            else:   
                for day in range(30):
                    day_ky = str(year) + str(i+1).zfill(2) + str(day+1).zfill(2)
                    print('(',day_ky,',',month_ky,',',quarter_ky,',',year_ky,',',half_year_ky,',',"'"+day_start_time+"'",',',"'"+day_end_time+"'",')',',')

def hour_data_generator():
    id = 0
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_HOUR (HOUR_KY) VALUES')
    for i in range(24):
        id = id + 1
        hour_ky = i 
        if i == 23:
            print('(',hour_ky,')',';')
        else:
            print('(',hour_ky,')',',')

def min_data_generator():
    #id  = 0 
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_MIN(MIN_KY, HOUR_KY) VALUES')
    for i in range(24):
        hour_ky = i
        for j in range(60):
            #id = id + 1
            min_ky = str(i) + str(j).zfill(2)
            print('(',min_ky,',',hour_ky,')',',')

def sec_data_generator():
    #id  = 0 
    print('INSERT INTO RETAIL_DWH.TEMP.TMP_SEC(SEC_KY, HOUR_KY) VALUES')
    for i in range(24):
        hour_ky = i
        for j in range(60):
            #id = id + 1
            min_ky = str(i) + str(j).zfill(2)
            for k in range(60):
                sec_ky = str(i) + str(j).zfill(2) + str(k).zfill(2)
                print('(',sec_ky,',',min_ky,',',hour_ky,')',',')

#year_data_generate('2020-08-02', '2022-03-02')
#half_year_data_generate('2020-08-02', '2022-03-02')
#quarter_year_data_generator('2020-08-02', '2022-03-02')
#month_data_generator('2020-08-02', '2022-03-02')
#day_data_generator('2020-08-02', '2022-03-02')
#hour_data_generator()
#min_data_generator()
#sec_data_generator()
import requests,sqlite3

def get_pm25_db(sort=False):
    columns,values = None, None
    try:
        conn = sqlite3.connect('./pm25.db')
        cursor = conn.cursor()

        columns = ['站點名稱','縣市','PM25','更新時間']
        #values = list(cursor.execute('select site,county,pm25,datacreationdate from data'))
        
        sqlstr= '''
            SELECT site, county, pm25, datacreationdate
            FROM data
            WHERE (site, datacreationdate) IN (
                SELECT site, MAX(datacreationdate)
                FROM data
                GROUP BY site
            )'''
        
        values = list(cursor.execute(sqlstr))
        

        if sort:
            values = sorted(values,key=lambda x:x[2],reverse=True)

    except Exception as e:
        print(e)
    return columns, values


def get_pm25(sort=False):
    columns,values=None,None
    try:
        url = 'https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
        resp = requests.get(url)
        datas = resp.json()['records']
        columns = list(datas[0].keys())
        values=[]
        for data in datas:
            data=list(data.values())
            try:
                data[2]=eval(data[2])
                values.append(data)
            except Exception as e:
                print(e)
        if sort:
            values=sorted(values,key=lambda x:x[2],reverse=True)
        
        print(values)
    except Exception as e:
        print(e)

    return columns,values

if __name__ =='__main__':
    print(get_pm25_db())

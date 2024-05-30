import requests

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
    print(get_pm25())

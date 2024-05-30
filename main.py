from flask import Flask,render_template,request
from datetime import datetime
from pm25 import get_pm25

app = Flask(__name__)

@app.route('/pm25',methods=['GET','POST'])
def pm25():
    if request.method == 'GET':
        columns,values = get_pm25()
    if request.method == 'POST':
        if request.form.get('sort'):
            columns,values = get_pm25(True)
        else:
            columns,values = get_pm25()
    
    return render_template('pm25.html',**locals())


@app.route('/')
def index():
    date=get_date()
    print(date)
    return render_template('index.html',date=date)

@app.route('/date')
def get_date():
    return datetime.now().strftime('%Y-%m-%d %h:%M:%S')

@app.route('/stock')
def stock():
    stocks=[
        {'分類':'日經指數','指數':'22,920.30'},
        {'分類':'香港指數','指數':'32,220.30'},
        {'分類':'泰國指數','指數':'92,923.30'},
        {'分類':'菲律賓指數','指數':'66,921.30'}
        ]
    
    return render_template('stock.html',stocks=stocks,datetime=get_date())


@app.route('/book')
@app.route('/book/<int:id>')
def get_book(id=None):
    try:
        books = {1:"html",2:"css",3:"javascript"}
        if id is not None:
            return books[id]
        else:
            return books
    except Exception as e:
        return '查詢錯誤，請重新輸入'



if __name__== '__main__':
    app.run(debug=True)
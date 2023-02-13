# app.py
from flask import Flask, render_template, request
import requests
#Flask 객체 인스턴스 생성
app = Flask(__name__)
from bs4 import BeautifulSoup
import steamAPI



def get_search_count(keyword):
    url = "https://www.google.com/search?q={}".format(keyword)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'lxml')
    number = soup.select_one('#result-stats').text
    # print(number) # 검색결과 약 7,320,000개 (0.47초) 
    number = number[number.find('약')+2:number.rfind('개')] # 7,320,000
    number = int(number.replace(',','')) # 7320000
    return {'keyword':keyword, 'number':number}


@app.route('/', methods=['GET','POST']) # 접속하는 url
def index():
        # 웹 페이지에서 name="xxx"인 요소의 value 가져오기
    print(request.form.get('keyword1'))
    print(request.form.get('keyword2'))
    keyword1 = request.form.get('keyword1')
    keyword2 = request.form.get('keyword2')

    # 위의 값이 있을 때만 크롤링 검색 결과 반환
    if keyword1 is not None and keyword2 is not None:
        data = {
            keyword1 : get_search_count(keyword1).get('number'),
            keyword2 : get_search_count(keyword2).get('number'), 
            'level' : 60,
            'point' : 360,
            'exp' : 450500,
            }
        return render_template('index.html',data=data)
    else:
        data = {'level': 60, 'point': 360, 'exp': 45000}
        return render_template('index.html', data=data)
    # if request.method == "POST":
    #     # user=request.form['user'] # 전달받은 name이 user인 데이터
    #     print(request.form.get('user')) # 안전하게 가져오려면 get
    #     user = request.form.get('user')
    #     data = {'level': 60, 'point': 360, 'exp': 45000}
    #     return render_template('index.html', user=user, data=data)
    # elif request.method == "GET":
    #     user = "반원"
    #     data = {'level': 60, 'point': 360, 'exp': 45000}
    #     return render_template('index.html', user=user, data=data)

if __name__=="__main__":
  app.run(debug=True)
#   print(get_search_count("나루토"))
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
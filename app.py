from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    # 在此处实现搜索逻辑
    results = ['a', 'b', 'c']  # 示例数据，您需要使用实际搜索结果替换此列表
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

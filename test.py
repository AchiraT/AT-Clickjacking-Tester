# from flask import Flask, request, render_template
# from check_clickjacking import check_clickjacking 

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')  # HTML form to input URL

# @app.route('/scan', methods=['POST'])
# def scan():
#     url = request.form['url']
#     result = check_clickjacking(url)
#     return render_template('result.html', result=result)  # Display results

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template
from check_clickjacking import check_clickjacking 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    html_content, result = check_clickjacking(url)
    
    with open('temp.html', 'w') as f:
        f.write(html_content)
    
    import webbrowser
    webbrowser.open('temp.html')
    
    return render_template('result.html', result=result)  

if __name__ == '__main__':
    app.run(debug=True)

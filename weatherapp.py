from flask import Flask, render_template, request
from weatherohad2202 import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    city_name = None
    id1 = None
    if request.method == 'POST':
        city_name = request.form['cityName']
        data, id1 = get_weather(city_name)
    return render_template('index.html', data=data, city_name=city_name, id1=id1)

if __name__ == '__main__':
    app.run(debug=True)

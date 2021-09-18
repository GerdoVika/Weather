from flask import Flask

app = Flask(__name__)

@app.route('/weather')
def get_weather_history():
    pass

if __name__ == '__main__':
    app.run()




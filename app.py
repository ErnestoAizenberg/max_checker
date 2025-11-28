from flask import Flask, render_template

def create_app() -> Flask:
    app = Flask(__name__)
    
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

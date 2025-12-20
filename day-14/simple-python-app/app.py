from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!..... This page is came from sample python app and got deployed by AWS Devops'

if __name__ == '__main__':
    app.run()



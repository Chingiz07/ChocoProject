from flask import Flask
import down_att

app = Flask(__name__)

@app.route('/')
def main():
    name = down_att.names
    return '<br>'.join(name)

if __name__ == '__main__':
    app.run()



# import os

# cmd = 'unoconv -f pdf --output=file-convert/outputFile file/2.docx'

# os.system(cmd)


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()

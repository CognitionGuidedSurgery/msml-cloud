__author__ = 'weigla'

from msmlcloud.web import app

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

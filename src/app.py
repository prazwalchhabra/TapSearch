import sys
import logging
from flask import Flask
from flask import jsonify, request, render_template
from TapSearch import tapsearch

# import config

# Initialise Flask application with cross origin support
app = Flask(__name__, template_folder='static')
# cors = CORS(app)

@app.route('/clear/', methods=['GET','POST'])
def clear_index():
    if request.method == 'GET':
        return render_template('delete_index.html')
    else:
        try:
            tapsearch.clear_index()
            return render_template('home.html', message="Message : Index cleared")
        except Exception as err:
            return render_template('home.html', message="Error : {}".format(str(err)))


@app.route('/index/', methods=['GET','POST'])
@app.route('/insert/', methods=['GET','POST'])
def insert_documents():
    if request.method == 'GET':
        return render_template('insert_index.html')
    else:
        try:
            text = request.form['index']
            tapsearch.insert_index(text)
            return render_template('home.html', message="Message : Documents Inserted")
        except Exception as err:
            return render_template('home.html', message="Error : {}".format(str(err)))

@app.route('/search/', methods=['GET','POST'])
def search_index():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        try:
            query = request.form['query']
            documents = tapsearch.search_index(query)
            return render_template('display_search.html', documents=documents)
        except Exception as err:
            return render_template('home.html', message="Error : {}".format(str(err)))

@app.route('/')
def landing_page():
    return render_template('home.html', message="")

# return redirect(url_for('gallery', gallery_name=gallery_name))

if __name__ == "__main__":
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    app.run()
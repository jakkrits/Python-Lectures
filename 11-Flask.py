from flask import Flask, request, make_response
import json

app = Flask(__name__)
@app.route('/')
# def hello():
#    return "Hello bitches"
def root():
    return "Request Path is: " + request.path

@app.route('/test')
def test():
    return "Request Path is: " + request.path

@app.route('/data', methods=['GET'])
def show_data():
    return "Show Data Here:"

@app.route('/data', methods=['POST'])
def handle_data():
    return "Handle POST request"

@app.route('/user/<username>')
def greet_user(username):
    return "Hi คุณ " + username

@app.route('/json')
def get_image():
    # create response
    response = make_response(json.dumps({'foo': 'bar'}))
    # set correct mimetype
    response.mimetype = 'application/json'
    return response

@app.route('/error')
def error_page():
    response = make_response('Error Page')
    response.status_code = 404
    return response

@app.route('/posts')
@app.route('/posts/page/<int:page_nb>')
def show_posts(page_nb = 1):
    first_msg = 1 + 50 * (page_nb - 1)
    last_msg = first_msg + 49
    return "Messages from {} to {}".format(first_msg, last_msg)

if __name__ == '__main__':
    app.run(debug = True)

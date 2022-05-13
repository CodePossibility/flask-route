from flask import Flask, request, make_response
from flask.views import MethodView

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST'])
def users():
    
    if request.method == 'GET':
        resp_dict = dict()
        if 'FirstName' in request.args:
            resp_dict['FirstName'] = request.args.get('FirstName')

        if 'LastName' in request.args:
            resp_dict['LastName'] = request.args.get('LastName')

        return resp_dict
    elif request.method == 'POST':
        user_json = request.json

        content_type = request.headers.get('Content-Type', None)

        resp_dict = dict()

        resp_dict['FirstName'] = user_json['FirstName']
        resp_dict['LastName'] = user_json['LastName']
        resp_dict['ContentType'] = content_type

        resp_obj = make_response(resp_dict)
        resp_obj.headers['Content-Type'] = 'application/json'

        return resp_obj


@app.route('/user/<uuid:uuid>')
def user(uuid):
    return str(uuid)

class ProjectAPI(MethodView):
    def get(self):
        return "Project List"

app.add_url_rule('/project', view_func=ProjectAPI.as_view('projects'))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


details = [
    {
        'id': 1,
        'fullname': u'nazirini ',
        'email': u'hansu@gmail.com',
        'phone': u'536780',
        'department': u'Team Lead',
        'computerID': u'AAA53',
        'description': u'Screen freezes when handing heavy apps',
        'done': False
    },
    {
        'id': 2,
        'fullname': u'Siraji',
        'email': u'world',
        'phone': u'6373892',
        'department': u'Facilitors',
        'computerID': u'875TRH',
        'description': u'Key board shortcuts not working',
        'done': False
    },
    {
        'id': 3,
        'fullname': u'papa ',
        'email': u'papa@gmail.com',
        'phone': u'3565362',
        'department': u'Student',
        'computerID': u'KKe5u',
        'description': u'No more space in the hard drive',
        'done': False
    },
    {
        'id': 4,
        'fullname': u'hadija',
        'email': u'had@gmail.com',
        'phone': u'015918',
        'department': u'Coordinations',
        'computerID': u'52879',
        'description': u'Screen takes long to start',
        'done': False
    }
]


@app.route('/nazirini/api/v1.0/details', methods=['GET'])
def get_all_request():
    return jsonify({'details': details})


@app.route('/nazirini/api/v1.0/details/<int:detail_id>', methods=['GET'])
def get_request(detail_id):
    for detail in details:
        if detail['id'] == detail_id:
            return jsonify({'detail': detail})
    abort(404)


@app.route('/nazirini/api/v1.0/details', methods=['POST'])
def create_request():
    if not request.get_json() or not 'fullname' in request.get_json():
        abort(400)
    detail = {
        'id': details[-1]['id'] + 1,
        'fullname': request.get_json()['fullname'],
        'email': request.get_json()['email'],
        'phone': request.get_json()['phone'],
        'department': request.get_json()['department'], 
        'computerID': request.get_json()['computerID'],
        'description': request.get_json().get('description'),
        'done': False
    }
    details.append(detail)
    return jsonify({'detail': detail}), 201


@app.route('/nazirini/api/v1.0/details/<int:detail_id>', methods=['PUT'])
def update_request(detail_id):
    detail = [detail for detail in details if detail['id'] == detail_id]
    if len(detail) == 0:
        abort(404)
    if not request.get_json():
        abort(400)

    if 'done' in request.get_json() and type(request.get_json()['done']) is not bool:
        abort(400)
    detail[0]['fullname'] = request.get_json().get('fullname', detail[0]['fullname'])
    detail[0]['email'] = request.get_json().get('email', detail[0]['email'])
    detail[0]['phone'] = request.get_json().get('phone', detail[0]['phone'])
    detail[0]['department'] = request.get_json().get('department', detail[0]['department'])
    detail[0]['computerID'] = request.get_json().get(
        'computerID', detail[0]['computerID'])
    detail[0]['description'] = request.get_json().get(
        'description', detail[0]['description'])
    detail[0]['done'] = request.get_json().get('done', detail[0]['done'])
    return jsonify({'detail': detail[0]})


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

meetups = [
     {
    'id': 1,
    'data': {
        'topic': 'The world today',
        'location': 'Accra',
        'happeningOn':'20th/2/1994'
    }
}
]
@app.route('/meeetups/<meetup-id>',methods=['GET'])
def fetch_meetup():
    return make_response(jsonify(
        {
            'Status': "Okay",
            'Message': "Success",
            'Meetups': meetups
        }
    ),200)

if __name__ == '__main__':
    app.run(debug = True)
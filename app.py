from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'todo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def getTodos():
    todo = mongo.db.todos
    output = []
    for t in todo.find():
        output.append({
            'id': str(t['_id']),
            'item' : t['item'],
            'is_done': t['is_done']
        })
    return jsonify({'result' : output})

@app.route('/<id>', methods=['GET'])
def getTodo(id):
    todo = mongo.db.todos
    t = todo.find_one({'_id' : id})
    if t:
        output = {'id' : str(t['_id']), 'item' : t['item'], 'is_done' : t['is_done']}
    else:
        output = "Cant find ID"
    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
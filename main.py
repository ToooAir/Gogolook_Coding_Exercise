from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
id_counter = 0

#GET /tasks (list tasks)
@app.route('/tasks', methods=['GET'])
def list_task():
    return jsonify(tasks)

#POST /task (create task)
@app.route('/task', methods=['POST'])
def create_task():
    request_data = request.get_json()
    if 'name' not in request_data:
        return jsonify("param is missing")

    else:
        global id_counter
        id_counter = id_counter + 1

        new_list = {'name':request_data['name'], 'status':0, 'id':str(id_counter)}
        tasks.append(new_list)
        return jsonify(new_list)

#PUT /task/<id> (update task)
@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    request_data = request.get_json()
    if 'name' not in request_data or 'status' not in request_data:
        return jsonify("param is missing")

    else:
        for i,task in enumerate(tasks):
            if task['id'] == id:
                new_list = {'name':request_data['name'], 'status':request_data['status'], 'id':id}
                tasks[i] = new_list
                return jsonify(new_list)

            elif i == len(tasks) - 1:
                return jsonify("id is not found")


#DELETE /task/<id> (delete task)
@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    for i,task in enumerate(tasks):
        if task['id'] == id:
            tasks.pop(i)
            resp = jsonify()
            resp.status_code = 200
            return resp

        elif i == len(tasks) - 1:
            return jsonify("id is not found")
        

app.run(host='0.0.0.0')
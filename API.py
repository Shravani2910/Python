##put and Delete HTTP Verbs
##working with API's--Json

#Example: Creating simple TO-DO list

from flask import Flask,jsonify,request

app=Flask(__name__)

##Initial data for my to-do list
items=[
    {"id":1,"name":"item1","Description":"This is item 1"},
    {"id":2,"name":"item2","Description":"This is item 2"}

]

@app.route('/')
def home():
    return "Sample to-do list App"

#Get method: retriving all the items and get:retrive specific item
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is none:
        return jsonify({"Error:Item not Found"})
    return jsonify(item)

##Post:Create new task-API
@app.route('/items'.methods['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error:Item not Found"})
    new_item={
        'id':items[-1]["id"]+1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

##Put:update an existing item

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item():
    item=next((item for item in items if item["id"]==item_id),None)
    if item is none:
        return jsonify({"Error:Item not Found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

##Delete: Delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item():
    global items
    items=[item for item in items if item["id"] != item_id]
    return jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)

   
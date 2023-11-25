from flask import Flask, render_template, request, redirect

import sqlRequests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    sqlRequests.createTable("test_table")
    dataTable = sqlRequests.getAllData()
    print(dataTable)
    if request.method == "GET":
        name = request.args.get("new_name")
        phone = request.args.get("new_phone")
        description = request.args.get("new_description")
        if name != "" and phone != "" and description != "" and name != None and phone != None and description != None:
            sqlRequests.addNewData(name, phone, description)
            print("Данные добавлены")
        idDelete = request.args.get("delete")
        print(idDelete)
        if idDelete != None:
            sqlRequests.deleteById(int(idDelete))
            print("Данные удалены")
        return render_template('index.html', dataTable=dataTable)


@app.route('/edit/<id>')
def editStringBook(id):
    getDataById = sqlRequests.getDataById(id)
    return render_template("edit.html", getDataById=getDataById)


@app.route('/edit', methods=['POST'])
def editStringBookPost():
    if request.method == "POST":
        id = int(request.form['id'])
        name = request.form['name']
        phone = request.form['phone']
        description = request.form['description']
        sqlRequests.updateDataById(id, name, phone, description)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

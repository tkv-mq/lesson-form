from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    note = open("note.txt", "a+", encoding="utf-8")
    note_lst = [i for i in note]
    note.close()
    return render_template('home.html', note_lst=note_lst)

@app.route("/hello/<string:user_name>")
def hello(user_name):
    user_name = user_name.capitalize()
    return render_template("hello.html", user_name=user_name)

@app.route("/add-note-form")
def add_note_form():
    return render_template("add_form.html")

@app.route("/add-note", methods=["POST"])
def add_note():
    note = request.form
    note_file = open("note.txt", "a+", encoding="utf-8")
    data = note['new-note'] + ' ' + note['new-date'] + "\n"
    note_file.write(data)
    note_file.close()
    return render_template("ok.html")

@app.route("/table-lst")
def table():
    note = open('note.txt', 'r+', encoding='utf-8')
    temp = note.read().split('\n')
    nd_lst = [i.split(' ') for i in temp]
    del nd_lst[-1]
    note.close()
    return render_template("table_lst.html", nd_lst=nd_lst)
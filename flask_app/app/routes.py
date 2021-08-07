# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db

# home page
@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)

# adds new tasks to the todo list database
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    deadline = request.form.get("deadline")
    new_todo = Todo(title=title, deadline=deadline)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

# updates current tasks
@app.route("/update/<int:todo_id>", methods=["GET", "POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if request.method == 'POST':
        newtitle = request.form.get("update_title")
        newdeadline = request.form.get('update_deadline')
        new_todo = Todo(id=todo_id, title=newtitle, deadline=newdeadline)
        db.session.add(new_todo)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("update.html", todo=todo)

# deletes tasks selected by user
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.id = request.form.get('deletebox')
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

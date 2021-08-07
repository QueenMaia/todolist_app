# TODO List App

TODO List is a Flask web application for keeping track of current and upcoming tasks as well as their deadlines.

### Built With
* [Python]()
* [HTML/CSS]()
* [Flask]()

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* python 3
  ```sh
  brew install python3
  ```
* virtualenv
  ```sh
  pip install virtualenv
  ```
* virtualenvwrapper
  ```sh
  pip install virtualenvwrapper
  ```
* flask
  ```sh
  pip install flask
  ```
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/QueenMaia/todolist_app.git
   ```
2. Install the aforementioned packages

3. Create and activate a new virtual environment

4. Run the application using one of the following commands:
   ```sh
   flask run
   ```

   ```sh
   python run.py
   ```
5. View the application by copying and pasting the IP address given by Flask into your browser.


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage
This app utilizes the Flask Web Application Framework to create a simple, interactive todo list. Users can add tasks to the list and have the option of updating the title and deadline of each task. After completing a task, users can delete the task from the list by checking the checkbox next to the task.
<!-- ![alt text](http://url/to/img.png) -->
The app uses the Flask-SQLAlchemy module to create a database that stores the id, title and deadline of each task.

```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    deadline = db.Column(db.String(200))
```
Python functions allow the app to add new tasks to the database as well as edit and delete specific tasks.

```python
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    deadline = request.form.get("deadline")
    new_todo = Todo(title=title, deadline=deadline)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))
```

To display the todo list and its updated tasks, the app utilizes html pages.

```HTML
<form action="/add" method="post">
    <div>
        <label>Add To TODO List</label>
        <br>
        <input type="text" name="title" placeholder="Enter Todo Item...">
        <input type="text" name="deadline" placeholder="Add Deadline...">
        <button type="submit">Add</button>
    </div>
</form>
```

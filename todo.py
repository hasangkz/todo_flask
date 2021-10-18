from flask import Flask,redirect,url_for,request,flash
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hasan/Desktop/PYTHON-TODO/todo.db'
db = SQLAlchemy(app)
app.secret_key = "todo"

@app.route("/")
def index ():
    todos = do.query.all()
    return render_template("index.html",todos = todos)


@app.route("/add",methods = ["POST"])
def add():
    title = request.form.get("title")
    
    newtodo = do(title = title,complete = False)
    db.session.add(newtodo)
    db.session.commit()
    flash("You have successfully added the task!","success")
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def complete(id):
    todo = do.query.filter_by(id=id).first()

    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<string:id>")
def delete(id):
    todo = do.query.filter_by(id=id).first()        

    db.session.delete(todo)
    db.session.commit()
    flash("You have successfully deleted the task!","success")
    return redirect(url_for("index"))


class do(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60))
    complete = db.Column(db.Boolean)
     
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)

from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
@app.route('/')
def default():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

@app.route('/new')
def newUser():
    return render_template("new.html")

@app.route('/show', methods=["POST"])
def showUser():
    pass
@app.route('/edit', methods=["POST"])
def editUser():
    pass
@app.route('/delete', methods=["POST"])
def deleteUser():
    pass

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'april python class is the coolest'

# our index route will handle rendering our form


@app.route('/')
def home():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)

    # storing data from request.form dictionary in the session dictionary
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    session['hidden'] = request.form['hidden_field']
    return redirect("/count")

# Count session


@app.route("/count")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("count.html")

# clearing out session


@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

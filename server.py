from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'april python class is the coolest'

# our index route will handle rendering our form


@app.route('/')
def home():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 2
    else:
        session['visits'] = 1
    return render_template("index.html")


# clearing out session

@app.route("/destroy")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

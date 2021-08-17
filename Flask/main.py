from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    if name:
        print(name)
        render_template("hello_user.html", user=name)
    return render_template("hello.html")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('form_name')
        return redirect(url_for("hello_world", name=name))
        print("É um POST!")
    return render_template("login.html")


if __name__ == '__main__':
    app.run()

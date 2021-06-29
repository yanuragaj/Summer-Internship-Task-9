from flask import Flask, request, render_template
import subprocess as sp
app = Flask("app")
global cmd


@app.route("/menu")
def menuform():
    form = render_template("index.html")
    return form


@app.route("/cmd_output")
def cmd_output():
    cmd = request.args.get("cmd_input")
    b = sp.getoutput(cmd)
    a = render_template('a.html', value=b)
    print(cmd)
    return a


app.run(debug=True)

from flask import Flask, session, render_template, request, redirect
from cpl_main import * 

app = Flask(__name__,template_folder='template')

@app.route('/', methods =["GET", "POST"])
def formMain():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        rno = request.form.get("regNo")
        kms=request.form.get("kms")
        success(rno,kms)
    return render_template("form.html")

@app.route('/success/', methods=['POST'])
def success(rno,kms):
    print("Average=Rs.",int(carValue(rno,kms)))
    avg=int(carValue(rno,kms))
    return render_template("success.html",average=avg)


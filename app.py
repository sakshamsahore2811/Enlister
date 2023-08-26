#Job portal application
from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobdata.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()


class JobData(db.Model):
    role = db.Column(db.String(50),primary_key = True)
    company = db.Column(db.String,nullable = False)
    salary = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(100),nullable=False)
    requirements = db.Column(db.String(500),nullable=False)
    def __repr__(self) -> str:
        return f"{self.role} - {self.company} - {self.salary} - {self.location} - {self.requirements}"


@app.route('/',methods=["GET","POST"])
def home(): 
    if request.method == "POST":
        role = request.form['role']
        company = request.form['company']
        salary = request.form['salary']
        location = request.form['location']
        requirements = request.form['requirements']
        jdata = JobData(role=role,company=company,salary=salary,location=location,requirements=requirements)
        db.session.add(jdata)
        db.session.commit()
    alldata = JobData.query.all()
    return render_template("index.html",alldata=alldata)

@app.route("/hire/")
def hire():
    return render_template("hire.html")

@app.route("/apply/")
def apply():
    return render_template("apply.html")


if __name__ == "__main__":
    app.run(debug=True)
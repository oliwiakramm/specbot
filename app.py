from flask import Flask,render_template,request,redirect,url_for
from doctors import scrape_doctors
from bot import ask_chat_for_specialist

app = Flask(__name__)
URL = "https://pesmed.pl/lekarz"

@app.route("/",methods=["GET","POST"])
def index():
    specialist = ""
    doctors = ""
    if request.method == 'POST':
        symptoms = request.form["symptoms"]
        specialist = ask_chat_for_specialist(symptoms)
        doctors = scrape_doctors(specialist)

    return render_template("index.html",specialist=specialist,doctors=doctors,url=URL)

@app.route("/reset",methods=['POST'])
def reset():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True,port=5001)
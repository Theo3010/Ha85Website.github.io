from flask import Flask, render_template

app = Flask(__name__)

navbar = ["Forside", "Fodbold", "Håndbold", "Badminton", "Esport", "Høvdingbold", "Volleyball", "Sponsor", "Om Ha85"]
fodboldList = {
    "1": {
        "name": "Fodbold - FC Silkeborg U13 Piger",
        "pris": "600 DKK",
        "date": "01-08-2021 - 31-07-2022",
    },
    "2": {
    "name": "Fodbold - FC Silkeborg U14 Drenge",
    "pris": "600 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "3": {
    "name": "Fodbold - FC Silkeborg U14 Piger",
    "pris": "600 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "4": {
    "name": "Fodbold - FC Silkeborg U15 Drenge",
    "pris": "600 DKK",
    "date": "01-08-2021 - 31-07-2022",
    }
}

handboldlist = {
    "1": {
    "name": "Trænerafslutning 19.april 2022 - Tilmelding",
    "pris": " ",
    "date": "01-08-2021 - 31-07-2022",
    },
    "2": {
    "name": "Håndbold - Trille Trolle (2016/2017",
    "pris": "250 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "3": {
    "name": "Håndbold Five-a-side",
    "pris": "150 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "4": {
    "name": "Håndbold U6 mix (2015)",
    "pris": "400 DKK",
    "date": "01-08-2021 - 31-07-2022",
    }
}

Badmintonlist = {
    "1": {
    "name": "Badminton - U13 samt øvede U11 (årg 2009/2012) sæson 21/22",
    "pris": "350 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "2": {
    "name": "Badminton - Ekstratræning sæson 21/22",
    "pris": "250 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "3": {
    "name": "Badminton - senior/Motion sæson 2021/2022",
    "pris": "800 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "4": {
    "name": "Badminton - U15/17, sæson 21/22",
    "pris": "350 DKK",
    "date": "01-08-2021 - 31-07-2022",
    }
}

Esportlist = {
    "1": {
    "name": "CS:Go (Senior) torsdag kl. 20.00 - 2021/22",
    "pris": "800 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "2": {
    "name": "CS:Go Begynder 2021/22",
    "pris": "600 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "3": {
    "name": "CS:Go Let øvede 2021/22",
    "pris": "850 DKK",
    "date": "01-08-2021 - 31-07-2022",
    },
    "4": {
    "name": "CS:Go Turneringshold 2021/22",
    "pris": "600 DKK",
    "date": "01-08-2021 - 31-07-2022",
    }
}

@app.route('/')
def index():
    return render_template('Forside.html', active="Forside", navbar=navbar)

@app.route("/Forside")
def home():
    return render_template("Forside.html", active="Forside", navbar=navbar)

@app.route("/Fodbold")
def fodbold():
    return render_template("fodbold.html", active="Fodbold", navbar=navbar, fodboldList=fodboldList)

@app.route("/Håndbold")
def handbold():
    return render_template("handbold.html", active="Håndbold", navbar=navbar, handboldlist=handboldlist)

@app.route("/Badminton")
def badminton():
    return render_template("badminton.html", active="Badminton", navbar=navbar, Badmintonlist=Badmintonlist)

@app.route("/Esport")
def esport():
    return render_template("esport.html", active="Esport", navbar=navbar, Esportlist=Esportlist)

@app.route("/Gymnastik Og Dans")
def gymnastik():
    return render_template("gymnastik.html", active="Gymnastik Og Dans", navbar=navbar)

@app.route("/Høvdingbold")
def hoevdingbold():
    return render_template("hoevdingbold.html", active="Høvdingbold", navbar=navbar)

@app.route("/Volleyball")
def volleyball():
    return render_template("volleyball.html", active="Volleyball", navbar=navbar)

@app.route("/løb")
def loeb():
    return render_template("loeb.html", active="Løb", navbar=navbar)

@app.route("/Sponsor")
def sponsor():
    return render_template("sponsor.html", active="Sponsor", navbar=navbar)

@app.route("/Om Ha85")
def omHa85():
    return render_template("omHa85.html", active="Om Ha85", navbar=navbar)





if __name__ == "__main__":
	app.run(debug=True, host="localhost", port=5000)
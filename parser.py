import csv
import webbrowser

def betoltes():
    tetok = []
    with open("anyagok.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tetok.append(row)
    return tetok

def html(tetok, terulet):
    sorok = ""
    for t in tetok:
        ar = float(t["Ár/Négyzetméter"]) * terulet
        sorok += f"""
        <tr>
            <td>{t['Tető anyaga']}</td>
            <td>{ar:,.0f}</td>
            <td>{t['Ajánlott csere (év)']}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="hu">
    <head>
        <meta charset="UTF-8">
        <title>Tető-ár számító</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav class="navbar">
            <img class="logo" src="logo.png">
            <ul>
                <li><a href="index.html">Főoldal</a></li>
                <li class="navbaractive"><a href="teto.html">Tetőztess Ma!</a></li>
                <li><a href="faq.html">GY. I. K.</a></li>
                <li><a href="kontakt.html">Kapcsolat</a></li>
            </ul>
        </nav>
        <div class="user-input" style="margin:20px 0;">
            <label for="hely">Tető kell? Mi Megcsináljuk!</label>
            <input type="text" id="hely" placeholder="Írja be a várost/utcát">
            <button id="kuldes">Küldés</button>
        </div>
        <h1>Tető-ár számító</h1>
        <p>Megadott terület: <b>{terulet:,.0f} m²</b></p>
        <table class="fade-in">
            <thead>
                <tr>
                    <th>Tető anyaga</th>
                    <th>Teljes ár (Ft)</th>
                    <th>Ajánlott csere (év)</th>
                </tr>
            </thead>
            <tbody>
                {sorok}
            </tbody>
        </table>
    <script src="script.js"></script>
    </body>
    </html>
    """
    with open("teto.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    try:
        terulet = float(input("Add meg a tető területét (m²): "))
    except ValueError:
        print("Hibás szám!")
        exit()

    tetok = betoltes()
    html(tetok, terulet)

    webbrowser.open("index.html")
roll_number = {
    1 : "Sanskriti",
    5 : "Satwik Srivastava",
    15 : "Shabbar Abbas Zaidi",
    20 : "Shambik Thakur",
    26 : "Shaswat Jaiswal",
    45 : "Shreyash",
    57 : "Siddhi Singh"
    }

clg_mail = {
    "Satwik Srivastava" : "satwik@bbdu.ac.in",
    "Shambik Thakur" : "shambik@bbdu.ac.in",
    "Sanskriti" : "sanskriti@bbdu.ac.in",
    "Shabbar Abbas Zaidi" : "shabbar@bbdu.ac.in",
    "Shreyash" : "shreyash@bbdu.ac.in",
    "Siddhi Singh":"siddhi@bbdu.ac.in",
    "Shaswat Jaiswal" : "shaswat2007.jaiswal@bbdu.ac.in"
}

def fetch_mail(roll_number, clg_mail):
    for x, y in roll_number.items():
        for a, b in clg_mail.items():
            if y == a:
                print(x, y, b)


fetch_mail(roll_number, clg_mail)

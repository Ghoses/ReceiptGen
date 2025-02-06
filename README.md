🛒 Lidl Kassenzettel Generator 🧾
Erstelle realistische Lidl-Kassenzettel als Screenshots – vollautomatisch mit Python und Selenium!
Dieses Projekt generiert zufällige Kassenzettel mit authentisch wirkenden Artikeln, Preisen, Mehrwertsteuer-Berechnung, Barcode und weiteren typischen Informationen. Dabei wird sichergestellt, dass der Gesamtbetrag immer innerhalb eines realistischen Rahmens liegt – ab einem Mindestbetrag von ca. 6,90 € bis maximal 23,00 €.

🚀 Features
Realistische Einkaufsbons:
Zufällige Artikel aus einer konfigurierbaren Warenliste inklusive Preisberechnung.
Mindestbetrag:
Es werden ausschließlich Kassenzettel mit einem Gesamtbetrag zwischen ca. 6,90 € und 23,00 € generiert.
Screenshot-Speicherung:
Ausgabe der Kassenzettel als Bilddateien (Screenshot) mittels Selenium & ChromeDriver.
Dynamische Preisberechnung:
Automatische Berechnung von Mehrwertsteuer, Nettobetrag und Gesamtpreis.
Einstellbarer Zeitraum:
Möglichkeit, Kassenzettel für einen beliebigen Zeitraum (mehrere Tage) zu generieren.
Einfache GUI:
Benutzerfreundliche Oberfläche mit Tkinter zur schnellen Bedienung.
White-Label-Fähigkeit:
Alle relevanten Informationen (Warenliste, Filialdaten, Logo-Pfad) werden über externe JSON-Dateien konfiguriert und sind somit leicht anpassbar.
🔧 Installation & Einrichtung
1️⃣ Voraussetzungen
Python 3.x (getestet mit 3.8+)
Google Chrome (aktuelle Version)
ChromeDriver für Selenium
(Wird automatisch installiert, falls nicht vorhanden – dank webdriver_manager.)
2️⃣ Python-Abhängigkeiten installieren
Öffne eine Konsole und führe folgenden Befehl aus:

bash
Kopieren
pip install -r requirements.txt
3️⃣ Konfiguration anpassen (optional)
Warenliste:
Passe die Artikelliste und Preise in der Datei warenliste.json an.
Filialdaten & Logo:
Ändere in der Datei config.json die Informationen zu den Filialen (Adresse, USt-ID etc.) sowie den Pfad zum Logo-Bild.
4️⃣ Anwendung starten
Starte das Script mit:

bash
Kopieren
python main.py
🎯 Nutzung
GUI:
Wähle in der grafischen Benutzeroberfläche den gewünschten Zeitraum oder einzelne Tage aus und starte die Generierung der Kassenzettel.
Ergebnis:
Die generierten Kassenzettel werden als PNG-Screenshots im aktuellen Arbeitsverzeichnis gespeichert.

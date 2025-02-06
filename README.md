# 🛒 Lidl Kassenzettel Generator 🧾

**Erstelle realistische Lidl-Kassenzettel als Screenshots – vollautomatisch mit Python und Selenium!**

Dieses Projekt generiert zufällige Kassenzettel mit authentisch wirkenden Artikeln, Preisen, Mehrwertsteuer-Berechnung, Barcode und weiteren typischen Informationen. Dabei wird sichergestellt, dass der Gesamtbetrag immer innerhalb eines realistischen Rahmens liegt – ab einem Mindestbetrag von ca. 6,90 € bis maximal 23,00 €.

## 🚀 Features

- **Realistische Einkaufsbons:**  
  Zufällige Artikel aus einer konfigurierbaren Warenliste inklusive Preisberechnung.
- **Mindestbetrag:**  
  Es werden ausschließlich Kassenzettel mit einem Gesamtbetrag zwischen ca. 6,90 € und 23,00 € generiert.
- **Screenshot-Speicherung:**  
  Ausgabe der Kassenzettel als Bilddateien (Screenshot) mittels Selenium & ChromeDriver.
- **Dynamische Preisberechnung:**  
  Automatische Berechnung von Mehrwertsteuer, Nettobetrag und Gesamtpreis.
- **Einstellbarer Zeitraum:**  
  Möglichkeit, Kassenzettel für einen beliebigen Zeitraum (mehrere Tage) zu generieren.
- **Einfache GUI:**  
  Benutzerfreundliche Oberfläche mit Tkinter zur schnellen Bedienung.
- **White-Label-Fähigkeit:**  
  Alle relevanten Informationen (Warenliste, Filialdaten, Logo-Pfad) werden über externe JSON-Dateien konfiguriert und sind somit leicht anpassbar.

---

## 🔧 Installation & Einrichtung

### Voraussetzungen
- **Python 3.x** (getestet mit 3.8+)
- **Google Chrome** (aktuelle Version)
- **ChromeDriver** für Selenium  
  *(Wird automatisch installiert, falls nicht vorhanden – dank `webdriver_manager`.)*

### Python-Abhängigkeiten installieren

Öffne eine Konsole und führe folgenden Befehl aus:

```bash
pip install -r requirements.txt
``` 

---

## 🔧 Konfiguration anpassen (optional)

- **Warenliste:** Passe die Artikelliste und Preise in der Datei warenliste.json an.
- **Filialdaten & Logo:** In der Datei config.json kannst du alle Details zu den Filialen (Adresse, USt-ID etc.) sowie den Pfad zum Logo-Bild anpassen.

- ## 🔧 Anwendung starten

```bash
python3 lidl_gui_v32.py

or

python lidl_gui_v32.py
``` 

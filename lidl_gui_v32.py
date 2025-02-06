import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import os
import random
import sys
import tempfile
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def resource_path(relative_path):
    """Gibt den absoluten Pfad zur Ressource zurück, egal ob das Skript als EXE oder als .py ausgeführt wird."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_json(dateiname):
    """Lädt eine JSON-Datei aus dem angegebenen relativen Pfad."""
    with open(resource_path(dateiname), "r", encoding="utf-8") as f:
        return json.load(f)

# Laden der Konfiguration (Logo und Filialdaten) aus config.json
config = load_json("stores.json")
logo_path = resource_path(config["logo"])
stores = config["stores"]

# Laden der Warenliste aus warenliste.json
available_items = load_json("list.json")

def generate_random_barcode_html(bar_count=25):
    """Generiert einen Barcode im HTML-Format."""
    barcode_parts = []
    barcode_parts.append(
        '<div style="text-align:center; margin-top:10px;">'
        '<div style="display:inline-block; white-space:nowrap; font-size:0; line-height:0;">'
    )

    for _ in range(bar_count):
        black_width = random.randint(1, 4)
        space_width = random.randint(1, 3)
        barcode_parts.append(
            f'<span style="display:inline-block; vertical-align:top; '
            f'width:{black_width}px; height:60px; background-color:black;"></span>'
        )
        barcode_parts.append(
            f'<span style="display:inline-block; vertical-align:top; '
            f'width:{space_width}px; height:60px; background-color:#fff;"></span>'
        )

    barcode_parts.append('</div></div>')
    return "".join(barcode_parts)

def generate_receipt_text(fixed_date):
    """Erstellt den vollständigen HTML-Text eines Kassenzettels mit Artikeln, Barcode und Datum."""

    # Wenn der aktuelle Tag generiert wird, setze die Uhrzeit zwischen 7 und 8 Uhr
    today_date = datetime.now().strftime("%d.%m.%Y")
    if fixed_date == today_date:
        fixed_time = f"{random.randint(7, 8):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    else:
        fixed_time = f"{random.randint(7, 22):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    
    time_obj = datetime.strptime(fixed_time, "%H:%M:%S")
    random_seconds = random.randint(4, 28)
    fixed_time_pay = (time_obj + timedelta(seconds=random_seconds)).strftime("%H:%M:%S")
    fixed_date_time = f"{fixed_date} {fixed_time}"
    fixed_date_time_pay = f"{fixed_date} {fixed_time_pay}"

    # Auswahl eines zufälligen Stores aus der geladenen Liste
    store = random.choice(stores)
    address_str = store['address'].replace('\n', '<br>')

    tse_number = random.randint(100000, 999999)
    kasse_number = f"{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    pruefwert = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/", k=30))
    pruefwertt = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/", k=40))
    signature_counter = random.randint(100000, 999999)
    serial_number = f"{random.randint(1000, 9999)} {random.randint(100000, 999999)}/{random.randint(1, 99)}"
    ust_id = store['ust_id']

    total_amount = 0
    items = []
    while total_amount < 6.91 or total_amount > 23.00:
        items = random.sample(available_items, random.randint(3, 6))
        total_amount = sum(price for _, price in items)

    vat = total_amount * 0.07
    net = total_amount - vat

    receipt_lines = []
    receipt_lines.append("                                   EUR")
    for item, price in items:
        line = f"{item:30}{price:8.2f} A"
        receipt_lines.append(line)

    receipt_lines.append("-" * 40)
    receipt_lines.append(f"zu zahlen                     {total_amount:8.2f}")
    receipt_lines.append("MWST%       MWST      Netto     Brutto")
    line_vat = f"A  7%{vat:11.2f}{net:11.2f}{total_amount:11.2f}"
    receipt_lines.append(line_vat)
    receipt_lines.append(f"TSE Transaktionsnummer: {tse_number}")
    receipt_lines.append(f"Seriennr. Kasse: {kasse_number}")
    receipt_lines.append(f"Prüfwert: {pruefwert}")
    receipt_lines.append(f"{pruefwertt}")
    receipt_lines.append(f"Signaturzähler: {signature_counter}")
    receipt_lines.append(f"{serial_number}   {fixed_date_time}")
    receipt_lines.append(f"UST-ID-NR: {ust_id}")
    receipt_lines.append("-" * 40)

    receipt_text = "\n".join(receipt_lines)
    bottom_text = f"""
    <div class="centered-info">K-U-N-D-E-N-B-E-L-E-G</div>
    <div class="centered-info">Bezahlung: Bar</div>
    <div class="centered-info">Datum {fixed_date_time_pay}</div>
    """
    bottom_block = f"""
    {bottom_text}
    {generate_random_barcode_html(bar_count=90)}
    """
    html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8" />
    <title>Kassenzettel {fixed_date_time}</title>
    <style>
    body {{
        margin: 20px;
        font-family: Consolas, monospace;
        font-size: 21.5px;
        font-weight: bolder;
        line-height: 1.8;
    }}
    .receipt-wrapper {{
        white-space: pre;
    }}
    .logo {{
        margin-bottom: 20px;
        text-align: center;
    }}
    .store-address {{
        text-align: center;
        font-weight: bold;
        margin: 1em 0;
    }}
    .centered-info {{
        text-align: center;
        margin: 0.3em 0;
    }}
    </style>
</head>
<body>
    <div class="logo">
        <img src="{logo_path}" alt="Logo" style="max-width: 150px;" />
    </div>
    <div class="store-address">
        {address_str}
    </div>
    <div class="receipt-wrapper">
{receipt_text}
    </div>
    {bottom_block}
</body>
</html>
"""
    return html_content

def take_screenshot_of_html(html_content, screenshot_name, width=561, height=1700):
    """Erstellt einen Screenshot des generierten HTML-Kassenzettels aus dem HTML-Inhalt."""
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html", encoding="utf-8") as temp_html_file:
        temp_html_file.write(html_content)
        temp_html_path = temp_html_file.name
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size={width},{height}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("file:///" + temp_html_path.replace('\\', '/'))
    driver.save_screenshot(screenshot_name)
    driver.quit()

    # Entfernt die temporäre HTML-Datei nach dem Screenshot
    os.remove(temp_html_path)

def generate_receipts_for_period(start_date_str, end_date_str):
    """Erstellt Kassenzettel für den angegebenen Zeitraum."""
    try:
        start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
        end_date = datetime.strptime(end_date_str, "%d.%m.%Y")
    except ValueError:
        raise ValueError("Ungültiges Datum. Bitte verwenden Sie das Format TT.MM.JJJJ.")

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%d.%m.%Y")
        receipt_html = generate_receipt_text(date_str)
        screenshot_name = f"{date_str}.png"
        take_screenshot_of_html(receipt_html, screenshot_name, 561, 1700)
        current_date += timedelta(days=1)

def run_script():
    """Führt die Kassenzettel-Generierung basierend auf den eingegebenen Datumswerten aus."""
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    try:
        generate_receipts_for_period(start_date, end_date)
        messagebox.showinfo("Erfolg", f"Kassenzettel für den Zeitraum {start_date} bis {end_date} wurden erfolgreich erstellt.")
    except Exception as e:
        messagebox.showerror("Fehler", f"Beim Erstellen der Kassenzettel ist ein Fehler aufgetreten:\n{e}")

def adjust_date(entry, days):
    """Ändert das Datum im Entry-Feld um die angegebene Anzahl Tage."""
    try:
        current_date = datetime.strptime(entry.get(), "%d.%m.%Y")
        new_date = current_date + timedelta(days=days)
        entry.delete(0, tk.END)
        entry.insert(0, new_date.strftime("%d.%m.%Y"))
    except ValueError:
        pass

def generate_receipt_for_day(date_str):
    """Erstellt einen Kassenzettel für ein einzelnes Datum."""
    try:
        receipt_html = generate_receipt_text(date_str)
        screenshot_name = f"{date_str}.png"
        take_screenshot_of_html(receipt_html, screenshot_name, 561, 1700)
        messagebox.showinfo("Erfolg", f"Kassenzettel für den Tag {date_str} wurde erfolgreich erstellt.")
    except Exception as e:
        messagebox.showerror("Fehler", f"Beim Erstellen des Kassenzettels ist ein Fehler aufgetreten:\n{e}")

# GUI erstellen
root = tk.Tk()
root.title("Shopping Simulator - White Label")
root.geometry("600x400")

current_date = datetime.now().strftime("%d.%m.%Y")

# Frame für die Datumseingaben
date_frame = tk.Frame(root)
date_frame.pack(pady=10)

# Startdatum
start_label = tk.Label(date_frame, text="Startdatum (TT.MM.JJJJ):")
start_label.grid(row=0, column=0, padx=5)
start_date_entry = tk.Entry(date_frame)
start_date_entry.insert(0, current_date)
start_date_entry.grid(row=0, column=1, padx=5)
tk.Button(date_frame, text="▲", command=lambda: adjust_date(start_date_entry, 1)).grid(row=0, column=3)
tk.Button(date_frame, text="▼", command=lambda: adjust_date(start_date_entry, -1)).grid(row=0, column=2)

# Enddatum
end_label = tk.Label(date_frame, text="Enddatum (TT.MM.JJJJ):")
end_label.grid(row=1, column=0, padx=5)
end_date_entry = tk.Entry(date_frame)
end_date_entry.insert(0, current_date)
end_date_entry.grid(row=1, column=1, padx=5)
tk.Button(date_frame, text="▲", command=lambda: adjust_date(end_date_entry, 1)).grid(row=1, column=3)
tk.Button(date_frame, text="▼", command=lambda: adjust_date(end_date_entry, -1)).grid(row=1, column=2)

# Generieren-Button
generate_button = tk.Button(root, text="Generieren (5 Sekunden je Tag)", command=run_script)
generate_button.pack(pady=20)

# Frame für die ersten 15 Tage des aktuellen Monats
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

current_month = datetime.now().strftime("%m.%Y")
for day in range(1, 16):
    date_str = f"{day:02d}.{current_month}"
    button = tk.Button(button_frame, text=date_str, command=lambda d=date_str: generate_receipt_for_day(d))
    button.grid(row=(day - 1) // 5, column=(day - 1) % 5, padx=5, pady=5)

# Footer-Label
footer_label = tk.Label(root, text="Scripted by Ghoses with Ai")
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()

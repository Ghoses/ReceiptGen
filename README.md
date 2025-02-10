# 🛒 ReceiptGen 🧾

**Create realistic receipts as screenshots – fully automated with Python and Selenium!**

This project generates random receipts with authentically appearing items, prices, VAT calculation, barcode, and other typical details. It ensures that the total amount always falls within a realistic range – from a minimum of approximately €6.90 to a maximum of €23.00.

## 🚀 Features

- **Realistic receipts:**  
  Random items from a configurable product list, including price calculation.
- **Minimum amount:**  
  Only receipts with a total amount between approximately €6.90 and €23.00 are generated.
- **Screenshot storage:**  
  Receipts are output as image files (screenshots) using Selenium & ChromeDriver.
- **Dynamic price calculation:**  
  Automatic calculation of VAT, net amount, and total price.
- **Customizable time period:**  
  Option to generate receipts for any given period (multiple days).
- **Simple GUI:**  
  A user-friendly interface built with Tkinter for quick operation.
- **White-label capability:**  
  All relevant information (product list, store data, logo path) is configured via external JSON files, making it easily customizable.

---

## 🔧 Installation & Setup

### Requirements
- **Python 3.x** (tested with 3.8+)
- **Google Chrome** (latest version)
- **ChromeDriver** for Selenium  
  *(Automatically installed if not present – thanks to `webdriver_manager`.)*

### Install Python Dependencies

Open a terminal and run the following command:

```bash
pip install -r requirements.txt
``` 

---

## 🔧 Adjust Configuration (optional)

- **Product list:** Adjust the item list and prices in the file warenliste.json.
- **Store data & Logo:** In the file config.json, you can modify all details about the stores (address, VAT ID, etc.) as well as the path to the logo image.

- ## 🔧 Start the Application

```bash
python3 receiptgen_gui_v34.py
``` 
or
```bash
python receiptgen_gui_v34.py
``` 
- ## 🔧 Compile exe by PyInstaller
```bash
python -m PyInstaller --onefile --noconsole --icon=logo.ico --add-data "stores.json;." --add-data "list.json;." --add-data "logo.png;." receiptgen_gui_v34.py
``` 

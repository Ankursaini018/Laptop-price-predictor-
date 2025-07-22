import pandas as pd
from flask import Flask, render_template, request
import joblib
model = joblib.load('model.joblib')
import os

app = Flask(__name__, static_folder='static')

search_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/project', methods = ["POST","GET"])
def predict():
    if request.method=='POST':
        brand = request.form['brand']
        processor_brand = request.form['processor_brand']
        processor_name = request.form['processor_name']
        processor_gnrtn = request.form['processor_gnrtn']
        ram_gb = request.form['ram_gb']
        ram_type = request.form['ram_type']
        ssd = request.form['ssd']
        hdd = request.form['hdd']
        os_ = request.form['os']
        os_bit = request.form['os_bit']
        graphic_card_gb = request.form['graphic_card_gb']
        Touchscreen = request.form['Touchscreen']
        msoffice = request.form['msoffice']
        warranty = request.form['warranty']

        brand_dict = {'ASUS': 1, 'Lenovo': 2, 'acer': 3, 'Avita': 4, 'HP': 5, 'DELL': 6, 'MSI': 7, 'APPLE': 8}
        processor_brand_dict = {'Intel' : 1, 'AMD':2, 'M1': 3}
        processor_name_dict = {'Core i3' : 1, 'Core i5':2, 'Celeron Dual':3, 'Ryzen 5':4, 'Core i7':5,'Core i9':6, 'M1':7, 'Pentium Quad':8, 'Ryzen 3':9, 'Ryzen 7':10, 'Ryzen 9':11}
        processor_gnrtn_dict = {'10th':5, 'Not Available':0, '11th':6, '7th':2, '8th':3, '9th':4, '4th':1,'12th':7}
        ram_type_dict = {'DDR4':3, 'LPDDR4':4, 'LPDDR4X':5, 'DDR5':6, 'DDR3':1, 'LPDDR3':2}
        os_dict = {'Windows':1, 'DOS':2, 'Mac':3}
        os_bit_dict = {'64': 1, '32': 2}
        touchscreen_dict = {'Yes': 1, 'No': 0}
        msoffice_dict = {'Yes': 1, 'No': 0}
        warranty_dict = {'1 Year': 1, '2 Year': 2, '3 Year': 3, 'No Warranty': 0}

        brand_code = brand_dict.get(brand, 0)
        processor_brand_code = processor_brand_dict.get(processor_brand, 0)
        processor_name_code = processor_name_dict.get(processor_name, 0)
        processor_gnrtn_code = processor_gnrtn_dict.get(processor_gnrtn, 0)
        def extract_number(val):
            if isinstance(val, str):
                return float(val.replace('GB', '').replace('gb', '').replace('TB', '').replace('tb', '').replace(' ', '').replace('MB', '').replace('mb', ''))
            return float(val)
        ram_gb_num = extract_number(ram_gb)
        ssd_num = extract_number(ssd)
        hdd_num = extract_number(hdd)
        graphic_card_gb_num = extract_number(graphic_card_gb)
        ram_type_code = ram_type_dict.get(ram_type, 0)
        os_code = os_dict.get(os_, 0)
        os_bit_code = os_bit_dict.get(os_bit, 0)
        touchscreen_code = touchscreen_dict.get(Touchscreen, 0)
        msoffice_code = msoffice_dict.get(msoffice, 0)
        warranty_code = warranty_dict.get(warranty, 0)

        missing_feature = 0 
        lst = [[brand_code, processor_brand_code, processor_name_code, processor_gnrtn_code, ram_gb_num,ssd_num, hdd_num, os_code,graphic_card_gb_num, touchscreen_code, warranty_code]]
        prediction = model.predict(lst)
        rounded_prediction = round(prediction[0], 2)
        search_history.append({
            'brand': brand,
            'processor_brand': processor_brand,
            'processor_name': processor_name,
            'processor_gnrtn': processor_gnrtn,
            'ram_gb': ram_gb,
            'ram_type': ram_type,
            'ssd': ssd,
            'hdd': hdd,
            'os': os_,
            'os_bit': os_bit,
            'graphic_card_gb': graphic_card_gb,
            'Touchscreen': Touchscreen,
            'msoffice': msoffice,
            'warranty': warranty,
            'prediction': rounded_prediction
        })
        print("prediction >>>>>>>>>>", prediction,brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os_,os_bit,graphic_card_gb,Touchscreen,msoffice,warranty)

        return render_template('project.html', prediction=rounded_prediction,
            brand=brand,
            processor_brand=processor_brand,
            processor_name=processor_name,
            processor_gnrtn=processor_gnrtn,
            ram_gb=ram_gb,
            ram_type=ram_type,
            ssd=ssd,
            hdd=hdd,
            os=os_,
            os_bit=os_bit,
            graphic_card_gb=graphic_card_gb,
            Touchscreen=Touchscreen,
            msoffice=msoffice,
            warranty=warranty)
    return render_template('project.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Contact Form - Name: {name}, Email: {email}, Message: {message}")
    return render_template('contact.html')

@app.route('/history')
def history():
    return render_template('history.html', history=search_history)

if __name__ == '__main__':
    app.run(debug=True)
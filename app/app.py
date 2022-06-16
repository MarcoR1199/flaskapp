   #1 detectar el request nombre y estado
   #2 llamar el script de node y pasarle los argumentos del nombre y el estado 
   #3 cuando se termine de ejecutar node guardarlo en una variable y va ir el resultado de la busqueda de la COMPAnia
   #4 regresar el Json con el estatus de la disponibilidad en true o false

from flask import Flask, request, render_template, redirect, url_for
from doctest import COMPARISON_FLAGS
#import requests

app = Flask(__name__)

state_addresses = {
    'California':'https://bizfileonline.sos.ca.gov/search/business',
    'Louisiana':'https://coraweb.sos.la.gov/CommercialSearch/CommercialSearch.aspx',
    'Florida':'https://search.sunbiz.org/Inquiry/CorporationSearch/ByName',
    
}

@app.route('/', methods=['GET', 'POST'])
def index():
    #direccion = "https://bizfileonline.sos.ca.gov/search/business"
    #return redirect(direccion)
   
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 
    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 
    'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 
    'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
    'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 
    'Virginia', 'Washington', 'Washington DC', 'West Virginia', 'Wisconsin', 'Wyoming']

    return render_template('index.html', states = states)

@app.route('/result', methods=['GET', 'POST'])
def get_company_search_values():
    if request.method == "POST":
        company_name = request.form.get('company-name')
        state_name = request.form.get('select-us-states')
        companyname = company_name.upper()
        print(companyname)
        print(state_name)
        return companyname, state_name
    return render_template('index.html')

estado = 'California'
print(state_addresses.get(estado))

if __name__=='__main__':
    app.run(debug=True,port=5000)
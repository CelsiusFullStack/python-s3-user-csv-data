from flask import Flask, request
import pandas as pd_users_csv
# separador de campo, automatic detect with engine python 
SEP=',' 
# Link users csv 
USER_CSV_URL = 'https://docs.google.com/spreadsheets/d/1aZvrEPvNGssSAQjNLJz1XEDBqAOk4nLs/gviz/tq?tqx=out:csv'
#Engine 
EPY='python'
SR=0
EBL=False
app = Flask(__name__)

def controller_users():
    user_data = pd_users_csv.read_csv(USER_CSV_URL,skiprows=SR,engine=EPY)
    user_data.tail()
    return {'status': 'Success', 'File Url' :USER_CSV_URL , 'Total List User': len(user_data)}

@app.route('/users')
def users():
    res = controller_users()
    return res
if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
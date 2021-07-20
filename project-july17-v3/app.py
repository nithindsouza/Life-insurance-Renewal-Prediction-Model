import numpy as np
from flask import Flask, request, render_template
import pickle
from flask_mysqldb import MySQL

#pip install flask_mysqldb
app = Flask(__name__)
model = pickle.load(open('pckl_model.pkl', 'rb'))

app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = 'root'
app.config['MySQL_DB'] = 'renewal_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    temp_output = round(prediction[0], 2)
    if (temp_output==1):
        output="Chances of Customer Renewing Policy: Yes"
    else:
        output="Chances of Customer Renewing Policy : No" 
    # ##MYSQL-FLASK-HTML
    # sex = request.form['sex']
    # Age = request.form['age']
    # children = request.form['children']
    # Smoker = request.form['smoker']
    # bmi = request.form['bmi']
    # education = request.form['education']
    # income = request.form['income']
    # Distinct_Parties_on_Claim = request.form['Distinct_Parties_on_Claim']
    # Type_of_insurance = request.form['Type_of_insurance']
    # Policy_Length = request.form['Policy_Length']
    # Claim_Type = request.form['Claim_Type']
    # Payment_method_ = request.form['Payment_method_']
    # Number_of_declarations = request.form['Number_of_declarations']
    # Number_of_authorizations_ = request.form['Number_of_authorizations_']
    # Handling_time_of_authorizations_and_declarations_ = request.form['Handling_time_of_authorizations_and_declarations_']
    # Duration_of_current_insurance_contract = request.form['Duration_of_current_insurance_contract']
    # Elapsed_time_since_last_contact_moment = request.form['Elapsed_time_since_last_contact_moment']
    # Product_usage_ = request.form['Product_usage_']
    # Elapsed_time_since_the_last_complaint = request.form['Elapsed_time_since_the_last_complaint']
    # Policy_Claim_Day_Diff = request.form['Policy_Claim_Day_Diff']
    # Claim_History = request.form['Claim_History']
    # Renewal_History = request.form['Renewal_History']
    # Customer_Complaint = request.form['Customer_Complaint']
    # Number_of_complaints = request.form['Number_of_complaints']
    # Customer_mentioned_that_they_are_going_to_switch = request.form['Customer_mentioned_that_they_are_going_to_switch']
    # Switching_barrier_ = request.form['Switching_barrier_']
    # Claim_Cancellation = request.form['Claim_Cancellation']
    # Brand_credibility_ = request.form['Brand_credibility_']
    # Claim_After_Renewal = request.form['Claim_After_Renewal']
    # Contracted_care_ = request.form['Contracted_care_']
    # Experience_during_contact_moment = request.form['Experience_during_contact_moment']
    # Premium_price_ = request.form['Premium_price_']
    # Outstanding_charges = request.form['Outstanding_charges']
    # Discount = request.form['Discount']
    # Deductible_excess_ = request.form['Deductible_excess_']
    # Renewal = temp_output
    # cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO renewal_table (sex, Age, children, Smoker,bmi,education, income,Distinct_Parties_on_Claim, Type_of_insurance, Policy_Length, Claim_Type, Payment_method_, Number_of_declarations, Number_of_authorizations_, Handling_time_of_authorizations_and_declarations_, Duration_of_current_insurance_contract, Elapsed_time_since_last_contact_moment, Product_usage_, Elapsed_time_since_the_last_complaint, Policy_Claim_Day_Diff, Claim_History, Renewal_History, Customer_Complaint, Number_of_complaints, Customer_mentioned_that_they_are_going_to_switch, Switching_barrier_, Claim_Cancellation, Brand_credibility_, Claim_After_Renewal, Contracted_care_, Experience_during_contact_moment, Premium_price_, Outstanding_charges, Discount, Deductible_excess_, Renewal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sex, Age, children, Smoker,bmi,education, income,Distinct_Parties_on_Claim, Type_of_insurance, Policy_Length, Claim_Type, Payment_method_, Number_of_declarations, Number_of_authorizations_, Handling_time_of_authorizations_and_declarations_, Duration_of_current_insurance_contract, Elapsed_time_since_last_contact_moment, Product_usage_, Elapsed_time_since_the_last_complaint, Policy_Claim_Day_Diff, Claim_History, Renewal_History, Customer_Complaint, Number_of_complaints, Customer_mentioned_that_they_are_going_to_switch, Switching_barrier_, Claim_Cancellation, Brand_credibility_, Claim_After_Renewal, Contracted_care_, Experience_during_contact_moment, Premium_price_, Outstanding_charges, Discount, Deductible_excess_, Renewal))
    # mysql.connection.commit()
    # cur.close()
    
    return render_template('index.html',prediction_text=output)
if __name__ == "__main__":
    app.run(debug = True)



import numpy as np
from flask import Flask, jsonify , render_template , request


# create a FLask instance
app=Flask(__name__)

model = None # Load Model

@app.route("/")
def Home():
    return render_template("index1.html")

"""
Attrition_Flag               object
Customer_Age                  int64
Gender                       object
Dependent_count               int64
Education_Level              object
Marital_Status               object
Income_Category              object
Card_Category                object
Months_on_book                int64
Total_Relationship_Count      int64
Months_Inactive_12_mon        int64
Contacts_Count_12_mon         int64
Credit_Limit                float64
Total_Revolving_Bal           int64
Avg_Open_To_Buy             float64
Total_Amt_Chng_Q4_Q1        float64
Total_Trans_Amt               int64
Total_Trans_Ct                int64
Total_Ct_Chng_Q4_Q1         float64
Avg_Utilization_Ratio       float64

"""

@app.route("/predict",methods=["POST"])
def predict():
    feat = [float(x) for x in request.form.values()]
    features = np.array(feat)
    predictions = model.predict(features)
    return render_template("index.html",predictions) # look in to it

if __name__ == "__main__":
    app.run(debug=True)

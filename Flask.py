from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')

@app.route('/')
def index():
    location = sorted(data["location"].unique())
    return render_template('index.html', location=location)

if __name__ == "__main__":
    app.run(debug=True)


# import pandas as pd
# import numpy as np
# import pickle
#
# data = pd.read_csv('Cleaned_data.csv')
# pipe = pickle.load(open("data.pkl", "rb"))
#
# # Define input parameters
# location = '7th Phase JP Nagar'
# bhk = 3.00
# bath = 3.00
# sqft = 2000
#
# input_data = pd.DataFrame([[location, bhk, bath, sqft]], columns=['location', 'total_sqft', 'bath', 'bhk'])
# prediction = pipe.predict(input_data)[0] * 1e3
# print(str(np.round(prediction, 2)))


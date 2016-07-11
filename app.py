from flask import Flask, request, render_template, jsonify
import datetime as dt
from dates import holidays
import numpy as np

holidays= list(holidays)

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/day-order', methods=['GET'])
def day_order():
	date = request.args.get('date')
	month = request.args.get('month')
	year = request.args.get('year')

	day_order = 1

	start = dt.date(2016,7,4)
	end = dt.date(int(year),int(month),int(date))
	days = np.busday_count(start, end)

	day_order+=days

	for i in range(len(holidays)):
		if start<holidays[i]<end:
			day_order-=1

	if day_order>5:
		day_order%=5

	if day_order==0:
		day_order=5

	return jsonify({str(end): day_order})

if __name__ == '__main__':
    app.run(debug=True)

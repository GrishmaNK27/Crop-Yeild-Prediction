
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = request.form['Year']
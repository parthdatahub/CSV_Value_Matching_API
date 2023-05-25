from flask import Flask, request, jsonify, render_template
import csv
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    # Check if file has a name
    if file.filename == '':
        return jsonify({'error': 'No file name'})

    # Check if file is a CSV file
    if file.filename.endswith('.csv'):
        template_values = ['value1', 'value2', 'value3']  # Example template values

        # Read the uploaded CSV file
        uploaded_values = []
        csv_reader = csv.reader(file.read().decode('utf-8').splitlines())
        for row in csv_reader:
            uploaded_values.extend(row)

        # Match template values with uploaded values
        matched_values = [value for value in template_values if value in uploaded_values]

        # Prepare CSV response
        response = []
        if matched_values:
            response.append(['Matched Values'])
            response.extend([[value] for value in matched_values])

        # Create a CSV file in memory
        output = StringIO()
        csv_writer = csv.writer(output)
        csv_writer.writerows(response)

        # Return the CSV file as a response
        output.seek(0)
        return output.getvalue(), 200, {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment; filename=result.csv'}
    else:
        return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.run()

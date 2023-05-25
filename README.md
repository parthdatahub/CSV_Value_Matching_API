# CSV_Value_Matching_API
This repository contains a Flask-based API that allows users to upload a CSV file, match its values against a predefined template, and receive a CSV file containing the matching values as the output.

# Problem Statement :

The goal of this project is to develop a CSV Value Matching API using Flask. The API provides two endpoints:

/: A GET request to this endpoint renders an HTML form where users can upload a CSV file.
/upload: A POST request to this endpoint handles the file upload and matching process.
The API checks if a file was uploaded, validates the file name, reads the contents of the CSV file, compares the values with a predefined template, and creates a CSV file containing the matching values. The matching CSV file is then returned as a response, allowing the user to download it.

# Requirements and Features :

Accepts only CSV files for upload.
Uses Flask and relevant libraries for file handling and rendering templates.
Handles various scenarios like missing files, empty files, and incorrect file formats gracefully, returning appropriate error responses.
Implements proper code organization, separation of concerns, and error handling practices.
Provides clear comments and documentation to facilitate understanding.
Ensures performance and scalability of the API.
Thoroughly tests the API, covering different scenarios and edge cases.

# Usage :

To use the CSV Value Matching API, follow these steps:

Clone the repository: $ git clone https://github.com/your-username/csv-value-matching-api.git
Install the necessary dependencies: $ pip install -r requirements.txt
Run the Flask application: $ python app.py
Access the API through your browser at http://localhost:5000.
Upload a CSV file using the provided form.
The API will match the values in the uploaded file against the predefined template and return a CSV file with the matching values as the output.

# Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Feel free to customize the description to fit your repository and provide any additional information or instructions as needed.

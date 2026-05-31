# Python CSV Report Automation

A practical Python automation project that cleans sales data from a CSV file and generates structured business reports.

This project was built as a small freelance-style deliverable: a client provides a raw CSV file, and the script returns cleaned data plus summary reports that can be used for business analysis.

## What This Project Does

The script reads a sales CSV file, cleans and standardizes the data, calculates revenue, filters paid transactions, and generates reports by month, category, and customer.

## Business Problem

Many small businesses and teams still handle reports manually in spreadsheets. This can be repetitive, slow, and error-prone.

This project shows how a simple Python automation can reduce manual work and generate consistent reports from raw data.

## Features

- Reads raw sales data from a CSV file
- Validates required columns before processing
- Cleans dates, numeric values, text fields, and payment status
- Calculates total order amount
- Filters paid transactions
- Generates monthly sales report
- Generates category sales report
- Generates customer spending report
- Supports command-line arguments for custom input/output paths

## Tech Stack

- Python
- Pandas
- CSV data processing
- Command-line interface with argparse

## Project Structure

```text
python-csv-report-automation/
│
├── data/
│   ├── raw/
│   │   └── sample_sales.csv
│   └── processed/
│       └── cleaned_sales.csv
│
├── reports/
│   ├── monthly_sales_report.csv
│   ├── category_sales_report.csv
│   └── customer_sales_report.csv
│
├── src/
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
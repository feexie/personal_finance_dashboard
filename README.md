# Personal Finance Dashboard

Welcome to the Personal Finance Dashboard—an interactive, user-friendly app designed to help users track their income, expenses, and monthly budgets effortlessly. Built using Streamlit and Pandas, this app demonstrates proficiency in data handling, visualization, and web-based interfaces. This project is ideal for individuals aiming to manage their personal finances and provides insights into budgeting trends and spending patterns.

## Features

This app offers the following features to make financial management seamless:

- **Transaction Entry Form**: Users can manually input their financial transactions, selecting a type (income or expense), category, amount, and date.
- **CSV File Upload**: Users can bulk upload transactions in CSV format for faster data entry.
- **Data Visualization**: A pie chart displays expenses by category, providing a visual breakdown of where money is being spent.
- **Budget Tracking**: Users set a monthly budget, and a progress bar indicates how much of the budget has been used.
- **Date Range Filtering**: Users can filter transactions by date to analyze spending within specific periods.
- **Summary Statistics**: Calculates and displays total income, expenses, and net savings for the selected date range.

## Technical Stack

- **Streamlit**: For building an interactive web-based dashboard.
- **Pandas**: For handling and analyzing financial data.
- **Matplotlib**: For visualizing expenses in a pie chart format.

This stack demonstrates proficiency in Python libraries commonly used in data science and web-based applications.

## Installation and Setup

Follow these steps to set up and run the app on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/feexie/personal_finance_dashboard
    cd personal-finance-dashboard
    ```
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the app:
    ```bash
    streamlit run app.py
    ```
5. Open the app:

    Streamlit will open the app in your default browser. You should see the title "Personal Finance Dashboard" on the main page.

## Usage Guide

Here’s how to use each section of the app:

### Adding a Transaction

In the "Add a New Transaction" section, select the transaction type (Income or Expense), choose a category, enter the amount, and specify the date. Click "Add Transaction" to save the transaction. This feature is useful for tracking individual entries on the go.

### Uploading a CSV File

In the "Upload a CSV File" section, upload a CSV file (e.g., sample_data.csv) that includes multiple transactions. The app will display the contents of the file in a table for a quick preview.

### Visualizing Expenses by Category

Once transactions are loaded, the app generates a pie chart to break down expenses by category, making it easy to see where most money is spent.

### Setting a Monthly Budget

In the "Set Monthly Budget Goal" section, use the slider to set a budget. The app displays your current spending as a progress bar, giving you a quick overview of your financial standing.

### Filtering Transactions by Date

Set a start date and end date in the "Filter Transactions by Date" section to view transactions within a specific period. This helps in reviewing financial activities for certain periods.

### Viewing Summary Statistics

At the end of the dashboard, summary statistics provide insights into total income, expenses, and savings within the specified date range, giving a comprehensive financial overview.

## Example Data File (Optional)

You can create a sample data file named `sample_data.csv` with the following structure to upload and test the app:

```plaintext
Date,Type,Category,Amount
2023-01-01,Income,Salary,5000
2023-01-05,Expense,Groceries,150
2023-01-10,Expense,Utilities,100
2023-01-15,Income,Freelance,1200
2023-01-20,Expense,Entertainment,200
2023-01-25,Expense,Transport,50
2023-01-30,Income,Investment,300
```

This file structure allows the app to categorize and process data for display and analysis.

## Future Enhancements

Some potential future improvements for this app include:

- **Persistent Storage**: Storing transaction data locally or in a database for continuous tracking.
- **Enhanced Data Analysis**: Adding charts to show income trends, monthly spending comparisons, and savings goals.
- **User Authentication**: Allowing different users to manage their own financial data.
- **Automated Alerts**: Sending notifications when spending nears the set budget.

## Why This Project Stands Out

This project showcases proficiency in building dynamic and interactive data applications using Streamlit, along with practical knowledge of data analysis and visualization. By creating a well-structured and user-friendly finance app, I demonstrate not only technical skills but also an understanding of end-user needs in personal finance management.

## Contact
For any questions or feedback, feel free to contact me through my [LinkedIn](https://linkedin.com/in/yusuf-yahaya-425482158) or email.

You can reach me at 1yahayamuhammadyusuf@gmail.com for any inquiries or feedback.











## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request to the main repository, describing your changes in detail.

Thank you for your contributions!


























































































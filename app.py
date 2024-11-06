import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the title and introduction
# Section: Upload a CSV File
st.header("Upload a CSV File")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Transactions:")
    st.write(data.head())
st.title("Personal Finance Dashboard")
st.write("Welcome! Use this app to track your expenses, income, and budgeting goals.")
# Section: Add a New Transaction
st.header("Add a New Transaction")

# Select transaction type (Income or Expense)
transaction_type = st.selectbox("Type", ["Expense", "Income"])

# Select category based on type
category = st.selectbox("Category", ["Salary", "Freelance", "Groceries", "Utilities", "Entertainment", "Transport", "Investment", "Other"])

# Amount and date inputs
amount = st.number_input("Amount", min_value=0.0, format="%.2f")
date = st.date_input("Date")

# Button to add transaction
if uploaded_file:
    # Filter data to only expenses
    expense_data = data[data['Type'] == 'Expense']

    # Group expenses by category
    pie_data = expense_data.groupby('Category').sum()

    # Create a pie chart
    st.header("Expense Breakdown by Category")
    fig, ax = plt.subplots()
    ax.pie(pie_data['Amount'], labels=pie_data.index, autopct='%1.1f%%')
    st.pyplot(fig)
if st.button("Add Transaction"):
    st.write(f"Transaction Added: {transaction_type}, {category}, ${amount}, on {date}")
    # Section: Set Monthly Budget Goal
    st.header("Set Monthly Budget Goal")

    # Set budget with a slider
    budget = st.slider("Monthly Budget", min_value=100, max_value=5000, step=100)
    st.write(f"Budget Set: ${budget}")

    if uploaded_file:
        current_spent = expense_data['Amount'].sum()
        st.write(f"Current Spending: ${current_spent:.2f}")

        # Display progress bar
        progress = current_spent / budget
        st.progress(min(progress, 1.0))  # Cap the progress bar at 100%
        # Section: Filter Transactions by Date
        st.header("Filter Transactions by Date")

        start_date = st.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
        end_date = st.date_input("End Date", value=pd.to_datetime("2023-12-31"))

        # Filter data based on date range
        if uploaded_file:
            filtered_data = data[(data['Date'] >= str(start_date)) & (data['Date'] <= str(end_date))]
            st.write("Filtered Transactions:")
            st.write(filtered_data)

            # Calculate total income, expenses, and savings

            # Add some visual appeal with colored metrics
            st.header("Summary Statistics")
            st.markdown(f"<h3 style='color: green;'>Total Income: ${total_income:.2f}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: red;'>Total Expenses: ${total_expense:.2f}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: blue;'>Savings: ${savings:.2f}</h3>", unsafe_allow_html=True)
            total_income = filtered_data[filtered_data['Type'] == 'Income']['Amount'].sum()
            total_expense = filtered_data[filtered_data['Type'] == 'Expense']['Amount'].sum()
            savings = total_income - total_expense

            st.header("Summary Statistics")
            st.write(f"Total Income: ${total_income:.2f}")
            st.write(f"Total Expenses: ${total_expense:.2f}")
            st.write(f"Savings: ${savings:.2f}")
# Loan_Amortization_Schedule
Creating a Loan Amortization Schedule with Prepayments using Python and Pandas

**Introduction**

Managing a loan can be a complex task, especially when it comes to tracking payments, interest, and prepayments. In this article, we’ll explore a Python script that generates a loan amortization schedule with the ability to apply prepayments. The script utilizes the Pandas library for data manipulation and Excel export.

**Loan Amortization Schedule**

A loan amortization schedule is a detailed table that breaks down each loan payment into its principal and interest components over the loan term. It helps borrowers understand how their payments are allocated and how the loan balance decreases over time.

**The Python Script**

The provided Python script calculates a loan amortization schedule with prepayments and generates an Excel file containing the schedule. It also calculates the total interest savings and tenure reduced due to the prepayments.

**Understanding the Code**

**Importing Libraries:** The script starts by importing the required libraries — pandas for data manipulation.
Defining the Main Function: The calculate_loan_schedule function is defined to calculate the loan schedule and prepayment-related details. It takes the loan amount, annual interest rate, loan term in months, and monthly prepayment amount as input.

**Calculating Monthly Payment:** The function calculates the monthly payment using the formula for calculating a fixed monthly payment for a loan with compound interest.

**Initializing Variables:** The function initializes variables like schedule to store the monthly payment details, remaining_balance to track the outstanding loan amount, and original_loan_amount and original_loan_term_months to store the original loan details for later use.

**Iterating Through Loan Term**: The function then iterates through each month of the loan term and calculates the interest payment, principal payment, and remaining balance for each month.

**Applying Prepayments:** The function applies prepayments during the first 8 years (96 months) of the loan term. The prepayment amount is added to the monthly payment during this period to expedite the loan payoff.

**Creating the Schedule:** The function appends the calculated details for each month to the schedule list.

**Calculating Summary:** The function calculates the total interest savings and the total tenure reduced due to prepayments.

**Example Usage:** The script provides an example usage section where you can input your loan details and get the loan schedule and summary.

**Creating DataFrame and Exporting to Excel:** The script converts the schedule list into a Pandas DataFrame and exports it to an Excel file named ‘loan_schedule.xlsx’.

**Displaying Summary:** The script prints the generated loan schedule’s Excel file path and displays the summary of total interest savings and tenure reduced.

**Conclusion**

Managing a loan can be made easier with a loan amortization schedule. This Python script demonstrates how to create a comprehensive loan schedule with prepayments using the Pandas library. By inputting your loan details into the example section, you can generate your personalized loan schedule and understand the impact of prepayments on interest savings and tenure reduction.

The provided script can be a valuable tool for borrowers looking to optimize their loan payments and understand the financial implications of making extra payments towards their loan. Additionally, this script can be extended and integrated into financial applications to provide loan tracking and repayment analysis to users.

Remember to always exercise caution and perform due diligence before making any financial decisions, as the terms and conditions of loans can vary.

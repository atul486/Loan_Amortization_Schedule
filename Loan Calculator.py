import pandas as pd

def calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_months, monthly_prepayment):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / (
            (1 + monthly_interest_rate) ** loan_term_months - 1)

    schedule = []
    remaining_balance = loan_amount

    original_loan_amount = loan_amount
    original_loan_term_months = loan_term_months

    for month in range(1, loan_term_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment

        if month <= 8 * 12:  # Apply prepayments only for the first 5 years
            remaining_balance -= (monthly_payment + monthly_prepayment - interest_payment)
        else:
            remaining_balance -= (monthly_payment - interest_payment)

        if remaining_balance <= 0:
            # Loan is fully paid, no need to continue calculating the schedule
            loan_term_months = month
            break

        schedule.append({
            'Month': month,
            'Monthly Payment': monthly_payment,
            'Interest Payment': interest_payment,
            'Principal Payment': principal_payment,
            'Prepayment': monthly_prepayment if month <= 8 * 12 else 0,
            'Remaining Balance': max(0, remaining_balance)  # Ensure balance doesn't go negative
        })

    # Calculate total interest savings and total tenure reduced
    original_interest = (monthly_payment * original_loan_term_months) - original_loan_amount
    new_interest = (monthly_payment * loan_term_months) - loan_amount
    interest_savings = original_interest - new_interest
    tenure_reduced_months = original_loan_term_months - loan_term_months

    summary = {
        'Total Interest Savings': interest_savings,
        'Total Tenure Reduced (months)': tenure_reduced_months
    }

    return schedule, summary

if __name__ == "__main__":
    # Example usage:
    loan_amount = 10600000  # Replace with your loan amount
    annual_interest_rate = 9.0  # Replace with your annual interest rate
    loan_term_years = 30  # Replace with your loan term in years
    monthly_prepayment = 50000  # Replace with your monthly prepayment amount

    loan_term_months = loan_term_years * 12

    schedule, summary = calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_months, monthly_prepayment)

    # Create a DataFrame from the loan schedule
    df = pd.DataFrame(schedule)

    # Export DataFrame to Excel
    output_file = 'loan_schedule.xlsx'
    df.to_excel(output_file, index=False)

    # Display summary
    print(f"Loan schedule has been generated and exported to '{output_file}'.")
    print("Summary:")
    print(summary)

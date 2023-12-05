# Tip Calculator

This is a simple Python script for calculating the total bill including a tip and splitting it among a specified number of people. It's a handy tool for calculating how much each person should contribute to a bill when dining out or sharing expenses.

## How to Use

1. Run the script by executing the Python code in your preferred Python environment.

```bash
python tip_calculator.py
```

2. You will be prompted to enter the following information:
   - **Total Bill Amount:** Enter the total amount of the bill.
   - **Tip Percentage:** Choose the tip percentage you want to give (10%, 12%, or 15%).
   - **Number of People:** Enter the number of people with whom you want to split the bill.

3. After providing the required information, the script will calculate the total payment including the tip and the amount each person should pay.

4. The script will then display the amount each person should contribute, rounded to two decimal places.

## Example

```bash
Welcome to the tip calculator.

What was the total bill? $100.50
What percentage tip would you like to give? 10, 12, or 15?12
How many people to split the bill?4

Each person should pay: $28.14
```

## Notes

- The script accepts bill amounts as floating-point numbers, tip percentages as integers (10, 12, or 15), and the number of people as integers.
- The final amount for each person is rounded to two decimal places for clarity.
- Feel free to modify and use this script as needed to simplify your bill-splitting calculations.
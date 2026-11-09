student_name = (input("Student Name: "))
daily_transport_cost = float(input("Daily Transport Cost: NGN "))
daily_feeding_cost = float(input("Daily Feeding Cost: NGN "))
number_of_days = int(input("Number of days on campus: "))
other_expenses = float(input("Other weekly expenses: NGN "))
total_transport = daily_transport_cost * number_of_days
total_feeding = daily_feeding_cost *number_of_days
total_weekly = total_transport + total_feeding + other_expenses
print("WEEKLY EXPENSE SUMMARY")
print(f"student: {student_name}")
print(f"transport total: NGN {daily_transport_cost:,.2f}")
print(f"feeding total: NGN {daily_feeding_cost:,.2f}")
print(f"other expenses: NGN {other_expenses:,.2f}")
print(f"Weekly total: NGN {total_weekly:,.2f}")
                             

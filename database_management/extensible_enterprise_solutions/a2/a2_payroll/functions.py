#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

def get_requirements():
    print("Payroll Calcuator");
    print("\nProgram Requirements\n"+
    "1. Must use float data type for user input.\n"+
    "2. Overtime rate: 1.5 times hourly rate (hours over 40).\n"+
    "3. Holiday rate: 2.0 times hourly rate (all holiday hours).\n"+
    "4. Must format currency with dollar sign, and round to two decimal places.\n"+
    "5. Create at least three functios that are caed by the program:\n"+
    "\ta. main(): cals at least two other functions"+
    "\tb. get_requirements(): displays the program requirements."+
    "\tc. calculate_payroll(): calcuates an individual one week paycheck.");


def payroll():
    print("\nInput:\n");
    standard_hours = float(input("Enter hours worked: "));
    holiday_hours = float(input("Enter holiday hours: "));
    hour_pay_rate = float(input("Enter hourly pay rate: "));

    if standard_hours<= 40:
        base_pay = standard_hours * hour_pay_rate
    else:
        base_pay = 40 * hour_pay_rate
    holiday_pay = 2 * (holiday_hours * hour_pay_rate)

    if standard_hours > 40:
        overtime_pay = ((standard_hours - 40) * hour_pay_rate) * 1.5
    else:
        overtime_pay = 0
    gross_pay = base_pay + holiday_pay + overtime_pay
    
    print("\nOutput:\n");
    print("Base pay: "+ "${0:.2f}".format(base_pay));
    print("Overtime pay: "+ "${0:.2f}".format(overtime_pay));
    print("Holiday pay: "+ "${0:.2f}".format(holiday_pay));
    print("Gross pay: "+ "${0:.2f}".format(gross_pay));
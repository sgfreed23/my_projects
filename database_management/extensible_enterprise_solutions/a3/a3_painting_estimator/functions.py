#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

SQFT_PER_GALLON =350

def get_requirements():
    print("Painting Estimator");
    print("\nProgram Requirements:\n"+
    "1. Calculate home interior paint cost (w/0 primer).\n"+
    "2. Must use float data types.\n"+
    "3. Must use SQFT_PER_GALLON constant.\n"+
    "4. Nust use iteration structure.\n"+
    "5. Format, right-align numbers, and round to two decimal places.\n"+
    "6. Create at least five functios that are called by the program:\n"+
    "\ta. main(): calls two other functions: get_requirements() and estimate_painting_cost()\n"+
    "\tb. get_requirements(): displays the program requirements.\n"+
    "\tc. estimate_painting_cost(): calculates interior home painting, and calls print functions.\n"+
    "\td. print_painting_estimate(): displays painting costs.\n"+
    "\te. print_painting_percentage(): displays paiting costs percentages.\n");

def estimate_painting_cost():
    user_continue = "y"
    while user_continue == "y":
        print("\nInput:")
        sqft = float(input("Enter total interior sq ft: "))
        ppg = float(input("Enter price per gallon of paint: "))
        rate = float(input("Enter painting rater per sq ft: "))

        print("\nOutput:")
        print_painting_estimate(sqft,ppg,rate)
        print_painting_percentage(sqft,ppg,rate)

        valid_input =False
        while valid_input != True:
            user_continue = input("Estimate another paint job? (y/n): ").lower()
            valid_input = user_continue == "y" or user_continue == "n"
    print("\nThank you for using our Painting Estimator")
    print("\nPlease see our web site: http://www.mysite.com")
    print()

def print_painting_estimate(sqft, ppg, rate):
    gallons = sqft / SQFT_PER_GALLON
    print("{0:23} {1:>9}".format("Item", "Amount"))
    print("{0:23} {1:>9,.2f}".format("Total Sq Ft:", sqft))
    print("{0:23} {1:>9,.2f}".format("Sq Ft per Gallon:", SQFT_PER_GALLON))
    print("{0:23} {1:>9,.2f}".format("Number of Gallons:", gallons))
    print("{0:23} {1:>8,.2f}".format("Paint Per Gallon:", ppg))
    print("{0:23} {1:>8,.2f}".format("Labor per Sq Ft:", rate))
    print()

def print_painting_percentage(sqft, ppg, rate):
    gallons = sqft / SQFT_PER_GALLON
    total_paint = gallons * ppg
    total_labor = rate * sqft
    total = total_paint + total_labor
    pct_paint = total_paint / total * 100
    pct_labor = total_labor / total * 100
    pct_total = pct_paint + pct_labor
    print("{0:9} {1:>10} {2:>12}".format("Cost", "Amount", "Percentage"))
    print("{0:9} {1:>9,.2f} {2:>11.2f}%".format("Paint:", total_paint, pct_paint))
    print("{0:9} {1:>9,.2f} {2:>11.2f}%".format("Labor:", total_labor, pct_labor))
    print("{0:9} {1:>9,.2f} {2:>11.2f}%".format("Total:", total, pct_total))
    print()


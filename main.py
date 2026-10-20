"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = annual_cost / (credits * SEMESTERS_PER_YEAR)
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost

def cost_of_skipped(class_period_cost, skipped_classes):
    """Give back the cost of skipped class periods by multiplying the cost of one class period by the number of skipped classes."""
    total_skipped_cost = (class_period_cost) * skipped_classes
    return total_skipped_cost
# ---- PROGRAM ----

def main():
    cost_per_year = float(input("Enter the annual cost of college: "))
    credits_this_semester = int(input("Enter the number of credits you are taking this semester: "))

    while True:
        # Show your menu here.
        print("")
        print("MAIN MENU: The Cost of College")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per 1 class period")
        print("6. Cost of skipped class periods. Worth it?") 
        print("Q. Quit")
        print("")
        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(cost_per_year):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(cost_per_year):.2f}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(cost_per_year):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(cost_per_year, credits_this_semester):.2f}")
        elif choice == "5":
            print(f"Cost per 1 class period: ${cost_per_class(cost_per_year, credits_this_semester):.2f}")
        elif choice == "6":
            skipped_classes = int(input("Enter the number of class periods you skipped: "))
            class_period_cost = cost_per_class(cost_per_year, credits_this_semester)
            print(f"Cost of skipped class periods: ${cost_of_skipped(class_period_cost, skipped_classes):.2f}")
        else:   
            print("Invalid option. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()

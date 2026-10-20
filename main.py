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


# ---- PROGRAM ----

def main():
    cost_per_year = float(input("Enter the annual cost of college: "))
    credits_this_semester = int(input("Enter the number of credits you are taking this semester: "))

    while True:
        # Show your menu here.

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
            print(f"Cost per class: ${cost_per_class(cost_per_year, credits_this_semester):.2f}")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()

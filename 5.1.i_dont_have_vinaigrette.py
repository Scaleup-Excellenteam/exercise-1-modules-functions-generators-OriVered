import random
from datetime import datetime, timedelta

def random_date_between(start_date, end_date):
    """
    Generate a random date between two given dates.

    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.

    Returns:
        random_date (datetime): A random date between the start and end dates.
    """
    delta = end_date - start_date
    random_days = random.randrange(delta.days + 1)
    return start_date + timedelta(days=random_days)


if __name__ == "__main__":
    """
    Get two dates as input from the user, generate a random date between them,
    and print the result. If the random date is a Monday, print "אין לי ויניגרט!".
    """
    start_date_str = input("Enter the first date (YYYY-MM-DD): ")
    end_date_str = input("Enter the second date (YYYY-MM-DD): ")

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    random_date = random_date_between(start_date, end_date)

    print(f"Random date: {random_date.strftime('%Y-%m-%d')}")

    if random_date.weekday() == 0:
        print("אין לי ויניגרט!")
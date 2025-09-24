import datetime
def display_current_datetime():
    now = datetime.datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date(days):
    future_date = datetime.datetime.now() + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")
def main():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: ")) 
    future_date = calculate_future_date(days)
    print(f"Future date: {future_date}")
if __name__ == "__main__":
    main()
from datetime import datetime

def show_date_time():
    now = datetime.now()

    print("Current Date and Time")
    print("---------------------")
    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%I:%M:%S %p"))
    print("Day:", now.strftime("%A"))
    print("Month:", now.strftime("%B"))
    print("Year:", now.strftime("%Y"))

show_date_time()

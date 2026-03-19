def convert_time_duration(hours):
    # calculate days
    days = int(hours // 24)
    # calculate remaining hours
    remaining_hours = hours % 24
    # calculate minutes
    minutes = int((remaining_hours % 1) * 60)
    # calculate remaining hours after subtracting minutes
    hours = int(remaining_hours)
    return days, hours, minutes

def main():
    hours = 50.5
    days, hours, minutes = convert_time_duration(hours)
    print(f"{days} days, {hours} hours, {minutes} minutes")

main()
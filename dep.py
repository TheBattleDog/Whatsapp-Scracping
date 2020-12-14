from datetime import datetime


def get_current_time():
    return datetime.now()


def to_time(s_time):
    time = datetime.now()
    try:
        time = time.strptime(s_time, "%I:%M %p")
    except ValueError:
        time.replace(hour=0)
    return time

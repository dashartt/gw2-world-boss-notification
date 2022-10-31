from datetime import datetime, timedelta
import pytz


def convert_to_time(value):
    return value.strftime("%H:%M")    


def convert_to_datetime(value):
    return datetime.strptime(value, '%H:%M')    


def get_time():
    brazil_timezone = pytz.timezone("Brazil/East")         
    current_time = datetime.now(brazil_timezone)
    return convert_to_time(current_time)    


def addition_n_minutes(value, minutes):  
    time_converted =  convert_to_datetime(value)

    time_added = time_converted + timedelta(minutes=minutes)

    return convert_to_time(time_added)    

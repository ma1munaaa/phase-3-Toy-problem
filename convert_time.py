def convert_to_24_hour(hour, minute, time_period):
    if time_period == "am":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:  
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
    
    
    hour_str = str(hour_24).zfill(2)
    minute_str = str(minute).zfill(2)
    
    return hour_str + minute_str


print(convert_to_24_hour(10, 30, "am"))  
print(convert_to_24_hour(11, 20, "pm"))  
print(convert_to_24_hour(6, 45, "am"))  
print(convert_to_24_hour(3, 55, "pm"))  

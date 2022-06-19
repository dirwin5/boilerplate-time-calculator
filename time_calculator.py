def add_time(start, duration, starting_day=None):
    
    start_l = start.split()
    #get start am/pm
    start_ampm = start_l[1]
    #get start hrs and mins
    start_time = start_l[0]
    start_time_l = start_time.split(':')
    start_hr = int(start_time_l[0])
    start_mins = int(start_time_l[1])
           
    #get duration hrs and mins
    duration_l = duration.split(':')
    duration_hrs = int(duration_l[0])
    duration_mins = int(duration_l[1])
       
    #output mins
    output_mins = start_mins + duration_mins
    if output_mins >= 60:
        output_mins = output_mins % 60
        duration_hrs += 1
    #convert to string
    output_mins = str(output_mins)
    if len(output_mins) == 1:
        output_mins = f"0{output_mins}"
    
      
    #output hour
    output_hour = (start_hr + duration_hrs) % 12
    if output_hour == 0:
        output_hour = 12
    
    #no of am/pm switches
    ampm_switches = (start_hr + duration_hrs) / 12
    ampm_switches = int(ampm_switches)
    
    #get output am/pm
    if ampm_switches % 2 == 0:
        output_ampm = start_ampm
    elif start_ampm == 'AM':
        output_ampm = 'PM'
    else:
        output_ampm = 'AM'
        
    #construct basic new time
    new_time = f"{output_hour}:{output_mins} {output_ampm}"    
    
    #get number of days difference
    half_day = 0
    if start_ampm == 'PM':
        half_day += 1
    half_day += ampm_switches
    days_no = half_day / 2
    days_no = int(days_no)   
    
    #test if starting day is given
    if starting_day is not None:
        days_l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        starting_day = starting_day.capitalize()
        starting_day_index = days_l.index(starting_day)
        output_day_index = (starting_day_index + days_no) % 7
        output_day = days_l[output_day_index]
        new_time = f"{new_time}, {output_day}"
        
    #test and add number of days
    if days_no == 1:
        new_time = f"{new_time} (next day)"
    if days_no >= 2:
        new_time = f"{new_time} ({days_no} days later)"
        
           
    return new_time
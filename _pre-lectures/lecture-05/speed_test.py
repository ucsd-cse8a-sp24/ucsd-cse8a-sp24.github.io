def speed_msg(isRainy, speed):
    
    if isRainy:
        if speed <=30:
            msg = "Drive Safely"
        else:
            msg = "It's rainy! SLOW DOWN!"
    else:
        if speed <= 40:
            msg = "Thank you!"
        else:
            msg = "Slow Down!"
            
    return msg

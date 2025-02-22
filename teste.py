import datetime

myinput = '07:10:00'

def extract_features_time(time:str):
    aux = time.split(':')
    hour = int(aux[0])
    minute = int(aux[1])
    second = int(aux[2])
    return hour,minute, second

print(extract_features_time(myinput))
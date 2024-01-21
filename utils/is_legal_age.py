import time

# birthdate: comes from time.strptime(birthdate, "%Y-%m-%d")
def is_legal_age(birthdate: time.struct_time):
    today = time.localtime()
    age = today.tm_year - birthdate.tm_year - ((today.tm_mon, today.tm_mday) < (birthdate.tm_mon, birthdate.tm_mday))
    return age >= 18

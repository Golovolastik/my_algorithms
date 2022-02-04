seconds = 5

def make_readable(seconds):
    HH = seconds // 3600
    MM = (seconds - HH * 3600) // 60
    SS = seconds - HH * 3600 - MM * 60
    return f"{str(HH).zfill(2)}:{str(MM).zfill(2)}:{str(SS).zfill(2)}"

print(make_readable(seconds))

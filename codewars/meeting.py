s = 'Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn'

def meeting(s):
    a = s.split(";")
    a = [x.upper() for x in a]
    a = sorted([x.split(":")[::-1] for x in a])
    a = [str('(' + x[0] + ', ' + x[1] + ')') for x in a]
    a = "".join(a)
    return a

print(meeting(s))
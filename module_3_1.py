calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(s):
    count_calls()
    tuple_ = (len(s), s.upper(), s.lower())
    return tuple_

def is_contains(s, l):
    count_calls()
    flag = False
    s = s.lower()
    for i in range(len(l)):
        l[i] = l[i].lower()
        if l[i] == s:
            flag = True
            return flag
            break
    return flag

print(string_info('Still a Live'))
print(string_info('blood run'))
print(is_contains('Aerowalk', ['Aero', 'walk', 'AeRoWaLk']))
print(is_contains('Camp Grounds', ['amp', 'gRound', 'CampGrounds']))
print(calls)




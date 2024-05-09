def find_short(s):
    # your code here
    x = s + ' '
    l = []
    for pos, char in enumerate(x):

        if char == ' ':
            l.append(pos)
            
    i = len(l) - 1

    k = []


    if min(filter(lambda x: x > 0, l)) > 0:
        return min(filter(lambda x: x > 0, l))
    while i >= 0:
        k.append(l[i] - l[i - 1] - 1)
            
        i-=1

    #print(min(filter(lambda x: x > 0, k)))
    return l



def test_cases():
    assert find_short("bitcoin take over the world maybe who knows perhaps") == 3
    assert find_short("turns out random test cases are easier than writing out basic ones") == 3
    
    assert find_short("lets talk about javascript the best language") == 3
    assert find_short("i want to travel the world writing code one day") == 1
    assert find_short("Lets all go on holiday somewhere very cold") == 2
    assert find_short("Let's travel abroad shall we") == 2

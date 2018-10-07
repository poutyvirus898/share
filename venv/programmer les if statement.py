lengte = float(input('vul hier je lengte in: '))
lengtGrens = 1.20
def lang_genoeg(lengte):
    if lengte >= lengtGrens:
        print('je bent lang genoeg!')
    else:
        print('sorry, je bent te klein!')
lang_genoeg(lengte)
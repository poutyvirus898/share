leeftijd = int(input('voer hier je leetijd in: '))
passpoort = str(input('heb je een passpoort? ja/nee: '))

if leeftijd >= 18 and passpoort == 'ja':
    print('gefeliciteerd! je mag stemmen')
else:
    print('sorry, je mag niet stemmen')

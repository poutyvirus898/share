grondtallen = [ 4, 5, 3, -81 ]

def kwadraten_som(grondtallen):
    som = 0
    for nummer in grondtallen:
        if nummer < 0:
            return 0

        som = (som + nummer)**2
    return som



kwadraten_som(grondtallen)
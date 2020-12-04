def validar(key=None):
    eje_legal = ['Legal', 'Neutral', 'Caótico']
    eje_moral = ['Bueno', 'Neutral', 'Maligno']

    sintax = {'Cualquiera no legal': [], 'Cualquiera legal': [], 'Cualquiera': [], 'Cualquiera Neutral': []}

    for legal in eje_legal:
        for moral in eje_moral:
            if legal == moral:
                name = 'Neutral Auténtico'
            else:
                name = ' '.join([legal, moral])

            if legal == 'Legal':
                sintax['Cualquiera legal'].append(name)
            elif legal != 'Legal':
                sintax['Cualquiera no legal'].append(name)
            if legal == 'Neutral' or moral == 'Neutral':
                sintax['Cualquiera Neutral'].append(name)
            sintax['Cualquiera'].append(name)

    if key is None:
        return sintax

    elif key in sintax:
        return sintax[key]

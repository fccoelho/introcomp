from romanos import converte_romanos, soma_janelas

def test_soma_janelas():
    nrl = [10,10,10,1,10]
    res = soma_janelas(nrl)
    assert res ==[20,1,10]

def test_convert_I():
    esperado = 1
    ar = 'I'
    resposta  = converte_romanos(ar)
    assert resposta == esperado

def test_convert_2():
    esperado = 2
    ar = 'II'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_3():
    esperado = 3
    ar = 'III'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_4():
    esperado = 4
    ar = 'IV'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_5():
    esperado = 5
    ar = 'V'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_6():
    esperado = 6
    ar = 'VI'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_7():
    esperado = 7
    ar = 'VII'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_8():
    esperado = 8
    ar = 'VIII'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_9():
    esperado = 9
    ar = 'IX'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_i():
    esperado = 1
    ar = 'i'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_10():
    esperado = 10
    ar = 'X'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_11():
    esperado = 11
    ar = 'XI'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_15():
    esperado = 15
    ar = 'XV'
    resposta = converte_romanos(ar)
    assert resposta == esperado

def test_convert_14():
    esperado = 14
    ar = 'XIV'
    resposta = converte_romanos(ar)
    assert resposta == esperado

"""
Testes para o módulo AS.
"""
import AS

def test_autor():
    assert isinstance(AS.AUTOR, str)
    assert len(AS.AUTOR) >= 1
    
def test_numquestions():
    for i in range(5):
        assert hasattr(AS, f'questao_{i+1}')
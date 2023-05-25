"""
Testes para a estrutura da entrega da avaliação 2.
"""
import a2

def test_autores():
    assert len(a2.AUTORES) == 2
    
def test_numquestions():
    for i in range(10):
        assert hasattr(a2, f'questao_{i+1}')
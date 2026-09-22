import pytest
from src.agendamento import pode_agendar

@pytest.mark.parametrize("horas, esperado", [
    (23.99, False), 
    (24.0, True),   
    (500, True),    
    (2160, True),   
    (2161, False),  
], ids=["test_menos_24h", "test_24h", "test_entre", "test_90_dias", "test_mais_90_dias"])
def test_validacao_antecedencia(horas, esperado):
    assert pode_agendar(horas) == esperado

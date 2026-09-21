## APÊNDICE A — Guia de execução manual passo a passo

*Aplicado para simulação das saídas descritas nas Etapas 11, 12 e 13, que dependem de runtime externo.*

**1. Preparação do ambiente**
Em um terminal (bash/powershell):
```bash
python -m venv venv
# No windows: venv\Scripts\activate
# No mac/linux: source venv/bin/activate
pip install pytest pytest-cov
```

**2. Arquivo do Desenvolvedor (`agendamento.py`)**
Crie o arquivo com o código abaixo:
```python
LIMITE_MIN_HORAS = 24
LIMITE_MAX_HORAS = 90 * 24

def pode_agendar(horas_antecedencia):
    return LIMITE_MIN_HORAS <= horas_antecedencia <= LIMITE_MAX_HORAS
```

**3. Arquivo do QA (`test_agendamento.py`)**
Crie o arquivo com os testes parametrizados:
```python
import pytest
from agendamento import pode_agendar

@pytest.mark.parametrize("horas, esperado", [
    (23.99, False), 
    (24.0, True),   
    (500, True),    
    (2160, True),   
    (2161, False),  
], ids=["test_menos_24h", "test_24h", "test_entre", "test_90_dias", "test_mais_90_dias"])
def test_validacao_antecedencia(horas, esperado):
    assert pode_agendar(horas) == esperado
```

**4. Execução dos testes e cobertura (Simulação SAÍDA ESPERADA)**
Comando 1 (Rodar testes com relatório v):
`pytest test_agendamento.py -v`
*Saída Esperada (Simulação):*
```
test_agendamento.py::test_validacao_antecedencia[test_menos_24h] PASSED
test_agendamento.py::test_validacao_antecedencia[test_24h] PASSED
...
```
Comando 2 (Rodar cobertura):
`pytest --cov=agendamento --cov-report=term-missing`
*Saída Esperada (Simulação):*
```
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
agendamento.py       3      0   100%
----------------------------------------------
```

**5. Renderização do Diagrama Mermaid**
Para visualizar o StateDiagram da Etapa 6, copie o bloco `mermaid` e cole no editor online gratuito em `https://mermaid.live`, ou instale a extensão "Markdown Preview Mermaid Support" no VS Code.

**6. Exportação para PDF**
Para converter este documento Markdown para entrega acadêmica (PDF), abra o arquivo no VS Code, instale a extensão `Markdown PDF` e execute o atalho `Export (pdf)`.

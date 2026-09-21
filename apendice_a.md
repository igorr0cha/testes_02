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

**4. Execução dos testes e cobertura (SAÍDA REAL)**
Comando 1 (Rodar testes com relatório v):
`python -m pytest test_agendamento.py -v`
*Saída Real:*
```
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\igor.itr\Videos\testes-02
plugins: cov-7.1.0
collecting ... collected 5 items

test_agendamento.py::test_validacao_antecedencia[test_menos_24h] PASSED  [ 20%]
test_agendamento.py::test_validacao_antecedencia[test_24h] PASSED        [ 40%]
test_agendamento.py::test_validacao_antecedencia[test_entre] PASSED      [ 60%]
test_agendamento.py::test_validacao_antecedencia[test_90_dias] PASSED    [ 80%]
test_agendamento.py::test_validacao_antecedencia[test_mais_90_dias] PASSED [100%]

============================== 5 passed in 0.08s ==============================
```
Comando 2 (Rodar cobertura):
`python -m pytest --cov=agendamento --cov-report=term-missing test_agendamento.py`
*Saída Real:*
```
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\igor.itr\Videos\testes-02
plugins: cov-7.1.0
collected 5 items

test_agendamento.py .....                                                [100%]

=============================== tests coverage ================================
______________ coverage: platform win32, python 3.13.14-final-0 _______________

Name             Stmts   Miss  Cover   Missing
----------------------------------------------
agendamento.py       4      0   100%
----------------------------------------------
TOTAL                4      0   100%
============================== 5 passed in 0.15s ==============================
```

**5. Renderização do Diagrama Mermaid**
Para visualizar o StateDiagram da Etapa 6, copie o bloco `mermaid` e cole no editor online gratuito em `https://mermaid.live`, ou instale a extensão "Markdown Preview Mermaid Support" no VS Code.

**6. Exportação para PDF**
Para converter este documento Markdown para entrega acadêmica (PDF), abra o arquivo no VS Code, instale a extensão `Markdown PDF` e execute o atalho `Export (pdf)`.

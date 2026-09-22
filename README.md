# Testes 02 - MediClinic

Projeto acadêmico de testes da regra de antecedência para agendamento.

## Estrutura

- `src/`: código da aplicação.
- `tests/`: testes automatizados com pytest.
- `docs/`: dossiê, apêndice de execução e material de apoio.
- `artifacts/`: PDFs e imagens gerados ou fornecidos como evidência.

Documentos principais:

- [Dossiê de QA](docs/Dossie_QA_MediClinic.md)
- [Apêndice de execução](docs/apendice_a.md)

As imagens e PDFs em `artifacts/` são evidências complementares; o código executável
fica exclusivamente em `src/` e os testes em `tests/`.

## Executar

```bash
source .venv/bin/activate
python -m pytest tests/test_agendamento.py -v
python -m pytest --cov=src.agendamento --cov-report=term-missing tests/test_agendamento.py
```

O ambiente virtual é opcional, mas recomendado. Para prepará-lo:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest pytest-cov
```
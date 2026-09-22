LIMITE_MIN_HORAS = 24
LIMITE_MAX_HORAS = 90 * 24

def pode_agendar(horas_antecedencia):
    return LIMITE_MIN_HORAS <= horas_antecedencia <= LIMITE_MAX_HORAS

OK_RESULT: 'yes'
FATAL_RESULT = 'no'

def check_if_aprove_or_not() -> str:

    result = input('¿Eres del Madrid?')

    if isinstance(result, str):
        if result.lower() == 'no':
            return 'Aprobado'
        return 'Suspendido'
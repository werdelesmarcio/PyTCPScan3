import socket
import sys

def verificar_porta(target, port):
    try:
        conexao = connect(target, port)
        return (port, conexao == 1)
    except socket.gaierror:
        return ('Erro', 'Hostname could not be resolved. Exiting')
    except socket.error:
        return ('Erro', 'Could not connect to target')

def imprimir_resultado(resultado):
    port, status = resultado
    if port == 'Erro':
        print(f' {status}')
        sys.exit()
    else:
        estado = 'OPEN' if status else 'CLOSE'
        cor = '\033[1;31m' if status else '\033[1;33m'
        print(f' [+] {"POSITIVE" if status else "NEGATIVE"} TO Port {port}:\tStatus: {cor}{estado}\033[m')

def main(target, ip, fp):
    try:
        for port in range(ip, fp+1):
            resultado = verificar_porta(target, port)
            imprimir_resultado(resultado)
    except KeyboardInterrupt:
        print('\n You pressed Ctrl+C\n The application has been stopped prematurely.')
        sys.exit()
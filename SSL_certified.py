import ssl
import socket
from datetime import datetime, timezone

def checa_ssl(domain, timeout=10, alerta_dias=30):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                certificado = ssl_sock.getpeercert()

        expira = datetime.strptime(certificado["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
        agora = datetime.now(timezone.utc)
        rest_dias = (expira - agora).days

        if rest_dias <= 0:
            status = "Expirado"
        elif rest_dias <= alerta_dias:
            status = 'Alerta'
        else:
            status = 'OK'

        return {
            "status": status,
            "Emitido": certificado["notBefore"],
            "Expira": expira.strftime("%d/%m/%Y %H:%M:%S %Z"),
            "Dias_restantes": rest_dias,
        }
    except Exception as error:
        return{
            "status": "error",
            "error": str(error)
        }



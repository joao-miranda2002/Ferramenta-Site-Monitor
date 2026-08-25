import json
from datetime import datetime

#importando funções
from SSL_certified import checa_ssl
from DNS_monitor import checa_dns
from Perfomance import checa_site
from Dominio import checa_dominio
from analise import get_analise
from notifica import notificando

config_arqv = "config.exemplo.json"

def carrega_config():
    with open(
        config_arqv,
        "r",
        encoding="utf-8"
    ) as arquivo:
        return json.load(arquivo)

def print_secao(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)

def monitor_cliente(cliente, settings):
    nome = cliente['nome']
    dominio = cliente['dominio']
    url = cliente['url']

    timeout = settings['timeout']
    alerta_dias = settings['Alerta_SSL']
    servidor_dns = settings['servidor_dns']

    print_secao(nome)

    print(f"Domínio: {dominio}")
    print(f"URL: {url}")

    #----------------------------------------------------------
    # SITE
    #----------------------------------------------------------

    print("\n[ SITE ]")

    website = checa_site(
        url,
        timeout
    )

    print(f"Status HTTP: {website.get('status_code')}")
    print(f"tempo: {website.get('response_time')}s")
    print("Online: ", website.get("online"))

    #----------------------------------------------------------
    # SSL
    #----------------------------------------------------------

    print('\n[ SSL ]')
    ssl = checa_ssl(
        dominio,
        timeout,
        alerta_dias
    )

    print(f"Status: {ssl.get('status')}")
    print(f"Dias restantes: {ssl.get('Dias_restantes')}")
    print(f"Expira: {ssl.get('Expira')}")

    #----------------------------------------------------------
    # DNS
    #----------------------------------------------------------

    print('\n[ DNS ]')

    dns = checa_dns(dominio, servidor_dns)

    for tipo_registro, registros in dns.items():
        print(f'\n{tipo_registro}:')

        for registro in registros:
            print(f'    {registro}')

    #----------------------------------------------------------
    # DOMÍNIO
    #----------------------------------------------------------

    print('\n[ DOMÍNIO ]')

    status_domain = checa_dominio(dominio)

    print(f"Status: {status_domain['status']}")

    #----------------------------------------------------------
    # ANALYTICS
    #----------------------------------------------------------
    
    print('\n[ ANALYTICS ]')

    analytics = get_analise(dominio)

    print(f"Status: {analytics['status']}")

    #----------------------------------------------------------
    # RESULTADO
    #----------------------------------------------------------
    
    return{
        "cliente": nome,
        "domain": dominio,
        "timestamp": datetime.now().isoformat(),
        "website": website,
        "ssl": ssl,
        "dns": dns,
        "Status_domain": status_domain,
        "Analytics": analytics
    }

def main():

    config = carrega_config()

    settings = config["settings"]

    print_secao("MONITOR SITE")
    print(f"Execução: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    resultados = []

    for cliente in config['clientes']:
        resultado = monitor_cliente(
            cliente, 
            settings
        )

        resultados.append(resultado)

    print_secao("MONITORAMENTO FINALIZADO")

if __name__ == "__main__":
    main()
        

    
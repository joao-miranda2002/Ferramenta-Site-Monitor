import dns.resolver

def registro(domain, tipo_registro, server_dns):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = server_dns

        respostas = resolver.resolve(domain, tipo_registro)
        return [
            str(resposta)
            for resposta in respostas
        ]
    except Exception:
        return[]

def checa_dns(domain, server_dns):
    dado_dns = {
        "A": registro(
            domain,
            "A",
            server_dns
        ),

        "AAAA": registro(
            domain,
            "AAAA",
            server_dns
        ),

        "MX": registro(
            domain,
            "MX",
            server_dns
        ),

        "TXT": registro(
            domain,
            "TXT",
            server_dns
        )
    }

    dado_dns["WWW_CNAME"] = registro(
        f"www.{domain}",
        "CNAME",
        server_dns
    )

    return dado_dns
import time
import requests

def checa_site(url, timeout = 10):
    try:
        start = time.perf_counter()

        response = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True
        )

        decorre =  time.perf_counter() - start

        return {
            "online": 200 <= response.status_code < 400,
            "status_code": response.status_code,
            "response_time": round(decorre, 3),
            "final_url": response.url
        }

    except requests.RequestException as error:
        return{
            "online": False,
            "status_code": None,
            "response_time": None,
            "error": str(error)
        }
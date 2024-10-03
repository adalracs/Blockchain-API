import requests
from error_handler import log_error, log_info

class BlockchainStatusClient:
    def __init__(self, base_url="http://64.202.191.20:5000"):
        self.base_url = base_url
        self.endpoint = "/is_chain_up"

    def check_chain_status(self):
        try:
            response = requests.get(f"{self.base_url}{self.endpoint}")
            response.raise_for_status()  # Raise an exception for HTTP errors

            data = response.json()
            status = {
                "is_active": data.get("is_up", False),
                "status_code": response.status_code
            }

            log_info("transacciones", "Chain Status Check", f"Status: {status}")
            return status

        except requests.RequestException as e:
            error_message = f"Error checking chain status: {str(e)}"
            log_error("transacciones", "critico", "API Request Failed", error_message)
            return {
                "is_active": False,
                "status_code": getattr(e.response, 'status_code', None),
                "error": error_message
            }

# Ejemplo de uso
if __name__ == "__main__":
    client = BlockchainStatusClient()
    status = client.check_chain_status()
    print(status)
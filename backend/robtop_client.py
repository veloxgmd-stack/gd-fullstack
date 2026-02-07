import requests


class RobTopClient:
    BASE_URL = "http://www.boomlings.com/database/"
    SECRET = "Wmfd2893gb7"

    def __init__(self):
        self.headers = {
            "User-Agent": "",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def _post(self, endpoint: str, payload: dict) -> str:
        """
        Internal method to send POST requests to RobTop servers.
        """

        url = f"{self.BASE_URL}{endpoint}.php"

        data = payload.copy()
        data["secret"] = self.SECRET

        response = requests.post(url, data=data, headers=self.headers)

        if response.text.strip() == "-1":
            raise Exception("Server returned -1 (Invalid request)")

        return response.text

    def _parse_colon_response(self, text: str) -> dict:
        """
        Parses colon-separated response into dictionary.
        """

        parts = text.split(":")
        parsed = {}

        for i in range(0, len(parts) - 1, 2):
            key = parts[i]
            value = parts[i + 1]
            parsed[key] = value

        return parsed

    def get_user_info(self, account_id: str) -> dict:
        """
        Fetch user info from RobTop servers.
        """

        raw = self._post("getGJUserInfo20", {
            "targetAccountID": account_id
        })

        parsed = self._parse_colon_response(raw)

        return self._map_user_fields(parsed)

    def _map_user_fields(self, data: dict) -> dict:
        """
        Maps numeric response keys to readable fields.
        """

        return {
            "username": data.get("1"),
            "playerID": data.get("2"),
            "stars": int(data.get("3", 0)),
            "demons": int(data.get("4", 0)),
            "rank": int(data.get("6", 0)),
            "accountID": data.get("16"),
            "coins": int(data.get("13", 0)),
            "userCoins": int(data.get("17", 0)),
            "diamonds": int(data.get("46", 0)),
            "cp": int(data.get("8", 0)),
            "icon": int(data.get("21", 0)),
            "ship": int(data.get("22", 0)),
            "ball": int(data.get("23", 0)),
            "ufo": int(data.get("24", 0)),
            "wave": int(data.get("25", 0)),
            "robot": int(data.get("26", 0)),
            "spider": int(data.get("43", 0)),
            "col1": int(data.get("10", 0)),
            "col2": int(data.get("11", 0)),
            "glow": data.get("28") == "1"
        }

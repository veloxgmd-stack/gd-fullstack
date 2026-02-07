from robtop_client import RobTopClient
import json

client = RobTopClient()

user = client.get_user_info("3541866")  # vortrox

print(json.dumps(user, indent=2))

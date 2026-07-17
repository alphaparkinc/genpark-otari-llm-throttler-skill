from client import OtariLlmThrottlerClient
client = OtariLlmThrottlerClient()
print(client.check_health(3000, 0.02))
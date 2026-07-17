class OtariLlmThrottlerClient:
    def check_health(self, stream_latency_ms: int, error_rate: float) -> dict:
        action = "throttle" if stream_latency_ms > 2500 or error_rate > 0.05 else "pass"
        return {"throttle_action": action, "fallback_active": action == "throttle"}
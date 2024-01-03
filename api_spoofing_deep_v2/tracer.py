from jaeger_client import Config


def initialize_tracer():
    config = Config(
        config = {
            'sampler': {'type': 'const', 'param': 1}
        },
        service_name = 'api-spoofing-deep-v2'
    )
    return config.initialize_tracer()
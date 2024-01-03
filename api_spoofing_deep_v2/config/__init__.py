from loguru import logger


def init_configuration():
    logger.level("RESPONSE", no=15, color="<green><green>")
    logger.level("LATENCY", no=15, color="<blue><bold>")
    logger.level("EXCEPTION", no=25, color="<red><bold>")
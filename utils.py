import os
import logging
import logging.handlers

PATH = os.path.abspath(os.path.dirname(__file__))


def spawn_logger(cfg, logger_name):
    """
    Get logger instance for config_name and logger name
    :param cfg: Current config name
    :param logger_name: Logger name, now error and info
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        os.path.join(PATH, 'logs/%s.%s.log' % (cfg, logger_name)),
        backupCount=5
    )
    handler.setFormatter(logging.Formatter(u'[%(asctime)s]  %(message)s'))
    logger.addHandler(handler)

    return logger


def get_variable(cfg, name, default, false_condition, fail_message):
    v = getattr(cfg, name, default)
    if false_condition(v):
        raise RuntimeError(fail_message)

    return v
import logging

# ANSI escape codes for colors
COLOR_CODES = {
    'RED': '\033[91m',
    'YELLOW': '\033[93m',
    'GREEN': '\033[92m',
    'RESET': '\033[0m'
}


def configure_logger():
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Set formatter
    formatter = LoggerFormatter('%(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(ch)


class LoggerFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        if levelname == 'ERROR':
            level_color = COLOR_CODES['RED']
        elif levelname == 'WARNING':
            level_color = COLOR_CODES['YELLOW']
        elif levelname == 'INFO':
            level_color = COLOR_CODES['GREEN']
        else:
            level_color = COLOR_CODES['RESET']

        original_message = record.msg
        formatted_levelname = f"{level_color}{levelname}"
        formatted_message = f"{level_color}{original_message}{COLOR_CODES['RESET']}"

        record.levelname = formatted_levelname
        record.msg = formatted_message

        return super().format(record)
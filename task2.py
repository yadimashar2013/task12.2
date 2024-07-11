import requests as rq
import logging


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('RequestsLogger')
logger.setLevel(logging.DEBUG)


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING


class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


# cозаем обрабочик файлов
info_handler = logging.FileHandler('success_responses.log')
warning_handler = logging.FileHandler('bad_responses.log')
error_handler = logging.FileHandler('blocked_responses.log')

# настройка обработчика и форматировщика
info_handler.setLevel(logging.INFO)
warning_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(message)s')
info_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)


# добавление обработчика к logger
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)
info_handler.addFilter(InfoFilter())
warning_handler.addFilter(WarningFilter())
error_handler.addFilter(ErrorFilter())


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com',
         'https://tiktok.com', 'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger.info(f'INFO: {site}, response - 200')
        else:
            logger.warning(f'WARNING: {site}, response - {response.status_code}')
    except Exception:
        logger.error(f"ERROR: {site}, NO CONNECTION")





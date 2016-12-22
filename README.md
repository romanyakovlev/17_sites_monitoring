# 17_sites_monitoring

Скрипт, который получает файл, состоящий из списка сайтов. Затем проверяет их на работоспособность.

# Подготовка

Устанавливаем необходимые библиотеки:
- requests
- whois
- datetime
- python-dateutil
- tld
- argparse

```sh
pip install -r requirements.txt
```

# Запуск

Запускаем скрипт

```sh
python3 check_sites_health.py file.txt
```
где file.txt - название вашего файла, передаваемого в качестве аргумента.

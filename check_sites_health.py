import requests
import argparse
import whois
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tld import get_tld


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    file_name = parser.parse_args().file_name
    return file_name


def load_urls4check(filepath):
    with open(filepath, 'r') as html_list:
        html_list_string = html_list.read()
    return html_list_string.split('\n')


def is_server_respond_with_200(url):
        site_request = requests.get(url)
        if site_request.status_code is 200:
            return True
        else:
            return False


def get_domain_expiration_date(domain_name):
    top_lvl_domain = check_edu_and_gov_tlds(get_tld(domain_name))
    whois_info = whois.whois(top_lvl_domain)
    one_month = relativedelta(months=+1)
    month_later = datetime.today() + one_month
    expiration_date = whois_info.expiration_date
    if expiration_date > month_later:
        return True
    else:
        return False


# whois не получает информацию по поддоменам .gov.ru / .edu.ru - запрашиваем gov.ru / edu.ru

def check_edu_and_gov_tlds(tld_string):
    if '.gov.ru' in tld_string:
        return 'gov.ru'
    if '.edu.ru' in tld_string:
        return 'edu.ru'
    return tld_string


def output_information(site_url, is_respond, is_paid):
    print("'{}' статус:\nstatus code 200 - {}\nоплачен на месяц "
             "вперед - {}\n".format(site_url, 'да' if is_respond else 'нет', 'да' if is_respond else 'нет'))


def get_site_info(site_url):
    is_respond = is_server_respond_with_200(site_url)
    is_paid = get_domain_expiration_date(site_url)
    return is_respond, is_paid


def go_throught_all_sites(sites_list):
    for site_url in sites_list:
        is_respond, is_paid = get_site_info(site_url)
        output_information(site_url, is_respond, is_paid)


if __name__ == '__main__':
    file_name = parse_arguments()
    sites = load_urls4check(file_name)
    print('Мониторинг сайтов\n')
    go_throught_all_sites(sites)

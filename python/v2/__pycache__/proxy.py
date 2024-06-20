from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_ip_port = 'ip:port'  # Substitua 'ip:port' pelo endereço do seu proxy

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy_ip_port}')

driver = webdriver.Chrome(options=chrome_options)

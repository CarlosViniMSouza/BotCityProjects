from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot, Browser, By
from botcity.plugins.http import BotHttpPlugin

def search_city_api(bot):
    http = BotHttpPlugin("https://servicodados.ibge.gov.br/api/v1/localidades/estados/13/regioes-metropolitanas")
    returnJSON = http.get_as_json()

    listCities = []

    for item in returnJSON:
        for value in item['municipios']:
            listCities.append(value['nome'])

    return listCities

def search_climate(bot, city):
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(city)
    bot.wait(1000)
    bot.enter()

def get_data(bot):
    count = 0

    while True:
        count += 1
        week_day = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[1]', By.XPATH).text
        max_temp = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[1]', By.XPATH).text
        min_temp = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[2]', By.XPATH).text

        print(f'Dia: {week_day} | Temperatura: Max = {max_temp} | Min = {min_temp}')

        if count == 8:
            break

def main():
    bot = WebBot()

    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://servicodados.ibge.gov.br/api/v1/localidades/estados/13/regioes-metropolitanas")

    # logic

    try:
        cities = search_city_api(bot)

        for value in cities:
            bot.browse("https://google.com")
            search_climate(bot, f'clima {value}, AM')
            
            print(f'\n Cidade: {value}')
            get_data(bot)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(3000)

    bot.stop_browser()

    print('Finished!')

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()

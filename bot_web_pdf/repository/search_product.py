from webdriver_manager.microsoft import EdgeChromiumDriverManager
from botcity.web import WebBot, Browser, By
from botcity.plugins.http import BotHttpPlugin

def search_product(bot, product):
    """
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(product)
    bot.wait(1000)
    bot.enter()
    """ 

    return null

def get_data(bot):
    """
    count = 0

    while True:
        count += 1
        week_day = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[1]', By.XPATH).text
        max_temp = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[1]', By.XPATH).text
        min_temp = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[2]', By.XPATH).text

        print(f'Dia: {week_day} | Temperatura: Max = {max_temp} | Min = {min_temp}')

        if count == 8:
            break
    """

    return null

def main():
    bot = WebBot()

    bot.browser = Browser.EDGE
    bot.driver_path = EdgeChromiumDriverManager().install()
    bot.browse("https://flordejambu.com/shop/")

    try:
        cities = search_city_api(bot)

        for product in cities:
            bot.browse("https://google.com")
            search_product(bot, product)
            
            print(f'\n Produto pesquisado: {product}')
            get_data(bot)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(3000)

    bot.stop_browser()

    print('Finished!')

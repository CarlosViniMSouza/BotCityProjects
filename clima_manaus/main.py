from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def search_city(bot, city):
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)
        print('carregando')

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

        print(f'Dia: {week_day}')
        print('Temperatura:')
        print(f'Max = {max_temp} | Min = {min_temp} \n')

        if count == 8:
            break

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://www.google.com")

    try:
        search_city(bot, 'clima manaus')
        bot.wait(1000)
        get_data(bot)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(3000)

    bot.wait(3000)
    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Import Webdriver_manager (added manually)
from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# added manually function
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

        # max_temp: //*[@id="web"]/ol[1]/li/div/div/div[2]/div/ul/li[1]/span/div[2]/span[1]
        max_temp = bot.find_element(f'//*[@id="web"]/ol[1]/li/div/div/div[2]/div/ul/li[1]/span/div[2]/span[1]').text

        # min_temp: //*[@id="web"]/ol[1]/li/div/div/div[2]/div/ul/li[1]/span/div[2]/span[2]
        min_temp = bot.find_element(f'//*[@id="web"]/ol[1]/li/div/div/div[2]/div/ul/li[1]/span/div[2]/span[2]').text

        print(f'Dia: {week_day}')
        print('Temperatura:')
        print(f'Max = {max_temp} | Min = {min_temp} \n')

        if count == 8:
            break

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("https://www.google.com")

    # Implement here your logic...
    try:
        search_city(bot, 'manaus clima')
        bot.wait(1000)
        get_data(bot)

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(3000)

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

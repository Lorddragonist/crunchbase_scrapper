import asyncio
from pyppeteer import launch
from pyppeteer.errors import NetworkError

async def main():
    try:
        browser = await launch(headless=False)
        page = await browser.newPage()
        await page.goto('https://www.upwork.com/nx/jobs/search/?sort=recency')
        selector = '.onetrust-accept-btn-handler'
        await page.waitForSelector(selector)
        print('Selector de coockies encontrado')
        await asyncio.sleep(2)
        await page.click(selector)
        print('Se dio click')
    #     await page.screenshot({'path': 'images/upwork.png'})
    # except TimeoutError:
    #     print("Error: El selector no apareció dentro del tiempo de espera.")
    except NetworkError as error:
        print(f"Error de red: {error}")
    finally:
        try:
            await asyncio.sleep(20)  # Pausa adicional antes de cerrar el navegador
            print('Se pauso antes de cerrar')
            #await browser.close()
        except NetworkError as error:
            print(f"Error de red al cerrar el navegador: {error}")

def ask_credentials():
    user = input('Por favor ingrese su usuario')
    pwd = input('Por favor use su contraseña')
    return {'user':user,'pwd':pwd}

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

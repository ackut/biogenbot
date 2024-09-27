from dotenv import load_dotenv
from yandex_gpt import YandexGPT, YandexGPTConfigManagerForAPIKey


load_dotenv()
config = YandexGPTConfigManagerForAPIKey()
yandex_gpt = YandexGPT(config_manager=config)



async def generate_bio(data: dict):
    messages = [
        {
            'role': 'system',
            'text': f'Придумай биографию для игрового персонажа, учитывая следующие данные: персонажа зовут {data["name"]}, ему {data["age"]} лет, сейчас он живёт в городе {data["city"]}, сейчас он работает {data["current_job"]}'
        }
    ]
    return await yandex_gpt.get_async_completion(messages=messages, timeout=600)

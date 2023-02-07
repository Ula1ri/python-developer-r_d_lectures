class Bot:
    def __init__(self, name,):
        self.name = name
    def say_name(self, name):
        return Bot(self.say_name)
    def send_message(self, message):
        return Bot(self.send_message())


class TelegramBot(Bot):
    def __init__(self, url, chat_id):
        self.url = url
        self.chat_id = chat_id
    def send_massage(self, message):
        super().send_message()
        return TelegramBot(self.send_message())
    def set_url(self, url):
        self.url = url
        print(url)
    def set_chat_id(self, chat_id):
        self.chat_id = chat_id
        print(f'TG bot says{message} to chat {chat_id} using {url}')

some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot('TG')
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
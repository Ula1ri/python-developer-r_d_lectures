class Bot:
    def __init__(self, name,):
        self.name = name
    def say_name(self, name):
        print(self.name)
    def send_message(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
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
        print(f'TG bot says{message} to chat {self.chat_id} using {self.url}')

some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot('TG')
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
from main import (updater, dp, CommandHandler, requests, json, config)

def myResponseOk(myResponse, context, update):
    jData = json.loads(myResponse.content)
    print(jData)
    result = []
    for key in jData['data']:
        result.append(str(key))
        result.append("\n")
    context.bot.send_message(chat_id=update.message.chat_id, text="".join(result))

#----Define telegram bot logic bellow----
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Alice's here! I'm Rades Ghani's bot. Nice to meet you!")
    print('success')
start_handler = CommandHandler('start', start)
dp.add_handler(start_handler)

def data_user(update, context):
    myResponse = requests.get(config.teleConfig.api+"/data_user")
    if(myResponse.ok):
        myResponseOk(myResponse, context, update)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
data_user_handler = CommandHandler('data_user', data_user)
dp.add_handler(data_user_handler)

def yearly(update, context):
    keyword = update.message.text.strip()
    keyword = keyword.split(" ",2)
    myResponse = requests.post(config.teleConfig.api+"/yearly", data = {"keyword":keyword[1], "year":keyword[2]})
    if (myResponse.ok):
        myResponseOk(myResponse, context, update)
    else:
        myResponse.raise_for_status(config.teleConfig.api+"/yearly")
yearly_handler = CommandHandler('yearly', yearly)
dp.add_handler(yearly_handler)
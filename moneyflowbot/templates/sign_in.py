def text_ask_for_key():
    text = ""
    text += "Отправи следующим сообщеним свой ключ"
    return text


def text_success(key):
    text = ""
    text += "Ключ: " + str(key) + " , успешно записан."
    text += "\n" + "теперь ты можешь семло записывать свои расходы"
    return text

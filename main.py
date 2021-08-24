import vk_api
import tkinter, time
from threading import Thread


VERSION = "v.0.1.0"


#Raid Funcions

def send_message(msg, conv_id, to_conv = True):
    if to_conv:
        user_id_ = 2000000000 + conv_id
    else:
        user_id_ = conv_id
    print(user_id_)

    return vk.messages.send(peer_id = user_id_, message = msg, random_id = 0)

def raid(conv_id, is_to_ls, counter_text):
    global counter
    while True:
        send_message("🐶🐱🐭🐹🐰🐻🧸🐼🐻‍❄️🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🦍🦧🐔🐧🐦🐤🐣🐥🐺🦊🦝 🐗 🐴 🦓 🦒 🦌 🦘 🦥 🦦 🦫 🦄 🐝 🐛 🦋 🐌 🪲 🐞 🐜 🦗 🪳 🕷 🕸 🦂 🦟 🪰 🪱 🦠 🐢 🐍 🦎 🐙 🦑 🦞 🦀 🦐 🦪 🐠 🐟 🐡 🐬 🦈 🦭 🐳 🐋 🐊 🐆 🐅 🐃 🐂 🐄 🦬 🐪 🐫 🦙 🐘 🦏 🦛 🦣 🐐 🐏 🐑 🐎 🐖 🦇 🐓 🦃 🕊 🦅 🦆 🦢 🦉 🦩 🦚 🦜 🦤 🪶 🐕 🦮 🐕‍🦺 🐩 🐈 🐈‍⬛ 🐇 🐀 🐁 🐿 🦨 🦡 🦔 🐾 🐉 🐲 🦕 🦖 🌵 🎄 🌲 🌳 🌴 🪴 🌱 🌿 ☘ 🍀 🎍 🎋 🍃 🍂 🍁 🌾 🌺 🌻 🌹 🥀 🌷 🌼 🌸 💐 🍄 🌰 🐚 🌎 🌍 🌏 🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 🌙 🌚 🌝 🌛 🌜 ⭐ 🌟 💫 ✨ ☄ 🪐 🌞 ☀ 🌤 ⛅ 🌥 🌦 ☁ 🌧 ⛈ 🌩 ⚡ 🔥 💥 ❄ 🌨 ☃ ⛄ 🌬 💨 🌪 🌫 🌈 ☔ 💧 💦 🌊", conv_id, is_to_ls)
        counter += 1
        counter_text["text"] = "Отправлено: " + str(counter)

def raid_launcher():
    start_btn.destroy()
    counter_text = tkinter.Label(text = "Отправлено:")
    counter_text.pack()
    Thread(target=raid, args=(int(conv_id.get()), is_to_ls.get(), counter_text )).start()

#Auth
token = "ВАШ ТОКЕН"
session = vk_api.VkApi(token = token)
vk = session.get_api()


#Draw simple UI
root = tkinter.Tk()

#Temp vars
counter = 0
is_to_ls = tkinter.BooleanVar()
is_to_ls.set(0)

root.title("Raid by PyPro " + VERSION)

tkinter.Label(text = "Настройка рейда...", font = "Arial 25").pack()
tkinter.Label(text = "ID беседы/ЛС для рейда").pack()
conv_id = tkinter.Entry()
conv_id.pack()
to_ls_checkbox = tkinter.Checkbutton(text = "Рейд в беседу", variable = is_to_ls)
to_ls_checkbox.pack()
tkinter.Label(text = "Интервал между спамом в секундах(1; 0.5; 0.05)").pack()
timer = tkinter.Entry(text = "0.5")
timer.pack()
timer.insert(0, "0.5")
start_btn = tkinter.Button(text = "Запуск рейда", command = raid_launcher)
start_btn.pack()


root.mainloop()

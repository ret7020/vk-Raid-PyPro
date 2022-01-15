import vk_api
import tkinter, time
from threading import Thread
import vk_captchasolver as vc
from random import randint
from config import *

sid, solved_captcha_code = None, None
#Raid Funcions

def send_message(msg, conv_id, to_conv, captcha_sid=None, captcha_code=None):
    if to_conv:
        user_id_ = 2000000000 + conv_id
    else:
        user_id_ = conv_id
    if DEBUG: print("Sending to", user_id_)
    return vk.messages.send(peer_id=user_id_, message=msg, random_id=0, captcha_sid=captcha_sid, captcha_key=captcha_code)
def edit_message(msg, msg_id, conv_id, to_conv=True, captcha_sid=None, captcha_code=None):
    if to_conv:
        user_id_ = 2000000000 + conv_id
    else:
        user_id_ = conv_id
    print(user_id_)
    return vk.messages.edit(peer_id=user_id_, message=msg, message_id = msg_id, random_id=0, captcha_sid=captcha_sid, captcha_key=captcha_code)
def raid(conv_id, is_to_ls, counter_text):
    global counter, sid, solved_captcha_code
    while True:
        try:
            #Lite message bypassing
            if anti_iris_mode.get():
                message_id = send_message("Всем привет!", conv_id, is_to_ls, captcha_sid=sid, captcha_code=solved_captcha_code)
                edit_message(3 * MESSAGE + str(randint(1000, 9999)), message_id, conv_id, is_to_ls, captcha_sid=sid, captcha_code=solved_captcha_code)
            #Raid
            else:
                send_message(3 * MESSAGE + str(randint(1000, 9999)), conv_id, is_to_ls, captcha_sid=sid, captcha_code=solved_captcha_code)
            counter += 1
            counter_text["text"] = "Отправлено: " + str(counter)
        except vk_api.Captcha as captcha:
            if DEBUG: print("Captcha needed. Solving...")
            sid = captcha.sid
            if DEBUG: print(f"Captcha data {sid}")
            solved_captcha_code = vc.solve(sid=sid, s=1)
            if DEBUG: print(f"Solved code {solved_captcha_code}")




def raid_launcher():
    start_btn.destroy()
    counter_text = tkinter.Label(text = "Отправлено:")
    counter_text.pack()
    Thread(target=raid, args=(int(conv_id.get()), is_to_ls.get(), counter_text )).start()

#Auth

session = vk_api.VkApi(token = TOKEN)
vk = session.get_api()


#Draw simple UI
root = tkinter.Tk()

#Temp vars
counter = 0
is_to_ls = tkinter.BooleanVar()
is_to_ls.set(0)
anti_iris_mode = tkinter.BooleanVar()
anti_iris_mode.set(0)

root.title("Raid by PyPro " + VERSION)

tkinter.Label(text = "Настройка рейда...", font = "Arial 25").pack()
tkinter.Label(text = "ID беседы/ЛС для рейда").pack()
conv_id = tkinter.Entry()
conv_id.pack()
to_ls_checkbox = tkinter.Checkbutton(text = "Рейд в беседу", variable = is_to_ls)
to_ls_checkbox.pack()
to_antiiris_checkbox = tkinter.Checkbutton(text = "Обход Ириса и др.", variable = anti_iris_mode)
to_antiiris_checkbox.pack()
tkinter.Label(text = "Интервал между спамом в секундах(1; 0.5; 0.05)").pack()
timer = tkinter.Entry(text = "0.5")
timer.pack()
timer.insert(0, "0.5")
start_btn = tkinter.Button(text = "Запуск рейда", command = raid_launcher)
start_btn.pack()


root.mainloop()

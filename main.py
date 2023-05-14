import play

play.set_backdrop("light blue")



@play.when_program_starts#функція для початку програми
def start():
    text1 = play.new_text(words="г-грати, с-спати, ї-їсти, п-погладити", x=0, y=280, font_size=50)
    text2 = play.new_text(words="Привіт, я Аміго!", x=0, y=240, font_size=50)
    play.new_image(image="Amigo_privetstvie.png", x=0, y=0, size=40)

@play.repeat_forever#ігровий цикл
def do():
    pass


play.start_program()#запуск програми
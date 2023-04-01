
def main(pbot, p8_bot, p8_human):
    
    phuman = 1 - pbot
    pbot_8 = (p8_bot * pbot) / (p8_bot * pbot + p8_human * phuman)
    print(pbot_8)

if __name__ == "__main__":

    pbot = 0.1
    p8_bot = 0.8
    p8_human = 0.05

    main(pbot, p8_bot, p8_human)

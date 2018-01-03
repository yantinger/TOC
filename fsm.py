from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text  
        return text.lower() == 'i wanna play lol'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'i wanna dissolve runestones'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'i wanna play a game'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'i wanna graduate'

    def on_enter_state4(self, update):
        update.message.reply_text("really wanna pass??")
        #self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
    

    def is_going_to_state45(self, update):
        text = update.message.text
        return text.lower() == 'yes'

    def on_enter_state5(self, update):
        update.message.reply_photo("https://i.imgur.com/uDZB8d2.jpg")
        #self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state4')

    def is_going_to_state55(self, update):
        text = update.message.text
        return text.lower() == 'fail'

    def on_enter_state5(self, update):
        update.message.reply_photo("https://i.imgur.com/uDZB8d2.jpg")
        #self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state4')

    def is_going_to_state56(self, update):
        text = update.message.text
        return text.lower() == 'pass'

    def on_enter_state6(self, update):
        update.message.reply_photo("https://i.imgur.com/iTqF4vW.jpg")
        #self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state4')

    def is_going_to_state66(self, update):
        text = update.message.text
        return text.lower() == 'fail'

    def on_enter_state6(self, update):
        update.message.reply_photo("https://i.imgur.com/iTqF4vW.jpg")
        #self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
    

    def is_going_to_state67(self, update):
        text = update.message.text
        return text.lower() == 'pass'

    def on_enter_state7(self, update):
        update.message.reply_photo("https://i.imgur.com/NEaRNG3.jpg")
        #self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')

    def is_going_to_state77(self, update):
        text = update.message.text
        return text.lower() == 'fail'

    def on_enter_state7(self, update):
        update.message.reply_photo("https://i.imgur.com/NEaRNG3.jpg")
        #self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')



    def is_going_to_state78(self, update):
        text = update.message.text
        return text.lower() == 'pass'

    def on_enter_state8(self, update):
        update.message.reply_photo("https://i.imgur.com/n5WiAoE.jpg")
        #self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')



    def is_going_to_state88(self, update):
        text = update.message.text
        return text.lower() == 'fail'

    def on_enter_state8(self, update):
        update.message.reply_photo("https://i.imgur.com/n5WiAoE.jpg")
        #self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')

    def is_going_to_state89(self, update):
        text = update.message.text
        return text.lower() == 'pass'

    def on_enter_state9(self, update):
        update.message.reply_photo("https://i.imgur.com/NsTenQs.jpg")
        #self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')


    def is_going_to_state99(self, update):
        text = update.message.text
        return text.lower() == 'pass'

    def on_enter_state9(self, update):
        update.message.reply_photo("https://i.imgur.com/NsTenQs.jpg")
        #self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')


    def is_going_to_state9u(self, update):
        text = update.message.text
        return text.lower() == 'home'

    def on_enter_user(self, update):
        update.message.reply_text("what do you want to do now?play?graduate?")
        #self.go_back(update)

    def on_exit_user(self, update):
        print('Leaving state9')



    def is_going_to_state4u(self, update):
        text = update.message.text
        return text.lower() == 'home'

    def on_enter_user(self, update):
        update.message.reply_text("what do you want to do now?play?graduate?")
        #self.go_back(update)

    def on_exit_user(self, update):
        print('Leaving state9')


    def on_enter_state1(self, update):
        update.message.reply_text("Welcome to the summoner's rift")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("Welcome to Tower of Savior")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("Sorry,there's no game to play")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

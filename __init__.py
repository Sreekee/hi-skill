from mycroft import MycroftSkill, intent_file_handler


class Hi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hi.intent')
    def handle_hi(self, message):
        self.speak_dialog('hi')


def create_skill():
    return Hi()


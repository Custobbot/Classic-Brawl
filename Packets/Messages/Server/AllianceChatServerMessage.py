from Utils.Writer import Writer


class AllianceChatServer(Writer):

    def __init__(self, client, player, msg_content):
        super().__init__(client)
        self.msg_content = msg_content
        self.id = 24312
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(self.player.messageTick)
        self.writeVint(0)
        self.writeVint(1)
        self.writeString(self.player.name)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.msg_content)
        self.writeVint(-1040385)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        print("[INFO] Message AllianceChatServerMessage has been sent.")
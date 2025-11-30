class User:
    def __init__(self, u_name):
        self.username = u_name
        self.chatroom = None
    
    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")


class ChatRoom:
    def __init__(self, name ):
        self.name = name
        self.users = []
        self.messages = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message) 
    
    def show_chat_history(self):
        print(f"\nChat History of {self.name}")
        for msg in self.messages:
            print(msg)


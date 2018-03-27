from flask import Flask, request
from handler.users import UsersHandler
from handler.chats import ChatsHandler
from handler.messages import MessageHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "DB Project"

@app.route('/Home')
def welcome():
    return "Welcome to DB Chat!"

@app.route('/Users')
def users():
    handler = UsersHandler()
    return handler.getAllUsers()

@app.route('/Users/<int:user_id>')
def getUserById(user_id):
    return UsersHandler().getUserByID(user_id)

@app.route('/GroupChats')
def chats():
    handler = ChatsHandler()
    return handler.getAllChats()

@app.route('/GroupChats/<int:chat_id>')
def getChatById(chat_id):
    return ChatsHandler().getChatByID(chat_id)

@app.route('/GroupChats/<string:chat_name>')
def getChatByName(chat_name):
    return ChatsHandler().findChat(chat_name)

@app.route('/GroupChats/Messages')
def messages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/GroupChats/Messages/<int:message_id>')
def getMessageById(message_id):
    return MessageHandler().getMessageByID(message_id)

@app.route('/GroupChats/Messages/Chat/<int:chat_id>')
def getChatMessages(chat_id):
    return MessageHandler().findChatMessages(chat_id)

if __name__ == '__main__':
    app.run()
from flask import Flask, request
from handler.users import UsersHandler
from handler.chats import ChatsHandler
from handler.messages import MessageHandler
from handler.reactions import ReactionsHandler
from handler.members import MembershipHandler
from handler.replies import ReplyHandler

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
    handler = UsersHandler()
    return handler.getUserByID(user_id)

@app.route('/Messages')
def getMessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/Users/Messages/<int:user_id>')
def getMessagesByUID(user_id):
    handler = MessageHandler()
    return handler.findUserMessages(user_id)

@app.route('/Messages/Replies')
def getReplies():
    handler = ReplyHandler()
    return handler.getAllReplies()

@app.route('/Users/Messages/Replies/<int:owner_id>')
def getRepliesByOwnerID(owner_id):
    handler = ReplyHandler()
    return handler.findByOwnerID(owner_id)



@app.route('Messages/Replies/<int:rep_id>')
def getRepliesByID(rep_id):
    handler = ReplyHandler()
    return handler.getReplyByID(rep_id)


@app.route('/Users/Memberships')
def memberships():
    handler = MembershipHandler()
    return handler.getAllMemberships()

@app.route('/Users/Memberships/<int:user_id>')
def membershipsByUID(user_id):
    handler = MembershipHandler()
    return handler.getMembershipByUID(user_id)

@app.route('/GroupChats')
def chats():
    handler = ChatsHandler()
    return handler.getAllChats()

@app.route('/GroupChats/<int:chat_id>')
def getChatById(chat_id):
    handler = ChatsHandler()
    return handler.getChatByID(chat_id)


# @app.route('/GroupChats/Messages')
# def messages():
#     handler = MessageHandler()
#     return handler.getAllMessages()

# @app.route('/GroupChats/Messages/<int:message_id>')
# def getMessageById(message_id):
#     return MessageHandler().getMessageByID(message_id)

@app.route('/GroupChats/Messages/<int:chat_id>')
def getChatMessages(chat_id):
    handler = MessageHandler()
    return handler.findChatMessages(chat_id)

@app.route('/GroupChats/Messages/Replies/<int:message_id>')
def getRepliesByMessageID(message_id):
    handler = ReplyHandler()
    return handler.findMessagesReplies(message_id)

@app.route('/GroupChats/Memberships/<int:chat_id>')
def membershipsByChatID(chat_id):
    handler = MembershipHandler()
    return handler.getMembershipByChatID(chat_id)



@app.route('/Users/Reactions')
def getReactions():
    handler = ReactionsHandler()
    return handler.getAllReactions()


@app.route('/Users/Reactions/<int:user_id>')
def getReactionsByID(user_id):
    handler = ReactionsHandler()
    return handler.getReactionsByUserID(user_id)





if __name__ == '__main__':
    app.run()
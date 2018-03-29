from flask import Flask, request
from handler.users import UsersHandler
from handler.chats import ChatsHandler
from handler.messages import MessageHandler
from handler.reactions import ReactionsHandler
from handler.members import MembershipHandler
from handler.replies import ReplyHandler
from handler.contacts import ContactHandler
from handler.admins import AdminsHandler
from handler.hashtags import HashtagsHandler
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

@app.route('/Messages/Replies/<int:message_id>')
def getRepliesByID(message_id):
    handler = ReplyHandler()
    return handler.findMessagesReplies(message_id)

@app.route('/Messages/Hashtags/<int:message_id>')
def getHashtagsInMessage(message_id):
    handler = HashtagsHandler()
    return handler.getHashtagsFromMessage(message_id)
@app.route('/Hashtags/<int:hashtag_id>')
def getMessageWithHashtag(hashtag_id):
    handler = HashtagsHandler()
    return handler.getMessagesWithHashtag(hashtag_id)
@app.route('/Hashtags')
def hashtags():
    handler = HashtagsHandler()
    return handler.getAllHashtags()


@app.route('/Users/Contacts')
def contacts():
    handler = ContactHandler()
    return handler.getAllContacts()

@app.route('/Users/Contacts/<int:user_id>')
def getContactsOfUser(user_id):
    handler = ContactHandler()
    return handler.getContactsByUserID(user_id)

@app.route('/Users/Memberships')
def memberships():
    handler = MembershipHandler()
    return handler.getAllMemberships()

@app.route('/Users/Memberships/<int:user_id>')
def membershipsByUID(user_id):
    handler = MembershipHandler()
    return handler.getMembershipByUID(user_id)

@app.route('/Users/Admins')
def admins():
    handler = AdminsHandler()
    return handler.getAllAdmins()

@app.route('/GroupChats')
def chats():
    handler = ChatsHandler()
    return handler.getAllChats()

@app.route('/GroupChats/<int:chat_id>')
def getChatById(chat_id):
    handler = ChatsHandler()
    return handler.getChatByID(chat_id)

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

@app.route('/GroupChats/Admins/<int:user_id>')
def chatsByAdmin(user_id):
    handler = AdminsHandler()
    return handler.getChatsAdministratedByUser(user_id)

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
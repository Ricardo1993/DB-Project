from flask import Flask, request, render_template
from handler.users import UsersHandler
from handler.group_chat import ChatsHandler
from handler.messages import MessageHandler
from handler.reaction import ReactionHandler
from handler.member_of import MembershipHandler
from handler.replies import ReplyHandler
from handler.contacts import ContactHandler
from handler.administrates import AdminsHandler
from handler.hashtag import HashtagsHandler


import psycopg2

app = Flask(__name__)


# @app.route('/')
# @app.route('/<user>')
# def index(user=None):
#     return render_template("user.html", user=user)
# # def home():
# #     return "DB Project"
#
# # @app.route('/bacon', methods=['GET', 'POST'])
# # def index():
# #     return "Method used: %s" % request.method
# @app.route('/profile/<name>')
# def profile(name):
#     return render_template("profile.html", name=name)


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
# @app.route('/Users/<string:user_name>')
# def getUserByName(user_name):
#     handler = UsersHandler()
#     return handler.getUserByName(user_name)

@app.route('/Messages')
def getMessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/Messages/<int:message_id>')
def getMessageById(message_id):
    handler = MessageHandler()
    return handler.getMessageByID(message_id)

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
@app.route('/Hashtags/<string:hashtag_text>')
def hashtagText(hashtag_text):
    handler = HashtagsHandler()
    return handler.getHashtagsByText(hashtag_text)

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
    # print(handler.findChatMessages(chat_id))
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
    handler = ReactionHandler()
    return handler.getAllReactions()

@app.route('/Users/Reactions/<int:user_id>')
def getReactionsByID(user_id):
    handler = ReactionHandler()
    return handler.getReactionsByUserID(user_id)

@app.route('/Messages/Reactions/<int:message_id>')
def getReactionsByMessageID(message_id):
    handler = ReactionHandler()
    return handler.getReactionsByMessageID(message_id)
@app.route('/Messages/Reactions/<int:message_id>/like')
def likes(message_id):
    handler = ReactionHandler()
    return handler.getMessageLikes(message_id)
@app.route('/Messages/Reactions/<int:message_id>/dislike')
def dislikes(message_id):
    handler = ReactionHandler()
    return handler.getMessageDislikes(message_id)

@app.route('/Messages/Reactions/<int:message_id>/like/count')
def likesCount(message_id):
    handler = ReactionHandler()
    return handler.getMessageLikesCount(message_id)
@app.route('/Messages/Reactions/<int:message_id>/dislike/count')
def dislikesCount(message_id):
    handler = ReactionHandler()
    return handler.getMessageDislikesCount(message_id)



@app.route('/GroupChats/Messages/<int:chat_id>/<int:user_id>')
def getChatMessagesOfUser(chat_id, user_id):
    handler = MessageHandler()
    return handler.findChatMessagesByUser(chat_id, user_id)

if __name__ == '__main__':
    app.run()
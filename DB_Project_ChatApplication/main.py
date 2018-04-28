from flask import Flask, request, render_template
from handler.users import UsersHandler
from handler.group_chat import ChatsHandler
from handler.message import MessageHandler
from handler.reaction import ReactionHandler
from handler.member_of import MembershipHandler
from handler.reply import ReplyHandler
from handler.contacts import ContactHandler
from handler.administrates import AdminsHandler
from handler.hashtag import HashtagsHandler


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

##############
# HOME ROUTE #
##############

@app.route('/Home')
def welcome():
    return "Welcome to DB Chat!"

########################
# USERS RELATED ROUTES #
########################

# Show all users in the db system
@app.route('/Users')
def users():
    handler = UsersHandler()
    return handler.getAllUsers()

# Get a user by user_id
@app.route('/Users/<int:user_id>')
def getUserById(user_id):
    handler = UsersHandler()
    return handler.getUserByID(user_id)

# Get user by name ex. Manuel+Rodriguez
@app.route('/Users/Name/<user_name>')
def getUserByName(user_name):
     handler = UsersHandler()
     print(user_name)
     x = user_name.split('+') #split name and parent name
     print(x)
     return handler.getUserByName(x[0],x[1])

##########################
# MESSAGE RELATED ROUTES #
##########################

# Show all messages in the db
@app.route('/Messages')
def getMessages():
    handler = MessageHandler()
    return handler.getAllMessages()

# Get a specific message by id
@app.route('/Messages/<int:message_id>')
def getMessageById(message_id):
    handler = MessageHandler()
    return handler.getMessageByID(message_id)

# Get all messages of a specific user
@app.route('/Users/Messages/<int:user_id>')
def getMessagesByUID(user_id):
    handler = MessageHandler()
    return handler.findUserMessages(user_id)

# Get all messages of a specific group
@app.route('/GroupChats/Messages/<int:group_id>')
def getChatMessages(group_id):
    handler = MessageHandler()
    return handler.findGroupMessages(group_id)

# Get all messages of a user in a specific group chat
@app.route('/GroupChats/Messages/<int:group_id>/<int:user_id>')
def getChatMessagesOfUser(group_id, user_id):
    handler = MessageHandler()
    return handler.findGroupMessagesByUser(group_id, user_id)

##########################
# REPLIES RELATED ROUTES #
##########################

# Get all messages that are replies
@app.route('/Messages/Replies')
def getReplies():
    handler = ReplyHandler()
    return handler.getAllReplies()

# Get all replies to a specific message
@app.route('/Messages/Replies/<int:message_id>')
def getRepliesByID(message_id):
    handler = ReplyHandler()
    return handler.findMessageReplies(message_id)

# Get all replies to a specific message
@app.route('/GroupChats/Messages/Replies/<int:message_id>')
def getRepliesByMessageID(message_id):
    handler = ReplyHandler()
    return handler.findMessageReplies(message_id)


##########################
# HASHTAG RELATED ROUTES #
##########################

# Get all hashtags in the db
@app.route('/Hashtags')
def hashtags():
    handler = HashtagsHandler()
    return handler.getAllHashtags()

# Get all hashtags in one specific message
@app.route('/Messages/Hashtags/<int:message_id>')
def getHashtagsInMessage(message_id):
    handler = HashtagsHandler()
    return handler.getHashtagsFromMessage(message_id)

# Get a specific hashtag by it's id
@app.route('/Hashtags/<int:hashtag_id>')
def getMessageWithHashtag(hashtag_id):
    handler = HashtagsHandler()
    return handler.getHashtagByID(hashtag_id)

# Get a specific hashtag by it's text ex. PRSeLevanta
@app.route('/Hashtags/Text/<hashtag_text>')
def hashtagText(hashtag_text):
    handler = HashtagsHandler()
    hashtag_text = '#' + hashtag_text # concat the # to the hashtag text
    return handler.getHashtagByText(hashtag_text)

###########################
# CONTACTS RELATED ROUTES #
###########################

# Get all contacts for all users
@app.route('/Users/Contacts')
def contacts():
    handler = ContactHandler()
    return handler.getAllContacts()

# Get a user contact list
@app.route('/Users/Contacts/<int:user_id>')
def getContactsOfUser(user_id):
    handler = ContactHandler()
    return handler.getContactsByUserID(user_id)

###############################
# MEMBERSHIPS RELATED ROUTES #
###############################

# Get all users memberships, meaning which groups are they related to
@app.route('/Users/Memberships')
def memberships():
    handler = MembershipHandler()
    return handler.getAllMemberships()

# Get all memberships in which a user participates, which groups a user is related to
@app.route('/Users/Memberships/<int:user_id>')
def membershipsByUID(user_id):
    handler = MembershipHandler()
    return handler.getMembershipByUID(user_id)

# Get all members of a chat
@app.route('/GroupChats/Memberships/<int:group_id>')
def membershipsByChatID(group_id):
    handler = MembershipHandler()
    return handler.getMembershipByChatID(group_id)

################################
# ADMINISTRATES RELATED ROUTES #
################################

# Get all group chats administrators
@app.route('/Users/Admins')
def admins():
    handler = AdminsHandler()
    return handler.getAllAdmins()

# Get what groups do a user administrates
@app.route('/Users/Admins/<int:user_id>')
def chatsByAdmin(user_id):
    handler = AdminsHandler()
    return handler.getChatsAdministratedByUser(user_id)

# Get the administrator of a group
@app.route('/GroupChats/Admins/<int:group_id>')
def adminsByGroup(group_id):
    handler = AdminsHandler()
    return handler.getAdminOfChatID(group_id)


#############################
# GROUP_CHAT RELATED ROUTES #
#############################

# Get all group chats
@app.route('/GroupChats')
def chats():
    handler = ChatsHandler()
    return handler.getAllChats()

# Get a specific group chat
@app.route('/GroupChats/<int:chat_id>')
def getChatById(chat_id):
    handler = ChatsHandler()
    return handler.getChatByID(chat_id)

###########################
# REACTION RELATED ROUTES #
###########################

# Get all reactions for all messages
@app.route('/Users/Reactions')
def getReactions():
    handler = ReactionHandler()
    return handler.getAllReactions()

# Get all reactions of a specific user
@app.route('/Users/Reactions/<int:user_id>')
def getReactionsByID(user_id):
    handler = ReactionHandler()
    return handler.getReactionsByUserID(user_id)

# Get all reactions to a specific message
@app.route('/Messages/Reactions/<int:message_id>')
def getReactionsByMessageID(message_id):
    handler = ReactionHandler()
    return handler.getReactionsByMessageID(message_id)

# Get all likes to a specific message
@app.route('/Messages/Reactions/<int:message_id>/likes')
def likes(message_id):
    handler = ReactionHandler()
    return handler.getMessageLikes(message_id)

# Get all dislikes to a specific message
@app.route('/Messages/Reactions/<int:message_id>/dislikes')
def dislikes(message_id):
    handler = ReactionHandler()
    return handler.getMessageDislikes(message_id)

# Get the count of likes to a specific message
@app.route('/Messages/Reactions/<int:message_id>/likes/count')
def likesCount(message_id):
    handler = ReactionHandler()
    return handler.getMessageLikesCount(message_id)

# Get the count of dislikes of a specific message
@app.route('/Messages/Reactions/<int:message_id>/dislikes/count')
def dislikesCount(message_id):
    handler = ReactionHandler()
    return handler.getMessageDislikesCount(message_id)


if __name__ == '__main__':
    app.run()
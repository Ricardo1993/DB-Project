from flask import Flask, request, render_template, jsonify
from handler.users import UsersHandler
from handler.group_chat import ChatsHandler
from handler.message import MessageHandler
from handler.reaction import ReactionHandler
from handler.member_of import MembershipHandler
from handler.reply import ReplyHandler
from handler.contacts import ContactHandler
from handler.administrates import AdminsHandler
from handler.hashtag import HashtagsHandler

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
# @app.route('/<user>')
# def index(user=None):
#     return render_template("user.html", user=user)
def home():
    return "DB Project"
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
# @app.route('/Users/Name/<user_name>/status')
# def getUserById(user_name):
#     handler = UsersHandler()
#     return handler.getUserStatus(user_name)


########################
# USERS RELATED ROUTES #
########################

# Show all users in the db system
@app.route('/Users', methods=['GET', 'POST'])
def users():
    handler = UsersHandler()
    # Json format
    # json = {'first_name': 'Heidi', 'last_name': 'Doe', 'users_phone': '7873334554', 'users_email': 'fake2@mail.com',
    #      'users_password': 'password'}

    if request.method == 'POST':
        print(request.json)
        print(handler.checkUser(request.json))
        if (handler.checkUser(request.json) is None):  # check if user already exist checking name and last , phone or email
            return handler.registerUser(request.json)  # form #returns users info added
        else:
            return jsonify(Error="Invalid registration."), 405
    elif request.method == 'GET':
        return handler.getAllUsers()
    else:
        return jsonify(Error="Method not allowed."), 405

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
    print('db')
    handler = MessageHandler()
    return handler.getAllMessages()

# Get a specific message by id
@app.route('/Messages/<int:message_id>')
def getMessageById(message_id):
    handler = MessageHandler()
    return handler.getMessageByID(message_id)

# Get a specific message by hashtag content
@app.route('/Messages/<hashtag_text>')
def getMessageByHashtag(hashtag_text):
    handler = MessageHandler()
    hHandler = HashtagsHandler()
    hashtag_text = '#' + hashtag_text  # concat the # to the hashtag text
    return hHandler.getMessagesWithHashtagText(hashtag_text)

# Get a specific message by hashtag content
@app.route('/Messages/<int:group_id>/<hashtag_text>')
def getMessageByHashtagAndGroup(group_id,hashtag_text):
    handler = MessageHandler()
    hHandler = HashtagsHandler()
    hashtag_text = '#' + hashtag_text  # concat the # to the hashtag text
    return hHandler.getMessagesWithHashtagTextAndGroup(hashtag_text,group_id)


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
@app.route('/GroupChats/Messages/<int:group_id>/<int:user_id>', methods = ['GET', 'POST'])
def getChatMessagesOfUser(group_id, user_id):
    handler = MessageHandler()
    mHandler = MembershipHandler()

    # JSON FORMAT
    # json = { "message_text": }

    if request.method == 'POST':
        #pre: group already exits
        #pre: user already exits
        print(mHandler.checkMember(group_id,user_id))
        if (mHandler.checkMember(group_id,user_id) is not None):  # check if user is a member
            return handler.sendMessage(request.json,user_id,group_id)  # parameters admin id and group id

        else:
            return jsonify(Error="User not member of group."), 405

    elif request.method == 'GET':
        return handler.findGroupMessagesByUser(group_id, user_id)
    else:
        return jsonify(Error="Method not allowed."), 405


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

@app.route('/Messages/Replies/<int:message_id>/<int:users_id>/<int:group_id>', methods = ['POST'])
def postReply(message_id,users_id,group_id):
    handler = ReplyHandler()
    #pre: user , group and message are real
    # json = { "message_text": }
    # message_id: message to reply to
    # user_id: person replying
    #group_id: group in which reply occurs
    if request.method == 'POST':
        return handler.reply(request.json,  message_id,users_id, group_id)
    else:
        return jsonify(Error="Method not allowed"), 405

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
@app.route('/Users/Contacts/<int:user_id>',methods=['GET', 'POST', 'DELETE'])

def getContactsOfUser(user_id):

    #JSON FORMAT
    #recives desired user to add name
    #json = {'first_name': 'Ricardo', 'last_name': 'Casares'}
    handler = ContactHandler()
    if request.method == 'GET':
        return handler.getContactsByUserID(user_id)
    elif request.method == 'POST':
        if (handler.checkContact(request.json) is not None):  # check if user already exist checking name and last
            return handler.addContact(request.json, user_id)  # returns user name added, user_id in which to add contact

        else:
            return jsonify(Error="User trying to add doesn't exists."), 405
    elif request.method == 'DELETE':
        if (handler.checkContact(request.json) is not None):  # check if user already exist checking name and last
            return handler.removeContact(request.json, user_id)  # returns user name remove

        else:
            return jsonify(Error="User to remove doesn't exists."), 405
    else:
        return jsonify(Error="Method not allowed"), 405
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

@app.route('/Users/Memberships/<user_name>')
def membershipsByUName(user_name):
    handler = MembershipHandler()
    print(user_name)
    x = user_name.split('+')  # split name and parent name
    print(x)
    return handler.getMembershipByUName(x[0], x[1])

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
@app.route('/Users/Admins/<int:user_id>',methods=['GET', 'POST', 'DELETE'])
def chatsByAdmin(user_id):
    handler = AdminsHandler()
    contactHandler = ContactHandler()
    groupHandler =  ChatsHandler()
    memberHandler = MembershipHandler()

    # JSON FORMAT
    #Group name and name of user to add/remove to group
    #json = {'group_name':'DB Class','first_name': 'John', 'last_name': 'Doe'}

    if request.method == 'GET':
        return handler.getChatsAdministratedByUser(user_id)

    # Add a user to a group
    elif request.method == 'POST':
        # check if user and group exist
        # if ( (memberHandler.checkContact(request.json) is not None) and (groupHandler.checkGroup(request.form) is not None) ):
        #     return memberHandler.addMember(request.json, user_id)  # returns user name added and group in which was added, user_id is of admin
        if ( (groupHandler.checkGroup(request.form) is not None) ):
            return memberHandler.addMember(request.json, user_id)  # returns user name added and group in which was added, user_id is of admin

        else:
            return jsonify(Error="User trying to add or group, doesn't exists."), 405

    elif request.method == 'DELETE':
        # check if user and group exist
        #print(form)
        if ( (memberHandler.checkContact(request.json) is not None) and (groupHandler.checkGroup(request.form) is not None) ):
            return memberHandler.removeMember(request.json, user_id)  # returns user name of member removed, parameter admin_id
        else:
            return jsonify(Error="Member or group doesn't exists."), 405
    else:
        return jsonify(Error="Method not allowed"), 405

# Get the administrator of a group
@app.route('/GroupChats/Admins/<int:group_id>')
def adminsByGroup(group_id):
    handler = AdminsHandler()
    return handler.getAdminOfChatID(group_id)


#############################
# GROUP_CHAT RELATED ROUTES #
#############################

# Get all group chats
@app.route('/GroupChats', methods=['GET', 'POST', 'DELETE'])
def chats():
    handler = ChatsHandler()
    adminHandler = AdminsHandler()
    usersHandler = UsersHandler()

    #Json format recieves name of group and name of administrator
    #json = {'group_name': 'DB Class', 'first_name': 'John', 'last_name':'Doe'}

    if request.method == 'POST':
        # PRE: user must exist
        if (handler.checkGroup(request.json) is None): #check if group already exist
             return handler.registerGroup(request.json) #recieves group name and user name (admin) from form

        else:
            return jsonify(Error="Invalid registration."), 405

    elif request.method == 'DELETE':
        # PRE: user must exist
        if (handler.checkGroup(request.json) is None): #check if group already exist
            return jsonify(Error="Invalid group."), 405
        else:
            return handler.removeGroup(request.json) #recieves name of user trying to delete and group
    elif request.method == 'GET':
        return handler.getAllChats()

    else:
        return jsonify(Error="Method not allowed."), 405

# Get a specific group chat
@app.route('/GroupChats/<int:chat_id>',methods=['GET', 'DELETE'])
def getChatById(chat_id):
    handler = ChatsHandler()
    if request.method == 'GET':
        return handler.getChatByID(chat_id)
    elif request.method == 'DELETE':
        if handler.checkGroup(request.json) is None:  # check if group already exist
            return jsonify(Error="Invalid group."), 405
        else:
            return handler.removeGroup(request.json)
    else:
        return jsonify(Error="Method not allowed"), 405
###########################
# REACTION RELATED ROUTES #
###########################

# Get all reactions for all messages
@app.route('/Users/Reactions')
def getReactions():
    handler = ReactionHandler()
    return handler.getAllReactions()
# @app.route('/Users/Reactions/count')
# def getReactionsCount():
#     handler = ReactionHandler()
#     return handler.getAllReactions()


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

# Post reaction of user to a message
@app.route('/Users/Reactions/<int:message_id>/<int:user_id>', methods = ['POST'])
def postReaction(message_id,user_id):
    handler = ReactionHandler()
    #pre: user exits and message exits
    #reaction must be either "like" or "dislike"
    #JSON FORMAT
    #
    # json = { "reaction": "like"}
    if request.method == 'POST':
        return handler.react(request.json, user_id, message_id) # user giving like/dislike and message in which to react
    else:
        return jsonify(Error="Method not allowed"), 405


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


########################
# Google trends routes #
########################
@app.route('/Users/active')
def activeUsers():
    handler = UsersHandler()
    return handler.getActiveUsers()

@app.route('/Messages/count')
def messageCount():
    handler = MessageHandler()
    return handler.getMessagesPerDay()

@app.route('/Messages/Replies/count')
def replyCount():
    handler = ReplyHandler()
    return handler.getRepliesPerDay()


@app.route('/Hashtags/Trends')
def trends():
    handler = HashtagsHandler()
    return handler.getTrends()

@app.route('/Reactions/countLikes')
def countLikes():
    handler = ReactionHandler()
    return handler.getLikesPerDay()

@app.route('/Reactions/countDislikes')
def countDislikes():
    handler = ReactionHandler()
    return handler.getDislikesPerDay()




if __name__ == '__main__':
    app.run()
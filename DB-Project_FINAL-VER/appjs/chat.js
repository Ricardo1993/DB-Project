angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$rootScope', '$location',
    function($http, $log, $scope, $rootScope, $location) {
        var thisCtrl = this;

        this.messageList = [];
        this.likesList = [];
        this.dislikesList = [];
        this.counter = 2;
        this.newText = "";
        this.reply = "";
        this.hashtag= "";
        this.likesOfMessage = 0;
        this.dislikesOfMessage = 0;

        this.loadHashtags = function(){
            var url = "http://localhost:5000/Hashtags/Text/" + thisCtrl.hashtag;
            console.log(url);

            $http.get(url).then(// success call back
            function (response){
                var ht = response.data.Hashtags[0]['hashtag'];
                var j = 0;
                console.log(ht);
                console.log(thisCtrl.hashtag);
                if (ht != null) {
                    if (ht === "#" + thisCtrl.hashtag) {
                        console.log("I am inside");
                        var newMessageList = [];
                        for (i = 0; i < thisCtrl.messageList.length; i++) {
                            console.log("inside loop");
                            if (thisCtrl.messageList[i]['message_text'].includes(thisCtrl.hashtag)) {
                                newMessageList[j] = thisCtrl.messageList[i]
                                j = j + 1;
                            }
                        }

                        console.log(newMessageList);
                        thisCtrl.messageList = newMessageList;
                        console.log(thisCtrl.messageList);
                        thisCtrl.hashtag = "";
                    }
                }
//                    thisCtrl.messageList = response.data.Messages;
//                    console.log(thisCtrl.messageList)
//                    console.log(thisCtrl.messageList[0]['dislikes'])

                }, // error callback
                function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            }
            )
        }

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            var url = "http://localhost:5000/GroupChats/Messages/" + $rootScope.groupIDChosen;
            console.log(url);

            $http.get(url).then(// success call back
                function (response){
                    thisCtrl.messageList = response.data.Messages;
                    console.log(thisCtrl.messageList)
                }, // error callback
                function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            }
            )
        };

        this.postMsg = function() {
            var msg = thisCtrl.newText;
            var url = "http://localhost:5000/GroupChats/Messages/" + $rootScope.groupIDChosen + "/" + $rootScope.userID;
            $http.post(url, {"message_text": msg}).then(// success call back
                function (response){
                      thisCtrl.newText = "";
                      thisCtrl.loadMessages();
                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            )
        };

        this.postReply = function(m) {
            var msg = thisCtrl.reply;
            var url = "http://localhost:5000/Messages/Replies/" + m.message_id + "/" + $rootScope.userID + "/" + $rootScope.groupIDChosen;
            $http.post(url, {"message_text": msg}).then(// success call back
                function (response){
                      thisCtrl.reply = "";
                      thisCtrl.loadMessages();

                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            )
        };

        this.like = function(m){
            var url = "http://localhost:5000/Users/Reactions/" + m.message_id + "/" + $rootScope.userID;
            $http.post(url, {"reaction": "like"}).then(// success call back
                function (response){
                    var row = thisCtrl.messageList.indexOf(m);
                    m.likes = m.likes + 1;
                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            )
        };

        this.dislike = function(m){
            var url = "http://localhost:5000/Users/Reactions/" + m.message_id + "/" + $rootScope.userID;
            $http.post(url, {"reaction": "dislike"}).then(// success call back
                function (response){
                    var row = thisCtrl.messageList.indexOf(m);
                    m.dislikes = m.dislikes + 1;
                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            )

        };

        this.goBack = function() {
            $location.url('/groups');
        }

        this.refresh = function() {
                this.loadMessages();
            $location.url('/chat');
        }

        this.showReactions = function(m) {
            console.log('message id ==== > ' + m['message_id']);
            var url = "http://localhost:5000/Messages/Reactions/" + m['message_id'] + "/likes";//"http://localhost:5000/GroupChats/Messages/" + $rootScope.groupIDChosen;
            console.log(url);
                $http.get(url).then(// success call back
                    function (response){
                        thisCtrl.likesList = response.data.Reactions;
                        console.log(thisCtrl.likesList);

                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                })

            url = "http://localhost:5000/Messages/Reactions/" + m['message_id'] + "/dislikes";//"http://localhost:5000/GroupChats/Messages/" + $rootScope.groupIDChosen;
            console.log(url);

                $http.get(url).then(// success call back
                    function (response){
    //                    console.log($scope.messageList)
                        thisCtrl.dislikesList = response.data.Reactions;
                        console.log(thisCtrl.dislikesList);

                }, // error callback
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                })



                };

      this.loadMessages();
//      this.loadAdmins();
}]);

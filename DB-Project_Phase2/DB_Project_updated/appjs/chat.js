angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 2;
        this.newText = "";

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            var url = "http://localhost:5000/Messages";

            $http.get(url).then(// success call back
                function (response){
//                    console.log($scope.messageList)
                    thisCtrl.messageList = response.data.Messages;
//                    console.log($scope.messageList)

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
            })};

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";

            var nextId = ++thisCtrl.messageList.length;
            thisCtrl.messageList.unshift({"message_date": "Sat, 31 Mar 2018 00:00:00 GMT", "message_id": nextId, "message_text": msg, "user_first_name": "Me", "user_last_name": "", "likes": 0, "dislikes": 0});
//            $scope.messageList.unshift({"id": nextId, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});
            thisCtrl.newText = "";
//            console.log(thisCtrl.messageList)
        };

         this.like = function(m){
            var row = thisCtrl.messageList.indexOf(m);
            m.likes = m.likes + 1
        };

        this.dislike = function(m){
            var row = thisCtrl.messageList.indexOf(m);
            m.dislikes = m.dislikes + 1
        };


        this.loadMessages();
}]);

//    var loggedIn = false;
//    console.log(loggedIn);

angular.module('AppChat').controller('GroupsController', ['$http', '$log', '$scope', '$rootScope', '$location',
    function($http, $log, $scope, $rootScope, $location) {
    console.log('GROUPS????');
        $scope.test = "testing";
        var thisCtrl = this;
        $rootScope.loggedIn = true;
        $rootScope.groupIDChosen = null;
        this.allOrMine = "";
        this.admin = [];
        this.firstName = "";
        this.lastName = "";
        this.user = [];
        this.groupList = [];

        this.loadGroups = function(){
            var url = ""; // + thisCtrl.firstName + "+" + thisCtrl.lastName;
            console.log(url);
//            if (thisCtrl.allOrMine == "" || thisCtrl.allOrMine == "Show My Groups") {
//                console.log("OVER HERE!")
//                thisCtrl.allOrMine = "Show All Groups";
                url = "http://localhost:5000/Users/Memberships/" + $rootScope.firstNameLogged + "+" + $rootScope.lastNameLogged;
//            } else {
//                thisCtrl.allOrMine = "Show My Groups";
//                url = "http://localhost:5000/GroupChats";
//            }
            $http.get(url).then(// success call back
                function (response){
                    console.log("chats response:    " +  JSON.stringify(response));
                    thisCtrl.groupList = response.data.Chats;
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

         this.enterGroup = function(g){
                console.log('hello groups!');
                console.log(g);
                    var ID = thisCtrl.groupList[thisCtrl.groupList.indexOf(g)]['group_id'];
                    $rootScope.groupIDChosen = ID; // g['chat_id'];
//                    var url = "http://localhost:5000/GroupChats/Admins/1";// + ID;
//                    var adminID = 0;
//                    $http.get("http://localhost:5000/GroupChats/Admins/1").then(// success call back
//                        function (response){
//                            console.log("response: " + JSON.stringify(response));
//                            console.log(response.data.Admins);
//                            thisCtrl.admin = response.data.Admins;//['admin_id']
//
//    //                      thisCtrl.groupList = response.data.Members;
//                            console.log("ADMIN! " + thisCtrl.admin)
//                            url = "http://localhost:5000/Users/Admins/" + thisCtrl.admin['admin_id'];
//                            console.log(url);
////                             $http.post(url, {"group_name":g.group_name, "first_name":$rootScope.firstNameLogged, "last_name":$rootScope.lastNameLogged}).then(// success call back
////                        function (response){
//////                            thisCtrl.groupList = response.data.Members;
////                        }, // error callback
////                        function (response){
////                            // This is the error function
////                            // If we get here, some error occurred.
////                            // Verify which was the cause and show an alert.
////                            var status = response.status;
////                            if (status == 0){
////                                alert("No hay conexion a Internet");
////                            }
////                            else if (status == 401){
////                                alert("Su sesion expiro. Conectese de nuevo.");
////                            }
////                            else if (status == 403){
////                                alert("No esta autorizado a usar el sistema.");
////                            }
////                            else if (status == 404){
////                                alert("No se encontro la informacion solicitada.");
////                            }
////                            else {
////                                alert("Error interno del sistema.");
////                            }
////                        })
//
//                    }, // error callback
//                    function (response){
//                        // This is the error function
//                        // If we get here, some error occurred.
//                        // Verify which was the cause and show an alert.
//                        var status = response.status;
//                        if (status == 0){
//                            alert("No hay conexion a Internet");
//                        }
//                        else if (status == 401){
//                            alert("Su sesion expiro. Conectese de nuevo.");
//                        }
//                        else if (status == 403){
//                            alert("No esta autorizado a usar el sistema.");
//                        }
//                        else if (status == 404){
//                            alert("No se encontro la informacion solicitada.");
//                        }
//                        else {
//                            alert("Error interno del sistema.");
//                        }
//                    })

//                } else {
                    var ID = thisCtrl.groupList[thisCtrl.groupList.indexOf(g)]['chat_id'];
                    $rootScope.groupIDChosen = ID; // g['chat_id'];
//                }

                $location.url('/chat');
//            var row = thisCtrl.messageList.indexOf(m);
//            m.likes = m.likes + 1;
        };

        this.loadGroups();
}]);
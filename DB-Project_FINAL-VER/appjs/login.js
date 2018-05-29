
angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$window', '$rootScope', '$location', //'mySharedService'
    function($http, $log, $scope, $window, $rootScope, $location) {
        var thisCtrl = this;
        this.firstName = "";
        this.lastName = "";
        this.password = "";
        this.user = [];

        thisCtrl.loginUser = function(){
            if (!$rootScope.loggedIn) {
                $rootScope.prueba = "";
                $rootScope.firstNameLogged = "";
                $rootScope.lastNameLogged = "";


            console.log(thisCtrl.firstName)
            console.log(thisCtrl.lastName)
            var url = "http://localhost:5000/Users/Name/" + thisCtrl.firstName + "+" + thisCtrl.lastName;
            console.log(url);
            $http.get(url).then(// success call back
                function (response){
                    console.log('in url')
                    thisCtrl.user = response.data.User;
                    if (thisCtrl.user != null) {
                        if (thisCtrl.password == thisCtrl.user['user_password']) {
                            console.log(thisCtrl.user);
                            console.log(thisCtrl.user['first_name'] + " " + thisCtrl.user['last_name'] + " | password: " + thisCtrl.user['user_password']);
                                                $rootScope.prueba = "probando";
                                                $rootScope.firstNameLogged = thisCtrl.firstName;
                                                $rootScope.lastNameLogged = thisCtrl.lastName;
                                                $rootScope.userID = thisCtrl.user['user_id'];

                            $location.url('/groups');
                        } else if (thisCtrl.password != thisCtrl.user['user_password']) {
                            console.log("incorrect password");
                        }
                    } else {
                        console.log("User not found");
                    }
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
            })} else {
                $location.url('/groups');
            }
            };
        thisCtrl.register = function() {
            console.log("REGISTER");
            $location.url('/register');
        }

        this.loginUser();
}]);
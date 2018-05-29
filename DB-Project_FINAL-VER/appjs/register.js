
angular.module('AppChat').controller('RegisterController', ['$http', '$log', '$scope', '$window', '$rootScope', '$location', //'mySharedService'
    function($http, $log, $scope, $window, $rootScope, $location) {
        var thisCtrl = this;
        this.firstName = "";
        this.lastName = "";
        this.phone = "";
        this.email = "";
        this.password = "";
        this.user = [];

        thisCtrl.register = function() {
            console.log("REGISTERING...");
            $rootScope.firstNameLogged = thisCtrl.firstName;
            $rootScope.lastNameLogged = thisCtrl.lastName;

                        var url = "http://localhost:5000/Users";
            console.log(url);
            $http.post(url, {
                "first_name": thisCtrl.firstName,
                "last_name": thisCtrl.lastName,
                "users_phone": thisCtrl.phone,
                "users_email": thisCtrl.email,
                "users_password": thisCtrl.password
            }).then(
                function (response){
                    console.log("SUCCESS");
                    $location.url('/groups')
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
}]);
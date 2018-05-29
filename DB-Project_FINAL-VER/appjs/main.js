(function() {

    var app = angular.module('AppChat',['ngRoute']);
//    var first_name = "";
//    var last_name = "";
//    var password = "";
//        var loggedIn = false;
//    console.log(loggedIn);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/register', {
            templateUrl: 'pages/register.html',
            controller: 'RegisterController',
            controllerAs : 'regCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/groups', {
            templateUrl: 'pages/groups.html',
            controller: 'GroupsController',
            controllerAs : 'groupsCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);

//    app.factory('mySharedService', function ($rootScope) {
//        var sharedService = {};
//        var sharedService.message = "";
//
//        sharedService.prepForBroadcast = function(msg) {
//            this.message = msg;
//            this.broadcastItem();
//        }
//        sharedService.broadcastItem = function() {
//            $rootScope.$broadcast('handleBroadcast');
//        }
//        return sharedService;
//    })
})();

var module = angular.module('MoviesApp', []);

module.controller("MoviesAppMainController", function($scope) {
    console.log($scope);
    $scope.MovieName = 'Test';

    $scope.Movies = [
        'Rocky',
        'Szklana Pułapka'
    ];

    $scope.MovieAdd = function() {
        $scope.Movies.push($scope.MovieName);
        $scope.MovieName = '';
    };

    $scope.RemoveAll = function() {
        $scope.Movies = [];
    };

});

module.directive('movieElement', function() {
    return {
        'restrict': 'AEC',
        'template': '<li class="list-group-item"><span ng-bind="_movie"></span><span ng-bind="$index"></span><button type="button" ng-click="MovieRemove($index);">Usuń</button></li>',
        'link': function($scope) {
            console.log($scope);
            $scope.MovieRemove = function(index) {
                $scope._movies.splice(index, 1);
            };
        },
        'scope': {
            '_movies' : '=movies',
            '_movie': '=movie'
        }
    };
});
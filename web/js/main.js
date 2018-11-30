/*eslint no-console: ["error", { allow: ["warn","info"] }] */

var app = angular.module("myApp", []);
var earth;
var nowroutePoint = [];


app.controller("myController", ["$scope", "$document", "$element", "$http", function ($scope, $document, $element, $http) {
	var allmarkerobj = [];
	var nowroute = [];

	$scope.announce = "";
	$scope.announcedetail = "";
	//台灣座標
	// earth.setView([120.982025, 23.973875], 1)
	// 轉到台灣座標
	// earth.panTo([23.973875, 120.982025]);#緯經

	$scope.initialize = function () {
		earth = new WE.map("earth_div", {
			sky: "img/"
		});
		earth.setView([46.8011, 8.2266], 2);

		var mapBounds = [
			[-85, -180],
			[85, 179.90966991]
		];
		var mapMinZoom = 0;
		var mapMaxZoom = 5;

		WE.tileLayer("http://140.113.73.212:9999/wgeWorldHistory/web/img/mapballs/ori/{z}/{x}/{y}.png", {
			bounds: mapBounds,
			minZoom: mapMinZoom,
			maxZoom: mapMaxZoom
		}).addTo(earth);
		$scope.allMarkerReady($scope.value);
		$scope.changeMapBall($scope.value);

		// $scope.testttt.removeFrom(earth);

		// earth.flyTo(routes[0]["coordinates"][1], routes[0]["coordinates"] [0])
		document.querySelector("body").addEventListener("touchmove", function (event) {
			event.preventDefault();
			// console.log(event);
		}, false);
		// document.querySelector(".horscroll").scrollLeft = document.querySelector(".horscroll").scrollWidth/40*20;


	};

	$scope.checkRoute = function (year) {

			nowroute = [];
			$scope.announce = "";
			$scope.announcedetail = "";
			$scope.iframe = "";

			$http({
				method: "POST",
				url: "http://140.113.73.212:8877/routesInThisYear",
				params: {
					year: year
				}
			}).then(function (response) {
				var routesdata = response.data;

				routesdata.forEach(function (routedata) {
					$scope.announce = routedata["routeName"];
					$scope.announcedetail = routedata["detail"];
					routedata["lines"].forEach(function (subroute) {
						try {
							var defaultPoly2 = new WebGLEarth.Polygon(earth);
							defaultPoly2.setFillColor("#000000", 0.0);
							defaultPoly2.setStrokeColor(`#${subroute["color"]}`, 1);
							subroute["coordinates"].forEach(coor => defaultPoly2.buildRoute(coor[1], coor[0]));
							defaultPoly2.disableClickToAdd();
							defaultPoly2.showDraggers(false);
							nowroute.push(defaultPoly2);
						} catch (error) {
							// console.log(1111);
						}
					});

					routedata["points"].forEach(function (point) {
						// console.log(point);
						if (point["name"] === "info") {
							var flagPin = earth.initMarker(point["coordinates"][1], point["coordinates"][0]);
							flagPin.bindPopup("<button style='border-width: 0px;' data-toggle='modal' data-target='#exampleModal' ng-bind='announce'>info</button>", {
								maxWidth: 30
							});
						} else {
							flagPin = earth.initMarker(point["coordinates"][1], point["coordinates"][0], `img/flags/${point["name"]}.png`, 22, 13);
							flagPin.bindPopup(point["name"], {
								maxWidth: 30
							});

						}



						nowroutePoint.push(flagPin);
					});
					if ($scope.announce === "鄭和第一次出航") {
						$scope.iframe = "https://www.youtube.com/embed/7-oI41NuCVk";
					}
				});
			}, function (error) {
				console.warn(error);
			});
		},

		$scope.allMarkerReady = function (year) {
			$http({
				method: "POST",
				url: "http://140.113.73.212:8877/allCityInThisYear",
				params: {
					year: year
				}
			}).then(function (response) {
				$scope.allmarker = response.data;
				$scope.allmarker.forEach(function (element) {
					var marker = WE.marker(element["coordinates"], "", 1, 1, element["name"]).addTo(earth);
					allmarkerobj.push(marker);
					var marker_pin = WE.marker(element["coordinates"]).addTo(earth);
					marker_pin.bindPopup(element["name"], {
						maxWidth: 30
					});
					allmarkerobj.push(marker_pin);
				});
				var nowCountry = document.querySelectorAll(".countrytag");
				nowCountry.forEach(e => $scope.addevent(year, e.id));
			}, function (error) {
				console.warn(error);
			});
		},
		$scope.zoomFunction = function () {
			if ($scope.zoom !== Math.round(earth.getZoom())) {
				$scope.zoom = Math.round(earth.getZoom());
				document.documentElement.style.setProperty("--countrysize", `${$scope.zoom*3}pt`);
				if ($scope.zoom < 5) {
					document.documentElement.style.setProperty("--countrydisplay", "none");
				} else {
					document.documentElement.style.setProperty("--countrydisplay", "auto");
				}
			}
		},

		$scope.zoombar = 2,
		$scope.value = 2016,
		$scope.min = -2000,
		$scope.max = 2020,
		document.getElementById("earth_div").addEventListener("wheel", $scope.zoomFunction),
		document.getElementById("earth_div").addEventListener("touchmove", $scope.zoomFunction),

		$scope.addevent = function (year, city) {
			$http({
				method: "POST",
				url: "http://140.113.73.212:8877/yeartoevent",
				params: {
					yearFrom: parseInt(year) - 100,
					yearTo: parseInt(year) + 100,
					city: city
				}
			}).then(function (response) {
				$scope.events = response.data;
				var thisCity = document.getElementById(city);
				var html = "";
				if (thisCity === null) {
					return;
				}

				$scope.events.forEach(value => {
					html += `<div class="flow event">
                  <img src="${value["image"]}"height="42" width="42">
                  <div style="display:none">${value["detail"]}</div>
                </div>`;
				});

				thisCity.style.width = "50vw";
				thisCity.innerHTML = html;

				const allEvents = document.querySelectorAll(".event");
				allEvents.forEach(event => event.addEventListener("click", $scope.eventDetail));

			}, function (error) {
				console.warn(error);
			});
		},

		$scope.eventDetail = function (e) {
			console.info(e);
			const allEvents = document.querySelectorAll(".event > div");
			var state = this.querySelector("div > div").style.display;
			allEvents.forEach(event => event.style.display = "none");
			if (state !== "block") {
				this.querySelectorAll("div")[0].style.display = "block";
			}
		},

		$scope.$watch("value", function (newValue, oldValue) {
			if (newValue !== oldValue) {
				// bgEarth();
				$scope.changeMapBall(newValue);
			}
		}, true),

		$scope.$watch("flyto", function (newValue, oldValue) {
			if (newValue === undefined && oldValue === undefined) {
				//pass
			} else {
				$scope.flytoCountry(newValue);
			}

		}, true),

		$scope.$watch("zoombar", function (newValue, oldValue) {
			if (newValue !== oldValue) {
				// bgEarth();
				earth.setZoom(newValue / 150 + 2);
				$scope.zoomFunction();
			}
		}, true),

		$scope.changeMapBall = function (year) {
			while (allYears.indexOf(year.toString()) == -1) {
				year -= 1;
			}
			var mapBounds = [
				[-85, -180],
				[85, 179.90966991]
			];
			var mapMinZoom = 0;
			var mapMaxZoom = 5;
			if ($scope.nowTileLayer === undefined) {
				//pass
			} else {
				$scope.nowTileLayer.removeFrom(earth);
			}
			$scope.nowTileLayer = WE.tileLayer("http://140.113.73.212:9999/wgeWorldHistory/web/img/mapballs/" + year + "/{z}/{x}/{y}.png", {
				bounds: mapBounds,
				minZoom: mapMinZoom,
				maxZoom: mapMaxZoom,
				opacity: 0.5
			}).addTo(earth);

			allmarkerobj.forEach(marker => marker.removeFrom(earth));
			nowroutePoint.forEach(marker => earth.removeMarker(marker));
			nowroute.forEach(rt => rt.destroy());
			$scope.allMarkerReady($scope.value);
			$scope.checkRoute($scope.value);

			//詢問此年有哪些國家
			// nowCountry = document.querySelectorAll('.countrytag');
			// nowCountry.forEach(e => $scope.addevent(year, e.id))

			//foreach.....
			// $scope.addevent(year, '法國');
		},

		$scope.flytoCountry = function (country) {
			$scope.allmarker.forEach(function (element) {
				if (element["name"] == country) {
					earth.panTo(element["coordinates"], 500);
					setTimeout(function () {
						// earth.zoomIn(5)
						earth.setZoom(5);
						$scope.zoombar = 450;
						$scope.zoomFunction();
					}, 3000);
				}
			});
		},


		// $scope.gtcolor = function () {
		// 	var cl = "#000000".replace(/0/g, function () {
		// 		return (~~(Math.random() * 16)).toString(16);
		// 	});
		// 	return cl;
		// },

		// $scope.demoyears = [
		// 	[-100, $scope.gtcolor()],
		// 	[1406, $scope.gtcolor()],
		// 	[1492, $scope.gtcolor()],
		// 	[1520, $scope.gtcolor()],
		// 	[2016, $scope.gtcolor()]
		// ],
		// $scope.pointScale = 100 / ($scope.demoyears.length + 1),
		// $scope.timelineInside = document.querySelector(".timeline > .inside"),

		$scope.chyear = function (e, target) {
			var oldtarget = e.currentTarget.parentElement.querySelector(".active");
			target = e.currentTarget;
			var parent = target.parentNode;

			target.classList.add("active");
			$scope.value = parseInt(target.id);

			var left = target.getBoundingClientRect().left;
			var width = window.innerWidth;
			var diff = left - width / 2;
			var targetleft = parent.scrollLeft + diff + target.getBoundingClientRect().width / 2;
			parent.scrollLeft = targetleft;

			if (oldtarget !== null) {
				oldtarget.classList.remove("active");
			}
			target.scrollIntoView();


		};

	$scope.menuYears = menuYears;
	// menu
	const menumenu = document.querySelector(".horscroll");



	function goTimeMenu(e) {
		var scrollSize = e.wheelDelta;
		// console.info(scrollSize);
		// console.info(this.scrollWidth);
		this.scrollLeft = this.scrollLeft - scrollSize * 2;


		e.preventDefault();

	}

	menumenu.addEventListener("mousewheel", goTimeMenu);

	$scope.frameframe = function () {
		console.log("aaaa");
		window.location = $scope.iframe;
	};
	// var announcetag = document.querySelector(".announce");
	// announcetag.addEventListener("click", $scope.frameframe);

	// 臨時輸入框
	$scope.searchCate = function () {
		var year = prompt("Please enter year", "1945");
		var category = prompt("Please enter category", "jade");
		if (year != null) {
			console.log(year);
			console.log(category);
			//換皮
			//換資料
		}
		return
	}
	// 臨時輸入框
}]);

////////////////////////////////////////////////////////////////////
app.filter("replace", [function () {
	return function (item) {
		return item.toString().replace(/-/, "BC ");
	};
}]);

app.filter("reverse", function () {
	return function (items) {
		return items.slice().reverse();
	};
});

////////////////////////////////////////////////////////////////////
function footerAlign() {
	$("footer").css("display", "block");
	$("footer").css("height", "auto");
	var footerHeight = $("footer").outerHeight();
	$("body").css("padding-bottom", footerHeight);
	$("footer").css("height", footerHeight);
}


$(document).ready(function () {
	footerAlign();
});

$(window).resize(function () {
	footerAlign();
});


window.onload = function () {
	document.addEventListener("touchstart", function (event) {
		if (event.touches.length > 1) {
			event.preventDefault();
		}
	});
	var lastTouchEnd = 0;
	document.addEventListener("touchend", function (event) {
		var now = (new Date()).getTime();
		if (now - lastTouchEnd <= 300) {
			event.preventDefault();
		}
		lastTouchEnd = now;
	}, false);
	document.addEventListener("gesturestart", function (event) {
		event.preventDefault();
	});
};








////////////////////////////////////////////////////////////////////
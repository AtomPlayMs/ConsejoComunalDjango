$(function(){
	if(navigator.geolocation){
		initialize(10.091119011848654, -69.32686198147582);
	}
	else{
		initialize(10.09143589763447, -69.32604658993529);
	}

	function getCoords(position){
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat,lng);
	}

	function getError(err){
		initialize(10.09143589763447, -69.32604658993529);
	}

	function initialize(lat,lng){
		var latlng = new google.maps.LatLng(lat,lng);
		var mapSettings = {
			center: latlng,
			zoom: 17,
			mapTypeId: google.maps.MapTypeId.HYBRID
		};
		var map = new google.maps.Map(document.getElementById("googleMap"),mapSettings);
		var marker = new google.maps.Marker({
			position: latlng,
			map: map,
			draggable: true,
			title: 'Arastrame'
		});

		google.maps.event.addListener(marker,'position_changed',function(){
			getMarkerCorrds(marker);
		});


	}

	function getMarkerCorrds(marker){
		var markerCorrds = marker.getPosition();
		$('#id_lat').val(markerCorrds.lat());
		$('#id_lng').val(markerCorrds.lng());
	}
});
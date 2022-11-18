let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 40.76, lng: -73.983 },
    zoom: 15,
    mapTypeId: "satellite",
    heading: 90,
    tilt: 45,
  });
}
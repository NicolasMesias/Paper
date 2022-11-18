//Tratar a la imagen del input
let imageLoaded = false;
$("#image-selector").change(function () {
	imageLoaded = false;
	let reader = new FileReader();
	reader.onload = function () {
		let dataURL = reader.result;
		$("#selected-image").attr("src", dataURL);
		$("#prediction-list").empty();
		imageLoaded = true;
	}
	
	let file = $("#image-selector").prop('files')[0];
	reader.readAsDataURL(file);
});

let model;
let modelLoaded = false;
$( document ).ready(async function () {
	modelLoaded = false;
    console.log( "Cargando modelo");
    model = await tf.loadLayersModel('../static/modelo js/model.json'); //aca el url
    console.log( "Modelo cargado");
	modelLoaded = true;
});

$("#predict-button").click(async function () {
	if (!modelLoaded) { alert("Debe cargarse el modelo primero"); return; }
	if (!imageLoaded) { alert("Debe ingresar una imagen primero"); return; }
	
	let image = $('#selected-image').get(0);
	//Nombre de la imagen
	let nombre_imagen = document.getElementById("image-selector").files[0].name;
	
	// Adaptar la imagen
	console.log( "Cargando imagen..." );
	let tensor = tf.browser.fromPixels(image, 3)
		.resizeNearestNeighbor([256, 256])
		.expandDims()
		.toFloat()
		.reverse(-1); // RGB -> BGR
	let predictions = await model.predict(tensor).data();
	console.log(predictions);
	let argmax = Array.from(predictions)
		.map(function (p, i) { 
			return {
				probability: p,
				className: TARGET_CLASSES[i] 
			};
		}).sort(function (a, b) {
			return b.probability - a.probability;
		}).slice(0, 1);

	$("#prediction-list").empty();
	argmax.forEach(function (p) {
		$("#prediction-list").append(`<p id="texto">Imagen analizada: <strong id="n_imagen">${nombre_imagen} </strong></p>`);
		$("#prediction-list").append(`<p id="resultado">Estado: <strong id="resultado2">${p.className}</strong></p>`);
		});
});
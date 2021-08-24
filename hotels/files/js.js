
$(".portfolio").addClass( "btn btn-primary" );
$("li").click(function(){
	$("#menu li").removeClass("btn btn-primary");
	$(".portfolio").removeClass("btn btn-primary");
	$(this).addClass( "btn btn-primary" );
});



$(".square").css({ opacity: 0 });
$(".square1").css({ opacity: 0 });
$(".square2").css({ opacity: 0 });
$(".square3").css({ opacity: 0 });



$(".square").mouseenter(function(){
	$(".square").css({ opacity: 1 });
	$(".contact").css({ opacity: 0.5 });
})
$(".square1").mouseenter(function(){
	$(".square1").css({ opacity: 1 });
	$(".contact1").css({ opacity: 0.5 });
})
$(".square2").mouseenter(function(){
	$(".square2").css({ opacity: 1 });
	$(".contact2").css({ opacity: 0.5 });
})
$(".square3").mouseenter(function(){
	$(".square3").css({ opacity: 1 });
	$(".contact3").css({ opacity: 0.5 });
})





$(".contact").mouseenter(function(){
	$(".square").css({ opacity: 1 });
	$(".contact").css({ opacity: 0.5 });
})
$(".contact1").mouseenter(function(){
	$(".square1").css({ opacity: 1 });
	$(".contact1").css({ opacity: 0.5 });
})
$(".contact2").mouseenter(function(){
	$(".square2").css({ opacity: 1 });
	$(".contact2").css({ opacity: 0.5 });
})
$(".contact3").mouseenter(function(){
	$(".square3").css({ opacity: 1 });
	$(".contact3").css({ opacity: 0.5 });
})




$(".contact").mouseout(function(){
	$(".square").css({ opacity: 0 });
	$(".contact").css({ opacity: 0 });
})
$(".contact1").mouseout(function(){
	$(".square1").css({ opacity: 0 });
	$(".contact1").css({ opacity: 0 });
})
$(".contact2").mouseout(function(){
	$(".square2").css({ opacity: 0 });
	$(".contact2").css({ opacity: 0 });
})
$(".contact3").mouseout(function(){
	$(".square3").css({ opacity: 0 });
	$(".contact3").css({ opacity: 0 });
})



jQuery(document).ready(function($) {
	
  $(function() {
    $(".rslides").responsiveSlides();
  });

  $(".explore_expander").click(function() {
  	$(".explore").animate({
  		height:300,

  	}, 1000, function(){

  	})

  });

});
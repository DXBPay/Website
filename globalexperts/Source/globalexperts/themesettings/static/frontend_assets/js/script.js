$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar-fixed-top");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});

// handle links with @href started with '#' only
$(document).on('click', 'a[href^="#"]', function(e) {
    // target element id
    var id = $(this).attr('href');

    // target element
    var $id = $(id);
    if ($id.length === 0) {
        return;
    }

    // prevent standard hash navigation (avoid blinking in IE)
    e.preventDefault();

    // top position relative to the document
    var pos = $id.offset().top;

    // animated top scrolling
    $('body, html').animate({scrollTop: pos},500);
});

/** login-form js **/


/*****check*****/
$(function () {
  	$('.navbar-toggle-sidebar').click(function () {
  		$('.navbar-nav').toggleClass('slide-in');
  		$('.side-body').toggleClass('body-slide-in');
  		$('#search').removeClass('in').addClass('collapse').slideUp(200);
  	});

  	$('#search-trigger').click(function () {
  		$('.navbar-nav').removeClass('slide-in');
  		$('.side-body').removeClass('body-slide-in');
  		$('.search-input').focus();
  	});
  });
  
  

    $(document).ready(function(){
        // Add minus icon for collapse element which is open by default
        $(".collapse.in").each(function(){
        	$(this).siblings(".card-header").find(".fa").addClass("fa-minus-circle").removeClass("fa-plus-circle");
        });
        
        // Toggle plus minus icon on show hide of collapse element
        $(".collapse").on('show.bs.collapse', function(){
        	$(this).parent().find(".fa").removeClass("fa-plus-circle").addClass("fa-minus-circle");
        }).on('hide.bs.collapse', function(){
        	$(this).parent().find(".fa").removeClass("fa-minus-circle").addClass("fa-plus-circle");
        });
		
		
    });
	
//Drop down menu slide animation
 // Add slideDown animation to Bootstrap dropdown when expanding.
  $('.dropdown').on('show.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // Add slideUp animation to Bootstrap dropdown when collapsing.
  $('.dropdown').on('hide.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
  });
	

//
jQuery(document).ready(function() {
	jQuery('.post').addClass("hidden").viewportChecker({
	    classToAdd: 'visible animated fadeInDown', // Class to add to the elements when they are visible
	    offset: 100    
	   });   
	   
	jQuery('.post-bounce').addClass("hidden").viewportChecker({
	    classToAdd: 'visible animated bounceInUp', // Class to add to the elements when they are visible
	    offset: 100    
	   }); 
	   
	  jQuery('.post-flip').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated flipInX', // Class to add to the elements when they are visible
		offset: 100    
	   }); 
	   
	jQuery('.post-slideUp').addClass("hidden").viewportChecker({
	    classToAdd: 'visible animated slideInUp', // Class to add to the elements when they are visible
	    offset: 100    
	   });  
}); 

//
$(function () {
  $('#demo1').scrollbox();
  $('#demo2').scrollbox({
    linear: true,
    step: 1,
    delay: 0,
    speed: 100
  });
  $('#demo3').scrollbox({
    //switchItems: 5,
    //distance: 144
	linear: true,
	 step: 1,
    delay: 0,
    speed: 20
  });
  $('#demo4').scrollbox({
    direction: 'h',
    //switchItems: 5,
    //distance: 670,
	linear: true,
	 step: 1,
    delay: 0,
    speed: 20
  });
  $('#demo5').scrollbox({
    direction: 'h',
    distance: 134
  });
  $('#demo5-backward').click(function () {
    $('#demo5').trigger('backward');
  });
  $('#demo5-forward').click(function () {
    $('#demo5').trigger('forward');
  });
});

//
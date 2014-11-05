$(document).ready(function(){
  $(".alert").delay(5000).fadeOut(2000);
  $(".alert").click(function(){
  		$(this).hide();
  });
});
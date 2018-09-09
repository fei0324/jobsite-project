// all_users signup.js
$(function(){
	$("#signUpButton").submit(function(event){
		$.ajax({
			url: "api/user/create/"
			}
			console.log(url)
		);
	});
});

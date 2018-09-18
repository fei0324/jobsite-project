// all_users signup.js
$(function(){
	console.log("Ready!")

	$("#signUpButton").click(function(event){

		var username = $("#signUpUsername").val();
		var email = $("#signUpEmail").val();
		var user_type = $("#signUpUserType").val();
		var password = $("#signUpPassword1").val();
		var confirm_password = $("#signUpPassword2").val();

		$.ajax({
			url: "/api/user/create/",
			data: {
				username: username,
				email: email,
				user_type: user_type,
				password: password,
				confirm_password: confirm_password,
			},
			method: "POST",
			//dataType: 'json',
			success: function(url, data) {
				console.log(url)
				console.log(data)
			},
			error: function(response) {
				console.log(response.responseJSON)
				$("#signUpError").append(response.responseJSON);
			},
		});
		return false;
	});
});

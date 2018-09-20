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
				alert("Thanks for signing up!");
			},
			error: function(response) {
				$("#signUpNonFieldError").text(response.responseJSON['non_field_errors']);
				$("#signUpUsernameError").text(response.responseJSON['username']);
				$("#signUpEmailError").text(response.responseJSON['email']);
				$("#signUpPasswordError").text(response.responseJSON['password']);
				$("#signUpConfirmPasswordError").text(response.responseJSON['confirm_password']);
			},
		});
		return false;
	});

	$("#loginButton").click(function(event){

		var username = $("#loginUsername").val();
		var password = $("#loginPassword").val();

		// if (!username || !password) {
		// 	$(".loginError").text("Username and password are required.")
		// } else {
		// 	$(".loginError").empty()
		// }

		var csrf_token = $("#csrf_token").children("input").val();

		$.ajax({
			url: "/user/login/",
			data: {
				username: username,
				password: password,
			},
			headers: {
				'X-CSRFToken': csrf_token,
			},
			method: "POST",
			success: function(data, status, response) {
				if (response.responseJSON['result'] == 'success') {
					window.location.href = "/"
				} else {
					console.log(response)
					$(".loginError").text(response.responseJSON['message'])
				};
			}
		});
		return false;
	});
});


// all_users signup.js
$(function(){
	console.log("Ready!")

	var username = $("#signUpUsername").val();
	var password1 = $("#signUpPassword1").val();
	var password2 = $("#signUpPassword2").val();

	var password = ""

	if (password1 == password2){
		password = password1
	} else {
		console.log("Passwords don't match.")
	}

	var user_type = $("#signUpUserType").val()

	$("#signUpButton").submit(function(event){
		$.ajax({
			url: "api/user/create/",
			data: {
				username: username,
				password: password,
				user_type: user_type,
			},
			method: "POST",
			success: function(url, data) {
				console.log(url)
				console.log(data)
			},
		});
	});
});

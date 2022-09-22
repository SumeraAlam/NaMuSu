
$(window).on("hashchange", function () {
	if (location.hash.slice(1) == "signup") {
		$(".page").addClass("extend");
		$("#login").removeClass("active");
		$("#signup").addClass("active");
	} else {
		$(".page").removeClass("extend");
		$("#login").addClass("active");
		$("#signup").removeClass("active");
	}
});
$(window).trigger("hashchange");

function validateLoginForm() {
	var usn = document.getElementById("logUsn").value;
	var password = document.getElementById("logPassword").value;

	if (usn == "" || password == "") {
		document.getElementById("errorMsg").innerHTML = "Please fill the required fields"
		return false;
	}

	else if (password.length < 8) {
		document.getElementById("errorMsg").innerHTML = "Your password must include atleast 8 characters"
		return false;
	}
	else {
		alert("Successfully logged in");
		return true;
	}
}
function validateSignupForm() {
	var mail = document.getElementById("signEmail").value;
	var usn = document.getElementById("signUsn").value;
    var password = document.getElementById("signPassword").value;
	var conformPassword = document.getElementById("conformPassword").value;

	if (mail == "" || usn == "" || password == ""  ) {
		document.getElementById("errorMsg").innerHTML = "Please fill the required fields"
		return false;
	}
    

	else if (password.length < 8) {
		document.getElementById("errorMsg").innerHTML = "Your password must include atleast 8 characters"
		return false;
	}
    else if(password !=conformPassword){
        document.getElementById("errorMsg").innerHTML = "Your password is incorrect"
		return false;
    }
	else if(usn.length!=10){
		document.getElementById("errorMsg").innerHTML = "Enter Valid USN"
		return false;
	}
	else {
		alert("Successfully signed up");
		return true;
	}
}

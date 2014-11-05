function validateForm() {
    var x = document.forms["signupform"]["email"].value;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".");
    if (atpos< 1 || dotpos<atpos+2 || dotpos+2>=x.length) {
        alert("Not a valid e-mail address");
        return false;
    }

    var pass = document.forms["signupform"]["password"].value;
    var pass_conf = document.forms["signupform"]["conf_password"].value;

    if(pass !== pass_conf){
    	alert("Passwords do not match!");
    	return false;
    }
    return true;
}
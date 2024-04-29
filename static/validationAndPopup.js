document.addEventListener("DOMContentLoaded", function() {
    // Get the reference to the div
    var div_toast = document.getElementById('the_msg_box');

    if (div_toast.innerText.length < 15) {
        document.getElementById('the_msg_box').style.display = 'none';
    } else {
        setTimeout(function() {
            // Hide the div by setting its display property to 'none'
            div_toast.style.display = 'block';
        }, 1000);

        setTimeout(function() {
            // Hide the div by setting its display property to 'none'
            div_toast.style.display = 'none';
        }, 5000); // 10000 milliseconds = 10 seconds
    }

});

function validateEmail(errorShow, btn) {
    var email = document.getElementById("username").value;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if ( email.length > 0 && !emailRegex.test(email) ) {
        document.getElementById(errorShow).innerText = 'invalid email address';
        document.getElementById(btn).disabled = true;
    } else {
        document.getElementById(errorShow).innerText = '';
        document.getElementById(btn).disabled = false;
    }
  }

  function validatePassword(errorShow, btn) {
    var password = document.getElementById("password").value;
    var passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
    
    if ( password.length > 0 && !passwordRegex.test(password) ) {
        document.getElementById(errorShow).innerText = 'invalid password';
        document.getElementById(btn).disabled = true;
    } else {
        document.getElementById(errorShow).innerText = '';
        document.getElementById(btn).disabled = false;
    }
  }
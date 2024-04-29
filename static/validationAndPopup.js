document.addEventListener("DOMContentLoaded", function() {
    // Get the reference to the div
    var div_toast = document.getElementById('the_msg_box');

    if (div_toast.innerText.length < 15) {
        document.getElementById('the_msg_box').style.display = 'none';
    } else {
        setTimeout(function() {
            div_toast.style.display = 'block';
        }, 1000);

        setTimeout(function() {

            div_toast.style.display = 'none';
        }, 5000);
    }

});

function EnableSubmit() {
    let all_error_msg = document.getElementsByClassName('msgError');
    console.log(all_error_msg);
    let flag = true
    for (let i= 0 ; i < all_error_msg.length ; i++) {

        if(all_error_msg[i].innerText == '') {
            flag = false;
        } else {
            flag = true;
        }
    }
    return flag;
    
}

function validateEmail(itemId, errorShow, btn) {
    var email = document.getElementById(itemId).value;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if ( email.length > 0 && !emailRegex.test(email) ) {
        document.getElementById(errorShow).innerText = 'invalid email address';
        document.getElementById(btn).disabled = true;
    } else {
        document.getElementById(errorShow).innerText = '';
        document.getElementById(btn).disabled = EnableSubmit();
    }
  }

  function validatePassword(itemId, errorShow, btn) {
    var password = document.getElementById(itemId).value;
    var passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
    
    if ( password.length > 0 && !passwordRegex.test(password) ) {
        document.getElementById(errorShow).innerText = 'invalid password';
        document.getElementById(btn).disabled = true;
    } else {
        document.getElementById(errorShow).innerText = '';
        document.getElementById(btn).disabled = EnableSubmit();
    }
  }

  function ValidatePhoneNumber(itemId, errorShow, btn) {
    let phone = document.getElementById(itemId).value ;
    let phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(phone)) {
        document.getElementById(errorShow).innerText = 'invalid phone number';
        document.getElementById(btn).disabled = true;
    } else {
        document.getElementById(errorShow).innerText = '';
        document.getElementById(btn).disabled = EnableSubmit();
    }
  }

  function validateText(itemId, errorShow, btn) {
    var name = document.getElementById(itemId).value.trim();
    var nameRegex = /^[a-zA-Z]+(?:-[a-zA-Z]+)*(?:\s+[a-zA-Z]+(?:-[a-zA-Z]+)*)*$/;
    if (name.match(nameRegex) && name.length >= 2 && name.length <= 30) {
        document.getElementById(errorShow).innerText = '';
        document.getElementById(btn).disabled = EnableSubmit();
    } else {
        document.getElementById(errorShow).innerText = 'invalid text';
        document.getElementById(btn).disabled = true;
    }
  }

  function validateDate(itemId, errorShow, btn) {
    var dateString = document.getElementById(itemId).value.trim(); 
    var dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateString.match(dateRegex)) {
      document.getElementById(errorShow).innerText = 'Please enter a date in YYYY-MM-DD format';
      document.getElementById(btn).disabled = true;
    }

    var dateParts = dateString.split('-');
    var year = parseInt(dateParts[0]);
    var month = parseInt(dateParts[1]) - 1; 
    var day = parseInt(dateParts[2]);
    var dateObj = new Date(year, month, day);

    if (dateObj.getFullYear() === year && dateObj.getMonth() === month && dateObj.getDate() === day) {
      document.getElementById(errorShow).innerText = ''; 
      document.getElementById(btn).disabled = EnableSubmit();
    } else {
      document.getElementById(errorShow).innerText = 'Please enter a valid date';
      document.getElementById(btn).disabled = true;
    }
  }

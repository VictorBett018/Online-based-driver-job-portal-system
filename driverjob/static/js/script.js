function checkpass(){
    if(document.signup.pwd.value!=document.signup.cpwd.value){
          alert('Password does not match!');
          document.signup.cpwd.focus();
          return false;
    }
return true;
  }
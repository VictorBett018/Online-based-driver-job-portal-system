function checkpass(){
    if(document.changepass.npass.value!=document.changepass.cnpass.value){
        alert('Password does not match!');
        document.changepass.cnpass.focus();
        return false;
    }
    return true;
}
   
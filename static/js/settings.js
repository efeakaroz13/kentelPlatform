function logout(){
    window.location.assign("/logout");
}

const alert = document.querySelector('ion-alert');

  alert.buttons = [
    {
        text: 'Continue',
        role: 'confirm',
        
    },
    {
      text: 'Cancel',
      role: 'cancel',
     
    },
    
  ];

  alert.addEventListener('ionAlertDidDismiss', (ev) => {
    if(ev.detail.role == "confirm"){
        window.open("/unsubscribe")
    }
  });
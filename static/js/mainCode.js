//KENTEL LTD
// Efe A.




console.log('\
             *@&,                      \n\
       %@@@@@@@@@@@@@#       @@@@@@@    \n\
     @@@@@@.        @@@*    %@@@@@@     \n\
   @@@@@@@            @@@   @@@@@@@     \n\
  @@@@@@@              @@@ @@@@@@@      \n\
 @@@@@@@@               @@@@@@@@@@      \n\
 @@@@@@@                 @@@@@@@@       \n\
/@@@@@@@                 ,@@@@@@@       \n\
@@@@@@@@                 @@@@@@@        \n\
/@@@@@@@                 @@@@@@*        \n\
 @@@@@@@                @@@@@@@         \n\
 @@@@@@@.              @@@@@@@*         \n\
  @@@@@@@             /@@@@@@@@        @\n\
   @@@@@@#           &@@@@@@ @@@      @@\n\
    /@@@@@@         @@@@@@    @@@@@@@@@#\n\
       @@@@@@@@&@@@@@@@,       @@@@@@@  \n\
 \n\n DO NOT PASTE CODE FROM INTERNET, YOUR CREDENTIALS MAY GET STOLEN.\
 \n Anyways,enjoy your experience, Kentel\
')
function main(){

	//
	
}

//helpful subfunctions
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}


setInterval(main,1000);
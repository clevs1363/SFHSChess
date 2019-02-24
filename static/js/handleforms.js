function handleSignUp() {
    function loadGraphs() {
        var email = document.getElementById('emailSignUp').value;
        var username = document.getElementById('usernameSignUp').value;
        var password = document.getElementById('passwordSignUp').value;
        var infoArray = [email, username, password];
        JSONInfoArray = JSON.stringify(infoArray);
        var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function(){
              if (this.readyState === 4 && this.status === 200) {
                var graphParams = getCardData(this.response);
                Plotly.plot('barGraph', graphParams.data);
              }
          };
          xhttp.open("POST", "/user/ " + JSONInfoArray + "");
          xhttp.send();
      }
}
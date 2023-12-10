

function sendClick(color) {
    fetch("https://" + document.location.hostname + ":5672/lights/" + color)
  .then((response) => response.json())
  .then((json) => console.log(json));
}
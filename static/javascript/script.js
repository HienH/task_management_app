let url = 'http://127.0.0:5000/todos'

var get_api_data = function httpGet(url) {
  var xmlHttp = new xmlHttpRequest();
  xmlHttp.open('GET', url, false);
  xmlHttp.send(null);
  return xmlHttp.responseText;
}


$(document).ready(function () {
	$("#search-box").keyup(function(){
		return search($('#search-box').val(), $('#dns').val())
	});
});


var search = function(q, dns) {
	if(!dns) {
		dns = 'http://localhost';
	}
	$.ajax({
		url: dns+":8080/search",
		//callback: "response",
		// Tell jQuery we're expecting JSONP
		//dataType: "jsonp",

		// Tell YQL what we want and that we want JSON
		data: {
			q: q
		},

		// Work with the response
		success: function (data) {
			response(data);
		}
	});
};


var response = function(data) {
	$('.results .total .number').html(data.total);
	$('.results .list').html('');
	data.hits.forEach(function (d) {
		var doc = d._source;
		$('.results .list').append('<tr><th rowspan="2">' + d._id + '</th><th>' + doc.title + '</th><tr><td>' + doc.summary + '</td></tr></tr>');
	});
};
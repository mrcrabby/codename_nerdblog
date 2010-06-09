$(function () {
	$("#new_article").click(function(){
		$.getJSON("adminajax/createarticleform",function(json){
			$("#admin_wrapper").html(json.html);
		});
	});
	
	$("#admin_container").accordion();
	$("input[name='article_publish']").datepicker();
	$("#createbtn").button({icons: {primary: 'ui-icon-disk'}});
	$("#createactivate").buttonset();

});
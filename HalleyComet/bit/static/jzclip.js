
$(function(){
	    ZeroClipboard.setMoviePath('../static/ZeroClipboard.swf');
		    var clip = new ZeroClipboard.Client();
			    
		    clip.setHandCursor( true ); 
			clip.glue('J_copy_clipboard_data');

	        clip.addEventListener('mouseDown', function (){
			clip.setText($('#d1').html());
				 });

			clip.addEventListener("complete", function (){
		    alert('复制成功,您现在可以将它分享到任意你想去的地方！')
				}); 
			$(window).resize(function(){
			clip.reposition();//窗口大小改变后重定位Flash
				});
});

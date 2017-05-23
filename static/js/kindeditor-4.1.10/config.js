KindEditor.ready(function(K) {
	K.create('textarea[name=content]',{
		width: '680px',
		height: '200px',
		uploadJson: '/admin/upload/kindeditor',
	});
});
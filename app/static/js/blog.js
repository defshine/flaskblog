(function($){

     var STATUS_OK = 200;

    function init(){
        initEvent();
        refreshCommentsList();
    }

    function initEvent(){
        $('.comment-submit').on('click',function(){
            saveComment();
        });
    }

    function refreshCommentsList(){
        var postId = $('.post-title').attr('data-key');
        var param = {
            postId:postId
        };
        $.post('/comments',param,function(data){

            if(data.status = STATUS_OK){
                loadCommentList(data.comments);
            }
        });
    }

    function loadCommentList(comments){
        var commentsContainer = $('.comments-container');
        var html = [];
        html.push('<h3>Comments</h3>');
        for(var i = 0 ; i < comments.length; i++){
            var c = comments[i];
            html.push('<div>');
            html.push('<span class="lead">'+c.comment_author+'</span>');
            html.push('&nbsp');
            html.push('<span class="glyphicon glyphicon-time"></span>');
            html.push('&nbsp');
            html.push('<span>'+c.comment_date+'</span>');

            html.push('<p>'+ c.comment_content+'</p>');
        }

        commentsContainer.empty();
        commentsContainer.html(html.join(''))
    }

    function saveComment(){
        var postId = $('.post-title').attr('data-key');
        var commentAuthor = $('.comment-author').val().trim();
        var commentContent = $('.comment-content').val().trim();

        if(commentAuthor == null || commentContent == null)
            return;
         if(commentAuthor == undefined || commentContent == undefined)
            return;
        if(commentAuthor == '' || commentContent == '')
            return;

        var param = {
            postId : postId,
            commentAuthor : commentAuthor,
            commentContent : commentContent
        };
        $.post('/comment',param,function(data){
            if(data.status = STATUS_OK){
                refreshCommentsList();
                $('.comment-author').val('')
                $('.comment-content').val('');
            }
        });
    }

    init();
})(jQuery);
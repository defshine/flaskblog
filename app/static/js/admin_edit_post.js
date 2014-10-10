(function ($) {

    $("#edit-post-content").qeditor({});
    var container = $('.admin-content-right');
    var POST_STATUS_DRAFT = 0;
    var POST_STATUS_PUBLISH = 1;
    var POST_STATUS_PRIVATE = 2;
    var STATUS_OK = 200;

    function _init() {

        _initEvent();
    }

    function _initEvent() {

        $('.edit-post-save-btn').on('click', function () {
            _savePosts();

        });

        $('.edit-post-publish-btn').on('click', function () {
            _publishPosts();

        });

        $('.edit-post-cancel-btn').on('click', function () {


        });

        $('a', '.edit-post-category-select-menu').each(function () {
            $(this).on('click', function () {
                console.log($(this).html());
                $('.edit-post-category-select-btn-value').html($(this).html());
                $('.edit-post-category-select-btn-value').attr('data-key', $(this).attr('data-key'));
                $('.dropdown-toggle').dropdown();

            });

        });

    }

    //ajax
    function _savePosts() {

        var categoryId = $('.edit-post-category-select-btn-value').attr('data-key');
        var postTitle = $('.admin-edit-post-title').val();
        var postContent = $('#edit-post-content').val();
        var postId = $('.admin-edit-post-title').attr('data-key');

        var url = '/post';
        var data = {
            categoryId: categoryId,
            title: postTitle,
            content: postContent,
            postStatus: POST_STATUS_DRAFT
        };
        if (postId != undefined && postId != '') {
            data.postId = postId;
        }

        $.post(url, data, function (data) {

            if (data.status == STATUS_OK) {

                var postId = data.postId;
                $('.admin-edit-post-title').attr('data-key', postId);

                $('.edit-alert').addClass('alert-info');
                $('.edit-alert-info').html('save success');


            } else {
                $('.edit-alert').addClass('alert-danger');
                $('.edit-alert-info').html('save failure');

            }
            $('.edit-alert').css('display','block');

        });

    }

    function _publishPosts() {

        var categoryId = $('.edit-post-category-select-btn-value').attr('data-key');
        var postTitle = $('.admin-edit-post-title').val();
        var postContent = $('#edit-post-content').val();
        var postId = $('.admin-edit-post-title').attr('data-key');


        var url = '/post';
        var data = {
            categoryId: categoryId,
            title: postTitle,
            content: postContent,
            postStatus: POST_STATUS_PUBLISH
        };
        if (postId != undefined && postId != '') {
            data.postId = postId;
        }

        $.post(url, data, function (data) {

            if (data.status == STATUS_OK) {

                var postId = data.postId;
                container.load('/admin/post/' + postId);

            }


        });

    }

    _init();


})(jQuery);
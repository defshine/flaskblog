(function ($) {

    var container = $('.admin-content-right');

     $("#new-post-content").qeditor({});


    var POST_STATUS_DRAFT = 0;
    var POST_STATUS_PUBLISH = 1;
    var POST_STATUS_PRIVATE = 2;
    var STATUS_OK = 200;


    function _init() {

        _initCategorySelectMenu();
        _initEvent();
    }


    function _initCategorySelectMenu() {

        _listCategory();

    }

    function _loadCategoryData(categories) {

        var html = '';
        var menu = $('.newpost-category-select-menu');
        if (categories.length > 0) {

            html += '<li role="presentation"><a role="menuitem" tabindex="-1" data-key="0" href="#">' + 'Uncategorized' + '</a></li>';

            for (var i = 0; i < categories.length; i++) {
                var category = categories[i];
                html += '<li role="presentation"><a role="menuitem" tabindex="-1" data-key="' + category.cat_id + '" href="#">' + category.cat_name + '</a></li>';
            }

        }

        menu.append($(html));

        $('a', '.newpost-category-select-menu').each(function () {
            $(this).on('click', function () {
                console.log($(this).html());
                $('.newpost-category-select-btn-value').html($(this).html());
                $('.newpost-category-select-btn-value').attr('data-key', $(this).attr('data-key'));
                $('.dropdown-toggle').dropdown();

            });

        });

    }

    function _initEvent() {

        $('.new-post-save-btn').on('click', function () {
            _savePosts();

        });

        $('.new-post-publish-btn').on('click', function () {
            _publishPosts();

        });

        $('.new-post-cancel-btn').on('click', function () {


        });

    }

    //ajax
    function _savePosts() {

        var categoryId = $('.newpost-category-select-btn-value').attr('data-key');
        var postTitle = $('.admin-new-post-title').val();
        var postContent = $('#new-post-content').val();
        var postId = $('.admin-new-post-title').attr('data-key');

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
            console.log('save post success----' + data);
            if (data.status == STATUS_OK) {

                var postId = data.postId;
                $('.admin-new-post-title').attr('data-key', postId);

            }

        });

    }

    function _publishPosts() {

        var categoryId = $('.newpost-category-select-btn-value').attr('data-key');
        var postTitle = $('.admin-new-post-title').val();
        var postContent = $('#new-post-content').val();
        var postId = $('.admin-new-post-title').attr('data-key');


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
            console.log('publish  post success----' + data);
            if (data.status == STATUS_OK) {

                var postId = data.postId;
                container.load('/admin/post/'+postId);


            }


        });

    }

    function _listCategory() {
        $.get('/categories', function (data) {
            console.log(data);
            _loadCategoryData(data.categories);

        });
    }


    _init();

})(jQuery);
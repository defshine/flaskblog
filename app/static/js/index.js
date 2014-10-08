(function($){

    var blogContainer = $('.blog-list-container-left-content');

    function _init(){

        _listPost();
        _listCategory();
    }

    function _initEvent(){

        $('.blog-title-btn').each(function(){

            $(this).on('click',function(){

                var postId = $(this).parent().parent().attr('data-key');
                console.log(postId);
                _findPost(postId);

            });

        });



    }

    function _loadPostData(posts){
        var html = [];
        for(var i = 0; i < posts.length; i++){
            var post = posts[i];
            html.push('<div class="blog-container-wrap-content-blog" data-key="'+post.postId+'">');
            html.push('<h2 class=""><a class="blog-title-btn" href="#">'+post.postTitle+'</a></h2>');
            html.push('<hr>');
            html.push('</div>');
        }
        blogContainer.append(html.join(''));
        _initEvent();

    }

    function _loadCategoryData(categories){
        var left = $('.blog-menu-category-left');
        var right = $('.blog-menu-category-right');

        for(var i = 0; i < categories.length; i++){
            var category = categories[i];
            var html = [];
            html.push('<li data-key="'+category.catId+'" >');
            html.push('<a href="#">'+category.catName+'</a>');
            html.push('</li>');

            if(i%2 == 0){
                left.append(html.join(''));
            }else{
                right.append(html.join(''));
            }
        }

    }


    //ajax
    function _listPost(){

        $.get('/posts', function(data){
            var posts = data.posts;
            _loadPostData(posts);
        });

    }

    function _findPost(postId){

        blogContainer.load('/view/post/'+postId);
    }

    function _listCategory(){
        $.get('/categories',function(data){
            var categories = data.categories;
           _loadCategoryData(categories);
        })
    }






    _init();



})(jQuery)
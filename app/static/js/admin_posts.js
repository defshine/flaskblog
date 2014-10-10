(function($){

    var container = $('.admin-content-right');

    $('.admin-edit-btn').each(function(){
        var $this = $(this);
        console.log($this);
        $this.on('click',function(){
            console.log($this.attr('data-key'))

            container.load('/admin/edit_post/'+$this.attr('data-key'));
        });

    });


})(jQuery)
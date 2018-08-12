$(function () {

    $(".subShopping").click(function () {

        var $subShopping = $(this);

        var $li = $subShopping.parents('li');

        var cartid = $li.attr('cartid');
        console.log(cartid);

        $.getJSON('/axf/subtocart/', {'cartid': cartid}, function (data) {
            console.log(data);
            if (data['status'] == '200'){
                if(data['goods_num'] == '0'){
                    $li.remove();
                }else{
                    $subShopping.next().html(data['goods_num']);
                }

                $("#total_price").html(data['total_price']);
            }
        })
    })

    $('.confirm').click(function () {

        var $confirm = $(this);

        var $li = $confirm.parents('li');

        var cartid = $li.attr('cartid');

        console.log(cartid);

        $.getJSON('/axf/changecartstatus/', {'cartid': cartid}, function (data) {

            console.log(data);

            if (data['status'] == '200'){

                if(data['is_select']){
                    $confirm.find('span').find('span').html('√');
                    if (data['is_all_select']){
                        $(".all_select").find('span').find('span').html('√');
                    }

                }else{
                    $confirm.find('span').find('span').html('');
                    $('.all_select').find('span').find('span').html('');
                }
                $("#total_price").html(data['total_price']);
            }

        })

    })

    $('.all_select').click(function () {

        /**
         *  全选初始状态
         *      有一个未选中，全选就是未选中
         *      全都是选中，全选按钮才是选中
         *
         *     点击全选
         *      如果全都是选中，全都变成未选中
         *      如果有一个未选中，应该全选
         *   列表，数组
         *      相当于 fori 遍历
         *      for item in items:
         *
         *
         *
         */
        selects = [];

        unselects = [];

        $('.confirm').each(function () {
            var $confirm = $(this);
            var $li = $confirm.parents('li');
            var cartid = $li.attr('cartid');
            console.log(cartid);

            if($confirm.find('span').find('span').html().length === 0){
            //    未选中元素
                unselects.push(cartid);
            }else{
            //    选中元素
                selects.push(cartid);
            }

        })

        console.log(selects);

        console.log(unselects);

        if (unselects.length === 0){
        //    所有变成未选中
            $.getJSON('/axf/changecartsstatus/', {'carts': selects.join('#'), 'select': false}, function (data) {
                console.log(data);
                if(data['status'] == '200'){
                    $('.confirm > span > span').html('');
                    $('.all_select > span > span').html('');
                     $("#total_price").html(data['total_price']);
                }
            })
        }else{
        //    所有变成选中
            $.getJSON('/axf/changecartsstatus/', {'carts': unselects.join("#"), 'select': true}, function (data) {
                console.log(data);
                if (data['status'] == '200'){
                    $('.all_select > span > span').html('√');
                    $('.confirm > span > span').html('√');
                    $("#total_price").html(data['total_price']);
                }
            })
        }
    })

    $("#make_order").click(function () {

        var selects = [];

        $(".confirm > span > span").each(function () {

            if($(this).html().length > 0){
                selects.push($(this).parents('li').attr('cartid'));
            }

        })

        if (selects.length === 0){
            alert('您还没有选择商品');
        }else{
            console.log(selects);

            $.getJSON('/axf/makeorder/', {'carts': selects.join("#")}, function (data) {
                console.log(data);
                if(data['status'] == '200'){
                    window.open('/axf/orderdetail/?order_id=' + data['orderid'], target='_self');
                }
            })

        }


    })
})
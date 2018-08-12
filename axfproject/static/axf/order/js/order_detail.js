$(function () {


    $("#alipay").click(function () {
        // alert("支付宝正在支付");
    //    调用支付平台 直接成功
        var orderid = $(this).attr('orderid');
    //     修改订单支付状态
        $.get('/axf/alipay/', {'orderid': orderid}, function (data) {

            console.log(data);

            if(data['status'] == '200'){
                window.open('/axf/mine/', target='_self');
            }

        }, 'json')
    })
})
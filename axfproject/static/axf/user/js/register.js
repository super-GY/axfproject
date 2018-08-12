$(function () {

})
function check_data() {
    var pwd = $("#my_pwd").val();
    var pwd_confirm = $("#my_pwd_confirm").val();
    //校验用户名是不是规则
    //邮箱是否合法
    //密码长度和规则 正则可以实现
    if (pwd==pwd_confirm){
       $("#my_pwd").val(md5(pwd));
       $("#my_pwd_confirm").val(md5(pwd_confirm))
    } else {
        // $(".help-block").html()
        alert("密码不一致")
        return false;

    }

}
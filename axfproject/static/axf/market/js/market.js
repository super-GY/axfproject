$(function () {
    var type_icon_is_up = false;
    $("#all_types_btn").click(function () {
        $("#category_container").toggle();
        type_icon_is_up = icon_toggle(type_icon_is_up)
    })
    $("#category_container").click(function () {
        $(this).toggle()
        type_icon_is_up = icon_toggle(type_icon_is_up)
    })

    var sort_icon_is_up = false;
    $("#all_sort_btn").click(function () {
        $("#sort_container").toggle();
        sort_icon_is_up = sort_icon_toggle(sort_icon_is_up)
    })
    $("#sort_container").click(function () {
        $(this).toggle()
        sort_icon_is_up = sort_icon_toggle(sort_icon_is_up)
    })
})
function icon_toggle(type_icon_is_up) {
        var $type_icon = $("#type_icon");
        if (type_icon_is_up == false) {
            $type_icon.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
            type_icon_is_up = true
        } else {
            $type_icon.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
            type_icon_is_up = false
        }
        return type_icon_is_up
}

function sort_icon_toggle(type_icon_is_up) {
        var $type_icon = $("#sort_icon");
        if (type_icon_is_up == false) {
            $type_icon.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
            type_icon_is_up = true
        } else {
            $type_icon.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
            type_icon_is_up = false
        }
        return type_icon_is_up
}
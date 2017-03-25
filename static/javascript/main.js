/**
 * Created by zth on 2017/3/26.
 */
$(function () {
    $("h1").css('position', 'relative').animate({
        left: '200px'
    }, "slow");
    $("h1").css('position', 'relative').animate({
        left: '0px'
    }, "slow");

    $(".footer section").animate({
        'top': '100'
    }, {duration: 2000});

    $(".footer section").animate({
        'top': '0'
    }, {duration: 2000});

    $(".nav li").on("click", function () {
        $(".nav li").removeClass("actived");
        $(this).addClass("actived");
    });

});
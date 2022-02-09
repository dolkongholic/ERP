$("li").click(function () {
    if ($(this).hasClass("active")) {
      $(this).children().css("display", "none");
      $(this).removeClass();
    } else {
      $(this).addClass("active");
      $(this).children().css("display", "block");
    }
  });
$("#btn1").on("click", function()  {
    let date = new Date();
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    let message = `本日は${year}年${month}月${day}日です`
    // jQueryを使って画面にメッセージを表示する
    $("#tBox").val(message);
  });

$("#btn1").css("color","red");

$(function(){
  var totalManageElement = $('input#id_file_set-TOTAL_FORMS');
  var currentFileCount = parseInt(totalManageElement.val());
  $('button#add').on('click', function(){
      var nameElement = $('<input>', {
          type: 'name',
          name: 'file_set-' + currentFileCount + '-name',
          id: 'id_file_set-' + currentFileCount + '-name',
      });
      var fileElement = $('<input>', {
          type: 'radio',
          name: 'file_set-' + currentFileCount + '-src',
          id: 'id_file_set-' + currentFileCount + '-src',
      });
      $('div#file-area').append(nameElement);
      $('div#file-area').append(fileElement);
      currentFileCount += 1;
      totalManageElement.attr('value', currentFileCount);
  });
});

$('.hoge').slick();

  function kakunin(){
    obj = document.test.linkselect;
  
    index = obj.selectedIndex;
    if (index != 0){
      href = obj.options[index].value;
      location.href = href;
    }
  }


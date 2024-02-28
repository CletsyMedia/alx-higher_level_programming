$(document).ready(function(){
  // Event listener for adding an item
  $(document).on('click', '#add_item', function(){
    $('ul.my_list').append('<li>Item</li>');
  });

  // Event listener for removing the last item
  $(document).on('click', '#remove_item', function(){
    $('ul.my_list li:last-child').remove();
  });

  // Event listener for clearing the list
  $(document).on('click', '#clear_list', function(){
    $('ul.my_list').empty();
  });
});

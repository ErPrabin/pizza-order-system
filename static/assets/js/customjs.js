$(document).ready(function () {
    console.log('ready');
  $("#plus").click(function () {
    quantity = parseInt($("#quantity").val()) ;
    price = $("#pizza-price").text();
    price = remove$(price);
    let total_price = (quantity+1) * price;
    console.log(quantity+1,price,total_price);
    $("#total_price").text(total_price);
  });

  $("h5").click(function () {
    console.log("clicked");
    alert("The paragraph was clicked.");
  });
});

function remove$(price){
    cost=price.split("$");
    return cost[1];
}

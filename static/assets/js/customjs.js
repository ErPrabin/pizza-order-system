$(document).ready(function () {
  $("#plus").click(function () {
    quantity = parseInt($("#quantity").val());
    price = $("#pizza-price").text();
    price = remove$(price);
    let total_price = (quantity + 1) * price;
    console.log(quantity + 1, price, total_price);
    $("#price").text("$" + total_price);
    $("#total_price").val(total_price);
    $("#total_quantity").val(quantity+1);
  });
  $("#minus").click(function () {
    quantity = parseInt($("#quantity").val());
    price = $("#pizza-price").text();
    price = remove$(price);
    let total_price = (quantity - 1) * price;
    console.log(quantity + 1, price, total_price);
    $("#price").text("$" + total_price);
    $("#total_price").val(total_price);
    $("#total_quantity").val(quantity-1);


  });

//   $("h5").click(function () {
//     console.log("clicked");
//     alert("The paragraph was clicked.");
//   });
});

function remove$(price) {
  cost = price.split("$");
  return cost[1];
}

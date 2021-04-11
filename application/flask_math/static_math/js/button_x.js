function clickBtn1(dimension) {
  const t1 = document.getElementById("InputFormula").value;
  document.getElementById("InputFormula").value = t1 + "*x**" + dimension.target.eventParam + "+";
}

window.onload = function () {
  var parent = document.getElementById("parent");
  for (var i = 1; i < 6; i++) {
    var element = document.createElement("button");
    element.innerText = "*x**" + i + "+";
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = String(i);
    element.classList.add("btn", "btn-outline-success");
    element.style.marginRight = "5px";
    element.style.padding="5px 5px 5px 5px";
    parent.appendChild(element);
  }
};

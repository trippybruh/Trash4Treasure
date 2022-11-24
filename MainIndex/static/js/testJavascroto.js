var x = 0

function changeHtmlpar() {
    x += 1;
    document.getElementById("test").innerHTML = "SCRIPT WORKS! (" + x + " times)";
}

function fixHeight() {
    document.getElementById("searchdiv").style.height = document.getElementById("accountdiv").style.height
}

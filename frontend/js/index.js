var getClass = (Class)=>document.getElementsByClassName(Class);
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector("nav").style.top = "0";
    document.querySelector("nav").classList.add('shadow');
  } else {
    document.querySelector("nav").style.top = "-60px";
    document.querySelector("nav").classList.remove('shadow');
  }
  prevScrollpos = currentScrollPos;
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.querySelector("nav").classList.add("scroll-navbar");
  } else {
    document.querySelector("nav").classList.remove("scroll-navbar");
    document.querySelector("nav").classList.remove('shadow');
  }
}

for (ClassIndex of getClass("bg-js-color")){
  if(Math.round(Math.random())){
    ClassIndex.style.backgroundColor = "#dc3545"
  }else{
    ClassIndex.style.backgroundColor = "#dc8b8c"
  }
}

function scrollBtn(){
  let currScroll = document.documentElement.scrollTop;
  document.documentElement.scrollTop = document.getElementsByTagName("header")[0].scrollHeight;
}

function appendForm(e){
  if(e.nextElementSibling.innerHTML){
    document.getElementById("append-form").append(document.getElementById('form-comment'));
  }else{
    e.nextElementSibling.append(document.getElementById('form-comment'));
  }
}

for (img of document.getElementsByClassName("img-card")){
  img.style.background = `url(${img.getAttribute("data-src")}) center no-repeat`;
}

var rellax = new Rellax('.rellax');
if(document.querySelector("body").hasAttribute("data-src")){
  document.querySelector("body").style.backgroundImage = `url(${document.querySelector("body").getAttribute("data-src")})`;
}
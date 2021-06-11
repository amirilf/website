var getId = (Id)=>document.getElementById(Id);
var getClass = (Class)=>document.getElementsByClassName(Class);
var queryS = (selector)=>document.querySelector(selector);

var nav = queryS("nav");
var header = queryS("header");
var prevScrollpos = window.pageYOffset;
var append_Form = getId("append-form");
var formComment = getId("form-comment");
var imgCard = getClass("img-card");
var controlBtnNavbar = true;



window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if(controlBtnNavbar){
    if (prevScrollpos > currentScrollPos) {
      nav.style.top = "0";
      nav.classList.add('shadow');
    } else {
      nav.style.top = "-60px";
      nav.classList.remove('shadow');
    }
  }
  prevScrollpos = currentScrollPos;
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    nav.classList.add("scroll-navbar");
  } else {
    nav.classList.remove("scroll-navbar");
    nav.classList.remove('shadow');
  }
};


function scrollBtn(){
  let currScroll = document.documentElement.scrollTop;
  document.documentElement.scrollTop = header.scrollHeight;
}

function appendForm(e){
  if(e.nextElementSibling.innerHTML){
    append_Form.append(formComment);
  }else{
    e.nextElementSibling.append(formComment);
  }
}

for (img of imgCard){
  img.style.background = `url(${img.getAttribute("data-src")}) center no-repeat`;
}


function btnNavbar(){
  controlBtnNavbar = !controlBtnNavbar;
}

if(queryS("body").hasAttribute("data-src")){
  queryS("body").style.backgroundImage = `url(${queryS("body").getAttribute("data-src")})`;
}


var rellax = new Rellax('.rellax');
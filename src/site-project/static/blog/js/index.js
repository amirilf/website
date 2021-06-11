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
var Append_Form = false;
var appendPlace;
var inputHidden;
var SocialNetworks = false;



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
    Append_Form = false;
    e.previousElementSibling.append(e.nextElementSibling.firstElementChild.lastElementChild);
    append_Form.append(formComment);
  }else{
    if(Append_Form){
      appendPlace.append(inputHidden);
    }
    Append_Form = true;
    appendPlace = e.previousElementSibling;
    inputHidden = e.previousElementSibling.firstElementChild;
    e.nextElementSibling.append(formComment);
    formComment.append(inputHidden);
  }
}

for (img of imgCard){
  img.style.background = `url(${img.getAttribute("data-src")}) center no-repeat`;
}


function btnNavbar(){
  controlBtnNavbar = !controlBtnNavbar;
}


function avatarSelect(e){
  getId("articel_input").value =  e.alt;
  for(avatar of getClass("img-avatar")){
    avatar.classList.remove("avatar-selected");
  }
  e.classList.add("avatar-selected");
}




function funcSocialNetworks(e){
  console.log(SocialNetworks);
  if(SocialNetworks){
    SocialNetworks = !SocialNetworks;
  }else{
    SocialNetworks = !SocialNetworks;
  }
}



for(message of getClass("p-message")){
  if(message.innerText.length > 500){
    message.nextElementSibling.classList.remove("d-none");
    message.parentElement.style.maxHeight = "200px"
    message.parentElement.classList.add("pb-4");
  }
}

function showMoreMessage(e){
  if(e.innerText == "show more"){
    e.innerText = "show less";
    e.parentElement.style.width = "auto";
    e.parentElement.classList.add("bg-opacity");
    e.parentElement.parentElement.style.maxHeight = "100%";
  }else{
    e.innerText = "show more";
    e.parentElement.style.width = "100%"
    e.parentElement.parentElement.style.maxHeight = "200px";
    e.parentElement.classList.remove("bg-opacity");
  }
}


if(queryS("body").hasAttribute("data-src")){
  queryS("body").style.backgroundImage = `url(${queryS("body").getAttribute("data-src")})`;
}

var swiper = new Swiper(".mySwiper", {
  loop: true,
  spaceBetween: 45,
  centeredSlides: true,
  autoplay: {
    delay: 4500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
var swiper = new Swiper(".mySwiper2", {
  slidesPerView: "auto",
  centeredSlides: false,
  spaceBetween: 5,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
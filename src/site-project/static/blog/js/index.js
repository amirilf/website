var getId = (Id) => document.getElementById(Id);
var getClass = (Class) => document.getElementsByClassName(Class);
var queryS = (selector) => document.querySelector(selector);





var nav = queryS("nav");
var prevScrollpos = window.pageYOffset;
var controlBtnNavbar = true;
window.onscroll = () => {
    var currentScrollPos = window.pageYOffset;
    if (controlBtnNavbar) {
        if (prevScrollpos > currentScrollPos) {
            nav.style.top = "0";
            for (s of nav.lastElementChild.getElementsByTagName("a")) {
                s.classList.add("text-dark")
            }
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
        for (s of nav.lastElementChild.getElementsByTagName("a")) {
            s.classList.remove("text-dark")
        }
        nav.classList.remove("scroll-navbar");
        nav.classList.remove('shadow');
    }
};

var header = queryS("header");
const scrollBtn = () => document.documentElement.scrollTop = header.scrollHeight;


var append_Form = getId("append-form");
var Append_Form = false;
var formComment = getId("form-comment");
var appendPlace;
var inputHidden;
const appendForm = (e) => {
    if (e.nextElementSibling.innerHTML) {
        Append_Form = false;
        e.previousElementSibling.append(e.nextElementSibling.firstElementChild.lastElementChild);
        append_Form.append(formComment);
    } else {
        if (Append_Form) {
            appendPlace.append(inputHidden);
        }
        Append_Form = true;
        appendPlace = e.previousElementSibling;
        inputHidden = e.previousElementSibling.firstElementChild;
        e.nextElementSibling.append(formComment);
        formComment.append(inputHidden);
    }
}


var imgCard = getClass("img-card");
for (img of imgCard) {
    img.style.background = `url(${img.getAttribute("data-src")}) center no-repeat`;
}
var imgTag = getClass("img-tag");
for (img of imgTag) {
    img.style.background = `url(${img.getAttribute("data-src")}) center no-repeat`;
}

const btnNavbar = () => {
    controlBtnNavbar = !controlBtnNavbar;
}


const avatarSelect = (e) => {
    getId("articel_input").value = e.dataset.avatar;
    for (avatar of getClass("img-avatar")) {
        avatar.classList.remove("avatar-selected");
    }
    e.classList.add("avatar-selected");
}



var SocialNetworks = false;
const funcSocialNetworks = (e) => {
    if (SocialNetworks) {
        SocialNetworks = !SocialNetworks;
    } else {
        SocialNetworks = !SocialNetworks;
    }
}

/////////// showMore ////////////

// for (message of getClass("p-message")) {
//     console.log(message.innerText)
//     if (message.innerText.length > 100) {
//         message.lastElementChild.classList.remove("d-none");
//         message.style.maxHeight = "200px"
//         message.parentElement.classList.add("pb-4");
//     }
// }

// function showMoreMessage(e) {
//     if (e.innerText == "show more") {
//         e.innerText = "show less";
//         e.parentElement.classList.add("bg-opacity");
//         e.parentElement.parentElement.style.maxHeight = "100%";
//         e.parentElement.style.position = "relative"
//         e.style.marginRight = "5px"; 
//     } else {
//         e.innerText = "show more";
//         e.parentElement.parentElement.style.maxHeight = "200px";
//         e.parentElement.style.position = "absolute"
//         e.parentElement.classList.remove("bg-opacity");
//         e.style.marginRight = "10px"; 
//     }
// }

/**
 *  Light Switch @version v0.1.2
 *  @author han109k
 */
if (document.querySelector("#form-comment")) {
    let form = document.querySelector("#form-comment") // there are many easy ways to get this element

    form.addEventListener("submit", evt => {
        // don't actually submit this form to its associated URL:
        submitComment();
        evt.preventDefault();
        // and schedule the timeout
        setTimeout(() => form.submit(), 3000);
    });
}
const submitComment = () => {
    const Toast = Swal.mixin({
        toast: true,
        position: 'bottom-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    Toast.fire({
        icon: 'success',
        title: "Your comment has been submit",
    })
}
const submitSearch = () => {
    if (getId("searchInput").value.trim().length < 3) {
        queryS("#inputErorr").classList.remove("d-none")
        return false
    }
    queryS("#inputErorr").classList.add("d-none")
    return true
}

var btnDarkMode = document.querySelector(".btn-dark-mode")
var darkModeToggle = document.querySelector(".dark-mode-button");
var lightSwitch = document.getElementById("lightSwitch");
if (lightSwitch) {
    darkMode();
    lightSwitch.addEventListener("change", () => {
        lightMode();
    });


    function darkMode() {
        let isSelected =
            localStorage.getItem("lightSwitch") !== null &&
            localStorage.getItem("lightSwitch") === "dark";
        darkModeToggle.classList.replace("fa-sun", "fa-moon");
        btnDarkMode.classList.replace("bg-white", "bg-dark")
        btnDarkMode.children[0].classList.replace("text-dark", "text-white")

        if (isSelected) {
            darkModeToggle.classList.replace("fa-moon", "fa-sun");
            btnDarkMode.classList.replace("bg-dark", "bg-white")
            btnDarkMode.children[0].classList.replace("text-white", "text-dark")


            // document.querySelectorAll(".bg-light").forEach((element) => {
            //     element.className = element.className.replace(/-light/g, "-dark");
            // });
            document.querySelectorAll(".page-link").forEach((e) => e.classList.add("bg-opacity"))
            document.querySelector("main").classList.add("bg-dark");
            document.querySelector("footer").classList.replace("bg-dark", "bg-glass-light");
            if (document.querySelector("#avatar-message")) {
                document.querySelector("#avatar-message").classList.replace("bg-light", "bg-dark");
            }
            if (document.querySelector(".message-box")) {
                document.querySelector(".message-box").classList.add("bg-gray");
            }
            if (document.querySelectorAll(".card")) {
                document.querySelectorAll(".card").forEach(element => {
                    element.classList.add("bg-gray");
                });
            }
            for (input of document.getElementsByTagName("input")) {
                if (input.classList.contains("bg-light")) {
                    input.classList.add("bg-light");
                    input.classList.add("text-dark");
                }
            }

            if (document.querySelector("main").classList.contains("text-dark")) {
                // document.querySelectorAll(".page-link").forEach((e) => e.classList.add("bg-opacity"))
                document.querySelector("main").classList.replace("text-dark", "text-light");
                document.querySelector("footer").classList.replace("text-light", "text-dark");
                for (i of document.getElementsByTagName("i")) {
                    if (i.classList.contains("text-dark")) {
                        i.classList.replace("text-dark", "text-light");
                    }
                }
                for (input of document.getElementsByTagName("input")) {
                    if (input.classList.contains("bg-light")) {
                        input.classList.replace("bg-light", "bg-dark");
                        input.classList.replace("text-dark", "text-light");
                    }
                }
                for (textarea of document.getElementsByTagName("textarea")) {
                    if (textarea.classList.contains("bg-light")) {
                        textarea.classList.add("bg-dark");
                        textarea.classList.add("text-light");
                    }
                }
                for (a of document.getElementsByTagName("a")) {
                    if (a.classList.contains("text-dark") && !a.classList.contains("badge") && !a.classList.contains("btn") && !a.classList.contains("nav-link")) {
                        a.classList.replace("text-dark", "text-light");
                    } else if (a.classList.contains("badge")) {
                        a.classList.replace("bg-dark", "bg-light");
                        a.classList.replace("text-light", "text-dark");
                    }
                }
                for (btn of document.getElementsByClassName("btn")) {
                    if (btn.classList.contains("btn-outline-dark")) {
                        btn.classList.replace("btn-outline-dark", "btn-outline-light");
                    }
                }
            } else {

                for (a of document.getElementsByTagName("a")) {
                    if (a.classList.contains("text-dark") && !a.classList.contains("badge") && !a.classList.contains("btn")) {
                        a.classList.replace("text-dark", "text-light");
                    } else if (a.classList.contains("badge")) {
                        a.classList.replace("text-light", "text-dark");
                        a.classList.replace("bg-dark", "bg-light");
                    }
                }
                for (textarea of document.getElementsByTagName("textarea")) {
                    if (textarea.classList.contains("bg-light")) {
                        textarea.classList.add("bg-dark");
                        textarea.classList.replace("text-dark", "text-light");
                    }
                }
                for (input of document.getElementsByTagName("input")) {
                    if (input.classList.contains("bg-light")) {
                        input.classList.replace("bg-light", "bg-dark");
                        input.classList.replace("text-dark", "text-light");
                    }
                }
                for (i of document.getElementsByTagName("i")) {
                    if (i.classList.contains("text-dark")) {
                        i.classList.replace("text-dark", "text-light");
                    }
                }
                for (btn of document.getElementsByClassName("btn")) {
                    if (btn.classList.contains("btn-outline-dark")) {
                        btn.classList.replace("btn-outline-dark", "btn-outline-light");
                    }
                }
                document.querySelector("main").classList.add("text-light");
                // document.querySelectorAll(".page-link").forEach((e) => e.classList.remove("bg-opacity"))
                document.querySelector("footer").classList.add("text-dark");
            } // set light switch input to true
            lightSwitch.checked = true;
        }
    }

    /**
     * @function lightmode
     * @summary: check whether the switch is on (checked) or not.
     * If the switch is on then set 'lightSwitch' local storage key and call @function darkmode
     * If the switch is off then it is light mode so, switch the theme and
     *  remove 'lightSwitch' key from local storage
     */
    function lightMode() {
        if (lightSwitch.checked) {
            localStorage.setItem("lightSwitch", "dark");
            darkMode();
        } else {
            for (btn of document.getElementsByClassName("btn")) {
                if (btn.classList.contains("btn-outline-light")) {
                    btn.classList.replace("btn-outline-light", "btn-outline-dark");
                }
            }
            for (i of document.getElementsByTagName("i")) {
                if (i.classList.contains("text-light")) {
                    i.classList.replace("text-light", "text-dark");
                }
            }

            for (textarea of document.getElementsByTagName("textarea")) {
                if (textarea.classList.contains("bg-dark")) {
                    textarea.classList.replace("bg-dark", "bg-light");
                    textarea.classList.replace("text-light", "text-dark");
                }
            }
            for (input of document.getElementsByTagName("input")) {
                if (input.classList.contains("bg-dark")) {
                    input.classList.replace("bg-dark", "bg-light");
                    input.classList.replace("text-light", "text-dark");
                }
            }
            //   document.querySelectorAll(".bg-dark").forEach((element) => {
            //     element.className = element.className.replace(/-dark/g, "-light");
            //   });
            document.querySelectorAll(".page-link").forEach((e) => e.classList.remove("bg-opacity"))
            document.querySelector("main").classList.remove("bg-dark");
            document.querySelector("footer").classList.replace("bg-glass-light", "bg-dark");
            if (document.querySelector(".message-box")) {
                document.querySelector(".message-box").classList.remove("bg-gray");
            }
            document.querySelectorAll(".card").forEach(element => {
                element.classList.remove("bg-gray");
            });
            for (a of document.getElementsByTagName("a")) {
                if (a.classList.contains("text-light")) {
                    a.classList.replace("text-light", "text-dark");
                } else if (a.classList.contains("badge")) {
                    a.classList.replace("bg-light", "bg-dark");
                    a.classList.replace("text-dark", "text-light");
                }
            }
            document.querySelector("main").classList.replace("text-light", "text-dark");
            document.querySelector("footer").classList.replace("text-dark", "text-light");
            if (document.querySelector("#avatar-message")) {
                document.querySelector("#avatar-message").classList.replace("bg-dark", "bg-light");
            }
            localStorage.removeItem("lightSwitch");
        }
    }
}

function toggleDarkMode() {
    if (!lightSwitch.checked) {
        lightSwitch.checked = true;
    } else {
        lightSwitch.checked = false;

        darkModeToggle.classList.replace("fa-sun", "fa-moon");
        btnDarkMode.classList.replace("bg-white", "bg-dark")
        btnDarkMode.children[0].classList.replace("text-dark", "text-white")
    }
    lightMode()
}



var shortLinkInput = getId("shortLink")
const copyTxtInput = () => {
    shortLinkInput.select();
    shortLinkInput.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(shortLinkInput.value);

    const Toast = Swal.mixin({
        toast: true,
        position: 'bottom-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    Toast.fire({
        icon: 'info',
        title: "The link was copied to Clipboard",
    })
}

if (getId("bgItem") != null) {
    getId("bgItem").style.backgroundImage = `url(${getId("bgItem").getAttribute("data-src")})`;
}

if (queryS("body").hasAttribute("data-src")) {
    queryS("body").style.backgroundImage = `url(${queryS("body").getAttribute("data-src")})`;
}
try{
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
}catch(err){

}
try{

}catch(err){
    if (document.getElementById(idrow)) {
        document.getElementById(idrow).insertBefore(cln, document.getElementById(idrow).firstChild);
    }
}
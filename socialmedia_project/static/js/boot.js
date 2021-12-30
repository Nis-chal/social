let  menuBtn = document.querySelector('.menu-btn');
let hamburger = document.querySelector('.menu-btn-burger');
let body = document.querySelector('.body')
let toggleTheme = document.querySelector('.theme-toggle')

// ============================hamburger-rotate=================================
menuBtn.addEventListener('click', toggleMenu);
let showMenu = false;
function toggleMenu() {
  if(!showMenu) {
    hamburger.classList.add('open');


    showMenu = true;
  } else {
    hamburger.classList.remove('open');


    showMenu = false;
  }
}

// =======================================toggle-theme===============================


let light_mode = localStorage.getItem("light_mode")
const darkModeToggle = document.querySelector('#light-mode-toggle')

const enableLightMode = () =>{
    document.body.classList.add("light-mode");
    localStorage.setItem("light_mode","enabled");
    toggleTheme.classList.toggle('fa-moon')
    toggleTheme.classList.toggle('fa-sun')
    
};
const disableLightMode =() =>{
    document.body.classList.remove("light-mode");
    localStorage.setItem("light_mode",null);
    toggleTheme.classList.toggle('fa-moon')
    toggleTheme.classList.toggle('fa-sun')
    
}
if(light_mode == 'enabled'){
    enableLightMode();

}
toggleTheme.addEventListener("click", ()=> {
    light_mode = localStorage.getItem("light_mode");

    if (light_mode !== "enabled"){
        enableLightMode()
    }
    else{
        disableLightMode();

    }
})






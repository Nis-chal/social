let showPassword = document.querySelector('.fas')
let password = document.querySelector('#password')

showPassword.addEventListener('click',()=>{
    if(password.type === "password"){
        password.type = "text"
        showPassword.classList.toggle('fa-eye-slash')
        showPassword.classList.toggle('fa-eye')
        
     
    }
    else{
        password.type = "password"
        showPassword.classList.toggle('fa-eye-slash')
        showPassword.classList.toggle('fa-eye')
        
    }
})
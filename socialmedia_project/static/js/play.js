
// animation loader

var loader = document.querySelector('.loader-animation')


window.addEventListener('load',function(){
  setInterval(function(){
    loader.classList.add('fade-out');

  },2000)
  
  
})


        

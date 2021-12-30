// admin nav-menu toggle 

var OffCan = document.querySelector('.btn-off')
    var OffCanvas = document.querySelector('.offcanvas')

    
OffCan.addEventListener('click', (e) => {
    OffCanvas.classList.toggle('.show')

})
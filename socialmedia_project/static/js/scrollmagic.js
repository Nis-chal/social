// play video on reaching center of the view port

var videos = document.querySelectorAll('.videos')
const controller = new ScrollMagic.Controller()

$('.videos').each(function(){
    const trigger = new ScrollMagic.Scene({
    triggerElement: this,

    triggerHook:"onCenter"
    
    


})



.addTo(controller)

.on("enter",(e)=>{
    this.play()
})
.on("leave",(e)=>{
    this.pause()
})

})
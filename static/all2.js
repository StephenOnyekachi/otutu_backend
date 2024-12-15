

const eye = document.querySelector(".eye")
const pass = document.querySelector(".pass")
eye.addEventListener('click', e => {
    if(pass.type === "password"){
        pass.type = "text"
        console.log('text')
    }else{
        pass.type = "password"
        console.log('password')
    }
});

const eye2 = document.querySelector(".eye2")
const pass2 = document.querySelector(".pass2")
eye2.addEventListener('click', e => {
    if(pass2.type === "password"){
        pass2.type = "text"
        console.log('text')
    }else{
        pass2.type = "password"
        console.log('password')
    }
});




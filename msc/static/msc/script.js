let navbar = document.querySelector('.navbar');
let navLinks = document.querySelectorAll('.nav-link');



class UI{
    static Alert(state, color, position, MSG){
        let message = document.createElement('div');
        message.style.position = 'absolute';
        message.style.width = '250px';
        message.style.top = '75px';
        message.style.left = '0px';
        message.style.right = '0px';
        message.style.margin = 'auto';
        message.style.zIndex = '2';
        message.className = `alert alert-${state} text-${color} text-${position}`;
        message.appendChild(document.createTextNode(`${MSG}`));
        document.body.insertBefore(message, navbar);
        setTimeout(function(){ message.remove() }, 5000);
    }
    static formAlert(state, color, position, MSG, containingEl, beforeEl){
        if (document.querySelector('.form-alert')){
            document.querySelector('.form-alert').remove();
            let div = document.createElement('div');
            div.className = `alert alert-${state} text-${position} text-${color} form-alert`;
            div.appendChild(document.createTextNode(`${MSG}`));
            containingEl.insertBefore(div, beforeEl);
            setTimeout(function(){ div.remove(); }, 3000);
        }else{
            let div = document.createElement('div');
            div.className = `alert alert-${state} text-${position} text-${color} form-alert`;
            div.appendChild(document.createTextNode(`${MSG}`));
            containingEl.insertBefore(div, beforeEl);
            setTimeout(function(){ div.remove(); }, 3000);
        }
    }
}

// to handle change in the color of navbar on scroll 
document.addEventListener('scroll', () => {
    if (document.documentElement.scrollTop > 30){
        navbar.classList.add('bg-active-light');
        navbar.style.padding = '3px 0px 5px 0px';
    }else{
        navbar.classList.remove('bg-active-light');
        navbar.style.padding = '20px 0px';
    }
});


removeActiveClass = () =>{
    for (var i =0; i < navLinks.length; i++){ // basically we remove the active class from everything
        navLinks[i].parentElement.classList.remove('active');
    }
}


changeActive = () => {
    navLinks.forEach(link => {
        link.addEventListener('click', function(){
            if (!this.parentElement.classList.contains('active')){
                removeActiveClass();
                this.parentElement.classList.add('active');// then add it to the one clicked on
            }
        });

    });
}

// this is for the clipboard functionality on our contact us icons 
whatsappBtn = new ClipboardJS('.whatsapp'); // this is to initialize the clip board obj
whatsappBtn.on('success', function(e){ // on success; display message to user 
    UI.Alert('success', 'black', 'center', "Whatsapp details copied; CTRL-V to paste");
});     

gmailBtn = new ClipboardJS('.gmail'); // this is to initialize the clip board obj
gmailBtn.on('success', function(e){ // on success; display message to user 
    UI.Alert('success', 'black', 'center', "Gmail address details copied; CTRL-V to paste");
});     



// on DOM content loaded 
document.addEventListener('DOMContentLoaded', function(){ 
    changeActive();
});


function toggleHam(x) {
    x.classList.toggle("change");

    let myMenu = document.getElementById('myMenu')
    let winDiv = document.getElementById('winDiv')

    if (myMenu.className === 'menu') {
        myMenu.className += ' menu-active'
        if (myMenu.className === 'menu menu-active') {
            winDiv.className = ' win-active'
        }
    } else {
        myMenu.className = 'menu'
        winDiv.className = 'win'
    }

}

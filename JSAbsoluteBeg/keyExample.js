//checking a particular key is pressed
window.addEventListener("keydown", checkKeyPressed, false);

function checkKeyPressed(e){
    if (e.keyCode == '65'){//a key code
        console.log("a key pressed");
    }
    //or can do the char code
    if (e.charCode == 97){
        console.log("a char pressed");
    }
}

//do something when the arrow keys are pressed 
window.addEventListener("keydown", moveSomething, false);

function moveSomething(e) {
    switch(e.keyCode){
        case 37:
            console.log("left key pressed");
            break;
        case 38:
            console.log("up key pressed");
            break;
        case 39:
            console.log("right key pressed");
            break;  
        case 40:
            console.log("down key pressed");
            break;  
    }
}

//detecting multiple key presses
window.addEventListener("keydown", keysPressed, false);
window.addEventListener("keyup", keysReleased, false);

var keys = [];

function keysPressed(e){
    //store entry for every key pressed
    keys[e.keyCode] = true;

    //ctrl + shift + 5
    if (keys[17] && keys[16] && keys[53]){
        //do something
        console.log("ctrl shift 5")
    }
    //ctrl + f
    if (keys[17] && keys[70]){
        //do something
        console.log("ctrl f")
        //prevent default browser behaviour
        e.preventDefault();
    }
}

function keysReleased(e){
    //mark keys that were released
    keys[e.keyCode] = false;
}
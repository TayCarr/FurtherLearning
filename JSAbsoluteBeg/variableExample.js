var counter = 0; //global
//in js something is global when it is a direct child of your windows browser window object
//can verify this if you check that counter and window.counter point to the same place
alert(window.counter == counter); //evaluates to true if it is

function returnCounter(){
    return counter;
}

function setState(){
    var state = "on";
    //state = 'on'; //if you do this and dont use var in declaration it will create a global variable
}
setState();
alert(state);//will not be able to access since the variable is local to in the function

function setStateB(){
    var state = "on";
    return state;
}
var state = setStateB()
alert(state);

//block scoping
var x = 100;

function blockScoping(){
    if (true){
        let x = 350; //using let in the declaration makes the variable in the scope of the block {} it is in
        alert(x + ' inside block');
    }
    alert(x + ' outside block');
}

blockScoping();

//redeclaring a var in a funct scope will make the first undefined 
var foo = 'hello';
function doSomething(){
    alert(foo); //this will be 'undefined'
    var foo = 'bye';
    alert(foo); //this will be 'bye'
}

doSomething();
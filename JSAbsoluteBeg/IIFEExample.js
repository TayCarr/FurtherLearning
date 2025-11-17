function areYouLucky() {
    //picks a random number between 0-100
    var foo = Math.floor(Math.random() * 100);

    if (foo > 50) {
        alert("You are lucky");
    } else {
        alert("You are not lucky");
    }
}
//call the function 
areYouLucky();

//anonymous functions
//if you do not give your name a function they are known as anonymous functions
//anon funct #1
var isLucky = function() {
    var foo = Math.floor(Math.random() * 100);

    if (foo > 50) {
        alert("You are lucky");
    } else {
        alert("You are not lucky");
    }
};
var me = isLucky();
alert(me);

//anon funct #2
window.setTimeout(function () {
    alert("Some words");
}, 2000);


//simple IIFE example 
(function () {
    var shout = "WORDS";
    alert(shout);
}) (); //addinf () usually means the stuff before run it, entire function is now treated as an expression

//an IIFE that takes an argument 
(function (a, b) {
    /*code here  */
}) (arg1, arg2);


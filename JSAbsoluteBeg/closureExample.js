
/****EXAMPLE 1****/
//regular calling function passing param
function calculateRectangleArea(length, width){
    return length * width;
}

var roomArea = calculateRectangleArea(10, 10);
//alert(roomArea);

/****EXAMPLE 2****/
//example of returning a function
function youSayGoodbye(){//self contained doesnt rely on outside variables to be passed
    alert('Goodbye');

    function andISayHello(){ //function within a function
        alert("Hello");
    }
    return andISayHello;//returns function
}

//var something = youSayGoodbye(); //assign the returned function
//something();//now call that variable and that var will call the function it holds

/****EXAMPLE 3****/
//often variables will be passed arund and need to be accessed 
function stopWatch(){
    var startTime = Date.now();
     function getDelay(){
        var elapsedTime = Date.now() - startTime; //relies on the outside variable
        alert(elapsedTime);
     }
     return getDelay;
}

var timer = stopWatch();//timer-> [stopWatch & getDelay] 
//code sees that it relies on the var in stopwatch so with the closure (scope/bubble) it makes sure that it is still available when it is need
//hence why it doesnt come up as undefined 

//do something that takes some time
for (var i = 0; i < 100000000; i++){
    var foo = Math.random() * 10000;

}
//call return function
timer();

//closure is a newly created function that also contains its variable context

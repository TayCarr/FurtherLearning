/*
var funnyGuy = {}; //created an object

//multiple ways to define a property 
//dot notation
funnyGuy.firstName = 'Name';
funnyGuy.lastName = 'Last';

//square bracket syntax
funnyGuy['firstName'] = 'Name';
funnyGuy['lastName'] = 'Last';

//literal notation for declaring properties
var funnyGuy = {
    firstName: 'Name',
    lastName: 'Last'
};

//create a method
var funnyGuy = {
    firstName: 'Name',
    lastName: 'Last',

    //method
    getName: function(){
        return "Name is: " + this.firstName + " " + this.lastName;
    }
};
alert(funnyGuy.getName());

//create other objects
var theDude = {
    firstName: 'Other',
    lastName: 'Name',

    //method
    getName: function(){
        return "Name is: " + this.firstName + " " + this.lastName;
    }
};
alert(theDude.getName());

var detective = {
    firstName: 'Debra',
    lastName: 'Morgan',

    //method
    getName: function(){
        return "Name is: " + this.firstName + " " + this.lastName;
    }
};
alert(detective.getName());
*/
//lots of duplicated things above, getName does not need to be duplicated
//first and last names are unique, so person could be an intermediate parent

var person = {
    getName: function(){
        return "Name is: " + this.firstName + " " + this.lastName; //this keyword is important to direct where to look for info
    }
};

var funnyGuy = Object.create(person);
funnyGuy.firstName = 'Name';
funnyGuy.lastName = 'Last';

alert(funnyGuy.getName());

var theDude = Object.create(person);
theDude.firstName = 'Other';
theDude.lastName = 'Name';

alert(theDude.getName());

var detective = Object.create(person);
detective.firstName = 'Debra';
detective.lastName = 'Morgan';

alert(detective.getName());

//extending  built in object 
//for example if you want to add a method to array, a shuffle function
//instead of building a function like shuffle(array)... if you want to do array.shuffle()
//you can use the objects prototype property 
Array.prototype.shuffle = function(){
    var input = this;

    for (var i = input.length - 1; i >= 0; i--){
        var randomIndex = Math.floor(Math.random() * (i + 1));
        var itemAtIndex = input[randomIndex];

        input[randomIndex] = input[i];
        input[i] = itemAtIndex;
    }
    return input;
}
//extending built in objects is controversial as you do not control the future of the object, the array object could get a shuffle function and then it would clash with your code and lead to some issues maybe
//to avoid it could give it a name so unique to your app that it is 0 chance that name would be used 
//nothing is stopping you from going and changing an existing function even and overwriting it, not sure why you would want to do this
//not gonna bother to write the example its just chnaging slice() to instead return "this is awsome"


//EQUALITY
/*
    == and != use type coersion so 42 == "42" will come back as true even though its num vs str
    BUT strict equality and inequality === and !=== would return false if given 42 === "42"
    generally strict is used more than the other, it will better help spot errors in your code

*/
alert(42 == "42");
alert(42 === "42");

//keep in mind comparing objects will act unexpectedly 

//NULL and UNDEFINED
//null stands for no value, setting a var to null gives it a clear indication that no value exists

//can set a value to null or even clear a set value to be null after use 
var test = null; //if you dont set as null then it will default to undefined and have unexpected behaviour 

if (test === null){ //good practice to use ===
    test = 'A name...';
} else {
    test = null;
}

//undefined represents something that hasnt been.. defined yet, the undefined primitive
// most commonly seen when you try to access a variable that has yet to have anything assigned to it
var myVar;
alert(myVar);//undefined

function doNothing() {
    return;
}

var weekendPlans = doNothing;
alert(doNothing); //undefined

//typically wont assign undefined to something but you may want to test if something is undefined
if (myVar === undefined){ //again want to use ===
    //do something 
    alert("define me!"); 
}
//null == undefined will result in true !!! but null === undefined will return false 
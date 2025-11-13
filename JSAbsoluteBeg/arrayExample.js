//creating array 
var groceries = []; //empty 
var groceries = ['apples', "mushroom", "bin bags", "milk", 'eggs', 'juice'];

for (var i = 0; i < groceries.length; i++){
    var item = groceries[i]; //iterate over array
}

//adding an item to the list, adds to the end
groceries.push("cookies"); //returns new length of array
//add an item to the start of the array 
groceries.unshift("bananas"); //returns new length of array

//removing an item from the array
var lastItem = groceries.pop();
var firstItem = groceries.shift();

//slice method
alert(groceries);
var newArray = groceries.slice(1, 4); //copied over, original array is not changed 
alert(newArray);

//finding items in an array
var resultIndex = groceries.indexOf("eggs", 0);
alert(resultIndex);

//merging arrays
var good = ["good", 'sweet', 'great', 'awsome'];
var bad = ['bad', 'stinky', 'nasty', 'awful'];
var goodAndBad = good.concat(bad);









// basics
var text = "some text";
var moreText = 'single quote text';
alert("more text");

//combine strings 
var initial = 'hello';
alert(initial + 'world');

alert("can do" + ' this too');

//accessing individual characters
var vowels = 'aeiou';
alert(vowels[2]);

for (var i = 0; i < vowels.length; i++){
    alert(vowels[i]);
}

//can also use the charAt method that returns a char at the specified position
alert(vowels.charAt(2)); //really only useful with old browsers like IE7....

//concate strings
var stringA = "simple string.";
var stringB = "also a simple string.";

alert(stringA + ' ' + stringB);

//can mix and match string literals with string primitives 
var textA = 'Please';
var textB = new String('stop!');
var combined = textA + " make it " + textB;

alert(combined); //combined type is a string primitive even though it has a mix

//can also use the concat method
var result = textA.concat('make this ', textB, ' ', 'aaaaa');
alert(result);

//substrings 
var theBigString = "This is a longer string for this example.";

//slice method
alert(theBigString.slice(10, 16));
alert(theBigString.slice(0, -6));
alert(theBigString.slice(-10, -7));

//substr method
var newString = theBigString.substr(0, 7); //if ommit the end index it will return the string from the given start till the end of the string substr(5)
console.log(newString);
alert(newString);

//splitting a string
var quote = "If you can add, you can subtract.";
var splitWords = quote.split(" "); //split on the spaces
//can split on w/e 

//finding something inside a string
var question = 'I wonder what the pigs did to make the birds angry.';
alert(question.indexOf('pigs'));//18
alert(question.indexOf('z'));//-1, not found
//lastIndexOf
alert(question.lastIndexOf("the"));
//can specify a starting point for indexOf
alert(question.indexOf("the", 20));

//match regex
var phrase = "There are 3 little pigs.";
var regexp = /[0-9]/;
var numbers = phrase.match(regexp);
alert(numbers[0]);//3

//upper and lower case methods
alert(phrase.toLowerCase());
alert(phrase.toUpperCase());







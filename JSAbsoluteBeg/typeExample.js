/*predefined js objects
* Array
* Boolean 
* Date
* Function
* Math
* Number
* RegExp
* String
*/

//array
var names = ['Jerry', 'Elaine', 'George', 'Kramer'];
var alsoNames = new Array('Dennis', 'Frank', 'Dee', 'Mac');

//round number
var roundNumber = Math.round('3.14');

//date
var today = new Date();

//boolean
var booleanObject = new Boolean(true);

//infinity
var bigNumber = Infinity;

//string
var hello = new String('Hello');

/* object form of the string boolean and number primitives 
object form and primitive form of these types look very similar, example: */
var movie = 'Pulp fiction';
var movieObj = new String('Pulp Fiction');

alert(movie);
alert(movieObj);
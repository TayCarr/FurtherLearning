//if you need to make sure the DOM or the page is loaded before your code runs

//more likely to use this to ensure code runs smoothly 
document.addEventListener("DOMContentLoaded", theDomHasLoaded, false);
//less likely to need this
window.addEventListener("load", pageFullyLoaded, false);

function theDomHasLoaded(e){
    //do something
}

function pageFullyLoaded(e){
    //do something
}

//in your scripts your browser parses your DOM sequentially from top to bottom, any script elements that are found get parsed in order they appear
//your script element has knowledge and access to the previous DOM elements but no knowledge of what is after 
//if script is at the bottom below a p and button then it will have access to those but if you load script prior to p and button it will not know they exist
//if must have script at the top could use the DOMcontentloader to ensure all is loaded before it runs 

//nice to have your script at the bottom as when it loads the html will stop running and page could look frozen 

//above mostly only applies to simple scripts there is ways to help load

//async allows a script to run asynchronously
<>
    //in your scripts your browser parses your DOM sequentially from top to bottom, any script elements that are found get parsed in order they appear
    //your script element has knowledge and access to the previous DOM elements but no knowledge of what is after 
    //if script is at the bottom below a p and button then it will have access to those but if you load script prior to p and button it will not know they exist
    //if must have script at the top could use the DOMcontentloader to ensure all is loaded before it runs 
    //nice to have your script at the bottom as when it loads the html will stop running and page could look frozen 
    //above mostly only applies to simple scripts there is ways to help load
    //async allows a script to run asynchronously
    <script async src='someRandomScript.js'></script> //by using async when a script element is parsed it does not block the rest of your browser from being responsive
    //async will not guarantee the order though you may have a few scripts marked as async and they may run out of order from what they appear
    //defer attribute will run in order in which they are defined but they only get exectuted just a few moments before the DOMContentLoaded event gets fired
    <script defer src='someOtherRandomScript.js'></script>
</>//had to wrap in jsx fragment... these lines are more from html example of showing script call
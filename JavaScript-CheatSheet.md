JavaScript CheatSheet	

Unicode standard: https://www.w3schools.com/charsets/ref_html_utf8.asp

https://www.w3schools.com/js/js_dates.asp

Where To:
	
	<script> Tag:
		<script> </script> # runs a script by calling
		<script src="script.js"></script> # runs extended script
	
	functions:
		function Hello(){document.getElementID("hello").innerHTML = "Hello"} # prints Hello
	
	<body> Tag:
		<body> </body>


Outputs:

	document.write() # Overwrites whole HTML document
	alert() | window.alert() # writes message to little pop up window
	console.log() # writes output in debug console
	window.print() # opportunity to print the page


Statements:

	let x, y;	# Declares 2 variables
	x = 4; 		# Statement 1
	y = x + x; 	# Statement 2
	let z = 6;
	
	let 		# declares block variable / a variable can only declared once
				(let x = 5; let x = 4;	# this is not allowed)
				# let and const have block scope so they cannot be declared inside a{}block and be used outside it --> defined variable can only be used inside block not outside the block
	var			# declares a variable , can be redeclared
	Hoisting: variables can be declared after usage
	ex: 
	x = 5;
	var x;	# declared after using it
	const		# declares an unredecalrable variable so it is constant, musst be declared
	
	// or /**/ is a comment

	operators: (= * + - / % ++ -- ** && || ! & | ^)

	Objects:
		const car = {
			type:"Fiat",
			model:"500", 
			color:"white"
		};					# assigns many values to a var.

	let x = "John";
	let y = new String("John");
	
	// typeof x will return string
	// typeof y will return object
	Also note that comparing two JavaScript objects will always return false.
	let x = false
	Boolean(x) # returns false
	typeof [var]	# returns type of a variable


Events:
	
	<element event='some Javascript'>
	example: <button onclick="document.getElementById('date').innerHTML = Date()">The time is?</button>
	or
	<button onclick="displayDate()">The time is?</button>


Strings:

	str.length 		# returns length of a variable
	str.slice(x,y)	# returns var from position x to y
	str.substr(x,y) # returns y length characters from position x
	substring(x, y) # same as .slice

	split string use backslash:
	let x = "Hello \
	World!";

	multiline string: 
	let x = "`
	Helfdas
	mskm
	`"
   
	let text = "I hate you"
	let newText = text.replace("hate", "love");		# replaces hate with love | and only the first match from the given value
	text.replace(/HATE/g, "love")	# replaces all matches with love

	text = txt.toUpperCase();		# converts to uppercase/lowercase letters
	"    -    ".toLowerCase();
	
	z = x.concat(" ", y);			# connects x to y
	.trim()							# returns string without whitespaces in both sides
	let text = "5";
	text.padStart(4,0)    # Returns 0005
	text.padEnd(4,0)  	  # Returns 5000
	let x = "love"
	x.charAt(0)"			# returns char at position 0 --> l
	x.cahrCodeAt(0)			# returns UTF-16 code of l
	x[0]					# returns l
	x.split(",")			# splits on commas
	x.includes("love")		# returns true
	let firstName = "John";
	let lastName = "Doe";
	let text = `Welcome ${firstName}, ${lastName}!`;	# allows variables in strings
	Infinity  # largest number point
	Hexadezimalnumbers are interpretet with 0x in beginning
	x.toString()		# number to string
	x.toExponential		
	x.toFixed(0)		# returns number with 0 numbers after comma ex. 10
	x.toPrecision(2)	# returns number two digits long ex. 9.8
	Number()			# returns number converted from an argument ex. Number(true) returns 1
	parseInt()			# parses string to an whole number
	parseFloat()
	

Arrays:

	const array_name = [item1, item2, ...];		# declares an array which cannot be reassigned, only elements can be reassigned, has block scope
	var array = [x, y]		# can be reassigned, no block scope
	array_name = []								# declares an array, items can be declares afterwards
	const cars = new Array(40)		# creates an Array with 40 undefined elements
	array.length	# returns numbers of values
	array[array.length -1];		# returns last value of array
	array.push()		# adds new element to array
	array.pop()			# removes last element
	array.shift()		# removes first element
	array.slice()		# can be used to add new elements into array
	array.concat(array) # merging existing array with choosen array
	array.sort()		# sorts the array alphabetically
	array.forEach(f)	# calls for each element a function 'f'
	array.map(f)		# creates a new array by performing a function 'f' on each element
	array.filter(f)		# creates a new array with array elements that passes the test 'f'
	array.every(f) 		# checks if all array elements passes the test 'f'
	array.indexOf(item, start)		# searches an arry for an element and returns its position
	array.includes()	# check if an element is presented in the array
	array.find(f)		# returns the value of the first item which passes the test 'f'


Date:

	new Date()	# returns current time
	new Date(year,month,day,hours,...)
	const d = new Date("2015-03-25T12:00:00Z")	# iso date
	get and set methods


Math:

	https://www.w3schools.com/js/js_math.asp
	math.pow(8,2); 		# returns 64
	math.sqrt(64);		# returns 8
	math.abs(-4.7); 	# returns 4.7
	math.random();		# returns random number
	Math.floor(Math.random() * 10); 	# returns random number from 0 to 9
	Math.floor(Math.random() * 10) + 1; 	# returns random number from 1 to 9
	floats:
	let x = 0.1;
	let y = 0.2;
	let z = x + y 	// does not return 0.3
	solution: multiplication
	let z = (x * 10 + y * 10) / 10;       // z will be 0.3
		

Conditions:
	
	IF:
		if(condition) {
			// block of code to be executed by true condition
		} else if (condition2) {
		} else {
		}
	
	SWITCH and Case:
		switch(expression) {
			case x:
				// block of code
				break;
			case y:
				// block of code
				break;
			default:
				// if there is no mtach default block is executed
		}
		
	For:
		for (let i = 0; i < 10; i++) {
			document.getElementID("test").innerHTML = i;
		} // same as c++
		
		for (let i = 0; i < 10; i++) {
			if (i == 3) { break; } // break jumps out of loop
				document.getElementID("test").innerHTML = i;
		} // same as c++
	
	For in:
		const numbers = [12,18,200];
		let txt = "";
		for (let x in numbers) {
		  txt += numbers[x];
		}
		// same with forEach
		numbers.forEach(myFunction);
		function myFunction(value) {
		  txt += value;
		}
	
	Iterables:
		var numbers = [1,2,3,4,5];
		for (var x of letters){
			numbers[x] += 1;
		}


Classes:

	class ClassName {
		constructor(name, year){
			this.name = name;
			this.year = year;
		} // always add an constructor
	}
		age() {
			let date = new Date();
			return date.getFullYear() - this.year;
		} // add methods to the class
	}
	let myCar1 = new ClassName("Ford", 2012);
	ageofcar = myCar1.age();


Specials:
	Sets: // sets are a array of unique variables
		const names = new Set(["Adolf","Mia","John"])
		//or
		const names2 = new Set()
		names2.add("Mia");
	
	Maps: // like two dimensional array
		const couples = new Map ([
		["Mia", "John"),
		["Jason", "Alone",]
		]);
		// or
		const couples = new Map()
		couples.set("Jason", "Alone");
		couples.get("Jason");	# returns alone
		couples.delete("Jason");
	
	RegExp:
		/w3schools/i		# regular expression
		w3schools			# is a pattern (used in a search)
		let x = text.search(/love/i)		# search variable text for match "love" and return the position --> do not have to be carefull of right spelling
	
	Errors:
		try {
			// code
		}
		catch(err) {
			// code
		}
		finally {
		 Block of code to be executed regardless of the try / catch result  // additional code to try and catch
		}
	
	strict mode:
		"use strict";	// activates strict mode
						// strict mode helps for a cleaner code and throws errors if variables are undeclared
		ex: "use strict";
			x = 3; 			// cause an error because x is not declared
	
	This: 
		// this keyword refers to an object or an element
		const person = {
		  firstName: "John",
		  lastName: "Doe",
		  id: 5566,
		  fullName : function() {
		    return this.firstName + " " + this.lastName;
		  }
		};	// returns John Doe

	Arrow Function:
		hello = () => "Hello World!"; 	// returns Hello World
		// works only if function only has one statement
	
	Debugging: 
		use console.log() to print code 
		to set breakpoints write "debugger;" in the line you want to set breakpoint
	
	Style of code:
		- Always use 2 spaces for indentation of code blocks(not tab)
		- Spaces around Operators
		- declare variables with camelCase (or under_scores)
		- always end single statement with semicolon
		- put the opening bracket at the end of the first line and end bracket at a new line after the statements
		- do not end a complex statement with a semicolon
		- line length < 80 charachters
		- variable and funtion names written as camelCase
		- global variables written in UPPERCASE
		- constants written in UPPERCASE
		- avoid new 		// declare and initialize elements in beginning
		- avoid == 			// use ===
		- avoid eval()		// allows arbitary code to be executed (run text as code) --> security problem XSS
		- use default in every switch and case
		- avoid number, string, and boolean as objects --> always treat them as values, also you cannot compare two objects
		
	Performance:
		- use defer="true" to load the script after the page  is loaded
		- avoid using with --> negative effect of speed
		
		
		
JSON: 

	json data is written in name/value pairs
	ex: {"firstName":"John"}
	JSON is commonly used to read data from a web server and print it on the web page.
	String in JSON syntax:
	let text = '{ "employees" : [' +
	'{ "firstName":"John" , "lastName":"Doe" },' +
	'{ "firstName":"Anna" , "lastName":"Smith" },' +
	'{ "firstName":"Peter" , "lastName":"Jones" } ]}';
	To convert the string into JS object:
	const obj = JSON.parse(text);


Async:

	Callbacks:
	A callback function is a function passed as a parameter to another function.
	function myCalculator(num1, num2, myCallback) {
	  let sum = num1 + num2;
	  myCallback(sum);
	}	//callbacks are used in asynchronus functions, where one function has to wait for another function
	commonly used in waiting for files:
	ex. waiting for files:
	function myDisplayer(some) {
	  document.getElementById("demo").innerHTML = some;
	}
	
	function getFile(myCallback) {
	  let req = new XMLHttpRequest();
	  req.open('GET', "mycar.html");
	  req.onload = function() {
	    if (req.status == 200) { // 200 is the value "OK" in html
	      myCallback(this.responseText);
	    } else {
	      myCallback("Error: " + req.status);
	    }
	  }
	  req.send();
	}
	getFile(myDisplayer);
	
	promises:
	// in js exist the Promise object which contains the produced code and the calls to the consuming code
	ex:
	let myPromise = new Promise(function(myResolve, myReject) {
	// "Producing Code" (May take some time)
	  myResolve(); // when successful
	  myReject();  // when error
	});
	// "Consuming Code" (Must wait for a fulfilled Promise)
	myPromise.then(
	  function(value) { /* code if successful */ },
	  function(error) { /* code if some error */ }
	);	
	ex. waiting for file:
	let myPromise = new Promise(function(myResolve, myReject) {
	  let req = new XMLHttpRequest();
	  req.open('GET', "mycar.htm");
	  req.onload = function() {
	    if (req.status == 200) {
	      myResolve(req.response);
	    } else {
	      myReject("File not Found");
	    }
	  };
	  req.send();
	});
	
	myPromise.then(
	  function(value) {myDisplayer(value);},
	  function(error) {myDisplayer(error);}
	);

	async:
	// async makes the function return a promise
	ex: 
	async function myFunction() {
	  return "Hello"; // same now as return Promise.resolve()
	}
	myFunction().then(
	  function(value) {myDisplayer(value);}, // code succesfull
	  function(error) {myDisplayer(error);} // code error	
	);

	await:
	// await waits for a promise (can only be used inside an async funtion)
	ex:
	async function myDisplay() {
	  let myPromise = new Promise(function(resolve, reject) {
	    resolve("I love You !!");
	  });
	  document.getElementById("demo").innerHTML = await myPromise;
	}
	myDisplay();
	ex waiting for file:
	async function getFile() {
	  let myPromise = new Promise(function(resolve) {
	    let req = new XMLHttpRequest();
	    req.open('GET', "mycar.html");
	    req.onload = function() {
	      if (req.status == 200) {
	        resolve(req.response);
	      } else {
	        resolve("File not Found");
	      }
	    };
	    req.send();
	  });
	  document.getElementById("demo").innerHTML = await myPromise;
	}
	getFile();


HTML DOM (Document Object Model):

	Info:
	when the web page is loaded the browser creates a dom of the page.
	It's constructed like a tree with the root element(<html>)and elements like(<head>, <body>, <p>, <title>, <h1>) 
	DOM defines the standard structure model for specific document types. 
		
	all document methods: https://www.w3schools.com/js/js_htmldom_document.asp
	
	const element = document.getElementById("intro");
	// example finds document with the id intro, if its not found it will return null
	
	validation: https://www.w3schools.com/js/js_validation.asp
	function validateForm() {
	  let x = document.forms["myForm"]["fname"].value;
	  if (x == "") {
	    alert("Name must be filled out");
	    return false;
	  }
	} // function returns an alert if names in a field is empty

	CSS:
	// to change style of a html element use:
	document.getElementById(id).style.property = new style
	ex:
	<html>
	<body>
	
	<p id="p2">Hello World!</p>
	
	<script>
	document.getElementById("p2").style.color = "blue";
	</script>
	
	</body>
	</html>
	

	animations:
	ex:
	<!DOCTYPE html>
	<html>
	<style> 
	#container { // container should be created with postition positive and animation with position absolute
	  width: 400px;
	  height: 400px;
	  position: relative;
	  background: yellow;
	}
	#animate {
	  width: 50px;
	  height: 50px;
	  position: absolute;
	  background-color: red;
	}
	</style>
	<body>
	
	<p><button onclick="myMove()">Click Me</button></p> 
	
	<div id ="container"> // all animations should be related to a container element	
	  <div id ="animate"></div>
	</div>
	
	<script>
	function myMove() {
	  let id = null;
	  const elem = document.getElementById("animate");   
	  let pos = 0;
	  clearInterval(id);
	  id = setInterval(frame, 5);
	  function frame() {
	    if (pos == 350) { // test if finished
	      clearInterval(id);
	    } else { 
	      //code to change the element style		
	      pos++; 
	      elem.style.top = pos + "px"; 
	      elem.style.left = pos + "px"; 
	    }
	  }
	}
	</script>
	
	</body>
	</html>

	events: 
	// jabvacript code can be executed if a an html event is activated
	examples:
	<button oncklick="displayDate()></button>
	<body onload="checkCookies()"> // is triggered when the user enters or leaves the page | onload, onunload
	others: onmouseover, onmouseout, onmousedown, onmouseup
	function addeventlisteners():
	element.addEventListener(event, function, useCapture)
	ex: // event listener fires when button is clicked
	document.getElementById("myBtn").addEventListener("click", displayDate)

	add event handler to an element:
	element.addEventListener("click", function(){alert("Hello World");}) // alert hello world if user clicks on an element
	
	Navigation:
	<html> is the root node
	<html> has no parents
	<html> is the parent of <head> and <body>
	<head> is the first child of <html>
	<body> is the last child of <html>
	and:
	
	<head> has one child: <title>
	<title> has one child (a text node): "DOM Tutorial"
	<body> has two children: <h1> and <p>
	<h1> has one child: "DOM Lesson one"
	<p> has one child: "Hello world!"
	<h1> and <p> are siblings
	document.body // displays the body of the document
	document.documentElement // displays full document
	
	nodes: // nodes are need by creating a new element
	https://www.w3schools.com/js/js_htmldom_nodes.asp
	<script>
	const para = document.createElement("p"); // creates new paragraph <p>
	const node = document.createTextNode("This is new."); // creates new text node for <p>
	para.appendChild(node); appends text node to <p>
	// now the element must be appended to an existing element
	const element = document.getElementById("div1"); //finds the element
	element.appendChild(para); // appends the element
	</script>

	html collections: https://www.w3schools.com/js/js_htmldom_collections.asp

	node list: 
	 // A NodeList object is a list (collection) of nodes extracted from a document.
	ex:
	const myNodeList = document.querySelectorAll("p");
	// The elements in the NodeList can be accessed by an index number. To access the second <p> node you can write:
	myNodeList[1]


Browser BOM (Browser Object Model):

	// every method and variable is element of the window
	determine size of the browser window:
	window.innerHeight (in pixels)
	window.innerWidth (in pixels)
	window.open() - open a new window
	window.close() - close the current window
	window.moveTo() - move the current window
	window.resizeTo() - resize the current window
	
	screen:
	screen.width	// returns width of the visitor screen in pixels
	screen.height 	// returns height of the visitor screen in pixels
	
	location:
	window.location.href returns the href (the URL) of the current page
	window.location.hostname returns the domain name of the web host
	window.location.pathname returns the path and filename of the current page
	window.location.protocol returns the web protocol used (http: or https:)
	window.location.port returns the number of the port of the current web page
	window.location.assign() loads a new document

	history:
	window.back()	// same as clicking back in the browser
	window.forward() // same as clicking forward in the browser (loads next url in the browser history)
	window.go() // loads a specific url from browser history
	
	navigator:
	navigator.cookieEneabled;	// returns true if cookies are enabled
	navigator.appVersion // returns the version information of the browser
	navigator.userAgent; // returns the user-agent header sent by the browser of the server
	navigator.platform; // returns the os of the browser
	navigator.online; // returns true if the browser is online
	
	timing:
	myVar = setTimeout(function, milliseconds) // after milliseconds function will be executed
	clearTimeout(myVar); // stops the execution set by setTimeout
	setInerval(function, milliseconds) // executes code in intervals
	clearInterval()

	cookies:
	create cookie:
	document.cookie = "username=John Doe; expires=Thu, 18 Dec 2021 12:00:00 UTC; path=/"; // example with username , visit date and path the cookie belongs to(current page)
	read cookie:
	let x = document.cookie;
	deleting cookie:
	set expires to a past date (!specify the path of the cookie!)
	ex: // stores name and how long it should store the cookie
	function setCookie(cname, cvalue, exdays) {
	  const d = new Date();
	  d.setTime(d.getTime() + (exdays*24*60*60*1000));
	  let expires = "expires="+ d.toUTCString();
	  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
	}	
	// to get a cookie (return the value of the cookie)
	function getCookie(cname) {
	  let name = cname + "=";
	  let decodedCookie = decodeURIComponent(document.cookie);
	  let ca = decodedCookie.split(';');
	  for(let i = 0; i <ca.length; i++) {
	    let c = ca[i];
	    while (c.charAt(0) == ' ') {
	      c = c.substring(1);
	    }
	    if (c.indexOf(name) == 0) {
	      return c.substring(name.length, c.length);
	    }
	  }
	  return "";
	} 
	// to check if cookie is set, if its then it display a greeting otherwise it will prompt a box and ask for the username, then it stores it for 365 days by calling the setCookie
	function checkCookie() {
	  let username = getCookie("username");
	  if (username != "") {
	   alert("Welcome again " + username);
	  } else {
	    username = prompt("Please enter your name:", "");
	    if (username != "" && username != null) {
	      setCookie("username", username, 365);
	    }
	  }
	}


API's:

	browser and server apis can extend the functionallity of a web server
	
	validation:
	checkValidity()	Returns true if an input element contains valid data.
	setCustomValidity()	Sets the validationMessage property of an input element.
	customError	Set to true, if a custom validity message is set.
	patternMismatch	Set to true, if an element's value does not match its pattern attribute.
	rangeOverflow	Set to true, if an element's value is greater than its max attribute.
	rangeUnderflow	Set to true, if an element's value is less than its min attribute.
	stepMismatch	Set to true, if an element's value is invalid per its step attribute.
	tooLong	Set to true, if an element's value exceeds its maxLength attribute.
	typeMismatch	Set to true, if an element's value is invalid per its type attribute.
	valueMissing	Set to true, if an element (with a required attribute) has no value.
	valid	Set to true, if an element's value is valid.
		
	storage api:
	localStorage.setItem(item) // stores data in storage
	localStorage.getItem(name)	// retrieves data from the storage
	sessionStorage.getItem(item) //stores data for one session
	sessionStorage.setItem(name) //stores data item in storagekey(n)	Returns the name of the nth key in the storage
	others:
	length	Returns the number of data items stored in the Storage object
	getItem(keyname)	Returns the value of the specified key name
	setItem(keyname, value)	Adds that key to the storage, or update that key's value if it already exists
	removeItem(keyname)	Removes that key from the storage
	clear()	Empty all key out of the storage	
	
	web worker:
	is a javascript which runs in background and doesn't affect the websites performance
	check if client supports web worker:
	if (typeof(Worker) !== "undefined") {
	  // Yes! Web worker support!
	  // Some code.....
	} else {
	  // Sorry! No Web Worker support..
	}
	ex: https://www.w3schools.com/js/js_api_web_workers.asp
		
	fetch api:
	it allows web browsers to make http requests to web servers
	ex: // fetches file and displays content
	 fetch(file)
	.then(x => x.text())
	.then(y => myDisplay(y));
			
	geolocation:
	// returns latitude and longtitue of the users position
	<script>
	const x = document.getElementById("demo");
	function getLocation() {
	  if (navigator.geolocation) {
	    navigator.geolocation.getCurrentPosition(showPosition);
	  } else {
	    x.innerHTML = "Geolocation is not supported by this browser.";
	  }
	}
	
	function showPosition(position) {
	  x.innerHTML = "Latitude: " + position.coords.latitude +
	  "<br>Longitude: " + position.coords.longitude;
	}
	</script>
	// error handling
	function showError(error) {
	  switch(error.code) {
	    case error.PERMISSION_DENIED:
	      x.innerHTML = "User denied the request for Geolocation."
	      break;
	    case error.POSITION_UNAVAILABLE:
	      x.innerHTML = "Location information is unavailable."
	      break;
	    case error.TIMEOUT:
	      x.innerHTML = "The request to get user location timed out."
	      break;
	    case error.UNKNOWN_ERROR:
	      x.innerHTML = "An unknown error occurred."
	      break;
	  }
	}
	// displaying result in a map
	function showPosition(position) {
	  let latlon = position.coords.latitude + "," + position.coords.longitude;
	
	  let img_url = "https://maps.googleapis.com/maps/api/staticmap?center=
	  "+latlon+"&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";
	
	  document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
	}
	 others:
	coords.latitude	The latitude as a decimal number (always returned)
	coords.longitude	The longitude as a decimal number (always returned)
	coords.accuracy	The accuracy of position (always returned)
	coords.altitude	The altitude in meters above the mean sea level (returned if available)
	coords.altitudeAccuracy	The altitude accuracy of position (returned if available)
	coords.heading	The heading as degrees clockwise from North (returned if available)
	coords.speed	The speed in meters per second (returned if available)
	timestamp	The date/time of the response (returned if available)
	
	example: // watches current position of client and is updating it:
	<script>
	const x = document.getElementById("demo");
	function getLocation() {
	  if (navigator.geolocation) {
	    navigator.geolocation.watchPosition(showPosition);
	  } else {
	    x.innerHTML = "Geolocation is not supported by this browser.";
	  }
	}
	function showPosition(position) {
	  x.innerHTML = "Latitude: " + position.coords.latitude +
	  "<br>Longitude: " + position.coords.longitude;
	}
	</script>


JS AJAX:
	
	It can:
	- Read data from a web server - after the page has loaded
	- Update a web page without reloading the page
	- Send data to a web server - in the background
	AJAX is not a programming language.
	AJAX is a technique for accessing web servers from a web page.
	AJAX stands for Asynchronous JavaScript And XML.
	AJAX allows web pages to be updated asynchronously by exchanging data with a web server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.

	xml http request:
	variable = new XMLHttpRequest();
	//define a callback function to execude code if the response is ready
	xhttp.onload = function() {
	  // Here you can use the Data
	}
	// to send a request to a server
	xhttp.open("GET", "ajax_info.txt");
	xhttp.send();
	methods:
	- new XMLHttpRequest()	Creates a new XMLHttpRequest object
	- abort()	Cancels the current request
	- getAllResponseHeaders()	Returns header information
	- getResponseHeader()	Returns specific header information
	- open(method, url, async, user, psw)	Specifies the request
	method: the request type GET or POST
	url: the file location
	async: true (asynchronous) or false (synchronous)
	user: optional user name
	psw: optional password
	- send()	Sends the request to the server
	Used for GET requests
	- send(string)	Sends the request to the server.
	Used for POST requests
	- setRequestHeader()	Adds a label/value pair to the header to be sent

	properties:
	- onload	Defines a function to be called when the request is recived (loaded)
	- onreadystatechange	Defines a function to be called when the readyState property changes
	- readyState	Holds the status of the XMLHttpRequest.
	0: request not initialized
	1: server connection established
	2: request received
	3: processing request
	4: request finished and response is ready
	- responseText	Returns the response data as a string
	- responseXML	Returns the response data as XML data
	status	Returns the status-number of a request
	200: "OK"
	403: "Forbidden"
	404: "Not Found"
	For a complete list go to the Http Messages Reference
	- statusText	Returns the status-text (e.g. "OK" or "Not Found")

	responses:
	XMLHttpRequest object has an inbuilt XML parser
	it can parse the response as an XML DOM onject
	const xmlDoc = xhttp.responseXML;
	const x = xmlDoc.getElementsByTagName("ARTIST");
	
	let txt = "";
	for (let i = 0; i < x.length; i++) {
	  txt += x[i].childNodes[0].nodeValue + "<br>";
	}
	document.getElementById("demo").innerHTML = txt;
	
	xhttp.open("GET", "cd_catalog.xml");
	xhttp.send();
	ex: // returns all header information from server response
	const xhttp = new XMLHttpRequest();
	xhttp.onload = function() {
	    document.getElementById("demo").innerHTML =
	    this.getAllResponseHeaders();
	}
	xhttp.open("GET", "ajax_info.txt");
	xhttp.send(); 
		
	xml file:
	example: // following code extracts data from xml file if a button is clicked, writes it into an html table and prints it to the web page
	function loadDoc() {
	  const xhttp = new XMLHttpRequest();
	  xhttp.onload = function() {myFunction(this);}
	  xhttp.open("GET", "cd_catalog.xml");
	  xhttp.send();
	}
	function myFunction(xml) {
	  const xmlDoc = xml.responseXML;
	  const x = xmlDoc.getElementsByTagName("CD");
	  let table="<tr><th>Artist</th><th>Title</th></tr>";
	  for (let i = 0; i <x.length; i++) {
	    table += "<tr><td>" +
	    x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue +
	    "</td><td>" +
	    x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue +
	    "</td></tr>";
	  }
	  document.getElementById("demo").innerHTML = table;
	}
		
	AJAX database:
	https://www.w3schools.com/js/js_ajax_database.asp

	
JSON:
https://www.w3schools.com/js/js_json_intro.asp

	


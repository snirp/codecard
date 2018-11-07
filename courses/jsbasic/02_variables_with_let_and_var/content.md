In a program, you may want to store some data: the name of your boss, his age, or his phone number. A variable is a "named storage" for such data. You can think of it as having two parts: a unique identifier or *variable name* and a location in memory that holds the data or *value*. 

# Variable declaration and assignment
Use the `let` keyword to create a variable in JavaScript.

```js
let message;
message = 'Hello!';
alert(message); // Hello!
```

This code sample:

1. Creates (in other words: declares or defines) a variable with the name “message”.
2. Assigns it a value using the assignment operator `=`. The value “Hello!” is now saved into the memory area associated with the variable.
3. Accesses the variable content by using the variable name.

For brevity, it is possible merge the variable declaration and assignment into a single line.

```js
let message = 'Hello!'; // define the variable and assign the value
alert(message); // Hello!
```

It's even possible to declare and assign multiple variables in one line:

```js
// Separate statements
let user = 'John';
let age = 25;
let message = 'Hello';

// Single statement on one line
let user = 'John', age = 25, message = 'Hello';

// Same, but formatted over several lines
let user = 'John'
  , age = 25
  , message = 'Hello';
```

All three variants achieve exactly the same result. Which one to use is a matter of personal preference. 

# The `var` keyword
The `var` keyword works almost the same as `let` and is mainly used in older code. It also declares a variable, but in a slightly different fashion, which may surprise novice programmers. The nuances require an in-depth knowledge of Javascript execution, so it may be better to avoid surprises for now and stick to `let`.

```js
var message = 'Hello!';
alert(message); // Hello!
```

# Changing values

After variables have been declared and assigned, they can be reassigned. 

```js
let message = 'Hello!';
let hello;

hello = message;
message = 'Bye!';

alert(hello); // Hello!
alert(message); // Bye!
```

Here we demonstrate two ways to to reassign a value:
- We assign the *value* of variable `message` to variable `hello`, by placing it to the right side of the assignment operator `=`.
- We assign the string value `Bye!` to `message`.



It's possible to declare a “constant” variable, using `const` instead of `let` or `var`. A constant must always be initialized with a value and it's not allowed to assign a value after declaration. Either action will result in an error.

```js
const age = 39;
age = 40; // TypeError: Assignment to constant variable
const name; // SyntaxError: Missing initializer in const declaration
```

When a programmer is sure that they never need to re-assign a variable, they can use `const` to guarantee that, and also to clearly show that fact to everyone.

# Uppercase constants
It is a common practice to use constants as aliases for difficult-to-remember values that are known prior to execution. Such constants are named using capital letters and underscores.

```js
const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// pick a color
let primaryColor = COLOR_ORANGE;
alert(primaryColor); // #FF7F00
```

Benefits:
- COLOR_ORANGE is much easier to remember than "#FF7F00".
- COLOR_ORANGE is less prone to typos than "#FF7F00".
- When reading the code, COLOR_ORANGE is much more meaningful than #FF7F00.

The uppercase convention is used only when the value is known prior to execution. For values that are calculated during runtime - and remain constant - normal naming conventions apply.

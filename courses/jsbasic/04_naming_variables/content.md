# Variable naming

The following is always true about variable names in JavaScript:

- The name may contain only letters, digits, dollar signs `$`, and underscores `_`.
- The first character must not be a digit.
- Names are case sensitive (`x` and `X` are different variables).
- Reserved words (JavaScript keywords like `this` or `class`) cannot be used as names.

It's recommended to stick to the following conventions:

- **camelCase**: When the name contains multiple words, camelCase is commonly used. That is: words go one after another, each following word starts with a capital letter: `myVeryLongName`.
- **libraries**: The names `$` and `_` are usually reserved for specific values: the *jquery* and *lodash* libraries.
- **underscored**: Names starting with `_` indicate non-public parts of an API.
- **Latin**: Non-latin letters are allowed, but not recommended (like `имя`).
- **ALL_CAPS** All-capital names for constants whose value is defined before runtime.
- **readable** Use human-readable names, and stay away from abbreviations. It may take longer to type, but this is easily offset by easier reading and debugging.
- **meaningful**: Name the variables so that they convey the meaning of the data: descriptive yet concise. It's commmon to spend some time coming up with good meaningful names. They should help others understand what's inside.
- **no recycling**: It's never a good idea to re-use a variable you declared earlier in a different context.
- **agreement**: When working in a team or contributing to an existing code base, stick to the naming conventions.

```js
// Valid
let userName;
let test2;

// Valid, but not recommended for "normal" use
let `_myVariable`;
let `我`;
let `MixEdcaSE`;
let `$`;
let `a`;

// Invalid
let 1a; // Cannot start with number
let let; // Reserved keyword
let class; // Reserved keyword
```
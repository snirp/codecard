As your program grows in complexity, the need arises to describe what happens and why. For this Javascript - like almost any other programming language - has *comments* which can be placed anywhere inside the script. They don’t affect the execution, because the engine simply ignores them.

# Inline comments
Inline comments start with two forward slash characters `//`. The rest of the line is regarded as a comment. They may occupy a full line of its own or follow a statement. The double slash usually followed by a single space. While not necessary, it makes for more readable code.

```js
// This comment occupies a full line
alert('Hello world');

alert('Hello world'); // This comment follows the statement
```

# Block comments
Block comments start with a forward slash and an asterisk `/*` and end with an asterisk and a forward slash `*/`. They may follow or precede a statement, but by convention the block comments are restricted to their own lines.

```js
 /* An example with two messages.
This is a block comment.
*/

alert('Hello world'); /* This is uncommon 
...
and this is frowned upon */ alert('Hello world');
```

# Commenting out
We noted that the engine ignores the content of comments, so if we put code inside `/*` ... `*/` it won’t execute. We can put that to good use to temporarily disable a section of code:

```js
 /* Commenting out the code
alert('Hello');
*/
alert('Hello world');
```

This is mainly used while developing a script and not so much in production code.

Most editors have a hotkey to comment out code. Select a piece of code and press `Ctrl` + `/` (inline comment) or `Ctrl` + `Shift` + `/` (block comment). Mac uses `Cmd` instead of `Ctrl`.


# No nested block comments
There is no support for `/*` ... `*/` inside another `/*` ... `*/`. Such code will die with an error:

```js
// DO NOT DO THIS:

/*
  /* nested comment ?!? */
*/
alert('Hello world');
```

# How to use comments
Comments increase the overall code footprint, but that’s usually not a problem at all. There are many tools which minify the code before publishing to the production server to save bandwidth. Amonst other things, they remove comments, so those do not appear in the working scripts. If comments do remain in production code, the engine will ignore them.

Comments are supposed to help programmers, whether it is the original programmer or someone else using or collaborating on the project. This means the comments must be maintained just like the code. A comment that contradicts the code is worse than no comment at all.

When you're just starting out, you may write lots of comments to help you understand what you're doing. But as you gain more experience, you should be looking to use comments to explain the *why* behind the code as opposed to the *what* or *how*. Unless the code is particularly tricky, looking at the code can generally tell what the code is doing or how it is doing it.

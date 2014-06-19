ToggleQuotes is a [Sublime Text][sublime] plugin which lets you easily toggle quote marks in your code.

## Installation ##

### With Package Control ###

If you have the [Package Control][package_control] package installed, you can install ToggleQuotes from inside Sublime Text itself. Open the Command Palette and select "Package Control: Install Package", then search for ToggleQuotes and you're done!

### Without Package Control ###

Go to your Sublime Text 2 Packages directory and clone the repository using the command below:

    git clone https://github.com/spadgos/sublime-ToggleQuotes.git ToggleQuotes

Don't forget to keep updating it, though!

## Example ##

Make one or more selections of strings including their quotes and then press the opposite quote mark. That is, if you have `"test"` press `'`, if you have `'test'`, press `"`.

```javascript
// With this selected:
"test"
// Press: '
// Result is:
'test'
```

Internal quotes are escaped, and already-escaped quotes are unescaped for you:

```javascript
// With this selected:
"hello 'world'"
// Press: '
// Result is:
'hello \'world\''

// With this selected:
'hello \'world\''
// Press: "
// Result is:
"hello 'world'"
```

If you have multiple selections which have different quote marks, you can toggle them all by pressing `Ctrl+'`

You can also toggle the quote marks of a string by simply putting your cursor inside the string and pressing `Ctrl+'`. The selection will expand to the entire string automatically.

## Version History ##

- **1.1.0** *January 15, 2012*
  - Added `Ctrl+'` hotkey to expand to selection inside of strings.
- **1.0.0** *November 8, 2011*
  - First release

[sublime]: http://www.sublimetext.com/
[package_control]: http://wbond.net/sublime_packages/package_control

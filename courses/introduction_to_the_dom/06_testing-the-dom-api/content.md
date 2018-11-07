This document provides samples for every interface that you can use in your own web development. In some cases, the samples are complete HTML pages, with the DOM access in a `<script>` element, the interface (e.g, buttons) necessary to fire up the script in a form, and the HTML elements upon which the DOM operates listed as well. When this is the case, you can cut and paste the example into a new HTML document, save it, and run the example from the browser.

There are some cases, however, when the examples are more concise. To run examples that only demonstrate the basic relationship of the interface to the HTML elements, you may want to set up a test page in which interfaces can be easily accessed from scripts. The following very simple web page provides a `<script>` element in the header in which you can place functions that test the interface, a few HTML elements with attributes that you can retrieve, set, or otherwise manipulate, and the web user interface necessary to call those functions from the browser.

You can use this test page or create a similar one to test the DOM interfaces you are interested in and see how they work on the browser platform. You can update the contents of the `test()` function as needed, create more buttons, or add elements as necessary.

```html
<html>
  <head>
    <title>DOM Tests</title>
    <script type="application/javascript">
    function setBodyAttr(attr, value){
      if (document.body) eval('document.body.'+attr+'="'+value+'"');
      else notSupported();
    }
    </script>
  </head> 
  <body>
    <div style="margin: .5in; height: 400;"> 
      <p><b><tt>text</tt></b></p> 
      <form> 
        <select onChange="setBodyAttr('text',
        this.options[this.selectedIndex].value);"> 
          <option value="black">black 
          <option value="darkblue">darkblue 
        </select>
        <p><b><tt>bgColor</tt></b></p>
        <select onChange="setBodyAttr('bgColor',
        this.options[this.selectedIndex].value);"> 
          <option value="white">white 
          <option value="lightgrey">gray
        </select>
        <p><b><tt>link</tt></b></p> 
        <select onChange="setBodyAttr('link',
        this.options[this.selectedIndex].value);">
          <option value="blue">blue
          <option value="green">green
        </select>  <small>
        <a href="http://some.website.tld/page.html" id="sample">
        (sample link)</a></small><br>
      </form>
      <form>
        <input type="button" value="version" onclick="ver()" />
      </form>
    </div>
  </body>
</html>
```

To test a lot of interfaces in a single page-for example, a "suite" of properties that affect the colors of a web page-you can create a similar test page with a whole console of buttons, textfields, and other HTML elements. The following screenshot gives you some idea of how interfaces can be grouped together for testing.

In this example, the drop-down menus dynamically update such DOM-accessible aspects of the web page as its background color (bgColor), the color of the hyperlinks (aLink), and color of the text (text). However, you design your test pages, testing the interfaces as you read about them is an important part of learning how to use the DOM effectively.
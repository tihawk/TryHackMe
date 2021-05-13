# TryHackMe walkthrough

## How websites work

> _tihawk | May 13, 2021_

----------------------------------------

### TASK 1. How websites work

<p>By the end of this room, you'll know how websites are created and will be introduced to some basic security issues.</p><p>When you visit a website your browser (<i>like Safari or Google Chrome</i>) makes a request to a web server asking for information about the page you're visiting and will respond with data that your browser uses to show you the page; a<span style="font-size:1rem"> web server is just a dedicated computer somewhere else in the world that handles your requests.</span></p><p><span style="font-size:1rem"><br /></span><span style="font-size:1rem"> </span><img src="https://assets.tryhackme.com/additional/how-websites-work/client%20server.png" style="font-size:1rem;width:100%;max-width:786px" /></p><p><span style="font-size:1rem">There are two major components that make up a website:</span></p><ol><li><span style="font-size:1rem">Front End (Client-Side) - the way your browser renders a website.</span></li><li><span style="font-size:1rem">Back End (Server-Side) - a server that processes your request and returns a response.</span></li></ol><p>There are many other processes involved in your browser making a request to a web server, but for now you just need to understand that you make a request to a server and it responds with data your browser uses to render information to you.<br /></p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>What term describes the way your browser renders a website?   </p>

```
Front end
```

----------------------------------------

### TASK 2. HTML

<p>Websites are primarily created using: </p><ul><li>HTML, to build websites and define their structure</li><li>CSS, to make websites look pretty by adding styling options</li><li>JavaScript, implement complex features on pages using interactivity</li></ul><p><b>H</b>yper<b>T</b>ext <b>M</b>arkup <b>L</b>anguage (HTML) is the language websites are written in. Elements (also known as tags) are the building blocks of HTML pages and tells the browser how to display content. The code snippet below shows a simple HTML document, the structure of which is the same for every website:</p><p><img src="https://assets.tryhackme.com/additional/how-websites-work/example_html.png" style="width:325px" class="note-float-right" /></p><p>The HTML structure (as shown in the screenshot) has the following components:</p><ul><li><span style="font-family:Ubuntu">The </span><code class="language-html">&lt;!DOCTYPE html&gt;</code><span style="font-family:Ubuntu"> defines that the page is a HTML5 document. This helps with standardisation across different browsers and tells the browser to use HTML5 to interpret the page.</span></li><li><span style="font-family:Ubuntu">The </span><code class="language-html">&lt;html&gt;</code><span style="font-family:Ubuntu"> element is the root element of the HTML page - all other elements come after this element.</span></li><li><span style="font-family:Ubuntu">The </span><code class="language-html">&lt;head&gt;</code><span style="font-family:Ubuntu"> element contains information about the page (such as the page title)</span></li><li><span style="font-family:Ubuntu">The </span><code class="language-html">&lt;body&gt;</code><span style="font-family:Ubuntu"> element defines the HTML document's body, only content inside of the body is shown in the browser.</span></li><li><span style="font-family:Ubuntu">The </span><code class="language-html">&lt;h1&gt;</code><span style="font-family:Ubuntu"> element defines a large heading</span></li><li><span style="font-family:Ubuntu">The </span><code class="language-html">&lt;p&gt;</code><span style="font-family:Ubuntu"> element defines a paragraph</span></li><li style="box-sizing:inherit"><span style="color:rgb(33, 37, 41);font-family:Ubuntu, monospace;font-size:1rem">There are many other elements (tags) used for different purposes. For example, there are tags for: buttons (<code class="language-html">&lt;button&gt;</code>), images (<code class="language-html">&lt;img&gt;</code>), lists, and much more. </span><br /></li></ul><p>Tags can contain attributes such as the class attribute which can be used to style an element (e.g. make the tag a different color) <code class="language-html">&lt;p class="bold-text"&gt;</code>, or the <i>src </i>attribute which is used on images to specify the location of an image: <code class="language-html">&lt;img src="img/cat.jpg"&gt;.</code><span style="font-size:1rem">An element can have multiple attributes each with its own unique purpose e.g. &lt;p attribute1="value1" attribute2="value2"&gt;</span></p><p>Elements can also have an id attribute (<code class="language-html">&lt;p id="example"&gt;</code>), which is unique to the element. Unlike the class attribute where multiple elements can use the same class, an element must have different id's to uniquely identify them. Element id's are used for styling and to identify it by JavaScript.</p><p><span style="font-size:1rem">You can view the HTML of any website by right clicking, and selecting "View Page Source" (Chrome) / "Show Page Source" (Safari).</span><br /></p><ul>
</ul>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. <p>Let's play with some HTML! On the right-hand side, you should see a box that renders HTML - If you enter some HTML into the box, and click the green "Render HTML Code" b<span style="font-size:1rem">utton</span><span style="font-size:1rem"> it will render your HTML on the page; you should see an image of some cats.</span></p>

```
OK
```

2. <p>One of the images on the cat website is broken - fix it and the image will reveal the hidden text answer!</p>

```
HTMLHERO
```

3. <p>Add a dog image to the page by adding another img tag (&lt;img&gt;) on line 11. The dog image location is img/dog-1.png</p>

```
DOGHTML
```

----------------------------------------

### TASK 3. JavaScript

<p>JavaScript (JS) is one of the most popular coding languages in the world and allows pages to become interactive. HTML is used to create the website structure and content, while JavaScript is used to control the functionality of webpages - without JavaScript a page would not have interactive elements, and would always be static. JS can dynamically update the page in real-time, giving functionality to change the style of a button when a particular event on the page occurs (such as when a user clicks a button), or to display moving animations.</p><p><span style="font-size:1rem">JavaScript is added within the page source code and can be either loaded within <code class="language-html">&lt;script&gt;</code> tags or can be included remotely with the src attribute: </span><code class="language-javascript">&lt;script src="/location/of/javascript_file.js"&gt;&lt;/script&gt;</code></p><p>The following JavaScript code finds a HTML element on the page with the id of "demo" and changes the element's contents to "Hack the Planet" : <code class="language-javascript">document.getElementById("demo").innerHTML = "Hack the Planet";</code></p><p>HTML elements can also have events, such as "onclick" or "onhover" that execute JavaScript when the event occurs. The following code changes the text of the element with the demo ID to Button Clicked: <code class="language-html">&lt;button onclick='document.getElementById("demo").innerHTML = "Button Clicked";'&gt;Click Me!&lt;/button&gt;</code> - onclick events can also be defined inside the JavaScript script tags, and not on elements directly. </p>


----------------------------------------

### QUESTIONS:

----------------------------------------

1. Click the "View Site" button on this task. On the right-hand side, add JavaScript that changes the demo element's content to "Hack the Planet"

```
JSISFUN
```

2. <p>Add the button HTML from this task that changes the element's text to "Button Clicked" on the editor on the right, update the code by clicking the "Render HTML+JS Code" button and then click the button.</p>

```
OK
```

----------------------------------------

### TASK 4. Sensitive Data Exposure

<p>Sensitive Data Exposure is when a website doesn't properly protect (or remove) sensitive clear-text information to the end-user; usually found in the frontend source code of sites.</p><p>We now know that websites are built using many HTML elements (tags), all of which we can see by simply "viewing the page source", a website developer may have forgotten to remove login credentials, hidden links to private parts of the website or other sensitive data shown in HTML or JavaScript.</p><p><img src="https://assets.tryhackme.com/additional/how-websites-work/html_source.png" style="width:504.928px;height:209.75px;float:right" class="note-float-right" />Sensitive information can be potentially leveraged to further an attacker's access within different parts of a web application. For example, there could be HTML comments with temporary login credentials, and if you viewed the page's source code and found this, you could use these credentials to login elsewhere on the application (or worse, used to access other backend components of the site).</p><p></p><p>Whenever you're assessing a web application for security issues, one of the first things you should do is review the page source code to see if you can find any exposed login credentials or hidden links.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. View the website on this task. What is the password hidden in the source code?

```
testpasswd
```

----------------------------------------

### TASK 5. HTML Injection

<p>HTML Injection is a vulnerability that occurs when unfiltered user input is displayed on the page. <span style="font-size:1rem">If a website fails to sanitize user input (filter any "malicious" text that a user inputs into a website), and that input is used on the page, an attacker can inject HTML code into a vulnerable website.</span></p><p>Input sanitization is very important in keeping a website secure, as information a user inputs into a website is often used in other frontend and backend functionality - a vulnerability you'll explore in another lab is database injection, where you can manipulate a database lookup query to login as another user by controlling the input that's directly used in the query - but for now, let's focus on HTML injection (which is client-side).</p><p>When a user has control of how their input is displayed, they can submit HTML (or JavaScript) code and the browser will use it on the page, allowing the user to control the page's appearance and functionality.</p><p><img src="https://assets.tryhackme.com/additional/how-websites-work/html_injection.png" style="width:100%" /></p><p>The image above shows how a form outputs text to the page. Whatever the user inputs into the "What's your name" field is passed to a JavaScript function and output to the page, which means if the user adds their own HTML or JavaScript in the field it's used in the sayHi function and is added to the page - this means you can add your own HTML (such as a &lt;h1&gt; tag) and it will output your input as pure HTML.</p><p>The general rule is never to trust user input - to prevent malicious input the website developer should sanitize everything the user enters before using it in the JavaScript function; in this case, the developer could remove any HTML tags.</p>

----------------------------------------

### QUESTIONS:

----------------------------------------

1. View the website on this task and inject HTML so that a malicious link to http://hacker.com is shown.

```
HTML_INJ3CTI0N
```


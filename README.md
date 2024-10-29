
<h1>WIKI</h1>
Project 1 for CS50’s Web Programming with Python and JavaScript.
<h2>Overview</h2>
A Wikipedia-like online encyclopedia.
<h2>Specification</h2>
The project completes the following requirements:
<ul>
  <li><strong>Entry Page: </strong>Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.<ul><li>The view should get the content of the encyclopedia entry by calling the appropriate util function.</li><li>If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.</li><li>If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.</li></ul></li>
     <li><strong>Index Page: </strong>
     Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.</li>
     <li><strong>Search: </strong>
     Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.<ul><li>If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.</li><li>If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.</li><li>Clicking on any of the entry names on the search results page should take the user to that entry’s page.</li></ul></li>
     <li><strong>New Page: </strong>
     Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
     <ul>
       <li>Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.</li>
       <li>Users should be able to click a button to save their new page.</li>
       <li>When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.</li>
       <li>Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.</li>
     </ul>
     </li>
  <li><strong>Edit Page: </strong>
     On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.<ul><li>The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).</li><li>The user should be able to click a button to save the changes made to the entry.</li><li>Once the entry is saved, the user should be redirected back to that entry’s page.</li></ul></li>
   <li><strong>Random Page: </strong>
    Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.</li>
  <li><strong>Markdown to HTML Conversion: </strong>
     On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via pip3 install markdown2.</li>
</ul>
<h2>Setup</h2>
To set up this project on your computer:

<ol>
  <li>Download this project:<br><code>git clone https://github.com/TahaFayyaz1/WIKI.git </code></li>
  <li>Install all necessary dependencies <br><code>pip install -r requirements.txt</code></li>
  <li>Make migrations <br><code>python manage.py makemigrations wiki</code></li>
  <li>Migrate <br><code>python manage.py migrate</code></li>
</ol>

<h2>Preview</h2>
A demonstration of my project's functionality has be recorded and uploaded on Youtube:
<a href="https://youtu.be/m4dIwKHnAz0">Project Demonstration</a>

# wiki
This is a Wiki encyclopedia project where users can create new pages with new information on the Wiki, edit a page and search for others.

# Installation 

To use this project first you need python and django

To install django
```bash
pip3 install Django
```

To run the project
```bash
python3 manage.py runserver
```

It also needs a package to convert Markdown to HTML

```bash
pip3 install markdown2
```
# Demo
Here it is a simple usage example on YouTube: [Demo](https://youtu.be/hpMAJKV1eAM)



## Entry Page
Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, will render a page that displays the contents of that encyclopedia entry.
* If an entry is requested that does not exist, the user will be presented with an error page indicating that their requested page was not found.
* If the entry does exist, the user will be presented with the page displaying the content of the entry.
## Index Page
User can click on any entry name and be taken directly to that entry page.

## Search
User can type a query into the search box in the sidebar to search for an encyclopedia entry.
* If the query matches an encyclopedia entry's name, the user will be redirected to that entry’s page.
    * If the query does not match the name of an encyclopedia entry, the user will be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.
    * Clicking on any of the entry names on the search results page will take the user to that entry’s page.

## New Page
Clicking “Create New Page” in the sidebar will take the user to a page where they can create a new encyclopedia entry with a title for the page and a textarea that must be writen in ```Markdown content```.
* After saving the page, if an encyclopedia entry with the provided title already exists, the user will see an error message.
* Otherwise, the encyclopedia entry will be saved to disk, and the user will be taken to the new entry’s page.
  
## Edit Page
On each entry page, the user will be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
    * The textarea is pre-populated with the existing Markdown content of the page.
    * Once the entry is saved, the user will be redirected back to that entry’s page.
## Random Page
Clicking “Random Page” in the sidebar will take user to a random encyclopedia entry.

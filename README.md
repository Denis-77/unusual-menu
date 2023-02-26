Django-app, which allows you to add menus (one or more) to the database through the admin panel, and draw menus by name on any desired page.
- Menu implemented using template tag
- Everything above the selected item is expanded. The first level of nesting under the selected item is also expanded.
- Stored in the database.
- Editable in standard Django-Admin
- The active menu item is determined from the URL of the current page
- There can be several menus on one page. They are identified by name.
- When you click on the menu, you go to the URL specified in it.
- Exactly 1 query to the database is required to render each menu
Only Django and the Python standard library were used.

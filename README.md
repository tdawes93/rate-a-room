Future things to add/change

JS script could be condensed. Need to figure out way to not repeat code for each set of star ratings


Test Problems
changed assertTrue test to assertLessEquals

Needed to create user and property instances to get review unittests to work 

Repetative code for displaying star ratings on property.html, solution was to use Django's built in {% include '.html' %} tags. Similar to extend, allowed variables to be used across the two templates.

Carousel on index.html was pulling all property data entries and laying them ontop of one another. Fix was made using an if loop to ensure the only first property of the for loop was displayed until the carousel nav buttons were used 

migration bug:
removed and uninstalled django-address, this messed up this dependancies in the migrations, attempted to fix by removing migrations. Easiest solution in the end was to duplicate the properties app, delete the old one, delete all migrations and migrate again. 

superuser password:
tdawes93
Casa2793

References:
Carousel code https://getbootstrap.com/docs/5.2/components/carousel/
Teaser code https://github.com/rmosolgo/bootstrap-teaser
Star code https://www.youtube.com/watch?v=AXwuF1C-Bso&ab_channel=Pyplane
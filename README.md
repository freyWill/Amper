# What is it all about
Amper is a lightweight e-commerce tech website written in Python Django

# Features

- View products
- Featured products
- Categories
- Rating
- Add to cart
- Checkout
- Product page
- ** Responsive, responsive, responsive **

# Setup:

Required:
* Python installed
* [Pip](https://pip.pypa.io/en/latest/) installed
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) installed
* Most of the commands are run in terminal/cmd

### Quick man's guide
**Windows**: `virtualenv env && env\Scripts\activate && pip install django==1.7.1 django-autofixture pillow django-cart django-ratings django-mptt && python manage.py migrate && python manage.py shell < generate_content.py && python manage.py runserver`
**Linux:** `virtualenv env && source env/Scripts/activate && pip install django==1.7.1 django-autofixture pillow django-cart django-ratings django-mptt && python manage.py migrate && python manage.py shell < generate_content.py && python manage.py runserver`
Now open http://localhost:8000 and enjoy
### Step by step
1. Clone the directory and open a cmd on windows or terminal on linux, then change directory (cd) to the root of the project.  
Root of the project will be `something/something/Amper`
2. Create the virtualenv: `virtualenv env`.
3. Activate virtualenv:  
**On windows:** `env/Scripts/activate`  
**On linux:** `source env/bin/activate`
4. Install requirements:  
` pip install django==1.7.1 django-autofixture django-ratings pillow django-cart django-mptt`
5. Create the database and generate dummy data:  
`python manage.py migrate && python manage.py shell < generate_content.py`
6. Run server:  
`python manage.py runserver`
7. Open a browser, visit http://localhost:8000 and enjoy :) !

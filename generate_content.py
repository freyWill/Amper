from product.models import Category, Product
from controller.models import Slide
from autofixture import AutoFixture
from django.contrib.auth.models import User

print "Creating categories"
entertainment = Category(title="Entertainment")
entertainment.save()

xbox = Category(title="Xbox", parent=entertainment)
xbox.save()

games = Category(title="Games", parent=xbox)
games.save()

joysticks = Category(title="Joysticks", parent=games)
joysticks.save()

tv = Category(title="TV", parent=entertainment)
tv.save()

mobile = Category(title="Mobile")
mobile.save()

smartphones = Category(title="Smartphones", parent=mobile)
smartphones.save()

tablets = Category(title="Tablets", parent=mobile)
tablets.save()

laptops = Category(title="Laptops")
tablets.save()

notebooks = Category(title="Notebooks", parent=laptops)
notebooks.save()

macbooks = Category(title="Macbooks", parent=laptops)
macbooks.save()

print "Creating superuser"
user = User.objects.create_user('root', 'll@gmail.com', 'toor')
user.is_superuser = True
user.is_staff = True
user.save()

print "Generating dummy slides"
fixture = AutoFixture(Slide)
entries = fixture.create(3)
print "Generating dummy products"
fixture = AutoFixture(Product)
entries = fixture.create(50)
print "done :) !"

from product.models import Category, Product, ExtraImage
from controller.models import Slide
from autofixture import AutoFixture
from django.contrib.auth.models import User

print "Creating categories"

entertainment = Category(title="Entertainment", slug="entertainment")
entertainment.save()

xbox = Category(title="Xbox", parent=entertainment, slug='xbox')
xbox.save()

games = Category(title="Games", parent=xbox, slug='games')
games.save()

joysticks = Category(title="Joysticks", parent=games, slug='joysticks')
joysticks.save()

tv = Category(title="TV", parent=entertainment, slug='tv')
tv.save()

mobile = Category(title="Mobile", slug='mobile')
mobile.save()

smartphones = Category(title="Smartphones", parent=mobile, slug='smartphones')
smartphones.save()

tablets = Category(title="Tablets", parent=mobile, slug='tablets')
tablets.save()

laptops = Category(title="Laptops", slug='laptops')
laptops.save()

notebooks = Category(title="Notebooks", parent=laptops, slug='notebooks')
notebooks.save()

macbooks = Category(title="Macbooks", parent=laptops, slug='macbooks')
macbooks.save()



print "Creating superuser"
user = User.objects.create_user('root', 'll@gmail.com', 'toor')
user.is_superuser = True
user.is_staff = True
user.save()

for i in range(0,10):
	user = User.objects.create_user("user"+str(i), 'user'+str(i)+"@gmail.com", 'toor')
	user.save()

print "Generating dummy slides"
fixture = AutoFixture(Slide)
entries = fixture.create(3)
print "Generating dummy products"
fixture = AutoFixture(Product)
entries = fixture.create(15)

print "Generating dummy additional images"
fixture = AutoFixture(ExtraImage)
entries = fixture.create(50)

print "done :) !"

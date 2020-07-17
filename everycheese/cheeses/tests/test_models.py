import pytest

pytestmark = pytest.mark.django_db

from ..models import Cheese
from .factories import CheeseFactory

def test___str__():
# 	cheese = Cheese.objects.create(
# 		name="Stracchino",
# 		description="semi-sweet cheese that goes well with starches",
# 		firmness=Cheese.Firmness.SOFT,
# 	)
	cheese = CheeseFactory()
	assert cheese.__str__() == cheese.name
	assert str(cheese) == cheese.name
from faker import Faker
from faker.providers import internet

fake = Faker('en_US')
# internet = Faker()
fake.add_provider(internet)
# print(fake.ipv4())

# for _ in range(1):
#   print(fake.name())
# print(fake.email())
# print(fake.text())
# print("\n")
# print(fake.random.setstate())

for i in range(3):
    # Raises a UniquenessException
    fake.unique.boolean()

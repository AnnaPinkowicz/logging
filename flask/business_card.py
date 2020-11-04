from faker import Faker
from faker.providers.phone_number.en_US import Provider

faker = Faker()


class BaseContact:
    def __init__(self, firstname, lastname, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f'firstname={self.firstname} lastname={self.lastname} ' \
               f'company={self.company} post={self.post} email={self.email}'

    def contact(self):
        return 'Contacted:{} {} \ntelephone:{} \nemail:{}'.format(
            self.firstname, self.lastname, self.contact_phone, self.email
        )

    @property
    def contact_phone(self):
        return self.phone

    @property
    def label_length(self):
        return len(self.firstname + ' ' + self.lastname)


class BusinessContact(BaseContact):
    def __init__(self, firstname, lastname, post, email, company, phone, business_phone):
        super().__init__(firstname, lastname, email, phone)
        self.business_phone = business_phone
        self.company = company
        self.post = post

    @property
    def contact_phone(self):
        return self.business_phone


def create_contacts(amount, kind):
    lits_of_contacts = []

    fake = Faker()
    if kind == BaseContact:
        for i in range(amount):
            lits_of_contacts.append(
                BaseContact(
                    firstname=fake.first_name(),
                    lastname=fake.last_name(),
                    email=fake.email(),
                    phone=fake.phone_number()
                )
            )

    elif kind == BusinessContact:
        for i in range(amount):
            lits_of_contacts.append(
                BusinessContact(
                    firstname=fake.first_name(),
                    lastname=fake.last_name(),
                    company= fake.company(),
                    post=fake.job(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    business_phone=fake.phone_number()

                )
            )

    return lits_of_contacts


for card in create_contacts(5, BaseContact):
    print(card.contact())
    print(card.label_length)
    print("------------------------")

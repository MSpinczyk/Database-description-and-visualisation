# Database name: Project1
## Schemas
1. public
2. schema2

## Tables
[1. actor<br>](#actor)
[2. store<br>](#store)
[3. address<br>](#address)
[4. category<br>](#category)
[5. city<br>](#city)
[6. country<br>](#country)
[7. customer<br>](#customer)
[8. film_actor<br>](#film_actor)
[9. film_category<br>](#film_category)
[10. inventory<br>](#inventory)
[11. language<br>](#language)
[12. rental<br>](#rental)
[13. staff<br>](#staff)
[14. payment<br>](#payment)
[15. film<br>](#film)
### actor
```
class Actor(Base):
    __tablename__ = 'actor'

    actor_id = Column(Integer, primary_key=True, server_default=text("nextval('actor_actor_id_seq'::regclass)"))
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))


```
### store
```
class Store(Base):
    __tablename__ = 'store'

    store_id = Column(Integer, primary_key=True, server_default=text("nextval('store_store_id_seq'::regclass)"))
    manager_staff_id = Column(ForeignKey('staff.staff_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, unique=True)
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    address = relationship('Addres')
    manager_staff = relationship('Staff')


```
### address
```
class Addres(Base):
    __tablename__ = 'address'

    address_id = Column(Integer, primary_key=True, server_default=text("nextval('address_address_id_seq'::regclass)"))
    address = Column(String(50), nullable=False)
    address2 = Column(String(50))
    district = Column(String(20), nullable=False)
    city_id = Column(ForeignKey('city.city_id'), nullable=False, index=True)
    postal_code = Column(String(10))
    phone = Column(String(20), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    city = relationship('City')


```
### category
```
class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True, server_default=text("nextval('category_category_id_seq'::regclass)"))
    name = Column(String(25), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))


```
### city
```
class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, server_default=text("nextval('city_city_id_seq'::regclass)"))
    city = Column(String(50), nullable=False)
    country_id = Column(ForeignKey('country.country_id'), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    country = relationship('Country')


```
### country
```
class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, server_default=text("nextval('country_country_id_seq'::regclass)"))
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))


```
### customer
```
class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, server_default=text("nextval('customer_customer_id_seq'::regclass)"))
    store_id = Column(SmallInteger, nullable=False, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    email = Column(String(50))
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    activebool = Column(Boolean, nullable=False, server_default=text("true"))
    create_date = Column(Date, nullable=False, server_default=text("('now'::text)::date"))
    last_update = Column(DateTime, server_default=text("now()"))
    active = Column(Integer)

    address = relationship('Addres')


```
### film_actor
```
class FilmActor(Base):
    __tablename__ = 'film_actor'

    actor_id = Column(ForeignKey('actor.actor_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    film_id = Column(ForeignKey('film.film_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    actor = relationship('Actor')
    film = relationship('Film')


```
### film_category
```
class FilmCategory(Base):
    __tablename__ = 'film_category'

    film_id = Column(ForeignKey('film.film_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    category_id = Column(ForeignKey('category.category_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    category = relationship('Category')
    film = relationship('Film')


```
### inventory
```
class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        Index('idx_store_id_film_id', 'store_id', 'film_id'),
    )

    inventory_id = Column(Integer, primary_key=True, server_default=text("nextval('inventory_inventory_id_seq'::regclass)"))
    film_id = Column(ForeignKey('film.film_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    store_id = Column(SmallInteger, nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    film = relationship('Film')


```
### language
```
class Language(Base):
    __tablename__ = 'language'

    language_id = Column(Integer, primary_key=True, server_default=text("nextval('language_language_id_seq'::regclass)"))
    name = Column(CHAR(20), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))


```
### rental
```
class Rental(Base):
    __tablename__ = 'rental'
    __table_args__ = (
        Index('idx_unq_rental_rental_date_inventory_id_customer_id', 'rental_date', 'inventory_id', 'customer_id', unique=True),
    )

    rental_id = Column(Integer, primary_key=True, server_default=text("nextval('rental_rental_id_seq'::regclass)"))
    rental_date = Column(DateTime, nullable=False)
    inventory_id = Column(ForeignKey('inventory.inventory_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    customer_id = Column(ForeignKey('customer.customer_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    return_date = Column(DateTime)
    staff_id = Column(ForeignKey('staff.staff_id'), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    customer = relationship('Customer')
    inventory = relationship('Inventory')
    staff = relationship('Staff')


```
### staff
```
class Staff(Base):
    __tablename__ = 'staff'

    staff_id = Column(Integer, primary_key=True, server_default=text("nextval('staff_staff_id_seq'::regclass)"))
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    email = Column(String(50))
    store_id = Column(SmallInteger, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    username = Column(String(16), nullable=False)
    password = Column(String(40))
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))
    picture = Column(LargeBinary)

    address = relationship('Addres')


```
### payment
```
class Staff(Base):
    __tablename__ = 'staff'

    staff_id = Column(Integer, primary_key=True, server_default=text("nextval('staff_staff_id_seq'::regclass)"))
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    email = Column(String(50))
    store_id = Column(SmallInteger, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    username = Column(String(16), nullable=False)
    password = Column(String(40))
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))
    picture = Column(LargeBinary)

    address = relationship('Addres')


```
### film
```
class Film(Base):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True, server_default=text("nextval('film_film_id_seq'::regclass)"))
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(ForeignKey('language.language_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    rental_duration = Column(SmallInteger, nullable=False, server_default=text("3"))
    rental_rate = Column(Numeric(4, 2), nullable=False, server_default=text("4.99"))
    length = Column(SmallInteger)
    replacement_cost = Column(Numeric(5, 2), nullable=False, server_default=text("19.99"))
    rating = Column(Enum('G', 'PG', 'PG-13', 'R', 'NC-17', name='mpaa_rating'), server_default=text("'G'::mpaa_rating"))
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))
    special_features = Column(ARRAY(Text()))
    fulltext = Column(TSVECTOR, nullable=False, index=True)

    language = relationship('Language')


```

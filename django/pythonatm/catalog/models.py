import datetime
from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #, AbstractUser
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save

id_list = []

def get_random_id(length, char_set, type):
    id = get_random_string(length, char_set)
    unique = False
    while not unique:
        id_with_type = id + type
        if id_with_type not in id_list:
            unique = True
        else:
            id = get_random_string(length, char_set)

    id_list.append(id + type)
    file = open("id.txt", "a")
    file.write(id + type + "\n")
    file.close()
    return id

# Create your models here.
""" Account """
class Account(models.Model):

    """ Primary Key for Account model """
    account_number = models.CharField(
        #verbose_name='Account',
        primary_key=True,
        validators=[MinLengthValidator(12)],
        max_length=12,
        default=0,
        help_text='Enter Account Number')

    # First and Second Name for Account
    first_name = models.CharField(
        #verbose_name='First',
        validators=[MinLengthValidator(1)],
        max_length=30,
        help_text='Enter first name of account holder')

    last_name = models.CharField(
        #verbose_name='Last',
        validators=[MinLengthValidator(1)],
        max_length=30,
        help_text='Enter last name of account holder')

    address = models.CharField(
        validators=[MinLengthValidator(1)],
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter address of account holder')


    # Phone Number for Account
    phone_number = models.CharField(
        #verbose_name='Phone',
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Enter phone number of account holder')

    # Balance for Account
    balance = models.IntegerField(
        #verbose_name='Balance',,
        default=0,
        help_text='Initial balance for Account')

    """ Links account to a specific user """
    bank_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        """String for representing the Account object."""
        return f'Account #: {self.account_number} - {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.account_number = get_random_id(12, "0123456789", "ACC")
        super(Account, self).save(*args, **kwargs)
        #number.save()

    def update(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Account."""
        return reverse('account-detail', args=[str(self.account_number)])



""" Card """
class Card(models.Model):

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    card_number = models.CharField(
        #verbose_name='Card',
        primary_key=True,
        validators=[MinLengthValidator(16)],
        max_length=16,
        default=0,
        help_text='Card number')

    """ Links account to a specific user """
    bank_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        help_text='Account that this Card is linked to')

    pin = models.CharField(
        validators=[MinLengthValidator(4)],
        max_length=4,
        help_text='Enter PIN for Card')

    first_name = models.CharField(
        #verbose_name='First',
        max_length=30,
        help_text='Enter first name of card holder')

    last_name = models.CharField(
        #verbose_name='Last',
        max_length=30,
        help_text='Enter last name of card holder')

    address = models.CharField(
        validators=[MinLengthValidator(1)],
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter address of card holder')


    phone_number = models.CharField(
        #verbose_name='Phone',
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Enter phone number for card holder')

    issue_date = models.DateField(
        null=True,
        blank=True,
        default=timezone.now)

    expiration_date = models.DateField(
        null=True,
        blank=True,
        default=(datetime.date.today() + datetime.timedelta(days=730)))

    # CARD_STATUS = (
    #     ('A', 'Activated'),
    #     ('D', 'Deactivtaed')
    # )
    #
    # status = models.CharField(
    #     max_length=1,
    #     choices=CARD_STATUS,
    #     blank=True,
    #     default='A',
    #     help_text='Card Status'
    # )

    def __str__(self):
        """String for representing the Model object."""
        return f'Card #: {self.card_number} - {self.first_name} {self.last_name} - Account #: {self.account.account_number}'

    def save(self, *args, **kwargs):
        self.card_number=get_random_id(16, "0123456789", "C")
        super(Card, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(Card, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Account."""
        return reverse('card-detail', args=[str(self.card_number)])



""" AT Machine """
class ATMachine(models.Model):
    """ Primary Key """
    machine_id = models.CharField(
        primary_key=True,
        validators=[MinLengthValidator(8)],
        max_length=8,
        verbose_name='ATM',
        help_text="Identification Number for ATM")

    address = models.CharField(
        validators=[MinLengthValidator(1)],
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter address of ATM')


    current_balance = models.IntegerField(
        help_text='Current Balance of ATM')

    minimum_balance = models.IntegerField(
        help_text='Minimum Balance for ATM')

    last_refill = models.DateField(
        null=True,
        default=timezone.now,
        blank=True)

    next_maintenance = models.DateField(
        null=True,
        default=timezone.now,
        blank=True)

    def __str__(self):
        return f'ATM at {self.address}'

    # def save(self, *args, **kwargs):
    #     slug_save(self, 16, '0123456789')
    #     Super(SomeModelWithSlug, self).save(*args, **kwargs)



""" ATMachine Refill """
class ATMachineRefill(models.Model):

    """ Primary Key """
    refill_id = models.CharField(
        primary_key = True,
        validators=[MinLengthValidator(6)],
        max_length=6,
        help_text='Refill Identification Number for Transaction')

    atm_machine=models.ForeignKey(
        ATMachine,
        on_delete=models.SET_NULL,
        null=True,
        help_text='ATM refill was done on')

    refill_amount=models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text='Refill amount')

    refill_date=models.DateField(
        null=True,
        blank=True,
        default=timezone.now)

    def __str__(self):
        return f'Refill #: {self.refill_id} - ${self.refill_amount} - Location: {self.atm_machine.address}'

    def save(self, *args, **kwargs):
        #refill_id = get_random_id(16, "0123456789", "R")
        atm = self.atm_machine
        atm.last_refill = self.refill_date
        atm.current_balance += self.refill_amount
        atm.next_maintenance = datetime.date.today() + datetime.timedelta(days=7)
        atm.save()
        self.refill_id = get_random_id(6, "0123456789", "R")
        super(ATMachineRefill, self).save(*args, **kwargs)



""" Transaction """
class Transaction(models.Model):

    """ Primary Key """
    transaction_id = models.CharField(
        primary_key=True,
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Identification Number for Transaction')

    # TRANSACTION_STATUS = (
    #     ('P', 'Pending'),
    #     ('A', 'Approved')
    # )

    # status = models.CharField(
    #     max_length=1,
    #     choices=TRANSACTION_STATUS,
    #     blank=True,
    #     default='A',
    #     help_text='Transaction Status')

    TRANSACTION_TYPE = (
        ('W', 'Withdrawal'),
        ('D', 'Deposit'),
    )

    type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPE,
        blank=True,
        default='W',
        help_text='Tranaction Type')

    # card = models.ForeignKey(
    #     Card,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     help_text='Account used in transaction')

    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Account used in transaction')

    atm_machine = models.ForeignKey(
        ATMachine,
        on_delete=models.SET_NULL,
        null=True,
        help_text='ATM transaction was done on')

    transaction_date = models.DateField(
        default=timezone.now)

    # response_code = models.CharField(
    #     max_length=1,
    #     default='0',
    #     help_text='Response Code for Tranaction')

    """ Links account to a specific user """
    bank_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    description = models.CharField(
        max_length=300,
        default='Transaction')

    def __str__(self):
        return f'Transaction #: {self.transaction_id} - {self.description} - {self.date}'

    def save(self, *args, **kwargs):
        self.transaction_id = get_random_id(10, "0123456789", "T")
        super(Transaction, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        #self.transaction_id = get_random_id(10, "0123456789", "T")
        super(Transaction, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Account."""
        return reverse('card-detail', args=[str(self.card_number)])

# def slug_save(obj, length, char_set):
#     if not obj.slug:
#         obj.slug = get_random_string(length, char_set)
#         slug_is_worng = True
#         while slug_is_wrong:
#             slug_is_wrong = False
#             other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
#             if len(other_objs_with_slug) > 0:
#                 slug_is_wrong = True
#             if slug_is_wrong:
#                 obj.slug = get_random_string(length, char_set)

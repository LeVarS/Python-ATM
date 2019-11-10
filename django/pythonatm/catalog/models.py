import datetime
from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #, AbstractUser
from django.utils.crypto import get_random_string

id_list = []

def get_random_id(length, char_set):
    id = get_random_string(length, char_set)
    unique = False
    while not unique:
        if id not in id_list:
            unique = True
        else:
            id = get_random_string(length, char_set)

    id_list.append(id)
    file = open("id.txt", "a")
    file.write(id + "\n")
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
        help_text='Enter first name for Account')

    last_name = models.CharField(
        #verbose_name='Last',
        validators=[MinLengthValidator(1)],
        max_length=30,
        help_text='Enter last name for Account')

    # Phone Number for Account
    phone_number = models.CharField(
        #verbose_name='Phone',
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Enter phone number for Account')

    # Balance for Account
    balance = models.IntegerField(
        #verbose_name='Balance',
        help_text='Initial balance for Account')

    """ Links account to a specific user """
    bank_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        """String for representing the Account object."""
        return f'Account: {self.account_number}, {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        account_number=get_random_id(12, "0123456789")
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
        help_text='Enter first name for Card')

    last_name = models.CharField(
        #verbose_name='Last',
        max_length=30,
        help_text='Enter last name for Card')

    phone_number = models.CharField(
        #verbose_name='Phone',
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Enter phone number for Account')

    issue_date = models.DateField(
        null=True,
        blank=True,
        default=timezone.now)

    expiration_date = models.DateField(
        null=True,
        blank=True,
        default=(datetime.date.today() + datetime.timedelta(days=1460)))

    CARD_STATUS = (
        ('A', 'Activated'),
        ('D', 'Deactivtaed')
    )

    status = models.CharField(
        max_length=1,
        choices=CARD_STATUS,
        blank=True,
        default='A',
        help_text='Card Status'
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'Card: {self.card_number} ({self.account})'

    def save(self, *args, **kwargs):
        card_number=get_random_id(16, "0123456789")
        super(Card, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Account."""
        return reverse('card-detail', args=[str(self.card_number)])



""" AT Machine """
class ATMachine(models.Model):
    """ Primary Key """
    machine_id = models.CharField(
        primary_key=True,
        validators=[MinLengthValidator(16)],
        max_length=16,
        help_text="Identification Number for ATM")

    current_balance = models.IntegerField(
        help_text='Current Balance of ATM')

    minimum_balance = models.IntegerField(
        help_text='Minimum Balance for ATM')

    last_refill = models.DateField(
        null=True,
        blank=True)

    next_maintenance = models.DateField(
        null=True,
        blank=True)

    def __str__(self):
        return f'ATM: {self.machine_id}'

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
        blank=True)

    def __str__(self):
        return f'ATM Refill: {self.refill_id} ${self.refill_amount}'

    # def save(self, *args, **kwargs):
    #     slug_save(self, 6, '0123456789')
    #     Super(SomeModelWithSlug, self).save(*args, **kwargs)



""" Transaction """
class Transaction(models.Model):

    """ Primary Key """
    transaction_id = models.CharField(
        primary_key=True,
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Identification Number for Transaction')

    TRANSACTION_STATUS = (
        ('P', 'Pending'),
        ('A', 'Approved')
    )

    status = models.CharField(
        max_length=1,
        choices=TRANSACTION_STATUS,
        blank=True,
        default='A',
        help_text='Transaction Status')

    TRANSACTION_TYPE = (
        ('PHC', 'Phone Change'),
        ('PIC', 'PIN Change'),
        ('CHW', 'Cash Withdrawal'),
        ('CHT', 'Cash Transfer'),
        ('BLE', 'Balance Enquiry')
    )

    type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPE,
        blank=True,
        default='CHW',
        help_text='Tranaction Type')

    card = models.ForeignKey(
        Card,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Card used in transaction')

    atm_machine = models.ForeignKey(
        ATMachine,
        on_delete=models.SET_NULL,
        null=True,
        help_text='ATM transaction was done on')

    transaction_date = models.DateField(
        default=timezone.now)

    response_code = models.CharField(
        max_length=1,
        default='0',
        help_text='Response Code for Tranaction')

    """ Links account to a specific user """
    bank_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.type} Transaction: {self.transaction_id}, {self.atm_machine}, {self.card}'

    # def save(self, *args, **kwargs):
    #     slug_save(self, 10, '0123456789')
    #     Super(SomeModelWithSlug, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Account."""
        return reverse('card-detail', args=[str(self.card_number)])

def slug_save(obj, length, char_set):
    if not obj.slug:
        obj.slug = get_random_string(length, char_set)
        slug_is_worng = True
        while slug_is_wrong:
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                slug_is_wrong = True
            if slug_is_wrong:
                obj.slug = get_random_string(length, char_set)

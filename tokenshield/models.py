from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):
    def _create_user(self, fullname, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not fullname:
            raise ValueError('The fullname field is required')
        
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(fullname=fullname, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, fullname=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(fullname, email, password, **extra_fields)

    def create_superuser(self, fullname=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(fullname, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(verbose_name='fullname', max_length=255, blank=False, null=False)
    email = models.EmailField(verbose_name="email", unique=True, blank=False)
    is_active = models.BooleanField(verbose_name="is_active", default=False)
    is_staff = models.BooleanField(verbose_name="is_staff", default=False)
    is_superuser = models.BooleanField(verbose_name="is_superuser", default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
    
    REQUIRED_FIELDS = ['fullname',]

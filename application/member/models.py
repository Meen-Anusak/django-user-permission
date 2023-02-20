from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.




class MemberManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users should have a email')

        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_member(self, newMember, email, password=None):
        try:
            # with transaction.atomic():
            #     if password is None:
            #         password = self.make_random_password(
            #             length=10, allowed_chars=string.ascii_letters + string.digits + "!@#$%^&*()")

            #     member = self.create_user(username, password)
            #     member.first_name = newMember['first_name']
            #     member.last_name = newMember['last_name']
            #     member.save()

            #     for r_id in newMember['role']:
            #         role = Role.objects.get(id=r_id)
            #         member.role.add(role)

            #     if newMember['dc']:
            #         for dc_id in newMember['dc']:
            #             dc = Dc.objects.get(id=dc_id)
            #             member.dc.add(dc)

            #     for sv_id in newMember['service']:
            #         service = Service.objects.get(id=sv_id)
            #         member.service.add(service)

            # return member
            pass
        except Exception as e:
            print(e)


class Member(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = MemberManager()

    def __str__(self):
        return self.email

    def tokens(self):
        token = RefreshToken.for_user(self)
        return {
            'refresh_token': str(token),
            'access_token': str(token.access_token)
        }

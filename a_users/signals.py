from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    user = instance
    
    # Add a profile if user is created
    if created:
        Profile.objects.create(
            user = user,
        )
    else:
        # update all emailaddress if exists
        try:
            email_address = EmailAddress.objects.get_primary(user)
            if email_address.email != user.email:
                email_address.email = user.email
                email_address.verified = False
                email_address.save()
        except:
            # if allauth emailaddress does not exist, create one
            EmailAddress.objects.create(
                user = user,
                email = user.email,
                primary = True,
                verified = False,
            )

@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()
        

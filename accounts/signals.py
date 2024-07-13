
from django.db.models.base import post_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile




# create receiver for signal

@receiver(post_save, sender=User) # decorator
def post_save_create_profile_receiver(sender, instance, created,**kwargs):
    

    # post_save.connect(post_save_create_profile_receiver,sender=User)
    # this same can be done by using a decorator
    
    # created is a flag, it becomes true when user is created
    if created:
        # create the user profile
        # as soon as the user is created, his profile will also be created
        UserProfile.objects.create(user=instance)
    
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the user profile if it does not exist
            UserProfile.objects.create(user=instance)
            
        
        
        
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class HealthRecord(models.Model):
     User= get_user_model()
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date = models.DateField(auto_now_add=True)
     CONDITION_CHOICES = [(i,str(i)) for i in range(1,6)]
     condition = models.IntegerField(choices=CONDITION_CHOICES,default=3,verbose_name="体調")
     mental_status = models.IntegerField(choices=CONDITION_CHOICES,default=3,verbose_name="精神状態")
     wakeup_time = models.DateTimeField(null=True,blank=True,verbose_name="起床時間")
     bed_time = models.DateTimeField(null=True,blank=True,verbose_name="就寝時間")
     sleep_duration = models.FloatField(null=True,blank=True,verbose_name="睡眠時間(h)")
     class Meta:
          ordering = ['-date']
          constraints = [
               models.UniqueConstraint(
                    fields=['user','date'],
                    name = 'unique_user_daily_record'
               )
          ]
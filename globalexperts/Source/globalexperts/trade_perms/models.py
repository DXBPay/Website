from django.db import models


class TradePermissions(models.Model):

    class Meta:

        managed = False  
                        

        permissions = ( 
            ('Trade_Admin', 'Admin'),
            ('Trade_Users', 'TradeUsers'),
        )
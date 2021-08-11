# Generated by Django 2.2 on 2021-05-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptotoken', '0006_auto_20210510_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencydetails',
            name='blackholeaddress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Hole Address'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='charity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Charity Wallet'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='liquiditylock',
            field=models.IntegerField(choices=[(0, 'UnLock'), (1, 'Lock')], default=0, verbose_name='Liquidity Lock'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='liquidtypool',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Liquidity Pool (PancakeSwap)'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='marketing',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Marketing Wallet'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='pancakeswap',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PancakeSwap Price'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='presaleprice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Dx Sale Pre-Sale Price'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='presupply',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Pre-Sale Supply (DxSale)'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='reward_distributed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Distributor Holder'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='teamwallet',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Team Wallet'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='teamwallet_duration',
            field=models.IntegerField(default=0, verbose_name='Team Wallet Duration'),
        ),
        migrations.AddField(
            model_name='currencydetails',
            name='token_burn',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Token Burn'),
        ),
    ]
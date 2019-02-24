from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='companies'
    )

    name = models.CharField(
        max_length=100, verbose_name=_('Razão Social'), null=False, blank=False
    )

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return 'pk {} -- Company {}'.format(self.pk, self.name)

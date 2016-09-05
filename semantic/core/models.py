# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(_(u'endereço'), max_length=80)
    complement = models.CharField(
        _('complemento'), max_length=80, null=True, blank=True)
    district = models.CharField(
        _('bairro'), max_length=80, null=True, blank=True)
    city = models.CharField(_('cidade'), max_length=80)
    uf = models.CharField(_('UF'), max_length=2)
    cep = models.CharField(_('CEP'), max_length=9, null=True, blank=True)

    class Meta:
        abstract = True


class People(TimeStampedModel, Address):
    first_name = models.CharField(_('nome'), max_length=50)
    last_name = models.CharField(
        _('sobrenome'), max_length=50, null=True, blank=True)
    email = models.EmailField(_('e-mail'), null=True, blank=True)

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

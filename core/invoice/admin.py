from django.contrib import admin

from .models import Invoice, InvoiceDetail

admin.site.register(InvoiceDetail)
admin.site.register(Invoice)


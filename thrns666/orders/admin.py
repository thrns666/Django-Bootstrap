from django.contrib import admin
from .models import Order, OrderItem
import csv
import datetime
from django.http import HttpResponse


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = f'attachment; filename = {opts.verbose_name}.csv'
    writer = csv.writer(responce)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # write header info
    writer.writerow([field.verbose_name for field in fields])
    # write data
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return responce

export_to_csv.short_description = 'Convert to CSV'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)
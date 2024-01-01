from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ["id", "description", "quantity", "unit_price", "price"]


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, required=False)
    class Meta:
        model = Invoice
        fields = ["id", "date", "customer_name", "details"]

    def create(self, validated_data):
        details_data = validated_data.pop("details", [])
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop("details", [])
        instance.date = validated_data.get("date", instance.date)
        instance.customer_name = validated_data.get(
            "customer_name", instance.customer_name
        )
        instance.save()


        if existing_details := instance.details.all():
            self.update_details(existing_details, details_data)
        elif details_data:
            InvoiceDetail.objects.create(invoice=instance, **details_data[0])

        return instance

    def update_details(self, existing_details, details_data):
        detail = existing_details[0]
        detail.description = details_data[0].get("description", detail.description)
        detail.quantity = details_data[0].get("quantity", detail.quantity)
        detail.unit_price = details_data[0].get("unit_price", detail.unit_price)
        detail.price = details_data[0].get("price", detail.price)
        detail.save()

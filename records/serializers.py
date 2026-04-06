from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number")
        return value


    class Meta:
        model = Record
        fields = ['id', 'amount', 'type', 'category', 'date', 'notes']
        read_only_fields = ['id', 'user']
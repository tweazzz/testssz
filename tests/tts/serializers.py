from rest_framework import serializers
from .models import Prepod, JobHistory
from django.forms import DateField

class YearField(serializers.Field):
    def to_representation(self, obj):
        return obj.year if obj else None

    def to_internal_value(self, data):
        try:
            return serializers.DateTimeField().to_internal_value(f"{data}-01-01T00:00:00Z")
        except serializers.ValidationError:
            raise serializers.ValidationError("Invalid year format")

class JobHistorySerializer(serializers.ModelSerializer):
    start_date = YearField()
    end_date = YearField()

    class Meta:
        model = JobHistory
        fields = ['start_date', 'end_date', 'job_characteristic']

class PrepodSerializer(serializers.ModelSerializer):
    job_history = JobHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Prepod
        fields = ['id','full_name', 'photo3x4', 'short_info', 'job_history']

    def to_representation(self, instance):
        representation = super(PrepodSerializer, self).to_representation(instance)
        job_history_data = JobHistorySerializer(instance.jobhistory_set.all().order_by('id'), many=True).data
        representation['job_history'] = job_history_data
        return representation

class PrepodCreateSerializer(serializers.ModelSerializer):
    job_history = JobHistorySerializer(many=True, required=False)

    class Meta:
        model = Prepod
        fields = ['full_name', 'photo3x4', 'short_info', 'job_history']

    def create(self, validated_data):
        full_name = validated_data.get('full_name')
        existing_prepod = Prepod.objects.filter(full_name=full_name).first()

        if existing_prepod:
            # Преподаватель с таким именем уже существует, возвращаем существующего
            return existing_prepod

        job_history_data = validated_data.pop('job_history', [])
        prepod = Prepod.objects.create(**validated_data)

        for job_data in job_history_data:
            JobHistory.objects.create(prepod=prepod, **job_data)

        return prepod
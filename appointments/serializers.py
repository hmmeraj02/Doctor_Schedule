from rest_framework import serializers
from .models import Appointment, Patient


class AppointmentSerializer(serializers.ModelSerializer):
    PatientId = serializers.IntegerField(write_only=True)
    AppointmentDate = serializers.DateField(source="appointment_date")
    AppointmentTime = serializers.TimeField(source="appointment_time")
    Reason = serializers.CharField(source="reason")

    class Meta:
        model = Appointment
        fields = ["PatientId", "AppointmentDate", "AppointmentTime", "Reason"]

    def create(self, validated_data):
        patient_id = validated_data.pop("PatientId")
        patient = Patient.objects.filter(id=patient_id).first()
        if not patient:
            raise serializers.ValidationError(
                {"PatientId": "Patient not found."})

        appointment = Appointment.objects.create(
            patient=patient, **validated_data)
        return appointment

    def to_representation(self, instance):
        return {
            "AppointmentId": instance.id,
            "PatientId": instance.patient.id,
            "AppointmentDate": str(instance.appointment_date),
            "AppointmentTime": str(instance.appointment_time)[:5],
            "Reason": instance.reason,
            "Message": "Appointment created successfully"
        }

from rest_framework import serializers

from wmapi.models import (
    BodyPart,
    Equipment,
    Exercise,
    ExerciseInstance,
    Muscle,
    Set,
    Workout,
    WorkoutPart,
)


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            "id",
            "name",
            "description",
            "duration_minutes",
            "start_datetime",
            "end_datetime",
            "workout_parts",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class WorkoutPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPart
        fields = [
            "id",
            "type",
            "exercises",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ExerciseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInstance
        fields = [
            "id",
            "exercise_id",
            "sets",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = [
            "id",
            "repetitions",
            "weight",
            "rest_seconds",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
            "image_url",
            "video_url",
            "overview",
            "keywords",
            "exercise_tips",
            "variations",
            "related_exercise_ids",
            "instructions",
            "exercise_type",
            "target_muscles",
            "body_parts",
            "equipments",
            "secondary_muscles",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class BodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

from rest_framework import serializers

from api.models.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "gender",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "birth_date",
            "ci",
        )

    def validate_email(self, email):
        print(email)
        return email

    def validate_name(self, name):
        print(name)
        if len(name) > 3:
            return "INVALIDUSER"
        return name

    def validate(self, attrs):
        # attrs -> attributes
        if list(attrs.get("name"))[0] == "황" and attrs.get("gender") != 0:
            raise ValueError

        return super().validate(attrs)

    def to_representation(self, instance):
        # 기본 시리얼라이저의 데이터를 가져옴
        represented = super().to_representation(instance)

        # 요청 객체를 가져옴
        request = self.context.get('request', None)

        # 요청 메서드에 따라 필드 삭제
        if request:
            if request.method == 'POST':
                for field in ["is_active", "is_staff", "is_superuser", "last_login"]:
                    represented.pop(field, None)
            elif request.method == 'GET':
                for field in ["is_staff", "is_superuser", "last_login", "gender", "ci", "birth_date"]:
                    represented.pop(field, None)

        return represented


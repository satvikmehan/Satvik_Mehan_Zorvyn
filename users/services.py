from .models import User

def create_user(validated_data):
    password = validated_data.pop('password')

    user = User(
        username=validated_data.get('username'),
        email=validated_data.get('email')
    )

    user.role = 'viewer'   # default role
    user.set_password(password)   # 🔥 hash password

    user.save()
    return user
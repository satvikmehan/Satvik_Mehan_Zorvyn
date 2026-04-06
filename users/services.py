from .models import User


def create_user(validated_data):
    """
    Handles user creation logic safely
    """

    # Force safe role
    validated_data['role'] = 'viewer'

    # Create user with hashed password
    user = User.objects.create_user(**validated_data)

    return user
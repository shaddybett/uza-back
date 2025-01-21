from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=200))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=200))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=[
        validate.Length(min=8, max=200),
        validate.Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            error="Password must contain at least one uppercase letter, one lowercase letter, one number and one special character"
        )
    ])
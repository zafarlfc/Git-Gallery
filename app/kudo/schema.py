from marshmallow import Schema, fields

class GitHubRepoSchema(Schema):
    id = fields.Int(required=True)
    repo_name = fields.Str(required=True)
    full_name = fields.Str(required=True)
    description = fields.Str(required=True)

class KudoSchema(GitHubRepoSchema):
    user_id = fields.Email(required=True)
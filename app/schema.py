from marshmallow import Schema, fields

class GitHubRepoSchema(Schema):
  id = fields.Int(required=True)
  repo_name = fields.Str()
  full_name = fields.Str()
  description = fields.Str()

class KudoSchema(GitHubRepoSchema):
  user_id = fields.Email(required=True)
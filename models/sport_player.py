from odoo import models, fields

class SportPlayer(models.Model):
    _name='sport.player'
    _description='Sport Player'
    
    
    name = fields.Char(
        string='Name',
        required=True
    )
    
    
    age = fields.Integer(
        string='Age',
    )
    
    
    position = fields.Char(
        string='Position',
    )
    
    
    team_id = fields.Many2one(
        string='Team',
        comodel_name='sport.team',
    )
    
    starting_team = fields.Boolean(
        string='Starting Team',
    )
    
    
    
    
    
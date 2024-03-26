from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'
    
    
    name = fields.Char(
        string='Name',
        required=True
    )
    
    logo = fields.Binary(
        string='logo',
    )
    
    player_list_ids = fields.One2many(
        string='Player List',
        comodel_name='sport.player',
        inverse_name='team_id',
    )
    
    
    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
    )
    
    
    
    
    
    
    
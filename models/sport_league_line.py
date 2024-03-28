from odoo import models, fields, api

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sports League Line'
    
    league_id = fields.Many2one(
        string='League',
        comodel_name='sport.league',
    )
    
    team_id = fields.Many2one(
        string='Team',
        comodel_name='sport.team',
    )
    
    points = fields.Integer(
        string='Points',
    )
    
    
    
    
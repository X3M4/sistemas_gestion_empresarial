from odoo import models, fields, api

class SportsLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sports League'
    
    name = fields.Char(
        string ='Name', 
        required=True)
    
    start_date = fields.Date(
        string='start_date'
    )
    
    end_date = fields.Date(
        string='end_date',
    )
    
    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
    )
    
    sport_league_ids = fields.One2many(
        string='Ligas',
        comodel_name='sport.league.line',
        inverse_name='league_id',
    )
    
    
    
    
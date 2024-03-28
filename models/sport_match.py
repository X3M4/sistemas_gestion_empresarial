from odoo import models, fields, api, Command

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'
    
    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
    )
    
    date = fields.Datetime(
        string='Date',
    )
    
    winner_team_id = fields.Many2one(
        string='Winner Team',
        comodel_name='sport.team',
    )
    
    score_winning = fields.Integer(
        string='Points',
        default = 3
    )
    
    match_line_ids = fields.One2many(
        string='Matchs',
        comodel_name='sport.match.line',
        inverse_name='match_id',
    )
    
    
#Match Lines Class    
class SportMatchLine(models.Model):
     _name ='sport.match.line'
     _description = 'Sport Match Line'
     
     match_id = fields.Many2one(
         string='Match',
         comodel_name='sport.match',
     )
     
     team_id = fields.Many2one(
         string='Team',
         comodel_name='sport.team',
     )
     
     score = fields.Integer(
         string='Score',
     )
     
        
    
    
    
    
    
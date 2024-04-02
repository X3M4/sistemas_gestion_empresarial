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
    
    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_team_id', '=', team.id)]).mapped('score_winning')
            record.points = sum(score_points)
    
    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()
    
class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sports League Line'
    _order = 'points desc'
    
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
    
    
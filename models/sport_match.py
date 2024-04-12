from odoo import models, fields, api, Command

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'
    _rec_name = 'sport_id'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    
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
        compute = '_compute_winner_team_id',
        store = True,
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
    
    
    league_id = fields.Many2one(
        string='League',
        comodel_name='sport.league',
        ondelete='restrict',
    )
    
    match_line_ids_count = fields.Integer(
        string = "Number of Matches",
    )
    
            
    @api.depends('match_line_ids.score')
    def _compute_winner_team_id(self):
        for record in self:
            winner = record.match_line_ids.sorted(key=lambda r: r.score, reverse=True)
            record.winner_team_id = winner[0].team_id.id if winner else False
    
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
     
     _sql_constraints = [
        ('team_id_unique', 'UNIQUE(match_id,team_id)', 'The team must not be duplicated!')
    ]
        
    
    
    
    
    
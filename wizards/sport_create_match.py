from odoo import models, fields, api


class SportCreateMatch(models.TransientModel):
    _name = 'sport.create.match'
    _description = 'Sport Create Match'
    
    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
        related='league_id.sport_id',
    )
    
    date = fields.Datetime(
        string='Date',
    )
    
    league_id = fields.Many2one(
        string='League',
        comodel_name='sport.league',
    )
    
    team_ids = fields.Many2many('sport.team', string='Teams')
    
    def create_match(self):
        #active_id = self.env.context.get('active_id')
        vals = {
           'sport_id': self.sport_id.id,
            'date': self.date,
            'league_id': self.league_id.id,
            'match_line_ids': [(0, 0, {'team_id': team.id}) for team in self.team_ids]
        }
        game=self.env['sport.match'].create(vals) 
        
        return {
            'name': 'Match',
            'view_mode': 'form',
            'res_model':'sport.match',
            'res_id': game.id,
            'type': 'ir.actions.act_window',
            'target': 'current'
        }
    
    
    
    
    

    

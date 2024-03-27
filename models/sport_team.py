from odoo import models, fields, Command

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
    
    number = fields.Integer(
        string='Roster',
        compute='_compute_number',
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
    
    def make_all_starters(self):
        for record in self.player_list_ids:
            record.starting_team=True
    
    def make_all_substitutes(self):
        for record in self.player_list_ids:
            record.starting_team=False
    
    def action_add_players_under_30(self):
        for record in self:
            players = self.env['sport.player'].search([('age', '<', 30), ('team_id', '=', False)])
            players |= record.player_list_ids 
            record.player_list_ids = [Command.set(players.ids)]
    
    def _compute_number(self):
        for record in self:
            record.number = len(record.player_list_ids) 
    
    
    
    
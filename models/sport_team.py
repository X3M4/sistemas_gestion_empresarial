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
        store=True,
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
    
    player_count = fields.Integer(
        string='Issue Count',
        compute='_compute_player_count',
    )
    
    def _compute_player_count(self):
        for record in self:
            record.player_count = len(record.player_list_ids)
        
    
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
    
    #Hacer smartbutton para equipo que te lleve a los jugadores
    def action_view_players(self):
        return{
            'name':'Players',
            'type': 'ir.actions.act_window',
            'res_model':'sport.player',
            'view_mode':'tree,form',
            'domain': [('team_id', '=', self.id)],
        }
    
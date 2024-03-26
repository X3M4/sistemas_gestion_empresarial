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
    
    position = fields.Selection(
        string='Position',
        selection=[
            ('portero', 'Portero'), 
            ('defensa', 'Defensa'),
            ('medio', 'Medio'),
            ('delantero', 'Delantero')]
    )
    
    team_id = fields.Many2one(
        string='Team',
        comodel_name='sport.team',
    )
    
    starting_team = fields.Boolean(
        string='Starting Team',
    )
    
    def action_make_starter(self):
        self.starting_team = True
    
    def action_make_substitute(self):
        self.starting_team = False
    
    
    
    
    
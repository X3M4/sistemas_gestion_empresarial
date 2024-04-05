from odoo import models, fields, api

class SportPlayer(models.Model):
    _name='sport.player'
    _description='Sport Player'
    
    
    name = fields.Char(
        string='Name',
        required=True
    )
    
    dob = fields.Date(
        string='Date of Birth',
        copy=False,
    )
    
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True
    )
    
    position = fields.Selection(
        string='Position',
        copy=False,
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
        default = True,
        copy=False,
    )
    
    sport = fields.Char(
        string='Sport',
        related='team_id.sport_id.name',
        store = True,
    )
    
    active = fields.Boolean(
        string='Active',
        default=True,
    )
    
    
    player_id = fields.Many2one(
        'sport.issue', 
        string='player',
        copy=False)
    
    
    def action_make_starter(self):
        self.starting_team = True
    
    def action_make_substitute(self):
        self.starting_team = False
    
    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                record.age = (fields.Date.today() - record.dob).days / 365
            else:
                record.age = 0
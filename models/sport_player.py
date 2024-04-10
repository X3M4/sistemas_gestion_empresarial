from odoo import models, fields, api, _

class SportPlayer(models.Model):
    _name='sport.player'
    _description='Sport Player'
    _inherits = {'res.partner': 'partner_id'}
    
    name = fields.Char(
        related='partner_id.name',
        inherited=True,
        readonly=False,
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
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
    
    #Método para copiar un jugador teniendo en cuenta la herencia
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if ('name' not in default) and ('partner_id' not in default):
            default['name'] = _("%s (copy)", self.name)
        return super().copy(default)
    
    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                record.age = (fields.Date.today() - record.dob).days / 365
            else:
                record.age = 0
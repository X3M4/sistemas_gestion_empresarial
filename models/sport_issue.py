from odoo import models, fields

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'
    
    name = fields.Char(
        string ='name', 
        required=True) 
    
    
    description = fields.Text(
        string = 'Description')
    
    
    date = fields.Date(
        string ='Date')
    
    
    assistance = fields.Boolean(
        string='Assistance',
        help = 'Show if the issue was assisted by medical service')
    
    
    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'draft'), 
            ('open', 'Open'),
            ('done', 'Done')],
        default = 'draft')
    
    
    user_id = fields.Many2one(
        string='User',
        comodel_name='res.users',
    )
    
    sequence = fields.Integer(
        string='sequence',
        default=10
        
    )
    
    solution = fields.Html(
        string='solution',
    )
    
    
    clinic_id = fields.Many2one(
        string='clinic',
        comodel_name='sport.clinic'
    )
    
    
    tag_ids = fields.Many2many(
        string='Tag',
        comodel_name='sport.issue.tag'
    )
    
    
    
    def action_open(self):
        self.ensure_one() #Se usa para asegurarse de que la función solamente se ejecuta sobre un registro
        self.state = 'open'
    
    def action_draft(self):
        self.ensure_one() #Se usa para asegurarse de que la función solamente se ejecuta sobre un registro
        self.state = 'draft'
    
    def action_done(self):
        self.ensure_one() #Se usa para asegurarse de que la función solamente se ejecuta sobre un registro
        self.state = 'done'
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
    
    
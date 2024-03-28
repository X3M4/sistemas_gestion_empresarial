from odoo import models, fields, api

class SportIssueAction(models.Model):
    _name='sport.issue.action'
    _description='Sport Issue Action'
    
    name = fields.Char(
        string ='name', 
        required=True)
    
    
    issue_id = fields.Many2one(
        string='Issue',
        comodel_name='sport.issue', 
    )
    
    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'draft'), 
            ('open', 'Open'),
            ('done', 'Done')],
        default = 'draft')
    
    
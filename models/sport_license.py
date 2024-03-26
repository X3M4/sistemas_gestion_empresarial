from odoo import fields, models

class SportLicense(models.Model):
    _name = 'sport.license'
    _description = 'Sport License'

    name = fields.Char(
        string='name',
        required=True
    )
      
    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
    )
      
    start_date = fields.Date(
        string='Start Date'
    )
    
    end_date = fields.Date(
        string='End Date'
    )
    
    
    
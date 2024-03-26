from odoo import models, fields

class SportClinic(models.Model):
    _name =  "sport.clinic"
    _description = "Sport Clinic"
    
    
    name = fields.Char(
        string='Name',
        required=True
    )
    
    phone = fields.Char(
        string='Phone',
    )
    
    email = fields.Char(
        string = 'E-mail'
    )
    
    issue_ids = fields.One2many(
        string='Issues',
        comodel_name='sport.issue',
        inverse_name='clinic_id',
    )    
    
    def action_check_assistance(self):
         self.issue_ids.write({'assistance': True})
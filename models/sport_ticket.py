from odoo import models, fields, api, _

class SportTicket(models.Model):
    _name = 'sport.ticket'
    _description = 'Sports Ticket'
    
    
    name = fields.Char(
        string='Name',
        required = True,
    )
    
    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
    )
    
    match_id = fields.Many2one(
        string='Match',
        comodel_name='sport.match',
    )
    
from odoo import api, fields, models, _


class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = 'Create Issue'
    
    
    name = fields.Char(
        string='Issue name',
    )
    
    clinic_id = fields.Many2one(
        'sport.clinic', 
        'Clinic', 
        default = lambda self: self.env.context.get('active_id'),
        )

    def create_issue(self):
        vals = {'name': self.name, 'clinic_id': self.clinic_id.id}
        issue=self.env['sport.issue'].create(vals)
        return {
            'name': 'Issue',
            'view_mode': 'form',
            'res_model':'sport.issue',
            'res_id': issue.id,
            'type': 'ir.actions.act_window',
            'target': 'current'
        }
    

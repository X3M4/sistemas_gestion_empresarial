from odoo import models, fields, _


class SportCheckIssuesTrue(models.TransientModel):
    _name = 'sport.check.issues.true'
    _description = 'Issues True'
    
    
    date = fields.Date(
        string='Date'
    )
    
    
    '''def set_done(self):
        active_ids = self.env.context.get('active_ids')
        issues = self.env['sport.issue'].browse(active_ids)
        issues.write({'date': self.date})
        issues.action_done()'''
    
    def set_done(self):
        issues = self.env['sport.issue'].search(['|', ('date', '=', self.date), ('date', '=', False)])
        for issue in issues:
            issue.action_done()


    
    

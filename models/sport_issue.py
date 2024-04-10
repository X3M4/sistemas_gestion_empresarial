from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError, UserError

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    # def _get_default_user(self):
    #     return self.env.user

    name = fields.Char(
        string='Name', 
        required=True, 
        copy=False)
    
    description = fields.Text(
        string='Description')
    
    date = fields.Date(
        string='Date', 
        default=fields.Date.today)
    
    assistance = fields.Boolean(
        string='Assistance', 
        help='Show if the issue has assistance')
    
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('done', 'Done')],
        string='State',
        default='draft',
        tracking=True
    )

    color = fields.Integer(
        string='Color', 
        default=0)
    
    user_id = fields.Many2one(
        'res.users', 
        string='User', 
        default=lambda self: self.env.user)
    
    sequence = fields.Integer(
        string='Sequence', 
        default=10)
    
    solution = fields.Html('Solution')
    
    assigned = fields.Boolean(
        'Assigned', 
        compute='_compute_assigned', 
        inverse='_inverse_assigned',
        store=True)
    
    clinic_id = fields.Many2one(
        'sport.clinic', 
        string='Clinic')
    
    player_id = fields.Many2one(
        'sport.player', 
        string='Player')
    
    tag_ids = fields.Many2many('sport.issue.tag', 'sport_issue_tags_rel', 'issue_id', 'tag_id', string='Tags')

    cost = fields.Float('Cost')

    user_phone = fields.Char('User phone')

    action_ids = fields.One2many('sport.issue.action', 'issue_id', string='Actions to do')
    
    #Añadir restricción con _sql_constraints en el que el nombre de la incidencia sea único.
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The name of the issue must be unique!')
    ]
    
    #CONSTRAINS
    @api.constrains('cost')
    def _check_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError(_('Cost cannot be negative')) # El símbolo _ sirve para indica que se puede traducir. Se debe importar
    
    
    # ACCIONES ONCHANGE
    @api.onchange('clinic_id')
    def _onchange_clinic(self):
        for record in self:
            if record.clinic_id:
                record.assistance = True
            else:
                record.assistance = False
                      
    #Cambiar la funcionalidad de user_phone, quitar el related y añadir un onchange para que cuando se cambie el usuario se traiga el teléfono de este usuario
    @api.onchange('user_id')
    def _onchange_user_phone(self):
        for record in self:
            if record.user_id:
                record.user_phone = record.user_id.phone
            else:
                record.user_phone = False        
    
    
    @api.depends('user_id')   
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)
    
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user
    
    
    
    def _search_assigned(self, operator, value):
        if operator == '=':
            return [('user_id', operator, value)]
        else:
            return[]
    
    def action_open(self):
        self.ensure_one() #Se usa para asegurarse de que la función solamente se ejecuta sobre un registro
        self.state = 'open'
    
    def action_draft(self):
        self.ensure_one() #Se usa para asegurarse de que la función solamente se ejecuta sobre un registro
        self.state = 'draft'
    
    def action_done(self):
        for record in self:
            if not record.date:
                raise UserError(_('Date is required'))
            self.state = 'done'
            #Para añadir el mensaje de la creación de la incidencia
            #msg_body = (_(f"The issue {record.name} ha passed to state {record.state} on date: {record.date}"))
            record.message_post(body=(_(f"The issue {record.name} ha passed to state {record.state} on date: {record.date}")))
    
    def action_add_tag(self):
        for record in self:
            tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
            if tag_ids:
                record.tag_ids = [Command.set(tag_ids.ids)]
            else:
                record.tag_ids = [Command.create({'name': record.name})]
    
    #Cron que busque las etiquetas de incidencias y elimine las que no se están usando.
    def _cron_unlink_unused_tags(self):
        tag_ids = self.env['sport.issue.tag'].search([])
        for tag in tag_ids:
            issue = self.env['sport.issue'].search([('tag_ids', 'in', tag.id)])
            if not issue:
                tag.unlink()
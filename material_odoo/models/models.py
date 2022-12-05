from odoo import models, fields, api
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class MaterialOdoo(models.Model):
    _name = 'material.odoo'
    _description = 'material odoo'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')], required=True)
    material_buy_price = fields.Integer(string='Material Buy Price', default="100", required=True)
    suplier_partner_id = fields.Many2one('res.partner', string='Suplier', required=True)

    @api.constrains('material_buy_price')
    def action_material(self):
        for r in self:
            if r.material_buy_price < 100:
                raise ValidationError('Angka yang dimasukkan tidak boleh lebih kecil dari 100')

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner'
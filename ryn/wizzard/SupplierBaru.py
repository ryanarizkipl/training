from odoo import api, fields, models


class SupplierBaru(models.TransientModel):
    _name = 'ryn.supplierbaru'

    # nm_per = fields.Many2one(comodel_name='ryn.supplier', string='Nama Perusahaan', required='True')
    # almbaru = fields.Char(string='Alamat Baru', required='False')
    
    barang_id = fields.Many2one(string='Nama Barang',comodel_name='ryn.barang',required='True')
    sup_id = fields.Many2one(string='Nama Perusahan',comodel_name='ryn.supplier',required='True')

    def button_supplier_baru(self):
        # for rec in self:
        #     self.env ['ryn.supplier'].search([('id', '=', rec.nm_per.id)]).write({'alamat': rec.nm_per.alamat + '+' +rec.almbaru})
        
        for rec in self:
            self.env ['ryn.supplier'].search([('id', '=', rec.sup_id.id)]).write({'barang_id': rec.barang_id + rec.sup_id})
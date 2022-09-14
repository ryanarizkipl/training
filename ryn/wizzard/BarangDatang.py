from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'ryn.barangdatang'

    barang_id = fields.Many2one(string='Nama Barang',comodel_name='ryn.barang',required='True')
    jumlah = fields.Integer(string='Jumlah',required='False')

    def button_barang_datang(self):
        for rec in self:
            self.env ['ryn.barang'].search([('id', '=', rec.barang_id.id)]).write({'stok': rec.barang_id.stok + rec.jumlah})
    
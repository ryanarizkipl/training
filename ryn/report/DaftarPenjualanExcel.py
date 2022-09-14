from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.ryn.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_trans = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(1, 0, 'No Nota')
        sheet.write(1, 1, 'Nama Pembeli')
        sheet.write(1, 2, 'Tanggal Transaksi')
        sheet.write(1, 3, 'Total Pembayaran')
        row = 2
        col = 0
        for obj in penjualan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, str(self.tgl_trans))
            sheet.write(row, col+3, str(obj.total_bayar))
            row += 1